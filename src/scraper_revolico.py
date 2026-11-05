"""Scraper de anuncios de venta de vehículos en Revolico.

Fase 2 del proyecto ICD Proyecto Mercado.

Consulta la búsqueda de carros de Revolico, obtiene el HTML con los
anuncios (cargados vía SSR + Apollo en el script `__NEXT_DATA__`) y
normaliza cada anuncio al esquema del proyecto.

Uso:
    python -m src.scraper_revolico --max-anuncios 30
"""

import argparse
import json
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Tuple

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.revolico.com"
SEARCH_PATH = "/search"
CATEGORY = "vehiculos"
SUBCATEGORY = "vehiculos-carros"
PAGE_LENGTH = 100
DEFAULT_MAX_ANUNCIOS = 30
REQUEST_TIMEOUT = 30
REQUEST_DELAY_SECONDS = 2.0
RAW_PATH = Path("data/raw/anuncios_revolico.json")
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
)


def _ahora_iso() -> str:
    """Timestamp UTC de la extracción (fecha_extraccion)."""
    return datetime.now(timezone.utc).isoformat()


def _build_search_url(page: int) -> str:
    params = {
        "category": CATEGORY,
        "subcategory": SUBCATEGORY,
        "page": page,
    }
    query = "&".join(f"{k}={v}" for k, v in params.items())
    return f"{BASE_URL}{SEARCH_PATH}?{query}"


def _extraer_anuncios(html: str) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    """Extrae los anuncios y el estado de Apollo desde el HTML."""
    soup = BeautifulSoup(html, "html.parser")
    script = soup.find("script", attrs={"id": "__NEXT_DATA__"})
    if script is None or script.string is None:
        return [], {}

    payload = json.loads(script.string)
    estado = (
        payload.get("props", {}).get("pageProps", {}).get("__APOLLO_STATE__")
        or {}
    )
    if not estado:
        return [], {}

    root_query = estado.get("ROOT_QUERY") or {}
    query_key = next((k for k in root_query if k.startswith("adsPerPage")), None)
    if query_key is None:
        return [], estado

    conexion = root_query[query_key] or {}
    edges = conexion.get("edges") or []
    anuncios: List[Dict[str, Any]] = []
    for edge in edges:
        nodo = edge.get("node") if isinstance(edge, dict) else None
        ref = nodo.get("__ref") if nodo else None
        if not ref:
            continue
        anuncio = estado.get(ref) or {}
        if anuncio.get("__typename") == "AdType":
            anuncios.append(anuncio)
    return anuncios, estado


def _normalizar_anuncio(
    anuncio: Dict[str, Any],
    estado: Dict[str, Any],
    fecha_extraccion: str,
) -> Dict[str, Any]:
    """Convierte el anuncio crudo del scraper al esquema del proyecto."""
    precio = anuncio.get("price")
    provincia = None
    municipio = None
    if anuncio.get("provinceId") is not None:
        provincia = (estado.get(f"ProvinceType:{anuncio.get('provinceId')}") or {}).get("name")
        municipio = (estado.get(f"MunicipalityType:{anuncio.get('municipalityId')}") or {}).get("name")
    ubicacion = None
    if provincia or municipio:
        ubicacion = ", ".join(p for p in [provincia, municipio] if p)

    return {
        "id_anuncio": anuncio.get("id"),
        "url": f"{BASE_URL}{anuncio.get('permalink')}" if anuncio.get("permalink") else None,
        "fecha_extraccion": fecha_extraccion,
        "fecha_publicacion": anuncio.get("updatedOnToOrder"),
        "titulo_original": anuncio.get("title"),
        "descripcion_original": anuncio.get("description"),
        "precio_original": precio,
        "moneda_original": anuncio.get("currency"),
        "precio_numerico": precio,
        "ubicacion": ubicacion,
        "imagenes": [anuncio["mainImage"]["gcsKey"]] if anuncio.get("mainImage") else [],
        "marca": None,
        "modelo": None,
        "tipo_vehiculo": None,
        "anio": None,
        "estado": None,
        "tiempo_de_uso_declarado": None,
        "tipo_motorizacion": None,
        "autonomia": None,
        "kilometraje": None,
        "transmision": None,
        "detalles_carroceria": None,
        "detalles_interior": None,
        "accesorios": [],
        "problemas_tecnicos": [],
        "otros_detalles": None,
    }


def scrape_revolico(
    max_anuncios: int = DEFAULT_MAX_ANUNCIOS,
    category: str = CATEGORY,
    subcategory: str = SUBCATEGORY,
    page_length: int = PAGE_LENGTH,
    delay: float = REQUEST_DELAY_SECONDS,
) -> List[Dict[str, Any]]:
    """Recolecta anuncios de la categoría de carros en Revolico."""
    anuncios: List[Dict[str, Any]] = []
    vistos: set = set()
    page = 1

    while len(anuncios) < max_anuncios:
        url = _build_search_url(page)
        respuesta = requests.get(
            url,
            timeout=REQUEST_TIMEOUT,
            headers={"User-Agent": USER_AGENT, "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "es-ES,es;q=0.9,en;q=0.8"},
        )
        respuesta.raise_for_status()
        ads, estado = _extraer_anuncios(respuesta.text)
        if not ads:
            break

        recolectados_en_pagina = 0
        for ad in ads:
            if ad.get("id") in vistos:
                continue
            vistos.add(ad.get("id"))
            anuncios.append(_normalizar_anuncio(ad, estado, _ahora_iso()))
            recolectados_en_pagina += 1
            if len(anuncios) >= max_anuncios:
                break

        if recolectados_en_pagina == 0 or len(ads) < page_length:
            break
        page += 1
        time.sleep(delay)

    return anuncios


def main() -> None:
    parser = argparse.ArgumentParser(description="Scraper de anuncios de carros en Revolico")
    parser.add_argument("--max-anuncios", type=int, default=DEFAULT_MAX_ANUNCIOS, help="Maximo de anuncios a recolectar")
    parser.add_argument("--out", type=str, default=str(RAW_PATH), help="Archivo JSON de salida")
    args = parser.parse_args()

    anuncios = scrape_revolico(max_anuncios=args.max_anuncios)
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(anuncios, f, ensure_ascii=False, indent=2, default=str)
        f.write("\n")
    print(f"Se recolectaron {len(anuncios)} anuncios -> {args.out}")


if __name__ == "__main__":
    main()

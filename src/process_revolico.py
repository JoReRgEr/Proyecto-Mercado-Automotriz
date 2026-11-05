"""Procesamiento de anuncios de Revolico (Fase 2 y Fase 3.1).

Lee los datos crudos de `data/raw/anuncios_revolico.json` y prepara una
version procesada en `data/processed/anuncios_revolico_processed_update.json`,
con la estructura definitiva del anuncio (Fase 3.1) y atributos extraidos.

Uso:
    python src/process_revolico.py
"""

import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional

RAW_PATH = Path("data/raw/anuncios_revolico.json")
PROCESSED_FILE = Path("data/processed/anuncios_revolico_processed_update.json")

TASA_USD_CUP = 920

BRANDS: Dict[str, str] = {
    "hyundai": "Hyundai",
    "kia": "Kia",
    "toyota": "Toyota",
    "nissan": "Nissan",
    "audi": "Audi",
    "honda": "Honda",
    "chevrolet": "Chevrolet",
    "bmw": "BMW",
    "volkswagen": "Volkswagen",
    "volvo": "Volvo",
    "mg": "MG",
    "tesla": "Tesla",
    "ford": "Ford",
    "fiat": "Fiat",
    "peugeot": "Peugeot",
    "renault": "Renault",
    "suzuki": "Suzuki",
    "jeep": "Jeep",
    "land rover": "Land Rover",
    "porsche": "Porsche",
    "dodge": "Dodge",
    "chrysler": "Chrysler",
    "mitsubishi": "Mitsubishi",
    "subaru": "Subaru",
    "mazda": "Mazda",
    "geely": "Geely",
    "byd": "BYD",
    "donga": "Donga",
    "bestune": "Bestune",
    "jac": "JAC",
    "proac": "Proac",
}

BRAND_REGEX = re.compile(r"\b(" + "|".join(re.escape(m) for m in BRANDS) + r")\b", re.IGNORECASE)

YEAR_PATTERN = re.compile(r"\b(19|20)\d{2}\b")

MODELO_STOPWORDS = {
    "nuevo", "usado", "seminuevo", "en", "para", "de", "con", "del", "los", "las",
    "el", "la", "un", "una", "gran", "s", "ltd", "limited", "ev", "evolucion",
    "primera", "primero", "segunda", "segundo", "max", "plus", "pro", "sport", "line",
    "ultimate", "ibl", "ibr", "ibn", "blanco", "blanca", "negro", "negra", "rojo",
    "roja", "azul", "gris", "plateado", "plateada", "verde", "beige", "marron",
    "año", "anos", "ano", "enchufable", "enchufe", "elctrico", "electrica", "elctrica",
}

ENGINE_WORDS = {
    "ibrido", "ibmido", "ibn", "electrico", "electrica", "eléctrico", "eléctrica",
    "electric", "hibrido", "hibrida", "hybrid", "motor", "turbo", "glv",
}


def _extraer_marca(texto: str) -> Optional[str]:
    """Extrae la marca a partir de palabras clave en el texto del anuncio."""
    match = BRAND_REGEX.search(texto)
    if match:
        return BRANDS[match.group(1).lower()]
    return None


def _extraer_anio(texto: str) -> Optional[int]:
    """Extrae el año de fabricación a partir del título/descripción."""
    match = YEAR_PATTERN.search(texto)
    if match:
        return int(match.group(0))
    return None


def _extraer_modelo(texto: str, marca: Optional[str]) -> Optional[str]:
    """Extrae el modelo como la secuencia de tokens tras la marca."""
    if not marca:
        return None
    lower = texto.lower()
    idx = lower.find(marca.lower())
    if idx == -1:
        return None
    tokens = texto[idx + len(marca):].split()
    modelo_tokens: List[str] = []
    for token in tokens:
        limpio = token.strip(".,:;-_*¡!¿?()[] ()")
        clave = limpio.lower()
        if not clave:
            continue
        if re.fullmatch(r"(19|20)\d{2}", clave):
            break
        if clave.isdigit() or clave in MODELO_STOPWORDS or clave in ENGINE_WORDS:
            continue
        if limpio.isalpha() and limpio.isupper():
            modelo_tokens.append(limpio.capitalize())
        elif limpio[0].isdigit():
            modelo_tokens.append(limpio.upper())
        elif limpio[0].isupper():
            modelo_tokens.append(limpio)
        else:
            modelo_tokens.append(limpio.capitalize())
    if not modelo_tokens:
        return None
    return " ".join(modelo_tokens)


def _extraer_tipo_vehiculo(texto: str) -> Optional[str]:
    """Detecta tipo de vehículo con base en expresiones explícitas."""
    lower = texto.lower()
    if re.search(r"electric|el[eí]ctrico|\bv\b", lower):
        return "eléctrico"
    if re.search(r"\bmoto", lower):
        return "moto"
    return None


def _extraer_kilometraje(texto: str) -> Optional[Any]:
    """Extrae el kilometraje declarado en el texto (sin convertir unidades)."""
    match = re.search(r"millas[:\s]*([\d.,]+)", texto, re.IGNORECASE)
    if not match:
        match = re.search(r"([\d.,]+)\s*mil\s*km", texto, re.IGNORECASE)
    if not match:
        match = re.search(r"(\d+)\s*millas\s*rodadas", texto, re.IGNORECASE)
    if not match:
        return None
    valor = match.group(1).replace(".", "").replace(",", "")
    try:
        return float(valor)
    except ValueError:
        return None


def _extraer_transmision(texto: str) -> Optional[str]:
    """Detecta la transmisión con expresiones explícitas."""
    if re.search(r"automatic", texto, re.IGNORECASE):
        return "automática"
    if re.search(r"manual", texto, re.IGNORECASE):
        return "manual"
    return None


def _extraer_motorizacion(texto: str) -> Optional[str]:
    """Detecta la motorización con expresiones explícitas."""
    lower = texto.lower()
    if re.search(r"electric|el[eí]ctrico|\bv\b", lower):
        return "eléctrico"
    if re.search(r"diesel", lower):
        return "diésel"
    if re.search(r"h[ií]brido|hibrido", lower):
        return "híbrido"
    if re.search(r"gasolina|nafta", lower):
        return "gasolina"
    return None


def _extraer_estado(texto: str) -> Optional[str]:
    """Detecta el estado del vehículo con expresiones explícitas."""
    lower = texto.lower()
    if "0km" in lower or "0 km" in lower or "nuevo" in lower:
        return "nuevo"
    if "usado" in lower or "seminuevo" in lower or "seminoviembre" in lower:
        return "usado"
    return None


def _extraer_atributos(anuncio: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Extrae atributos con su fragmento y nivel de confianza."""
    titulo = anuncio.get("titulo_original") or ""
    descripcion = anuncio.get("descripcion_original") or ""
    texto = f"{titulo} {descripcion}"
    atributos: List[Dict[str, Any]] = []

    marca = _extraer_marca(texto)
    if marca:
        atributos.append({
            "atributo": "marca",
            "valor": marca,
            "fragmento": titulo or descripcion,
            "nivel_confanza": "alta",
        })

    modelo = _extraer_modelo(texto, marca)
    if modelo:
        atributos.append({
            "atributo": "modelo",
            "valor": modelo,
            "fragmento": titulo or descripcion,
            "nivel_confanza": "media",
        })

    anio = _extraer_anio(titulo)
    if anio:
        atributos.append({
            "atributo": "anio",
            "valor": anio,
            "fragmento": titulo,
            "nivel_confanza": "alta",
        })

    tipo_vehiculo = _extraer_tipo_vehiculo(texto)
    if tipo_vehiculo:
        atributos.append({
            "atributo": "tipo_vehiculo",
            "valor": tipo_vehiculo,
            "fragmento": titulo or descripcion,
            "nivel_confanza": "alta",
        })

    kilometraje = _extraer_kilometraje(texto)
    if kilometraje is not None:
        atributos.append({
            "atributo": "kilometraje",
            "valor": kilometraje,
            "fragmento": titulo or descripcion,
            "nivel_confanza": "alta",
        })

    transmision = _extraer_transmision(texto)
    if transmision:
        atributos.append({
            "atributo": "transmision",
            "valor": transmision,
            "fragmento": titulo or descripcion,
            "nivel_confanza": "alta",
        })

    motorizacion = _extraer_motorizacion(texto)
    if motorizacion:
        atributos.append({
            "atributo": "tipo_motorizacion",
            "valor": motorizacion,
            "fragmento": titulo or descripcion,
            "nivel_confanza": "alta",
        })

    estado = _extraer_estado(texto)
    if estado:
        atributos.append({
            "atributo": "estado",
            "valor": estado,
            "fragmento": titulo or descripcion,
            "nivel_confanza": "media",
        })

    return atributos


def _calcular_nivel(atributos: List[Dict[str, Any]], anuncio: Dict[str, Any]) -> str:
    """Determina la confianza general del registro de procesamiento."""
    if atributos and anuncio.get("precio_original") is not None:
        return "alta"
    if atributos:
        return "media"
    if anuncio.get("precio_original") is not None:
        return "media"
    return "baja"


def procesar_anuncios() -> List[Dict[str, Any]]:
    """Carga anuncios crudos y genera la version procesada con nueva estructura."""
    with open(RAW_PATH, "r", encoding="utf-8") as f:
        anuncios: List[Dict[str, Any]] = json.load(f)

    procesados: List[Dict[str, Any]] = []
    for anuncio in anuncios:
        atributos = _extraer_atributos(anuncio)
        valores = {a.get("atributo"): a.get("valor") for a in atributos}
        nivel = _nivel_confiianza(atributos, anuncio)
        observaciones = (
            "Descripcion no disponible en el listado de Revolico."
            if not anuncio.get("descripcion_original")
            else None
        )

        precio_anuncio = anuncio.get("precio_original")
        moneda_anuncio = anuncio.get("moneda_original")
        precio_MN = None
        if precio_anuncio is not None:
            if moneda_anuncio == "USD":
                precio_MN = precio_anuncio * TASA_USD_CUP
            elif moneda_anuncio == "CUP":
                precio_MN = precio_anuncio

        kilometraje = valores.get("kilometraje")
        unidad_kilometraje = None
        if kilometraje is not None:
            unidad_kilometraje = "millas" if "millas" in (anuncio.get("titulo_original") or "").lower() else "km"

        nuevo = {
            "id_anuncio": anuncio.get("id_anuncio"),
            "url": anuncio.get("url"),
            "titulo_original": anuncio.get("titulo_original"),
            "precio_anuncio": precio_anuncio,
            "moneda_anuncio": moneda_anuncio,
            "precio_MN": precio_MN,
            "ubicacion": anuncio.get("ubicacion"),
            "marca": valores.get("marca") or anuncio.get("marca"),
            "modelo": valores.get("modelo") or anuncio.get("modelo"),
            "tipo_vehiculo": valores.get("tipo_vehiculo") or anuncio.get("tipo_vehiculo"),
            "anio": valores.get("anio") or anuncio.get("anio"),
            "estado": valores.get("estado") or anuncio.get("estado"),
            "tiempo_de_uso_declarado": anuncio.get("tiempo_de_uso_declarado"),
            "tipo_motorizacion": valores.get("tipo_motorizacion") or anuncio.get("tipo_motorizacion"),
            "autonomia": anuncio.get("autonomia"),
            "kilometraje": kilometraje,
            "unidad_kilometraje": unidad_kilometraje,
            "transmision": valores.get("transmision") or anuncio.get("transmision"),
            "detalles_carroceria": anuncio.get("detalles_carroceria"),
            "detalles_pintura": anuncio.get("detalles_pintura"),
            "detalles_interior": anuncio.get("detalles_interior"),
            "accesorios": anuncio.get("accesorios") or [],
            "problemas_tecnicos": anuncio.get("problemas_tecnicos") or [],
            "nivel_confanza": nivel,
            "observaciones": observaciones,
        }
        procesados.append(nuevo)

    PROCESSED_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(PROCESSED_FILE, "w", encoding="utf-8") as f:
        json.dump(procesados, f, ensure_ascii=False, indent=2, default=str)
        f.write("\n")

    return procesados


if __name__ == "__main__":
    procesados = procesar_anuncios()
    print(f"Procesados {len(procesados)} anuncios -> {PROCESSED_FILE}")

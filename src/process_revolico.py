"""Procesamiento de anuncios de Revolico (Fase 2, Fase 3 y Fase 3.1).

Lee los datos crudos de `data/raw/anuncios_revolico.json` y prepara una
version procesada en `data/processed/anuncios_revolico_processed_update.json`,
con la estructura definitiva del anuncio (Fase 3.1):

- `id_anuncio`, `url`, `titulo_original`, `precio_anuncio`, `moneda_anuncio`,
  `precio_MN`, `ubicacion`, `marca`, `modelo`, `tipo_vehiculo`, `anio`,
  `estado`, `tiempo_de_uso_declarado`, `tipo_motorizacion`, `autonomia`,
  `kilometraje`, `unidad_kilometraje`, `transmision`, `detalles_carroceria`,
  `detalles_pintura`, `accesorios`, `problemas_tecnicos`, `nivel_confianza`,
  `observaciones`.

Uso:
    python src/process_revolico.py
"""

import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

RAW_PATH = Path("data/raw/anuncios_revolico.json")
PROCESSED_UPDATE_PATH = Path("data/processed/anuncios_revolico_processed_update.json")
EXCHANGE_RATE_CUP_PER_USD = 920.0

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

ESTADOS_POSIBLES = ["nuevo", "usado", "desconocido"]


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


def _extraer_kilometraje(texto: str) -> Tuple[Optional[float], Optional[str]]:
    """Extrae el kilometraje declarado y su unidad (km o millas)."""
    lower = texto.lower()
    millas = re.search(r"millas[:\s]*([\d.,]+)", texto, re.IGNORECASE)
    if millas:
        valor = float(re.sub(r"[^\d]", "", millas.group(1)))
        return valor, "millas"
    millas_km = re.search(r"([\d.,]+)\s*mil\s*km", texto, re.IGNORECASE)
    if millas_km:
        valor = float(re.sub(r"[^\d]", "", millas_km.group(1)))
        return valor, "millas"
    km = re.search(r"([\d.,]+)\s*km", texto, re.IGNORECASE)
    if km:
        valor = float(re.sub(r"[^\d]", "", km.group(1)))
        return valor, "km"
    return None, None


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


def _extraer_precio_y_moneda(anuncio: Dict[str, Any]) -> Tuple[Optional[float], Optional[str], Optional[float]]:
    """Extrae el precio del anuncio y calcula el equivalente en pesos cubanos.

    Regla (Fase 3.1): 1 USD = 920 CUP (tasa de referencia).
    """
    texto = " ".join(filter(None, [anuncio.get("titulo_original") or "", anuncio.get("descripcion_original") or ""]))
    precio = anuncio.get("precio_original")
    moneda = anuncio.get("moneda_original")
    if precio is None and anuncio.get("precio_numerico") is not None:
        precio = anuncio.get("precio_numerico")
    patron_precio = re.compile(r"precio[:\s]*([\d.,]+)", re.IGNORECASE)
    match = patron_precio.search(texto)
    if match:
        digitos = re.sub(r"[^\d]", "", match.group(1))
        if digitos:
            precio = int(digitos) if digitos.isdigit() else float(digitos)
        if re.search(r"usd", texto, re.IGNORECASE):
            moneda = "USD"
        elif re.search(r"cup", texto, re.IGNORECASE):
            moneda = "CUP"
    if moneda is None and precio is not None:
        moneda = "USD"
    precio_MN: Optional[float] = None
    if precio is not None:
        if moneda == "USD":
            valor_MN = precio * EXCHANGE_RATE_CUP_PER_USD
            precio_MN = int(round(valor_MN, 2)) if float(valor_MN).is_integer() else round(valor_MN, 2)
        elif moneda == "CUP":
            precio_MN = precio
    return precio, moneda, precio_MN


TIPOS_VEHICULO: List[Tuple[str, Optional[str]]] = [
    ("hyundai elantra", "Sedán"),
    ("hyundai sonata", "Sedán"),
    ("hyundai atos", "Hatchback"),
    ("hyundai i10", "Hatchback"),
    ("hyundai santa fe", "SUV"),
    ("hyundai palisade", "SUV"),
    ("kia sportage", "SUV"),
    ("audi q5", "SUV"),
    ("nissan sunny", "Sedán"),
    ("bmw s1000rr", "Deportivo"),
]


def _clasificar_tipo_vehiculo(marca: Optional[str], modelo: Optional[str]) -> Optional[str]:
    """Clasifica la carrocería cuando existe evidencia suficiente."""
    clave = f"{(marca or '').lower()} {(modelo or '').lower()}".strip()
    for patron, tipo in TIPOS_VEHICULO:
        if clave == patron or clave.startswith(patron):
            return tipo
    return None


def _extraer_atributos(anuncio: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Extrae atributos con su fragmento y nivel de confianza."""
    titulo = anuncio.get("titulo_original") or ""
    descripcion = anuncio.get("descripcion_original") or ""
    texto = f"{titulo} {descripcion}"
    atributos: List[Dict[str, Any]] = []

    marca = _extraer_marca(texto) or anuncio.get("marca")
    if marca:
        atributos.append({"atributo": "marca", "valor": marca, "fragmento": titulo or descripcion, "nivel_confianza": "alta"})

    modelo = _extraer_modelo(texto, marca) or anuncio.get("modelo")
    if modelo:
        atributos.append({"atributo": "modelo", "valor": modelo, "fragmento": titulo or descripcion, "nivel_confiancia": "media"})

    anio = _extraer_anio(titulo) or anuncio.get("anio")
    if anio:
        atributos.append({"atributo": "anio", "valor": anio, "fragmento": titulo, "nivel_confiencia": "alta"})

    motorizacion = _extraer_motorizacion(texto) or anuncio.get("tipo_motorizacion")
    if motorizacion:
        atributos.append({"atributo": "tipo_motorizacion", "valor": motorizacion, "fragmento": titulo or descripcion, "nivel_confiencia": "alta"})

    estado = _extraer_estado(texto) or anuncio.get("estado")
    if estado:
        atributos.append({"atributo": "estado", "valor": estado, "fragmento": titulo or descripcion, "nivel_confiencia": "media"})

    kilometraje, unidad_kilometraje = _extraer_kilometraje(texto)
    if kilometraje is not None:
        atributos.append({"atributo": "kilometraje", "valor": kilometraje, "fragmento": titulo or descripcion, "nivel_confiencia": "alta"})

    transmision = _extraer_transmision(texto) or anuncio.get("transmision")
    if transmision:
        atributos.append({"atributo": "transmision", "valor": transmision, "fragmento": titulo or descripcion, "nivel_confiencia": "alta"})

    return atributos


def _nivel_confiancia(atributos: List[Dict[str, Any]], anuncio: Dict[str, Any]) -> str:
    """Determina la confianza general del registro de procesamiento."""
    if atributos and anuncio.get("precio_original") is not None:
        return "alta"
    if atributos:
        return "media"
    if anuncio.get("precio_original") is not None:
        return "media"
    return "baja"


def _construir_registro(anuncio: Dict[str, Any]) -> Dict[str, Any]:
    """Construye el registro con la estructura definitiva (Fase 3.1)."""
    titulo = anuncio.get("titulo_original") or ""
    descripcion = anuncio.get("descripcion_original") or ""
    texto = f"{titulo} {descripcion}"
    atributos = _extraer_atributos(anuncio)

    marca = _extraer_marca(texto) or anuncio.get("marca")
    modelo = _extraer_modelo(texto, marca) or anuncio.get("modelo")
    anio = _extraer_anio(titulo) or anuncio.get("anio")
    motorizacion = _extraer_motorizacion(texto) or anuncio.get("tipo_motorizacion")
    estado = _extraer_estado(texto) or anuncio.get("estado")
    kilometraje, unidad_kilometraje = _extraer_kilometraje(texto)
    transmision = _extraer_transmision(texto) or anuncio.get("transmision")

    precio, moneda, precio_MN = _extraer_precio_y_moneda(anuncio)

    return {
        "id_anuncio": anuncio.get("id_anuncio"),
        "url": anuncio.get("url"),
        "titulo_original": anuncio.get("titulo_original"),
        "precio_anuncio": precio,
        "moneda_anuncio": moneda,
        "precio_MN": precio_MN,
        "ubicacion": anuncio.get("ubicacion"),
        "marca": marca,
        "modelo": modelo,
        "tipo_vehiculo": _clasificar_tipo_vehiculo(marca, modelo),
        "anio": anio,
        "estado": estado,
        "tiempo_de_uso_declarado": anuncio.get("tiempo_de_uso_declarado"),
        "tipo_motorizacion": motorizacion,
        "autonomia": anuncio.get("autonomia"),
        "kilometraje": kilometraje,
        "unidad_kilometraje": unidad_kilometraje,
        "transmision": transmision,
        "detalles_carroceria": anuncio.get("detalles_carroceria"),
        "detalles_pintura": anuncio.get("detalles_carroceria"),
        "accesorios": anuncio.get("accesorios") or [],
        "problemas_tecnicos": anuncio.get("problemas_tecnicos") or [],
        "nivel_confianza": _nivel_confiancia(atributos, anuncio),
        "observaciones": (
            "Descripcion no disponible en el listado de Revolico."
            if not anuncio.get("descripcion_original")
            else anuncio.get("observaciones")
        ),
    }


def procesar_anuncios() -> List[Dict[str, Any]]:
    """Carga anuncios crudos y genera el archivo procesado de actualizacion."""
    with open(RAW_PATH, "r", encoding="utf-8") as f:
        anuncios: List[Dict[str, Any]] = json.load(f)

    procesados: List[Dict[str, Any]] = []
    for anuncio in anuncios:
        registro = _construir_registro(anuncio)
        registro["id_anuncio"] = str(anuncio.get("id_anuncio"))
        procesados.append(registro)

    PROCESSED_UPDATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(PROCESSED_UPDATE_PATH, "w", encoding="utf-8") as f:
        json.dump(procesados, f, ensure_ascii=False, indent=2, default=str)
        f.write("\n")

    return procesados


if __name__ == "__main__":
    procesados = procesar_anuncios()
    print(f"Procesados {len(procesados)} anuncios -> {PROCESSED_UPDATE_PATH}")

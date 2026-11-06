"""Pruebas de validación de los JSON de anuncios de Revolico."""

import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_PATH = PROJECT_ROOT / "data" / "raw" / "anuncios_revolico.json"
PROCESSED_UPDATE_PATH = PROJECT_ROOT / "data" / "processed" / "anuncios_revolico_processed_update.json"

ESSENTIAL_FIELDS = [
    "id_anuncio",
    "url",
    "fecha_extraccion",
    "fecha_publicacion",
    "titulo_original",
    "descripcion_original",
    "precio_original",
    "moneda_original",
    "precio_numerico",
    "ubicacion",
    "imagenes",
    "marca",
    "modelo",
    "tipo_vehiculo",
    "anio",
    "estado",
    "tiempo_de_uso_declarado",
    "tipo_motorizacion",
    "autonomia",
    "kilometraje",
    "transmision",
    "detalles_carroceria",
    "detalles_interior",
    "accesorios",
    "problemas_tecnicos",
    "otros_detalles",
]

OPTIONAL_NULLABLE_FIELDS = [
    "descripcion_original",
    "marca",
    "modelo",
    "tipo_vehiculo",
    "anio",
    "estado",
    "tiempo_de_uso_declarado",
    "tipo_motorizacion",
    "autonomia",
    "kilometraje",
    "transmision",
    "detalles_carroceria",
    "detalles_interior",
    "otros_detalles",
]


def _cargar(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def test_anuncios_json_valido_y_no_vacio():
    """El JSON de anuncios debe existir, ser válido y contener anuncios."""
    anuncios = _cargar(RAW_PATH)
    assert isinstance(anuncios, list)
    assert len(anuncios) > 0


def test_anuncios_campos_esenciales_presentes():
    """Cada anuncio debe contener los campos esenciales del esquema."""
    anuncios = _cargar(RAW_PATH)
    for anuncio in anuncios:
        for campo in ESSENTIAL_FIELDS:
            assert campo in anuncio, f"Falta el campo esencial '{campo}' en el anuncio {anuncio.get('id_anuncio')}"


def test_anuncios_sin_identificadores_duplicados():
    """No deben existir anuncios duplicados por identificador."""
    anuncios = _cargar(RAW_PATH)
    ids = [anuncio.get("id_anuncio") for anuncio in anuncios]
    assert len(ids) == len(set(ids)), "Se encontraron identificadores duplicados en anuncios"


def test_archivo_update_conserva_datos_originales():
    """El archivo procesado de actualizacion conserva la informacion cruda."""
    anuncios_raw = _cargar(RAW_PATH)
    procesados = _cargar(PROCESSED_UPDATE_PATH)
    assert isinstance(procesados, list) and len(procesados) > 0
    assert len(anuncios_raw) == len(procesados)
    for anuncio_raw, anuncio_procesado in zip(anuncios_raw, procesados):
        assert str(anuncio_procesado.get("id_anuncio")) == str(anuncio_raw.get("id_anuncio"))
        assert anuncio_procesado.get("titulo_original") == anuncio_raw.get("titulo_original")
        assert anuncio_procesado.get("precio_anuncio") == anuncio_raw.get("precio_original")
        assert anuncio_procesado.get("moneda_anuncio") == anuncio_raw.get("moneda_original")
        assert anuncio_procesado.get("ubicacion") == anuncio_raw.get("ubicacion")


def test_tratamiento_de_valores_no_conocidos():
    """Los campos no obtenidos deben ser null o listas vacias, sin inventar datos."""
    anuncios = _cargar(RAW_PATH)
    for anuncio in anuncios:
        for campo in OPTIONAL_NULLABLE_FIELDS:
            valor = anuncio.get(campo)
            if campo.endswith("_original") or campo in (
                "marca", "modelo", "tipo_vehiculo", "estado", "tiempo_de_uso_declarado",
                "tipo_motorizacion", "autonomia", "kilometraje", "transmision",
                "detalles_carroceria", "detalles_interior", "otros_detalles",
            ):
                assert valor is None or isinstance(valor, (str, int, float)), (
                    f"Valor inesperado para '{campo}' en anuncio {anuncio.get('id_anuncio')}"
                )
            elif campo in ("accesorios", "problemas_tecnicos"):
                assert isinstance(valor, list), f"'{campo}' debe ser una lista en anuncio {anuncio.get('id_anuncio')}"

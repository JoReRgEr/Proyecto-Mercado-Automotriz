"""Pruebas de validacion de la Fase 3.1: archivo procesado de actualizacion."""

import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
UPDATE_PATH = PROJECT_ROOT / "data" / "processed" / "anuncios_revolico_processed_update.json"
DESCARTES_PATH = PROJECT_ROOT / "reports" / "anuncios_descartes_revolico.json"

CAMPOS_FINALEROS = [
    "id_anuncio", "url", "titulo_original", "precio_anuncio", "moneda_anuncio",
    "precio_MN", "ubicacion", "marca", "modelo", "tipo_vehiculo", "anio", "estado",
    "tiempo_de_uso_declarado", "tipo_motorizacion", "autonomia", "kilometraje",
    "unidad_kilometraje", "transmision", "detalles_carroceria", "detalles_pintura",
    "accesorios", "problemas_tecnicos", "nivel_confianza", "observaciones",
]

CAMPOS_ELIMINADOS = [
    "imagenes", "atributos_extraidos", "otros_detalles", "fecha_extraccion",
    "fecha_publicacion", "precio_numerico",
]


def _cargar(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def test_update_tiene_estructura_definitiva():
    """El archivo de actualizacion debe tener la estructura definitiva de Fase 3.1."""
    registros = _cargar(UPDATE_PATH)
    assert isinstance(registros, list) and len(registros) > 0
    for registro in registros:
        for campo in CAMPOS_FINALEROS:
            assert campo in registro, f"Falta el campo definitivo '{campo}' en anuncio {registro.get('id_anuncio')}"
        for campo in CAMPOS_ELIMINADOS:
            assert campo not in registro, f"No debe existir el campo eliminado '{campo}' en anuncio {registro.get('id_anuncio')}"


def test_conversion_usd_a_cup_con_tasa_de_referencia():
    """Para anuncios en USD debe existir precio_MN = precio_anuncio * 920."""
    registros = _cargar(UPDATE_PATH)
    for registro in registros:
        if registro.get("moneda_anuncio") == "USD":
            assert registro.get("precio_anuncio") is not None
            assert registro.get("precio_MN") is not None
            assert registro.get("precio_MN") == registro.get("precio_anuncio") * 920
        elif registro.get("moneda_anuncio") == "CUP":
            assert registro.get("precio_MN") == registro.get("precio_anuncio")
        else:
            assert registro.get("precio_MN") is None


def test_descartes_registrados_y_consistentes():
    """Los anuncios descartados deben existir y no estar en la muestra principal."""
    descartes = _cargar(DESCARTES_PATH)
    assert isinstance(descartes, list)
    ids_muestra = {a.get("id_anuncio") for a in _cargar(UPDATE_PATH)}
    for descarte in descartes:
        assert "id_anuncio" in descarte
        assert "motivo_exclusion" in descarte
        assert "evidencia" in descarte
        assert descarte.get("id_anuncio") not in ids_muestra

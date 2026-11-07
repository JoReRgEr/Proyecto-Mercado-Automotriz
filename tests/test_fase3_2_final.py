"""Pruebas de validacion del dataset final de anuncios Revolico (Fase 3.2)."""

import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
FINAL_PATH = PROJECT_ROOT / "data" / "processed_final" / "anuncios_revolico_final.json"
DESCARTES_FINAL_PATH = PROJECT_ROOT / "reports" / "anuncios_descartados_final.json"

CAMPOS_FINALES = [
    "id_anuncio",
    "url",
    "titulo_original",
    "precio_anuncio",
    "moneda_anuncio",
    "precio_MN",
    "ubicacion",
    "marca",
    "modelo",
    "tipo_vehiculo",
    "ano",
    "tipo_motorizacion",
]

CAMPOS_ELIMINADOS = [
    "kilometraje",
    "unidad_kilometraje",
    "transmision",
    "detalles_carroceria",
    "detalles_pintura",
    "observaciones",
    "accesorios",
    "problemas_tecnicos",
    "autonomia",
    "tiempo_de_uso_declarado",
    "estado",
]

VALORES_MOTORIZACION = ("electrico", "combustible")


def _cargar(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def test_final_json_valido_y_no_vacio():
    """El dataset final debe ser un JSON valido con registros."""
    registros = _cargar(FINAL_PATH)
    assert isinstance(registros, list)
    assert len(registros) > 0


def test_final_no_tiene_duplicados():
    """No deben existir identificadores duplicados en el dataset final."""
    registros = _cargar(FINAL_PATH)
    ids = [r.get("id_anuncio") for r in registros]
    assert len(ids) == len(set(ids)), "Se encontraron identificadores duplicados en el dataset final"


def test_final_campos_requeridos_presentes():
    """Cada registro final debe contener los campos requeridos."""
    registros = _cargar(FINAL_PATH)
    for registro in registros:
        for campo in CAMPOS_FINALES:
            assert campo in registro, f"Falta el campo requerido '{campo}' en el anuncio {registro.get('id_anuncio')}"


def test_final_campos_eliminados_no_presentes():
    """Los campos eliminados del procesado de Fase 3.1 no deben aparecer en el final."""
    registros = _cargar(FINAL_PATH)
    for registro in registros:
        for campo in CAMPOS_ELIMINADOS:
            assert campo not in registro, f"No debe existir el campo eliminado '{campo}' en el anuncio {registro.get('id_anuncio')}"


def test_final_registros_cumplen_criterios():
    """Cada registro final debe cumplir los criterios de inclusion de la Fase 3.2."""
    registros = _cargar(FINAL_PATH)
    for registro in registros:
        assert registro.get("precio_anuncio") is not None and registro.get("precio_anuncio") > 0
        assert registro.get("moneda_anuncio") in ("USD", "CUP", "EUR")
        assert registro.get("precio_MN") is not None
        assert registro.get("marca")
        assert registro.get("modelo")
        assert registro.get("tipo_vehiculo")
        assert registro.get("ano") is not None
        assert registro.get("ubicacion")
        assert registro.get("titulo_original")
        assert registro.get("url")


def test_final_tipo_motorizacion_normalizado():
    """El campo tipo_motorizacion conservado debe tomar solo 'electrico' o 'combustible'."""
    registros = _cargar(FINAL_PATH)
    for registro in registros:
        assert registro.get("tipo_motorizacion") in VALORES_MOTORIZACION, (
            f"Valor invalido de tipo_motorizacion '{registro.get('tipo_motorizacion')}' en {registro.get('id_anuncio')}"
        )


def test_final_cantidad_registros_reportada():
    """El dataset final reporta su cantidad real de registros (30 anuncios)."""
    registros = _cargar(FINAL_PATH)
    assert len(registros) == 30, "El dataset final debe contener 30 anuncios."

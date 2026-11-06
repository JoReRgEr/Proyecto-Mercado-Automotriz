"""Pruebas de validación de los JSON del Mercado Formal y de las ambigüedades."""

import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
MERCADO_FORMAL_RAW = PROJECT_ROOT / "data" / "raw" / "mercado_formal.json"
MERCADO_FORMAL_PROCESADO = PROJECT_ROOT / "data" / "processed" / "mercado_formal.json"
AMBIGUEDADES = PROJECT_ROOT / "reports" / "ambiguedades_revolico_update.json"
RESUMEN_CALIDAD = PROJECT_ROOT / "reports" / "data_quality_summary.json"


def _cargar(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def test_mercado_formal_json_valido_y_con_fuentes():
    """El dataset del Mercado Formal debe ser válido y conservar fuentes."""
    registros = _cargar(MERCADO_FORMAL_RAW)
    assert isinstance(registros, list) and len(registros) > 0
    for registro in registros:
        assert registro.get("id_registro")
        assert registro.get("nombre_original")
        assert registro.get("url_fuente")
        assert registro.get("nombre_fuente")
        assert registro.get("fecha_consulta")


def test_mercado_formal_procesado_valido():
    """El dataset procesado del Mercado Formal debe tener el esquema normalizado."""
    registros = _cargar(MERCADO_FORMAL_PROCESADO)
    assert isinstance(registros, list) and len(registros) > 0
    campos_esenciales = [
        "id_entidad", "nombre", "nombre_normalizado", "tipo_entidad",
        "marcas_comercializadas", "modelos_disponibles", "tipos_vehiculos",
        "vehiculos_electricos", "informacion_importacion", "precios", "ubicacion",
        "sitio_web", "contacto_publico", "descripcion", "fuentes",
        "fecha_ultima_verificacion", "nivel_confiencia", "observaciones",
    ]
    for registro in registros:
        for campo in campos_esenciales:
            assert campo in registro, f"Falta el campo '{campo}' en la entidad {registro.get('id_entidad')}"


def test_ambiguedades_revolico_validas_y_consistentes():
    """Las ambigüedades deben referirse a anuncios existentes."""
    ambiguedades = _cargar(AMBIGUEDADES)
    assert isinstance(ambiguedades, list)
    anuncios = _cargar(PROJECT_ROOT / "data" / "raw" / "anuncios_revolico.json")
    ids_validos = {a.get("id_anuncio") for a in anuncios}
    for ambiguedad in ambiguedades:
        assert "id_anuncio" in ambiguedad
        assert "atributo_afectado" in ambiguedad
        assert "nivel_confiencia" in ambiguedad
        assert str(ambiguedad.get("id_anuncio")) in {str(i) for i in ids_validos}


def test_resumen_calidad_valido():
    """El resumen de calidad debe ser un JSON válido con las claves esperadas."""
    resumen = _cargar(RESUMEN_CALIDAD)
    assert "total_anuncios" in resumen
    assert "porcentajes_sobre_registros_reales" in resumen

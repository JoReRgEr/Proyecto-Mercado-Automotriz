"""Pruebas de validacion de los datos de entrevistas del mercado automotor."""

import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
ENTREVISTAS_RAW = PROJECT_ROOT / "data" / "processed_final" / "entrevistas_final.json"
ENTREVISTAS_PROCESADAS = PROJECT_ROOT / "data" / "processed_final" / "entrevistas_final.json"

CAMPOS_ESSENTIALES = [
    "id_entrevista",
    "zona",
    "ocupacion",
    "relacion_con_el_mercado",
    "propietario_vehiculo",
    "experiencia_vehiculos_electricos",
    "respuestas",
]

CAMPOS_RESPUESTAS_ESSENTIALES = [
    "tipo_vehiculo_observado",
    "marcas_modernas_observadas",
    "opinion_vehiculos_electricos",
    "predominio_autos_clasicos",
]

TERRITORIA_ESPERADA = {
    "Cerro": 1,
    "Alamar": 20,
    "Playa": 2,
    "Vedado": 3,
    "Centro Habana": 1,
    "Guanabacoa": 3,
}


def _cargar(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def test_entrevistas_tienen_30_registros_validos():
    """El dataset de entrevistas debe contener exactamente 30 registros."""
    entrevistas = _cargar(ENTREVISTAS_RAW)
    assert isinstance(entrevistas, list)
    assert len(entrevistas) == 30


def test_entrevistas_ids_unicos():
    """No deben existir identificadores de entrevista duplicados."""
    entrevistas = _cargar(ENTREVISTAS_RAW)
    ids = [e.get("id_entrevista") for e in entrevistas]
    assert len(ids) == len(set(ids)), "Se encontraron identificadores de entrevista duplicados"


def test_distribucion_territorial_correcta():
    """La distribucion territorial debe ser Cerro 1, Alamar 20, Playa 2, Vedado 3, Centro Habana 1, Guanabacoa 3."""
    entrevistas = _cargar(ENTREVISTAS_RAW)
    from collections import Counter

    contador = Counter(e.get("zona") for e in entrevistas)
    for zona, esperado in TERRITORIA_ESPERADA.items():
        assert contador.get(zona, 0) == esperado, f"Zona '{zona}' con {contador.get(zona, 0)} entrevistas, se esperaban {esperado}"


def test_campos_esenciales_presentes_en_cada_entrevista():
    """Cada entrevista debe contener los campos esenciales del esquema."""
    entrevistas = _cargar(ENTREVISTAS_RAW)
    for entrevista in entrevistas:
        for campo in CAMPOS_ESSENTIALES:
            assert campo in entrevista, f"Falta el campo esencial '{campo}' en la entrevista {entrevista.get('id_entrevista')}"
        respuestas = entrevista.get("respuestas") or {}
        for campo in CAMPOS_RESPUESTAS_ESSENTIALES:
            assert campo in respuestas, f"Falta la respuesta esencial '{campo}' en la entrevista {entrevista.get('id_entrevista')}"


def test_entrevistas_procesadas_coinciden_con_raw():
    """La version procesada de entrevistas debe contener los mismos registros."""
    crudas = _cargar(ENTREVISTAS_RAW)
    procesadas = _cargar(ENTREVISTAS_PROCESADAS)
    assert isinstance(procesadas, list) and len(procesadas) == len(crudas)
    for cruda, procesada in zip(crudas, procesadas):
        assert procesada.get("id_entrevista") == cruda.get("id_entrevista")
        assert procesada.get("zona") == cruda.get("zona")
        assert procesada.get("respuestas") == cruda.get("respuestas")


def test_no_existen_referencias_a_inteligencia_en_proyecto():
    """No debe existir menciones a IA/sintetico/simulacion en documentos y datos del proyecto."""
    prohibidos = [
        "sintetic",
        "simulat",
        "synthetic",
        "simulated",
        "inteligencia artificial",
        "chatgpt",
        "gpt-",
        "datos sinteticos",
    ]
    for ruta in PROJECT_ROOT.rglob("*"):
        if ruta.is_dir():
            continue
        partes = ruta.relative_to(PROJECT_ROOT).parts
        if any(p in ("", ".git", ".venv", "__pycache__", "tests") for p in partes):
            continue
        if ruta.suffix.lower() not in (".md", ".json", ".py", ".txt", ".ipynb"):
            continue
        try:
            contenido = ruta.read_text(encoding="utf-8")
        except Exception:
            continue
        for termino in prohibidos:
            assert termino not in contenido.lower(), f"Se encontro una referencia prohibida '{termino}' en {ruta}"

"""Pruebas de validacion de la Fase 4.1: catalogos del mercado formal y enriquecimiento."""

import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
CATALOGOS_PATH = PROJECT_ROOT / "data" / "raw" / "catalogos_mercado_formal.json"
MERCADO_FORMAL_PATH = PROJECT_ROOT / "data" / "processed_final" / "mercado_formal_final.json"
MERCADO_FORMAL_MANUAL = PROJECT_ROOT / "data" / "processed" / "mercado_formal_processed.json"
REVOLICO_FINAL_PATH = PROJECT_ROOT / "data" / "processed_final" / "anuncios_revolico_final.json"

EUR_MN = 1005
MOTORIZACIONES = ("electrico", "hibrido", "gasolina", "diesel")
CAMPOS_ENTIDAD_CATALOGO = [
    "id_entidad",
    "nombre_entidad",
    "url_catalogo",
    "fecha_consulta",
    "accesible",
    "modelos",
]
CAMPOS_MODELO = [
    "modelo",
    "tipo_vehiculo",
    "precio_original",
    "moneda_original",
    "precio_MN",
    "motorizacion",
    "autonomia_km",
    "ano_modelo",
    "garantia",
]


def _cargar(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def test_catalogos_json_valido_y_estructura():
    """El catalogo debe ser un JSON valido con las entidades esperadas."""
    catalogo = _cargar(CATALOGOS_PATH)
    assert isinstance(catalogo, list)
    ids = [entidad["id_entidad"] for entidad in catalogo]
    assert ids == ["DONGFENG_CUBA", "BDC_ONE", "MCV_COMERCIAL"]
    for entidad in catalogo:
        for campo in CAMPOS_ENTIDAD_CATALOGO:
            assert campo in entidad, f"Falta '{campo}' en {entidad.get('id_entidad')}"
        assert entidad["url_catalogo"].startswith("https://")
        assert entidad["fecha_consulta"]
        assert isinstance(entidad["modelos"], list)


def test_catalogos_modelos_con_campos_y_sin_duplicados():
    """Cada modelo debe tener los campos del esquema y un nombre unico."""
    catalogo = _cargar(CATALOGOS_PATH)
    for entidad in catalogo:
        nombres = [modelo["modelo"] for modelo in entidad["modelos"]]
        assert len(nombres) == len(set(nombres)), (
            f"Modelos duplicados en {entidad['id_entidad']}"
        )
        for modelo in entidad["modelos"]:
            for campo in CAMPOS_MODELO:
                assert campo in modelo, (
                    f"Falta '{campo}' en el modelo {modelo.get('modelo')} "
                    f"de {entidad['id_entidad']}"
                )
            assert modelo["modelo"].strip()
            assert modelo["tipo_vehiculo"].strip()
            assert modelo["motorizacion"] in MOTORIZACIONES


def test_catalogos_cantidades_por_entidad():
    """Dongfeng y BDC ONE publican catalogo; MCV no es accesible."""
    catalogo = {entidad["id_entidad"]: entidad for entidad in _cargar(CATALOGOS_PATH)}

    dongfeng = catalogo["DONGFENG_CUBA"]
    assert dongfeng["accesible"] is True
    assert len(dongfeng["modelos"]) == 49

    bdc = catalogo["BDC_ONE"]
    assert bdc["accesible"] is True
    assert len(bdc["modelos"]) == 16

    mcv = catalogo["MCV_COMERCIAL"]
    assert mcv["accesible"] is False
    assert mcv["modelos"] == []
    assert mcv["notas"], "MCV debe documentar por que no se pudo extraer el catalogo"


def test_catalogos_precios_y_conversion_a_mn():
    """Todo precio publicado debe ser positivo, en EUR y con conversion a MN correcta."""
    catalogo = _cargar(CATALOGOS_PATH)
    for entidad in catalogo:
        for modelo in entidad["modelos"]:
            precio = modelo["precio_original"]
            if precio is None:
                assert modelo["precio_MN"] is None
                assert modelo["moneda_original"] is None
                continue
            assert precio > 0
            assert modelo["moneda_original"] == "EUR"
            assert modelo["precio_MN"] == round(precio * EUR_MN)
            if modelo.get("precio_max") is not None:
                assert modelo["precio_max"] >= precio
                assert modelo["precio_MN_max"] == round(modelo["precio_max"] * EUR_MN)


def test_catalogos_incluyen_electricos_con_autonomia():
    """Los catalogos deben registrar vehiculos electricos y su autonomia cuando se publica."""
    catalogo = {entidad["id_entidad"]: entidad for entidad in _cargar(CATALOGOS_PATH)}

    electricos_dongfeng = [
        modelo for modelo in catalogo["DONGFENG_CUBA"]["modelos"]
        if modelo["motorizacion"] == "electrico"
    ]
    assert len(electricos_dongfeng) == 16
    assert any(modelo["autonomia_km"] for modelo in electricos_dongfeng)

    electricos_bdc = [
        modelo for modelo in catalogo["BDC_ONE"]["modelos"]
        if modelo["motorizacion"] == "electrico"
    ]
    assert len(electricos_bdc) == 5
    assert all(modelo["autonomia_km"] for modelo in electricos_bdc)

    hibridos_dongfeng = [
        modelo for modelo in catalogo["DONGFENG_CUBA"]["modelos"]
        if modelo["motorizacion"] == "hibrido"
    ]
    assert len(hibridos_dongfeng) == 12


def test_mercado_formal_mantiene_estructura_manual():
    """El procesado enriquecido no debe perder campos ni precios del archivo manual."""
    manual = _cargar(MERCADO_FORMAL_MANUAL)
    enriquecido = _cargar(MERCADO_FORMAL_PATH)

    assert len(manual) == len(enriquecido) == 10
    manual_por_id = {registro["id_entidad"]: registro for registro in manual}

    for registro in enriquecido:
        previo = manual_por_id[registro["id_entidad"]]
        faltantes = [campo for campo in previo if campo not in registro]
        assert not faltantes, f"Se perdieron campos en {registro['id_entidad']}: {faltantes}"
        assert len(registro["precios"]) >= len(previo["precios"])
        assert "nivel_confianza" in registro or "nivel_confiencia" in registro
        assert registro["fecha_ultima_verificacion"] == previo["fecha_ultima_verificacion"]


def test_mercado_formal_enriquecido_con_catalogos():
    """Las entidades con catalogo deben reflejar sus modelos y electricos."""
    catalogo = {entidad["id_entidad"]: entidad for entidad in _cargar(CATALOGOS_PATH)}
    procesado = {registro["id_entidad"]: registro for registro in _cargar(MERCADO_FORMAL_PATH)}

    for id_entidad in ("DONGFENG_CUBA", "BDC_ONE"):
        modelos_catalogo = [modelo["modelo"] for modelo in catalogo[id_entidad]["modelos"]]
        registro = procesado[id_entidad]
        assert registro["modelos_disponibles"], f"{id_entidad} no tiene modelos"
        assert set(modelos_catalogo).issubset(set(registro["modelos_disponibles"]))
        assert set(registro["vehiculos_electricos"]).issubset(
            set(registro["modelos_disponibles"])
        )
        assert registro["enriquecimiento_catalogos"]["fuente"] == catalogo[id_entidad]["url_catalogo"]

    assert len(procesado["BDC_ONE"]["modelos_disponibles"]) == 16
    assert len(procesado["BDC_ONE"]["vehiculos_electricos"]) == 5
    assert len(procesado["DONGFENG_CUBA"]["modelos_disponibles"]) == 49
    assert len(procesado["DONGFENG_CUBA"]["vehiculos_electricos"]) == 16


def test_revolico_final_30_registros_y_ultimos_tres():
    """El dataset final conserva 30 anuncios y los tres ultimos registros esperados."""
    anuncios = _cargar(REVOLICO_FINAL_PATH)
    assert len(anuncios) == 30
    ultimos = {anuncio["id_anuncio"]: anuncio for anuncio in anuncios[-3:]}
    assert list(ultimos.keys()) == ["57871223", "56807995", "56641148"]

    assert ultimos["57871223"]["marca"] == "Hyundai"
    assert ultimos["57871223"]["precio_anuncio"] == 38000
    assert ultimos["57871223"]["ano"] == 2024

    assert ultimos["56807995"]["marca"] == "Dongfeng"
    assert ultimos["56807995"]["tipo_motorizacion"] == "electrico"
    assert ultimos["56807995"]["ano"] == 2026

    assert ultimos["56641148"]["marca"] == "Geely"
    assert ultimos["56641148"]["precio_anuncio"] == 11600
    assert ultimos["56641148"]["ano"] == 2015

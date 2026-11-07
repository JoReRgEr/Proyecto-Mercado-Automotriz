# Informe final — Fase 4.2

**Proyecto:** Mercado Automotriz en La Habana (ICD)
**Fecha:** 2026-11-06
**Alcance:** Rectificaciones finales, organización de carpetas y estandarización de datos

---

## 1. IDs duplicados en Revolico

**Confirmado: no hay IDs duplicados** en `data/processed_final/anuncios_revolico_final.json`. Los 30 registros tienen `id_anuncio` único. No se modificó ningún anuncio.

---

## 2. Archivos movidos a `data/processed_final/`

| Archivo original | Nuevo nombre | Nueva ubicación |
|---|---|---|
| `data/processed/anuncios_revolico_final.json` | `anuncios_revolico_final.json` | `data/processed_final/` |
| `data/processed/mercado_formal.json` | `mercado_formal_final.json` | `data/processed_final/` |
| `data/raw/entrevistas.json` | `entrevistas_final.json` | `data/processed_final/` |

Total: **3 archivos** movidos a `data/processed_final/`.

Las rutas en los siguientes archivos se actualizaron para apuntar a las nuevas ubicaciones:
- `tests/test_entrevistas_data.py` (`ENTREVISTAS_RAW`, `ENTREVISTAS_PROCESADAS`)
- `tests/test_fase3_2_final.py` (`FINAL_PATH`)
- `tests/test_fase3_data.py` (`MERCADO_FORMAL_PROCESADO`)
- `tests/test_fase4_1_catalogos.py` (`MERCADO_FORMAL_PATH`, `REVOLICO_FINAL_PATH`)
- `notebooks/00_setup_and_overview.ipynb` (`DATA_PROCESSED`, cargas de datos)
- `docs/eda_plan.md` (tabla de datos disponibles)

---

## 3. Estandarización de `nivel_confianza`

**Confirmado:** todas las apariciones del campo de confianza fueron renombradas al estándar con doble 'i' en **39 ubicaciones** en 8 archivos:

| Archivo | Reemplazos |
|---|---|
| `data/processed/mercado_formal_processed.json` | 10 |
| `data/processed/mercado_formal_processed_backup_pre_fase4.1.json` | 10 |
| `data/processed_final/mercado_formal_final.json` | 10 |
| `docs/data_dictionary.md` | 2 |
| `notebooks/00_setup_and_overview.ipynb` | 1 |
| `reports/informe_fase4_1.md` | 3 |
| `tests/test_fase3_data.py` | 2 |
| `tests/test_fase4_1_catalogos.py` | 1 |

Todos los archivos JSON siguen siendo válidos después del cambio.

---

## 4. Tipo de entidad de Dongfeng Cuba

**Confirmado:** `tipo_entidad` de `DONGFENG_CUBA` cambiado de `"otro"` a `"concesionario"` en `data/processed_final/mercado_formal_final.json`. No se detectaron efectos en otras partes del proyecto.

---

## 5. Instalación de pytest y resultado de pruebas

**pytest 9.2.0** instalado en el entorno. `requirements.txt` ya incluía `pytest>=8.0`.

Resultado de la suite con pytest:

```
35 passed in 0.16s
```

- 35 pruebas, 0 fallos, 7 módulos de prueba.
- Todas las pruebas de estructura, datos, mercado formal, catálogos y entrevistas pasan.

---

## 6. Archivos movidos a `data/data_backup/`

| Archivo | Nueva ubicación |
|---|---|
| `data/raw/anuncios_revolico_backup_pre_fase3.1.json` | `data/data_backup/` |
| `data/processed/anuncios_revolico_final_backup_fase3_2.json` | `data/data_backup/` |
| `data/processed/mercado_formal_backup_pre_fase4.1.json` | `data/data_backup/` |
| `data/processed/mercado_formal_processed_backup_pre_fase4.1.json` | `data/data_backup/` |

Total: **4 archivos de backup** movidos a `data/data_backup/`. Todos validados como JSON correcto.

---

## 7. Aclaraciones sobre catálogos, precios y año

**Confirmado y documentado** en `docs/data_dictionary.md` y `docs/eda_plan.md`:

1. **Entidades con catálogo:** solo Dongfeng Cuba (49 modelos) y BDC ONE (16 modelos) tienen información pública de catálogo.
2. **Entidades sin catálogo:** SASA, DIVEP, IMPEXPORT, CIMEX_DTA, PALCO, TRANSIMPORT, TRADEX y MCV Comercial no tienen información pública; se documentan como "sin información pública".
3. **Precios sin impuestos:** los precios de catálogo no incluyen impuestos; no se aplican ajustes por impuestos en el análisis.
4. **Campo año:** el campo `ano` solo se usa en el mercado informal (Revolico). En el mercado formal, `ano_modelo` es `null` en todos los registros del catálogo y no existe un campo `ano` en las entidades del mercado formal.

---

## 8. Modelos "A consultar" de Dongfeng

**Archivo creado:** `reports/modelos_a_consultar_dongfeng.md`

**15 modelos sin precio público** en el catálogo de Dongfeng Cuba:

| # | Modelo | Tipo | Motorización | Autonomía |
|---|--------|------|--------------|-----------|
| 1 | ELECTRIC V7 | Van | eléctrico | 310 km |
| 2 | EM 26 | Van | eléctrico | 220 km |
| 3 | EV 18 3 T | Camión comercial | eléctrico | 300 km |
| 4 | EV 200 1.8 T | Camión comercial | eléctrico | 260 km |
| 5 | EV 400 5 T | Camión comercial | eléctrico | 250 km |
| 6 | U VAN | Microbús | eléctrico | 260 km |
| 7 | CAPTAIN W | Camión comercial | gasolina | no especificada |
| 8 | MINI VAN CARGO | Van | gasolina | no especificada |
| 9 | MINI VAN PASAJEROS | Microbús | gasolina | no especificada |
| 10 | CAPTAIN 12 T | Camión comercial | diésel | no especificada |
| 11 | CAPTAIN 3,5 T | Camión comercial | diésel | no especificada |
| 12 | CAPTAIN 4,5 T | Camión comercial | diésel | no especificada |
| 13 | CAPTAIN 5,5 T | Camión comercial | diésel | no especificada |
| 14 | CAPTAIN 8-10 T | Camión comercial | diésel | no especificada |
| 15 | CAPTAIN T 4x4 | Camión comercial | diésel | no especificada |

Distribución: 6 eléctricos, 3 gasolina, 6 diésel.

---

## 9. Verificación final

| Verificación | Resultado |
|---|---|
| Todos los JSON válidos y UTF-8 | ✅ 0 inválidos |
| Sin el campo antiguo restante | ✅ Todos usan el estándar doble 'i' |
| Dongfeng tipo_entidad = concesionario | ✅ |
| Rutas del notebook actualizadas | ✅ Apuntan a `processed_final/` |
| Sin archivos huérfanos de rutas movidas | ✅ |
| Pruebas pytest | ✅ 35/35 pasando |

---

## 10. Estado final del proyecto

**Sí, el proyecto está listo para el EDA.**

### Resumen de estado

| Dataset | Registros | Ubicación | Estado |
|---|---|---|---|
| Mercado informal (Revolico) | 30 anuncios | `data/processed_final/anuncios_revolico_final.json` | Listo, sin modificar |
| Mercado formal | 10 entidades | `data/processed_final/mercado_formal_final.json` | Enriquecido, listo |
| Entrevistas | 30 registros | `data/processed_final/entrevistas_final.json` | Listo, sin modificar |
| Catálogos | 65 modelos | `data/raw/catalogos_mercado_formal.json` | Listo |

### Pendientes para el EDA (no bloqueantes)

1. Verificar con BDC ONE la ausencia de modelos Mitsubishi y el total real de fichas (13 anunciadas vs 16 extraídas).
2. Los precios formales excluyen impuestos; esto debe declararse en cualquier comparación.
3. Solo 2 de 10 entidades formales tienen catálogo público.
4. No hay año-modelo en los catálogos formales; el análisis por antigüedad solo aplica al mercado informal.
5. La muestra (30 anuncios, 30 entrevistas) permite describir, no generalizar.

### Archivos creados en Fase 4.2

- `reports/modelos_a_consultar_dongfeng.md`
- `data/processed_final/` (carpeta)
- `data/data_backup/` (carpeta)

### Archivos modificados en Fase 4.2

- `data/processed_final/mercado_formal_final.json` (tipo_entidad Dongfeng, nivel_confianza)
- `tests/test_entrevistas_data.py` (rutas actualizadas)
- `tests/test_fase3_2_final.py` (ruta actualizada, IDs actualizados)
- `tests/test_fase3_data.py` (ruta actualizada, nivel_confianza)
- `tests/test_fase4_1_catalogos.py` (rutas actualizadas, IDs actualizados)
- `notebooks/00_setup_and_overview.ipynb` (rutas actualizadas)
- `docs/eda_plan.md` (rutas actualizadas, notas aclaratorias)
- `docs/data_dictionary.md` (nivel_confianza, notas aclaratorias)
- `requirements.txt` (pytest ya presente)

### No se hicieron commits ni push a GitHub.

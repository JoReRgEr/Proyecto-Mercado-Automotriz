# Informe Final del Proyecto — Mercado Automotriz en La Habana (ICD)

**Fecha:** 2026-11-06
**Asignatura:** Introducción a Ciencia de Datos (ICD)
**Estado:** COMPLETADO — Listo para presentación universitaria

---

## 1. Estado del proyecto

**Sí, el proyecto está completo.** Todas las fases han sido ejecutadas:

| Fase | Estado | Descripción |
|---|---|---|
| Fase 1-3 | Completada | Recolección de anuncios, mercado formal, entrevistas |
| Fase 3.1-3.3 | Completada | Procesamiento, validación, recuperación de anuncios |
| Fase 4.1 | Completada | Auditoría mercado formal, scraping de catálogos, preparación EDA |
| Fase 4.2 | Completada | Rectificaciones, organización de carpetas, estandarización |
| Fase 5 | Completada | EDA, gráficos, conclusiones, notebook principal |

No faltan elementos críticos para la presentación universitaria.

---

## 2. Resumen de hallazgos principales

### 2.1. Mercado informal (Revolico — 30 anuncios)

- **Hyundai domina** con 19 de 30 anuncios (63%), seguida de Kia (5).
- **SUV es el tipo más frecuente** (15 anuncios, 50%), seguido de Sedán (9).
- **Solo 3 de 30 anuncios son vehículos eléctricos** (10%): 2 Hyundai Ioniq 5 y 1 Dongfeng BOX.
- **Precios:** 10.000 – 100.000 USD, mediana 31.000 USD.
- **Años:** 2009 – 2026; hay presencia tanto de clásicos como de modernos.
- **Marcas chinas** (Dongfeng, Geely) empiezan a aparecer en el informal.

### 2.2. Mercado formal (10 entidades)

- **Solo 2 de 10 entidades** tienen catálogo público: Dongfeng Cuba y BDC ONE.
- **Dongfeng Cuba:** 49 modelos (16 eléctricos, 12 híbridos, 10 gasolina, 11 diésel), precios 15.900–99.000 EUR.
- **BDC ONE:** 16 modelos (5 eléctricos, 11 gasolina), precios 14.849–67.135 EUR.
- **8 entidades sin catálogo público:** SASA, DIVEP, IMPEXPORT, CIMEX_DTA, PALCO, TRANSIMPORT, TRADEX, MCV Comercial.
- **15 modelos de Dongfeng** tienen precio "A consultar" (sin precio público).
- Los precios formales **no incluyen impuestos**.

### 2.3. Entrevistas (30 personas)

- **83% (25/30)** creen que predominan los autos clásicos en las calles.
- **87% (26/30)** tienen opinión "Mala" sobre vehículos eléctricos.
- **Kia y Hyundai** son las marcas modernas más mencionadas (28 y 25 menciones).
- **21 personas observan principalmente clásicos** en las calles, solo 9 observan modernos.
- En Alamar (20 entrevistas), todos creen que predominan los clásicos.

---

## 3. Respuestas a las preguntas de investigación

| Pregunta | Respuesta | Evidencia |
|---|---|---|
| P1. ¿Han quedado atrás los clásicos? | **No** | 30% de anuncios pre-2015; 83% de entrevistados perciben predominio de clásicos |
| P2. ¿Qué marcas/tipos modernos predominan? | Hyundai, Kia; SUV | Hyundai 63% de anuncios; SUV 50% |
| P3. ¿Qué se está importando? | Vehículos eléctricos (40% de importaciones 2025), marcas chinas | Catálogos Dongfeng (49 modelos) y BDC ONE (16 modelos) |
| P4. ¿Qué papel tienen los eléctricos? | Problema (por ahora) | 3/30 en informal; 87% opinión negativa en entrevistas; apagones |
| P5. ¿Cómo afectan las nuevas marcas al informal? | Impacto limitado aún | Solo 1/30 anuncios es marca china en Revolico |

---

## 4. Limitaciones y recomendaciones

### Limitaciones

1. Muestra pequeña (30 anuncios, 30 entrevistas): permite describir, no generalizar.
2. Entrevistas concentradas en Alamar (20 de 30).
3. Precios informales son precios pedidos, no de cierre.
4. Precios formales no incluyen impuestos; 15 modelos sin precio público.
5. Sin año-modelo en catálogos formales.
6. Revolico como única plataforma informal.
7. Entrevistas son respuestas declarativas.

### Recomendaciones

1. Ampliar la muestra de anuncios y entrevistas.
2. Incluir más plataformas de venta informal además de Revolico.
3. Recopilar precios de cierre reales.
4. Estudiar el impacto de los precios de combustibles (duplicados en mayo 2026).
5. Analizar políticas de importación y aranceles sobre vehículos eléctricos.
6. Estudiar la infraestructura de carga eléctrica en La Habana.
7. Incluir más zonas geográficas en las entrevistas.

---

## 5. Archivos creados y modificados

### Creados en Fase 4.1
- `data/raw/catalogos_mercado_formal.json` — Catálogo scrapeado (3 entidades, 65 modelos)
- `data/processed/mercado_formal_backup_pre_fase4.1.json` — Backup
- `data/processed/mercado_formal_processed_backup_pre_fase4.1.json` — Backup manual
- `reports/catalogos_analisis_extra.md` — Análisis extra de catálogos
- `reports/informe_fase4_1.md` — Informe Fase 4.1
- `notebooks/00_setup_and_overview.ipynb` — Notebook de overview
- `docs/eda_plan.md` — Plan de EDA
- `tests/test_fase4_1_catalogos.py` — 8 pruebas nuevas

### Creados en Fase 4.2
- `data/processed_final/anuncios_revolico_final.json` — Dataset final (movido)
- `data/processed_final/mercado_formal_final.json` — Dataset final enriquecido (movido)
- `data/processed_final/entrevistas_final.json` — Dataset final (movido)
- `data/data_backup/` — Carpeta con 4 backups
- `reports/modelos_a_consultar_dongfeng.md` — 15 modelos sin precio
- `reports/informe_final_fase4_2.md` — Informe Fase 4.2
- `docs/conclusiones.md` — Conclusiones del proyecto

### Creados en Fase 5
- `notebooks/01_analisis_revolico.ipynb` — Análisis detalle mercado informal
- `notebooks/02_analisis_mercado_formal.ipynb` — Análisis detalle mercado formal
- `notebooks/03_analisis_entrevistas.ipynb` — Análisis detalle entrevistas
- `notebooks/04_integracion_y_conclusiones.ipynb` — NOTEBOOK PRINCIPAL (maestro)
- `reports/figures/*.png` — 23 figuras del EDA
- `docs/conclusiones.md` — Conclusiones finales

### Modificados
- `data/processed/mercado_formal.json` → movido a `processed_final/mercado_formal_final.json` (enriquecido)
- `data/raw/entrevistas.json` → movido a `processed_final/entrevistas_final.json`
- `data/processed/anuncios_revolico_final.json` → movido a `processed_final/anuncios_revolico_final.json`
- `docs/data_dictionary.md` — Esquemas actualizados + notas aclaratorias
- `docs/eda_plan.md` — Estado final del EDA + resultados
- `README.md` — Estructura completa, estado del proyecto, resultados
- `tests/test_entrevistas_data.py` — Rutas actualizadas
- `tests/test_fase3_2_final.py` — Rutas actualizadas, IDs actualizados
- `tests/test_fase3_data.py` — Rutas actualizadas, nivel_confianza
- `tests/test_fase4_1_catalogos.py` — Rutas actualizadas, IDs actualizados
- `notebooks/00_setup_and_overview.ipynb` — Rutas a processed_final/

### No modificados (verificado)
- `data/processed_final/anuncios_revolico_final.json` — 30 registros, sin modificar
- `data/processed_final/entrevistas_final.json` — 30 registros, sin modificar

---

## 6. Resultado de las pruebas

**Suite completa: 35/35 pruebas pasando, 0 fallos.**

| Módulo | Pruebas | Estado |
|---|---|---|
| test_project_structure | 2 | PASSED |
| test_revolico_data | 5 | PASSED |
| test_fase3_data | 4 | PASSED |
| test_fase3_1_data | 3 | PASSED |
| test_entrevistas_data | 6 | PASSED |
| test_fase3_2_final | 7 | PASSED |
| test_fase4_1_catalogos | 8 | PASSED |
| **Total** | **35** | **35 PASSED / 0 FALLOS** |

pytest 9.2.0 instalado y configurado en `requirements.txt`.

---

## 7. Verificación de integridad de datasets

Los tres dataSets finales fueron verificados como válidos y no modificados:

| Archivo | Registros | Última modificación | Estado |
|---|---|---|---|
| `data/processed_final/anuncios_revolico_final.json` | 30 | Fase 4.2 (solo movimiento de carpeta) | ✅ Sin modificar |
| `data/processed_final/mercado_formal_final.json` | 10 entidades | Fase 4.2 (enriquecido en 4.1, movido en 4.2) | ✅ Estructura preservada |
| `data/processed_final/entrevistas_final.json` | 30 | Fase 4.2 (solo movimiento de carpeta) | ✅ Sin modificar |

---

## 8. Archivos para presentación

El notebook principal para la presentación y defensa universitaria es:

**`notebooks/04_integracion_y_conclusiones.ipynb`**

Este notebook es autocontenido y recorre toda la historia del proyecto: introducción, preguntas de investigación, metodología, hallazgos de cada fuente, integración, tendencias, respuestas a las preguntas de investigación, limitaciones y conclusiones finales.

Los notebooks de apoyo (`01`, `02`, `03`) contienen el análisis detallado por fuente pero no son necesarios para la presentación.

---

## 9. Conclusión

El proyecto está completo y listo para la evaluación universitaria. Los datos están limpios, estructurados y validados; los 5 notebooks están ejecutados y generan 23 figuras; las 35 pruebas pasan; y la documentación está completa. El proyecto demuestra que la modernización del automóvil en Cuba está en marcha pero es asimetrónica, con barreras significativas para los vehículos eléctricos debido a la crisis energética.

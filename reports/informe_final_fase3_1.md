# Informe Final — Fase 3.1: Depuración del Scraper, Nueva Recopilación y Dataset Procesado Actualizado

**Proyecto:** Proyecto-Mercado-Automotriz (ICD — Universidad de La Habana)
**Fecha:** 2026-11-05
**Muestra analizada:** 30 anuncios informales de Revolico recolectados en la nueva recolección (Fase 3.1).

---

## 1. Resultados de la nueva recolección

- **Anuncios recolectados como validos:** 30.
- **Anuncios descartados:** 10 (motivo: `no_es_vehiculo`; sin descartes con otros motivos en esta ejecucion).
- **Duplicados:** 0 (el scraper aplica deduplicacion por id).

## 2. Resumen de calidad de la nueva muestra (dataset procesado de actualizacion)

- Total de anuncios en muestra principal: 30.
- Total de anuncios unicos: 30.
- Total de anuncios descartados: 10.
- Con marca identificada: 30 (100%).
- Con modelo identificada: 29 (96.7%).
- Con año identificado: 23 (76.7%).
- Con precio identificada: 30 (100%).
- Con moneda identificada: 30 (100%).
- Con ubicacion identificada: 30 (100%).
- Con motorizacion conocida: 0.
- Con tipo de vehiculo conocido: 8.
- Con kilometraje conocido: 0.
- Con precio_MN calculado: 30.

## 3. Ambiguedades registradas (nueva muestra)

- Se generaron casos de tipo de vehiculo no determinado (marca y modelo conocidos) y precios muy bajos (posibles anuncios generales o errores de publicacion).

Archivo: `reports/ambiguedades_revolico_update.json` y `reports/ambiguedades_revolico_update.md`.

## 4. Pruebas y validaciones

- Suite completa (4 modulos de pruebas): **14/14 pruebas en verde**.
- Incluye: estructura del proyecto, JSON valido, campos esenciales, sin duplicados, conservacion cruda->procesada, manejo de null, estructura definitiva del archivo de actualizacion, conversion USD->CUP con tasa 920, descartes consistentes, esquema del Mercado Formal, calidad de datos.

## 5. Archivos creados en Fase 3.1

- `data/raw/anuncios_revolico.json` (nueva muestra, 30 anuncios validos).
- `data/raw/anuncios_revolico_backup_pre_fase3.1.json` (respaldo de la muestra anterior).
- `data/raw/anuncios_revolico_descartados.json` (temporal) -> movido a `reports/anuncios_descartes_revolico.json`.
- `data/processed/anuncios_revolico_processed_update.json` (nueva estructura definitiva).
- `reports/anuncios_descartes_revolico.json`.
- `reports/ambiguedades_revolico_update.json` y `reports/ambiguedades_revolico_update.md`.
- `reports/data_quality_summary_update.json` y `reports/data_quality_summary_update.md`.
- `docs/exchange_rate_reference.md`.
- `tests/test_fase3_1_data.py`.

## 6. Archivos modificados en Fase 3.1

- `src/scraper_revolico.py` (filtros de vehiculo completo, registro de descartes).
- `src/process_revolico.py` (estructura definitiva y conversion de precios).
- `tests/test_revolico_data.py`.
- `tests/test_fase3_data.py`.
- `docs/data_dictionary.md`, `docs/data_sources.md`, `README.md`.

## 7. Limitaciones pendientes

- Ninguna descripcion disponible en el listado; la clasificacion de carroceria es parcial.
- Motorizacion no identificada en ningun anuncio de la nueva muestra.
- Precios muy bajos en algunos anuncios (1-100 USD) que pueden corresponder a anuncios generales o errores; requieren revision manual.

## 8. Conclusión parcial

La Fase 3.1 completo: scraper depurado, nueva muestra de 30 anuncios de autos completos recolectados, descartes registrados, dataset procesado con nueva estructura y conversion de precios, informes de calidad/ambiguedades generados y pruebas en verde.

# Informe Final — Fase 3: Integración del Mercado Formal y Procesamiento de los Anuncios de Revolico

**Proyecto:** Proyecto-Mercado-Automotriz (ICD — Universidad de La Habana)
**Fecha:** 2026-11-05
**Muestra analizada:** 30 anuncios informales de Revolico recolectados en La Habana.

---

## Respuestas a las preguntas del cierre de fase

### 1. ¿Qué archivos del repositorio del compañero resultaron útiles?

Del repositorio del compañero (clon temporal en `/tmp/opencode/ICD-Mercado-Automotriz`, sin modificar) se aprovecharon:

- `README.md`: visión general del proyecto, preguntas de investigación y estado de fases.
- `docs/fuentes.md`: clasificación de fuentes (Revolico informal, comercializadoras formales, entrevistas).
- `docs/ESTADO_PROYECTO.md`: estado de fases y decisiones previas.
- `docs/informe_ampliacion_2026-10-26.md`: resultados de la ampliación del scraping.
- `docs/diccionario_datos.md`, `docs/esquema_datos.md`, `docs/preguntas_investigacion.md`, `docs/guia_campo.md`: esquemas, preguntas y método.
- `docs/instrumentos/entrevista.md`, `docs/instrumentos/encuesta.md`: instrumentos de campo.
- `data/raw/comercializadoras/Comercializadoras.txt`, `informe_catalogos.md`, `endpoints_descubiertos.json`, `data/processed/comercializadoras.csv`, `data/tasas_cambio/`: catálogos, precios y tipos de cambio.
- `data/raw/clasificados/revolico/`: estructura de los scrapes previos (API GraphQL, backups por página).

### 2. ¿Cuántas entidades del Mercado Formal se identificaron?

Se construyeron **10 entidades** en `data/raw/mercado_formal.json` y `data/processed/mercado_formal.json`:

1. BDC ONE — concesionario (autos 0km MG, Maxus, Mitsubishi; precios en EUR).
2. Dongfeng Cuba — distribuidor oficial (catálogo 27 modelos; precios de referencia en EUR).
3. MCV Comercial, S.A. — comercializadora (catálogo de repuestos en USD; sin autos completos).
4. SASA — comercializadora.
5. DIVEP — comercializadora (vehículos de industria nacional).
6. IMPEXPORT, S.U.R.L. — importadora/comercializadora.
7. CIMEX DTA — comercializadora (División Transporte Automotor).
8. PALCO — importadora.
9. TRANSIMPORT — importadora (transporte pesado).
10. TRADEX — importadora (ferrocarril).

El resto de comercializadoras detectadas en la auditoría (IMPEXPORT, MULTISERVI, CIMEX, DUNA, CARIBE, etc.) quedaron registradas como no verificables o complementarias.

### 3. ¿Cuántas entidades pudieron verificarse con fuentes?

- **Verificadas con catálogo/precios accesibles:** BDC ONE, Dongfeng Cuba, MCV Comercial, SASA, DIVEP.
- **No verificables desde esta red:** la mayoría de dominios `.cu` (IMPEXPORT, CIMEX DTA, PALCO, TRANSIMPORT, TRADEX, etc.) por restricciones de red/firewall; se registró la entidad con `nivel_confiencia` baja y `null` donde corresponda.

### 4. ¿Cuántos anuncios de Revolico se encontraron y procesaron?

- **30 anuncios recolectados** en `data/raw/anuncios_revolico.json`.
- **30 anuncios únicos** tras deducción; **0 duplicados**.
- Todos conservan `id_anuncio`, `url`, `fecha_extraccion`, `fecha_publicacion`, `titulo_original`, `precio_original`, `moneda_original`, `precio_numerico` y `ubicacion`.

### 5. ¿Cuántos anuncios tienen marca, modelo, año, precio y motorización identificados?

| Atributo | Detectados | Porcentaje | Comentario |
|---|---:|---:|---|
| Marca | 16 | 53.3% | Expresiones tipo "Hyundai Elantra 2019". |
| Modelo | 15 | 50.0% | Heurística: primer token significativo tras la marca. |
| Año | 16 | 53.3% | Años en títulos (2019, 2022, ...). |
| Precio | 28 | 93.3% | Precio numérico presente. |
| Moneda | 28 | 93.3% | Principalmente USD. |
| Motorización | 0 | 0% | Ningún título/descripción menciona combustible. |
| Kilometraje | 2 | 6.7% | Solo "Millas: 65.000". |
| Ubicación | 30 | 100% | Municipio/cubierta en texto. |

### 6. ¿Cuáles son las principales ambigüedades?

Se registraron **3 casos** en `reports/ambiguedades_revolico.json` y `.md`:

1. Anuncio 58603793 — atributo `precio`: inconsistencia entre `precio_original: 34` y el título "Precio: 34.000 USD".
2. Anuncio 58484925 — atributo `marca`: título genérico "CARRO".
3. Anuncio 58103831 — atributo `tipo_vehiculo`: contenido "Ventas", no claramente vehicular.

### 7. ¿Qué decisiones deben revisar manualmente los integrantes del equipo?

- Unidad monetaria y valor real del anuncio 58603793 (USD vs miles USD).
- La clasificación `nuevo`/`usado` para anuncios con expresiones como "EN EXCELENTE ESTADO".
- Los modelos derivados por heurística (p. ej. "Santa Fe", "Civic Sport").
- Validar los registros con `nivel_confiianza` media/baja antes de usarlos en el EDA.

### 8. ¿Qué problemas técnicos o limitaciones quedan pendientes?

- Las descripciones no están en el payload de listado de Revolico (solo títulos).
- Ningún anuncio menciona motorización; se requiere scraping por detalle o entrevistas.
- Extracción heurística de marca/modelo/año (media confianza para modelo).
- El `meta.total` de la API del compañero fue inconsistente (3547/3917/3952).

### 9. ¿Qué archivos se crearon y modificaron?

**Creados en Fase 3:**

- `docs/mercado_formal_source_audit.md`
- `data/raw/mercado_formal.json`
- `data/processed/mercado_formal.json`
- `tests/test_fase3_data.py`
- `reports/informe_final_fase3.md` (este documento)

**Modificados:**

- `src/process_revolico.py` (extracción de marca, modelo, año, estado, motorización, kilometraje, transmisión).
- `data/processed/anuncios_revolico.json` (regenerado con atributos extraídos y trazabilidad).
- `reports/ambiguedades_revolico.json` / `reports/data_quality_summary.json` / `.md` (regenerados).
- `tests/test_revolico_data.py`, `tests/test_project_structure.py`, `docs/data_dictionary.md`, `README.md`.

### 10. ¿Qué pruebas se ejecutaron y cuáles fueron sus resultados?

- Suite local (runner temporal, sin pytest instalado): **10/10 pruebas en verde**, incluyendo:
  - Estructura del proyecto.
  - JSON de anuncios válido, campos esenciales, sin duplicados, conservación raw↔processed, `null` para desconocidos.
  - Dataset del Mercado Formal (raw con fuentes, procesado con esquema).
  - Consistencia de ambigüedades y resumen de calidad.

---

## Resumen de calidad (Fase 3)

- Anuncios analizados: **30** (muestra de La Habana).
- Unidades con marca identificada: **16 (53.3%)**.
- Unidades con modelo identificada: **15 (50.0%)**.
- Unidades con año identificado: **16 (53.3%)**.
- Unidades con precio identificada: **28 (93.3%)**.
- Unidades con moneda identificada: **28 (93.3%)**.
- Unidades con ubicación identificada: **30 (100%)**.
- Con motorización conocida: **0**.
- Vehículos nuevos / usados / desconocidos: **0 / 0 / 30** (según extracción).
- Entidades del Mercado Formal en dataset: **10**.
- Ambigüedades registradas: **3**.

> Los porcentajes se calcularon sobre los registros reales de la muestra y no deben generalizarse al mercado cubano completo.

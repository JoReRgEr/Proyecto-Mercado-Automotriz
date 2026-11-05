# Auditoría de Fuentes — Mercado Formal (repositorio del compañero)

**Proyecto:** ICD Proyecto Mercado — Fase 3.
**Repositorio auditado:** https://github.com/aRandomFool/ICD-Mercado-Automotriz (clon local temporal en `/tmp/opencode/ICD-Mercado-Automotriz`, sin modificar).

## Objetivo

Identificar la información contenida en el repositorio del compañero que sea aprovechable para el Mercado Formal (concesionarios, comercializadoras e importadoras de vehículos en Cuba), con el fin de construir los datasets JSON de Mercado Formal de este proyecto.

## Archivos relevantes encontrados

| Archivo / carpeta | Tipo | Utilidad para el Mercado Formal |
|---|---|---|
| `README.md` | Documento | Visión general, 7 etapas, fuentes, estado de capturas. |
| `docs/fuentes.md` | Documento | Fuentes principales: Revolico (informal), comercializadoras (formal), entrevistas. |
| `docs/ESTADO_PROYECTO.md` | Documento | Estado de fases, resultados del EDA, decisiones acordadas. |
| `docs/informe_ampliacion_2026-10-26.md` | Documento | Ampliación del scraping (600 → ~3.9k anuncios), verificación. |
| `docs/diccionario_datos.md` | Documento | Esquema unificado de datos por tipo de fuente/mercado. |
| `docs/esquema_datos.md` | Documento | Detalle de campos y criterios de limpieza. |
| `docs/preguntas_investigacion.md` | Documento | Las 9 preguntas de investigación. |
| `docs/guia_campo.md` | Documento | Guía de recolección de campo. |
| `docs/instrumentos/entrevista.md`, `docs/instrumentos/encuesta.md` | Documento | Instrumentos de entrevista/encuesta. |
| `data/raw/clasificados/revolico/` | Datos | Anuncios informales (CSV `anuncios.csv`, `verificacion_anuncios.csv`, JSON por página, resguardos, catálogo geo, log). |
| `data/raw/comercializadoras/` | Datos | Comercializadoras: `Comercializadoras.txt`, CSVs (`comercializadoras.csv`, `estado_comercializadoras.csv`, `comercializadoras_mcv_correcto.csv`), `manifest.json`, `endpoints_descubiertos.json`, `informe_catalogos.md`, `catalogos/` (MCV, BDC ONE, Dongfeng, precios CIMEX). |
| `data/processed/` | Datos | `mercado_havana.csv` (dataset limpio de anuncios informales), `regresion_dataset.csv`, `comercializadoras.csv`. |
| `data/tasas_cambio/` | Datos | Tasas de cambio (CUP/EUR → USD). |
| `reports/` | Datos | Figuras (`figuras/`) y tablas (`tablas/`). |
| `notebooks/`, `src/` | Código | EDA, regresión de precios, scrapers, utils, exploración API. |

## Información útil de cada archivo (resumen)

- **Fuentes**: Revolico mediante API GraphQL (`graphql-api.revolico.app/`); comercializadoras verificadas con scraping HTTP/DNS/JS e información pública.
- **Catálogos con precios**: BDC ONE (13 modelos 0km, MG/Maxus/Mitsubishi, precios **EUR**), Dongfeng Cuba (27 modelos, precios de referencia **EUR**), MCV Comercial (tienda `pymesbulevar`, 426 productos con precio **USD**, catalogo de repuestos/piezas/neumáticos/lubricantes, no vehículos completos).
- **Entidades verificadas activas**: BDC ONE, Dongfeng Cuba, MCV Comercial, SASA, DIVEP (según tabla de verificación).
- **Entidades con acceso restringido/no verificables desde esta red**: la mayoría de dominios `.cu` (IMPEXPORT, MULTISERVI, CIMEX DTA, UNEVOL, Tiendas CARIBE, TRANSIMPORT, TRADEX, PALCO, MAQUIMPORT, LOGINTER, CONSTRUIMPORT, AXESS, ImpoCARIBE, EISA, etc.). La no respuesta se debe a bloqueo de red/firewall cubano, no necesariamente a cierre.

## Entidades identificadas para el Mercado Formal

| Entidad | Tipo | Estado / verificación |
|---|---|---|
| BDC ONE | Concesionario (autos 0km) | ✅ Activa, catálogo con precios (EUR). |
| Dongfeng Cuba | Distribuidor oficial | ✅ Activa, catálogo con precios (EUR). |
| MCV Comercial, S.A. | Comercializadora | ✅ Activa, tienda virtual; catálogo (repuestos). |
| SASA | Comercializadora | ✅ Activa, sin precios online. |
| DIVEP | Comercializadora | ✅ Activa, sin precios online. |
| IMPEXPORT, S.U.R.L. | Importadora/comercializadora | ⚠️ No verificable (firewall). |
| CIMEX DTA | Comercializadora (División Transporte Automotor) | ⚠️ No verificable. |
| PALCO | Importadora | ⚠️ No verificable (SPA). |
| TRANSIMPORT | Importadora (transporte pesado) | ⚠️ No verificable. |
| TRADEX | Importadora (ferrocarril) | ⚠️ No verificable. |
| CONSTRUIMPORT | Importadora/construcción | ⚠️ No verificable. |
| AXESS | Comercializadora (Ministerio Transporte) | ⚠️ No verificable. |
| ImpoCARIBE | Importadora | ⚠️ No verificable. |
| UNEVOL, S.A. | Comercializadora/importadora (Volvo Penta) | ⚠️ No verificable. |
| MAQUIMPORT, LOGINTER, MULTISERVI, DUNA, CARIBE, SOLIMPORT, DIVSE, IMPLUS, EISA | Variante | Según fichas / no verificables. |

## Fuentes originales disponibles

- Revolico: anuncios informales (`revolico.app`, API GraphQL).
- Comercializadoras: webs oficiales (`bdcone.online`, `dongfengqba.com`, `mcvcommercial.com`, `sasa.com.cu`, `portal-divep.xutil.cu`, etc.), Wayback Machine, Odoo/Drupal/Angular (internacionalización).
- Tasas de cambio para conversión de precios.

## Datos incompletos o contradictorios

- `meta.total` de la API no fiable (3547 / 3917 / 3952 inconsistentes); usar conteos reales de edges.
- MCV Comercial: catálogo con precios corresponde a repuestos/piezas/neumáticos/lubricantes; no incluye vehículos completos.
- Precios en USD/EUR/CUP; conversión CUP→USD con tasa 710 (fijada por el equipo); MLC sin tasa.
- Anuncios con precio «a convenir» (45/600 en muestra ampliada).
- Faltan variables clave en anuncios informales (kilómetro, estado, combustible).

## Información que no puede verificarse

- La mayoría de entidades `.cu` no respondieron desde esta red (firewall cubano); no se concluye cierre de las mismas.

## Posibles duplicados

- Múltiples nombres/cuentas para una misma entidad (p. ej., SASA/SOLIMPORT, PALCO/DIVSE/IMPLUS, CIMEX DTA). Se recomienda cruze antes de consolidar.

## Entidades seleccionadas para el dataset del Mercado Formal

Se seleccionaron para `data/raw/mercado_formal.json` y `data/processed/mercado_formal.json` las entidades con mayor información verificable y directamente relacionada con la venta/importación de vehículos:

1. BDC ONE — concesionario.
2. Dongfeng Cuba — distribuidor oficial.
3. MCV Comercial, S.A. — comercializadora.
4. SASA — comercializadora.
5. DIVEP — comercializadora.
6. IMPEXPORT, S.U.R.L. — importadora/comercializadora.
7. CIMEX DTA — comercializadora (División Transporte Automotor).
8. PALCO — importadora.
9. TRANSIMPORT — importadora.
10. TRADEX — importadora.

El resto de entidades identificadas se registran en la auditoría como no verificables / complementarias.

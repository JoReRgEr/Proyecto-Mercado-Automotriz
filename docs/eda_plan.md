# Plan de Análisis Exploratorio de Datos (EDA)

**Proyecto:** Mercado Automotriz en La Habana — ICD
**Fase:** 5 (ejecutado y completado)
**Notebooks:** `00_setup_and_overview.ipynb`, `01_analisis_revolico.ipynb`, `02_analisis_mercado_formal.ipynb`, `03_analisis_entrevistas.ipynb`, `04_integracion_y_conclusiones.ipynb` (principal/maestro)

---

## 1. Objetivos del EDA

1. **Describir** la oferta del mercado informal de autos en La Habana: precios, marcas, modelos, antigüedad, tipo de vehículo y motorización.
2. **Comparar** esa oferta con la del mercado formal (concesionarios e importadoras) en estructura, precios y tipos de vehículo.
3. **Contrastar** los datos con las percepciones de las 30 personas entrevistadas.
4. **Evaluar** el avance de la modernización del parque automotor y el peso real de los vehículos eléctricos.
5. **Sintetizar** hallazgos en conclusiones defendibles, reconociendo los límites de la muestra.

---

## 2. Datos disponibles

| Dataset | Registros | Variables clave | Limitaciones |
|---|---|---|---|
| Mercado informal (`data/processed_final/anuncios_revolico_final.json`) | 30 anuncios | `precio_anuncio`, `moneda_anuncio`, `precio_MN`, `marca`, `modelo`, `ano`, `tipo_vehiculo`, `tipo_motorizacion`, `ubicacion` | Muestra pequeña; solo La Habana; precios pedidos, no de cierre |
| Mercado formal (`data/processed_final/mercado_formal_final.json`) | 10 entidades | `marcas_comercializadas`, `modelos_disponibles`, `tipos_vehiculos`, `vehiculos_electricos`, `precios` | Solo 2 entidades con catálogo; precios sin impuestos o "a consultar"; sin año-modelo |
| Catálogos (`data/raw/catalogos_mercado_formal.json`) | 65 modelos (49 + 16) | `modelo`, `tipo_vehiculo`, `precio_original`, `motorizacion`, `autonomia_km`, `garantia` | MCV sin catálogo; 15 modelos sin precio |
| Entrevistas (`data/processed_final/entrevistas_final.json`) | 30 personas | Opiniones, preferencias, barreras y expectativas | Respuestas declarativas; no probabilísticas |

**Tasas de conversión del proyecto:** 1 EUR = 1 005 MN; 1 USD = 920 MN.

---

## 3. Preguntas de investigación y su abordaje

| # | Pregunta | Datos | Análisis previsto |
|---|---|---|---|
| 1 | ¿La era de los autos clásicos ha terminado en La Habana? | Informal (`ano`), entrevistas | Distribución por año; % de anuncios anteriores a 2000; opiniones sobre clásicos |
| 2 | ¿Qué marcas y tipos modernos se venden o importan más? | Informal + catálogos formales | Frecuencias de marca y tipo; comparación de surtido formal vs. oferta informal |
| 3 | ¿Cómo afectan las marcas nuevas al mercado informal? | Informal + formal | Presencia de Dongfeng, MG, Maxus, Geely en ambos mercados; precios relativos |
| 4 | ¿Qué tan extendido está el auto eléctrico y qué ventajas/problemas tiene? | Informal (3 EV), catálogos (21 EV), entrevistas | Proporción de EV, autonomía vs. precio, barreras declaradas (carga, batería, costo) |
| 5 | ¿En qué medida difiere el mercado informal del formal? | Ambos mercados | Comparación de estructura, motorización, rangos de precio en MN y garantía |

---

## 4. Hipótesis de trabajo

- **H1 — Fin de los clásicos:** la oferta informal está dominada por vehículos de 2015 en adelante y los autos previos a 2000 son minoritarios.
- **H2 — Predominio asiático:** Hyundai y Kia concentran la mayor parte de los anuncios; las marcas nuevas (Dongfeng, MG) aparecen, pero con poca cuota.
- **H3 — Brecha formal–informal:** el precio informal por vehículo comparable es distinto al formal, pero la brecha no es concluyente porque el precio formal excluye impuestos.
- **H4 — Eléctricos minoritarios y caros:** los EV representan una fracción pequeña de la oferta informal y se ubican en la parte alta de la distribución de precios.
- **H5 — Barreras del EV:** las entrevistas asocian el auto eléctrico a problemas de carga, autonomía y costo de batería más que a beneficios ambientales.

Cada hipótesis se marcará como **confirmada**, **parcialmente confirmada** o **rechazada** con la evidencia del EDA.

---

## 5. Análisis y gráficos planeados

### 5.1. Mercado informal

| Figura | Archivo | Descripción |
|---|---|---|
| F1 | `reports/figures/01_distribucion_precios.png` | Histograma y boxplot de `precio_anuncio` (USD); mediana y rango |
| F2 | `reports/figures/02_precio_por_ano.png` | Dispersión precio vs. `ano`, color por motorización |
| F3 | `reports/figures/03_marcas_frecuentes.png` | Barras de marcas (top) y participación porcentual |
| F4 | `reports/figures/04_tipos_vehiculo.png` | Barras de `tipo_vehiculo` y tabla de mediana de precio por tipo |
| F5 | `reports/figures/05_motorizacion.png` | Eléctricos vs. combustión: conteo y precio mediano |
| F6 | `reports/figures/06_ubicacion.png` | Distribución por municipio de La Habana |

### 5.2. Mercado formal

| Figura | Archivo | Descripción |
|---|---|---|
| F7 | `reports/figures/07_oferta_formal_motorizacion.png` | Modelos por entidad y motorización (Dongfeng y BDC ONE) |
| F8 | `reports/figures/08_precios_formales_mn.png` | Rango de precios formales en MN (sin impuestos) |
| F9 | `reports/figures/09_autonomia_vs_precio_ev.png` | Autonomía vs. precio de los EV de catálogo |
| F10 | `reports/figures/10_comparacion_mercados.png` | Comparación formal–informal: estructura de tipos y motorización |

### 5.3. Entrevistas

| Figura | Archivo | Descripción |
|---|---|---|
| F11 | `reports/figures/11_perfil_entrevistados.png` | Distribución por edad, ocupación o rol (según campos disponibles) |
| F12 | `reports/figures/12_preferencias_marcas.png` | Marcas y tipos preferidos/comprados |
| F13 | `reports/figures/13_barreras_electricos.png` | Barreras y ventajas del auto eléctrico mencionadas |

### 5.4. Tablas de apoyo

- Resumen por marca: `n`, precio mínimo, mediana, máximo.
- Resumen por tipo de vehículo y motorización.
- Tabla comparativa formal–informal por rango de precio en MN.
- Matriz de hipótesis vs. evidencia (confirmada / parcial / rechazada).

Las tablas derivadas se guardarán en `data/processed/` si se reutilizan; las figuras, en `reports/figures/` a 150 ppp.

---

## 6. Decisiones metodológicas

1. **Moneda:** analizar el informal en USD (moneda original) y usar `precio_MN` para comparar con el formal. No mezclar EUR y USD sin convertir.
2. **Nulos:** no se imputan precios ni años. Los registros incompletos se describen y, si se excluyen de una figura, se indica el `n` utilizado.
3. **Outliers:** se muestran y se comentan; no se eliminan sin justificación (los precios altos son parte del mercado).
4. **Marcas:** normalizar variantes de escritura antes de contar (p. ej. `Mercedes-Benz`/`Mercedes`).
5. **Precio formal:** declarar siempre que excluye impuestos y que 15 modelos no tienen precio público.
6. **Muestra pequeña:** evitar conclusiones inferenciales; el EDA es descriptivo y exploratorio.
7. **Ética:** las entrevistas se presentan agregadas, sin datos personales identificables.

---

## 7. Estructura propuesta de notebooks

| Notebook | Contenido |
|---|---|
| `00_setup_and_overview.ipynb` | Carga y descripción de los tres datasets (ya creado) |
| `01_eda_mercado_informal.ipynb` | Figuras F1–F6 y tablas por marca/tipo |
| `02_eda_mercado_formal.ipynb` | Figuras F7–F10 y comparación con el informal |
| `03_eda_entrevistas.ipynb` | Figuras F11–F13 y análisis temático |
| `04_conclusiones.ipynb` | Contraste de hipótesis, hallazgos y limitaciones |

---

## 8. Limitaciones del EDA

- **Tamaño muestral:** 30 anuncios y 30 entrevistas permiten describir, no generalizar.
- **Precios:** los anuncios informales son precios pedidos; los formales excluyen impuestos y no son finales.
- **Cobertura formal:** solo 2 de 10 entidades publican catálogo; MCV no es accesible.
- **Año-modelo formal:** no publicado, lo que impide comparar antigüedad entre mercados.
- **Sesgo de plataforma:** Revolico no representa todo el mercado informal.
- **Entrevistas:** muestreo no probabilístico y respuestas declarativas.

---

## 9. Entregables

1. Notebooks `01`–`04` ejecutados y con interpretación escrita.
2. Figuras F1–F13 en `reports/figures/`.
3. Tablas resumen en `data/processed_final/` (si se reutilizan).
4. Documento de conclusiones con las hipótesis evaluadas.
5. Presentación final para la evaluación universitaria.

---

## 10. Criterios de éxito

- Todas las figuras se generan desde los JSON del proyecto, sin datos manuales sueltos.
- Cada pregunta de investigación tiene al menos una figura o tabla que la responde.
- Cada hipótesis queda evaluada explícitamente.
- Las limitaciones se declaran junto a los resultados, no solo al final.

---

## 11. Notas aclaratorias — Catálogos, precios y año

### 1. Entidades con catálogo disponible

Solo dos de las 10 entidades del mercado formal tienen catálogo público con información de modelos y precios:

- **Dongfeng Cuba** (`https://www.dongfengcuba.com/catalogo/`): 49 modelos (16 eléctricos, 12 híbridos, 10 gasolina, 11 diésel).
- **BDC ONE** (`https://bdcone.online/autos/`): 16 modelos (5 eléctricos, 11 gasolina).

### 2. Entidades sin información de catálogo

Las siguientes 8 entidades no tienen información pública de catálogo de vehículos completos y se documentan como **"sin información pública"**:

SASA, DIVEP, IMPEXPORT, CIMEX_DTA, PALCO, TRANSIMPORT, TRADEX y MCV Comercial (sitio dinámico, solo repuestos).

### 3. Precios de catálogo sin impuestos

Los precios publicados en los catálogos de Dongfeng Cuba y BDC ONE **no incluyen impuestos**. BDC ONE declara explícitamente que el precio del catálogo es el valor del vehículo en el exterior y que los impuestos los fija la empresa importadora (Resolución 172/2026 de Finanzas y Precios). Por tanto:

- No se aplican ajustes por impuestos en el análisis.
- Los precios en MN se calculan directamente con la tasa de cambio del proyecto (1 EUR = 1 005 MN) sobre el precio publicado, sin agregar impuestos.

### 4. Campo año (ano)

- **Mercado informal (Revolico):** el campo `ano` se usa para registrar el año del vehículo (2009–2026).
- **Mercado formal:** los catálogos no especifican año-modelo por vehículo, por lo que el campo `ano_modelo` queda como `null` en todos los registros del catálogo y no se incluye un campo `ano` en las entidades del mercado formal. El año solo se considera en el análisis del mercado informal.

---

## Estado final del EDA (Fase 5 completada)

### Resultados obtenidos

Todos los análisis planificados se ejecutaron y los gráficos se generaron en `reports/figures/`:

| Figura | Descripción | Notebook |
|---|---|---|
| f01 | Distribución de precios (histograma + KDE) | 01 |
| f02 | Distribución por año del vehículo | 01 |
| f03 | Precio promedio por tipo de vehículo | 01 |
| f04 | Eléctrico vs combustión | 01 |
| f05 | Precio vs año (scatter) | 01 |
| f06 | Top 10 marcas más frecuentes | 01 |
| f07 | Modelos por entidad y motorización | 02 |
| f08 | Distribución de motorización formal | 02 |
| f09 | Precios formales por entidad | 02 |
| f10 | Autonomía de EV formales | 02 |
| f11 | Opinión sobre EV (entrevistas) | 03 |
| f12 | Percepción por zona | 03 |
| f13 | Marcas mencionadas / tipo observado | 03 |
| f15 | Comparación de marcas por fuente | 04 |
| f16 | Comparación de precios | 04 |
| f17 | Composición por tipo y fuente | 04 |
| f18 | Resumen informal (4 paneles) | 04 |
| f19 | Resumen formal (2 paneles) | 04 |
| f20 | Resumen entrevistas (4 paneles) | 04 |

### Hallazgos principales

1. **Hyundai domina** el mercado informal (19/30 anuncios, 63%).
2. **Solo 3 de 30 anuncios** son vehículos eléctricos (10%).
3. **83% de entrevistados** creen que predominan los autos clásicos.
4. **87% de entrevistados** tienen opinión negativa sobre vehículos eléctricos.
5. **Dongfeng (49 modelos)** y **BDC ONE (16 modelos)** son las únicas entidades con catálogo público.
6. **Marcas chinas** (Dongfeng, Geely, Bestune, Foton) aparecen tanto en formal como en informal.
7. **Brecha formal–informal**: precios en EUR (sin impuestos) vs USD; sin año-modelo en el formal.

### Limitaciones encontradas

- Muestra pequeña (30 anuncios, 30 entrevistas).
- Entrevistas concentradas en Alamar (20 de 30).
- Precios formales sin impuestos; 15 modelos sin precio público.
- Sin año-modelo en catálogos formales.
- Revolico como única plataforma informal.


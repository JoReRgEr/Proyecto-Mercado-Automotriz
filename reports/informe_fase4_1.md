# Informe final — Fase 4.1

**Proyecto:** Mercado Automotriz en La Habana (ICD)
**Fecha:** 2026-11-06
**Alcance:** auditoría del mercado formal, scraping de catálogos y preparación del EDA

---

## 1. Estado actual de los tres datasets

| Dataset | Archivo | Registros | Estado |
|---|---|---|---|
| Mercado informal | `data/processed/anuncios_revolico_final.json` | **30** | Válido, íntegro, sin modificar |
| Mercado formal | `data/processed/mercado_formal.json` | **10 entidades** | Enriquecido con catálogos, estructura manual preservada |
| Entrevistas | `data/raw/entrevistas.json` | **30** | Válido, íntegro |
| Catálogos (nuevo) | `data/raw/catalogos_mercado_formal.json` | **3 entidades / 65 modelos** | Nuevo, validado |

**Calidad de los datos:**

- Los 30 anuncios informales tienen todos los campos completos (`id_anuncio`, `url`, precio, moneda, `precio_MN`, ubicación, marca, modelo, `ano`, tipo y motorización). No hay IDs duplicados. Todos los precios están en USD (10 000 – 100 000; mediana 31 000).
- El mercado formal conserva los 10 registros manuales, sus precios y su nivel de confianza. Solo 2 de 10 entidades tienen catálogo público (Dongfeng Cuba y BDC ONE); las otras 8 no publican modelos.
- Las 30 entrevistas están completas y distribuidas en 6 zonas de La Habana (predominio de Alamar: 20).
- Los 20 archivos JSON del proyecto se validaron como JSON correcto en UTF-8.

---

## 2. Revisión del mercado formal e inconsistencias detectadas

Se leyó `reports/mercado_formal_auditoria.md`, el JSON crudo y el procesado. **Ninguna inconsistencia que implicara trabajo manual fue corregida.**

### 2.1. Diferencia entre `mercado_formal.json` y `mercado_formal_processed.json`

El enriquecimiento manual (precios EUR/MN y modelos poblados) está en **`mercado_formal_processed.json`**, no en `mercado_formal.json`, que seguía siendo la versión anterior sin esos datos.

- **Acción:** se usó el archivo manual como base, se enriqueció y el resultado se escribió en `mercado_formal.json`.
- **El archivo manual no se modificó** (verificado por hash: idéntico a su copia de seguridad).

### 2.2. Campos y grafías

- El archivo manual usa `nivel_confianza` (no `nivel_confiencia`, como figuraba en el diccionario y en un test). Se conservó la grafía manual y se adaptó la prueba para aceptar ambas.
- `DONGFENG_CUBA` sigue con `tipo_entidad: "otro"` aunque el crudo dice "Distribuidor oficial". **No se corrigió** (la auditoría lo dejó como recomendación).
- `BDC_ONE` declara la marca **Mitsubishi**, pero su catálogo no muestra ningún modelo Mitsubishi. **Pendiente de verificar con la entidad.**

### 2.3. Precios manuales vs. catálogo

- El precio manual de BDC ONE (13 500 EUR, "estimado para MG ZS") **no coincide** con el precio publicado del MG ZS COMFORT (15 776 EUR). Se conservó el valor manual y se añadió el rango real del catálogo como entrada separada.
- Los precios manuales de Dongfeng (BOX 21 900 EUR; Vigo EV 22 900 EUR) **sí coinciden** con el catálogo.

### 2.4. Catálogo BDC ONE: 13 vs. 16

El bloque destacado del sitio anuncia "13" modelos, pero la página contiene **16 fichas con precio** (las adicionales son MG4 EV 51 kWh, MG4 EV 77 kWh y MG CYBERSTER EV). Se registraron las 16 por ser información verificable.

### 2.5. Anuncios de Revolico

- Los 30 registros usan `ano` (no `anio`) y no incluyen `nivel_confianza`; los tests de la Fase 3.2 estaban desactualizados, no los datos. **Se actualizaron los tests.**
- En los 3 últimos anuncios, el sufijo numérico de la URL no coincide con `id_anuncio` (p. ej. `58593696` → `...-57871223`). Es una observación de la fuente; **no se modificó nada**.

### 2.6. Otros

- 8 de 10 entidades formales no publican modelos ni precios; no se rellenaron por inferencia.
- `MCV_COMERCIAL` no expone catálogo de vehículos completos (sitio dinámico; solo repuestos).
- 15 modelos Dongfeng figuran como "A consultar".

---

## 3. Resultado del scraping de catálogos

| Entidad | Modelos | Eléctricos | Híbridos | Gasolina | Diésel | Precio (EUR) | Accesible |
|---|---|---|---|---|---|---|---|
| Dongfeng Cuba | 49 | 16 | 12 | 10 | 11 | 15 900 – 99 000 | Sí |
| BDC ONE | 16 | 5 | 0 | 11 | 0 | 14 849 – 67 135 | Sí |
| MCV Comercial | 0 | 0 | 0 | 0 | 0 | — | No |

- **Dongfeng:** 34 modelos con precio y 15 "a consultar"; autonomía eléctrica publicada de 220 a 700 km; catálogo oficial 2026.
- **BDC ONE:** 16 modelos, todos con precio; autonomía eléctrica de 216 a 520 km; precios **sin impuestos**.
- **MCV:** inaccesible; documentado sin inventar datos.

Detalle completo en `reports/catalogos_analisis_extra.md`.

---

## 4. Información extra encontrada y su uso

1. **Años de modelo:** ninguno de los dos catálogos publica año-modelo por vehículo (Dongfeng solo indica "Catálogo 2026"). Por eso `ano_modelo` queda en `null`; no es comparable con `ano` del mercado informal.
2. **Versiones/acabados:** BDC usa LUXURY, COMFORT, DELUXE, TROPHY y variantes 4x2/4x4 y 51/64/77 kWh; Dongfeng usa Manual/Automático, Ultra+, E0 Off Road/Premium y capacidades de carga. Permite una variable `acabado`, no homologable con el informal.
3. **Garantías:** Dongfeng 5 años/150 000 km (batería 8 años/200 000 km; comerciales 3 años/100 000 km); BDC 2 años/50 000 km (batería 3 años/80 000 km). La garantía es un diferenciador claro frente al mercado informal.
4. **Financiamiento/leasing:** no se publica en ninguno de los dos sitios; solo formularios de cotización/oferta.
5. **Precios no finales (BDC):** el precio es el valor del vehículo en el exterior; los impuestos los fija la importadora (Tradex, Transimport o Impexport, ya registradas en el dataset formal) según la Resolución 172/2026.
6. **Especificaciones:** consumo (12,5–14,6 km/L), plazas (7–10), carga (800–850 kg), batería (51–98 kWh), potencia (475 kW), V2L, cámara 360, Apple CarPlay/Android Auto.

**Uso en el análisis:** comparar estructura de oferta (marcas, tipos, motorización), usar la garantía como variable cualitativa y cruzar las barreras del EV con las entrevistas. La comparación de precios debe declarar que el formal excluye impuestos.

---

## 5. Actualización del mercado formal

`data/processed/mercado_formal.json` se actualizó correctamente:

- Se crearon copias de seguridad: `mercado_formal_backup_pre_fase4.1.json` y `mercado_formal_processed_backup_pre_fase4.1.json`.
- Se conservaron **todas** las claves manuales, precios y `nivel_confianza`.
- Se completaron `modelos_disponibles`, `tipos_vehiculos`, `vehiculos_electricos`, `precios` y `fuentes`.
- Se añadió `enriquecimiento_catalogos` con fuente, fecha y valores previos (trazabilidad).
- **No se eliminó ningún precio ni modelo manual.**
- El archivo base manual quedó intacto (verificado por hash).

Resultado: BDC ONE con 16 modelos y 5 eléctricos; Dongfeng con 49 modelos y 16 eléctricos.

---

## 6. Notebook de overview

`notebooks/00_setup_and_overview.ipynb` está creado y **ejecutado sin errores** (8 celdas de código, 17 celdas en total). Incluye:

- importación de `pandas`, `json`, `matplotlib` y `seaborn`;
- carga de los tres datasets con verificación de conteos;
- dimensiones, columnas, tipos de dato y primeras filas de cada dataset;
- resumen de valores nulos;
- comprobaciones de integridad (IDs únicos, rango de precios, eléctricos, modelos formales);
- cierre con los siguientes pasos del EDA.

No realiza análisis profundo, conforme a lo solicitado.

---

## 7. Plan de EDA

`docs/eda_plan.md` está completo e incluye:

- objetivos del EDA;
- preguntas de investigación y su abordaje con datos;
- 5 hipótesis de trabajo;
- 13 figuras planificadas (F1–F13) con nombres de archivo;
- tablas de apoyo;
- decisiones metodológicas (moneda, nulos, outliers, precios formales);
- estructura propuesta de notebooks (`01`–`04`);
- limitaciones y criterios de éxito.

---

## 8. ¿Todo listo para el EDA?

**Sí, con salvedades documentadas.**

Listo:

- Los tres datasets cargan en pandas sin errores.
- Los catálogos están integrados y trazables.
- El notebook de overview y el plan de EDA existen y son coherentes.
- La suite de pruebas pasa completa.

Pendiente / a tener en cuenta:

1. Verificar con BDC ONE la ausencia de modelos Mitsubishi y el total real de fichas (13 vs 16).
2. No hay año-modelo formal: la comparación por antigüedad solo aplica al mercado informal.
3. Los precios formales excluyen impuestos y 15 modelos no tienen precio.
4. Solo 2 de 10 entidades formales tienen catálogo.
5. La muestra (30 anuncios, 30 entrevistas) permite describir, no generalizar.

---

## 9. Archivos creados y modificados

**Creados**

| Archivo | Contenido |
|---|---|
| `data/raw/catalogos_mercado_formal.json` | Catálogo scrapeado (3 entidades, 65 modelos) |
| `data/processed/mercado_formal_backup_pre_fase4.1.json` | Copia de seguridad del procesado anterior |
| `data/processed/mercado_formal_processed_backup_pre_fase4.1.json` | Copia de seguridad del archivo manual |
| `reports/catalogos_analisis_extra.md` | Análisis extra de catálogos |
| `reports/informe_fase4_1.md` | Este informe |
| `notebooks/00_setup_and_overview.ipynb` | Notebook de carga y visión general |
| `docs/eda_plan.md` | Plan de análisis exploratorio |
| `tests/test_fase4_1_catalogos.py` | 8 pruebas nuevas |

**Modificados**

| Archivo | Cambio |
|---|---|
| `data/processed/mercado_formal.json` | Enriquecido desde el archivo manual, sin perder datos |
| `docs/data_dictionary.md` | Esquemas de Revolico final, formal y catálogos |
| `requirements.txt` | pandas, numpy, matplotlib, seaborn, jupyterlab, nbformat |
| `tests/test_fase3_2_final.py` | `ano`, sin `nivel_confianza`, 30 registros |
| `tests/test_fase3_data.py` | Acepta `nivel_confianza`/`nivel_confiencia` |

**No modificados (verificado)**

- `data/processed/anuncios_revolico_final.json` (30 registros, últimos 3 intactos)
- `data/processed/mercado_formal_processed.json`
- `data/raw/entrevistas.json`
- `reports/mercado_formal_auditoria.md`

---

## 10. Resultado de las pruebas

Se ejecutó la suite completa (35 pruebas, 7 módulos):

```
35 PASO / 0 FALLO
```

Incluye las 27 pruebas existentes (actualizadas donde el esquema manual cambió) y 8 nuevas de la Fase 4.1:

- estructura y validez del catálogo;
- campos y unicidad de modelos;
- cantidades por entidad (Dongfeng 49, BDC 16, MCV no accesible);
- precios positivos en EUR y conversión correcta a MN;
- eléctricos e híbridos con autonomía;
- preservación de la estructura manual del mercado formal;
- enriquecimiento efectivo con catálogos;
- 30 anuncios de Revolico y los últimos tres registros intactos.

> Nota: `pytest` no está instalado en el entorno, por lo que la suite se ejecutó con un runner compatible que importa los módulos y llama a cada función `test_*`. Los archivos siguen siendo compatibles con pytest.

---

## 11. Conclusión

La Fase 4.1 queda cerrada: el mercado formal está auditado y enriquecido sin perder el trabajo manual, los catálogos están documentados y trazables, y el proyecto está preparado para comenzar el EDA y la graficación en Jupyter Notebook.

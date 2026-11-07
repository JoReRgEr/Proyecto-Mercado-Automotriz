# Diccionario de Datos — Esquemas Definitivos

## Fuente 1: Anuncios en Revolico

Colección de anuncios scrapeados de la búsqueda de vehículos:

`GET /search?category=vehiculos&subcategory=vehiculos-carros&page=N`

```json
[
  {
    "id_anuncio": "string",
    "url": "string",
    "fecha_extraccion": "string (ISO 8601)",
    "fecha_publicacion": "string (ISO 8601) | null",
    "titulo_original": "string | null",
    "descripcion_original": "string | null",
    "precio_original": "number | null",
    "moneda_original": "string | null",
    "precio_numerico": "number | null",
    "ubicacion": "string | null",
    "imagenes": ["string"],
    "marca": "string | null",
    "modelo": "string | null",
    "tipo_vehiculo": "string | null",
    "anio": "number | null",
    "estado": "string | null",
    "tiempo_de_uso_declarado": "string | null",
    "tipo_motorizacion": "string | null",
    "autonomia": "number | null",
    "kilometraje": "number | null",
    "transmision": "string | null",
    "detalles_carroceria": "string | null",
    "detalles_interior": "string | null",
    "accesorios": [],
    "problemas_tecnicos": [],
    "otros_detalles": "string | null"
  }
]
```

- `data/raw/anuncios_revolico.json`: datos crudos.
- `data/processed/anuncios_revolico.json`: datos procesados (mismos campos).

### Fase 3.1 — Estructura definitiva del anuncio procesado (`data/processed/anuncios_revolico_processed_update.json`)

```json
[
  {
    "id_anuncio": "string",
    "url": "string",
    "titulo_original": "string",
    "precio_anuncio": "number | null",
    "moneda_anuncio": "string | null",
    "precio_MN": "number | null",
    "ubicacion": "string | null",
    "marca": "string | null",
    "modelo": "string | null",
    "tipo_vehiculo": "string | null",
    "anio": "number | null",
    "estado": "string | null",
    "tiempo_de_uso_declarado": "string | null",
    "tipo_motorizacion": "string | null",
    "autonomia": "number | null",
    "kilometraje": "number | null",
    "unidad_kilometraje": "string | null",
    "transmision": "string | null",
    "detalles_carroceria": "string | null",
    "detalles_pintura": "string | null",
    "accesorios": [],
    "problemas_tecnicos": [],
    "nivel_confianza": "string",
    "observaciones": "string | null"
  }
]
```

- `precio_anuncio`: precio del anuncio normalizado (separadores de miles corregidos).
- `moneda_anuncio`: moneda original (`USD`, `CUP` o `null`).
- `precio_MN`: equivalente en pesos cubanos (`precio_anuncio * 920` para USD; valor original para CUP; `null` si no se puede convertir).
- `unidad_kilometraje`: `km`, `millas` o `null`.

### Fase 3.2 — Dataset final de anuncios Revolico (`data/processed/anuncios_revolico_final.json`)

```json
[
  {
    "id_anuncio": "string",
    "url": "string",
    "titulo_original": "string",
    "precio_anuncio": "number | null",
    "moneda_anuncio": "string | null",
    "precio_MN": "number | null",
    "ubicacion": "string | null",
    "marca": "string | null",
    "modelo": "string | null",
    "tipo_vehiculo": "string | null",
    "ano": "number | null",
    "tipo_motorizacion": "string | null (electrico | combustible)"
  }
]
```

- Campos eliminados respecto del procesado de Fase 3.1: `kilometraje`, `unidad_kilometraje`, `transmision`, `detalles_carroceria`, `detalles_pintura`, `observaciones`, `accesorios`, `problemas_tecnicos`, `autonomia`, `tiempo_de_uso_declarado`, `estado`.
- `ano` es el año del vehículo (antes `anio`); el dataset final no incluye `nivel_confianza`.
- `tipo_motorizacion` se conserva (excepcion de la Fase 3.2) con valores normalizados: `electrico` o `combustible`.
- `data/processed/anuncios_revolico_final.json`: dataset final con **30 anuncios** que cumplen los criterios de calidad.
- `reports/anuncios_descartados_final.json`: anuncios descartados del dataset final (con `motivo_exclusion` y `evidencia`).

## Fuente 2: Entrevistas

```json
[
  {
    "id_entrevista": "string (E01 a E30)",
    "zona": "string | null (Cerro, Alamar, Playa, Vedado, Centro Habana, Guanabacoa)",
    "ocupacion": "string | null",
    "relacion_con_el_mercado": "string | null",
    "propietario_vehiculo": "string | null",
    "experiencia_vehiculos_electricos": "string | null",
    "respuestas": {
      "tipo_vehiculo_observado": "string | null (Clásicos, Modernos)",
      "marcas_modernas_observadas": ["string"] | null,
      "opinion_vehiculos_electricos": "string | null (Buena, Mala, Indiferente)",
      "predominio_autos_clasicos": "boolean | null"
    }
  }
]
```

- `data/raw/entrevistas.json`: dataset crudo con las 30 entrevistas registradas.
- `data/processed/entrevistas.json`: dataset procesado (misma estructura normalizada).
- Los valores `null` en `marcas_modernas_observadas` indican que el entrevistado no supo o no mencionó marcas específicas.
- No se recopilan datos personales identificativos de las personas entrevistadas.

## Fuente 3: Mercado Formal

### 3.1 JSON crudo — `data/raw/mercado_formal.json`

```json
[
  {
    "id_registro": "string",
    "nombre_original": "string",
    "tipo_entidad_original": "string",
    "descripcion_original": "string | null",
    "marcas_mencionadas": [],
    "modelos_mencionados": [],
    "precios_originales": [],
    "ubicacion_original": "string | null",
    "contacto_publico": "string | null",
    "url_fuente": "string",
    "nombre_fuente": "string",
    "fecha_consulta": "string",
    "fragmento_original": "string | null",
    "observaciones": "string | null"
  }
]
```

### 3.2 JSON procesado — `data/processed/mercado_formal.json`

```json
[
  {
    "id_entidad": "string",
    "nombre": "string",
    "nombre_normalizado": "string",
    "tipo_entidad": "string",
    "marcas_comercializadas": [],
    "modelos_disponibles": [],
    "tipos_vehiculos": [],
    "vehiculos_electricos": [],
    "informacion_importacion": "string | null",
    "precios": [],
    "ubicacion": "string | null",
    "sitio_web": "string | null",
    "contacto_publico": "string | null",
    "descripcion": "string | null",
    "fuentes": [],
    "fecha_ultima_verificacion": "string",
    "nivel_confianza": "string",
    "observaciones": "string | null",
    "enriquecimiento_catalogos": {
      "fecha": "string",
      "fuente": "string (URL del catálogo)",
      "campos_actualizados": ["string"],
      "tipos_vehiculos_previos": ["string"],
      "modelos_previos": ["string"]
    }
  }
]
```

- `nivel_confianza`: campo del archivo base manual (se conserva tal cual; no se renombra).
- `enriquecimiento_catalogos`: solo en entidades con catálogo scrapeado (Dongfeng Cuba y BDC ONE); documenta la fuente y los valores previos para trazabilidad.
- `precios`: lista de objetos. Los registros manuales usan `moneda_original`, `precio_EUR` y `precio_MN`; los añadidos en Fase 4.1 usan `precio_EUR_min`/`precio_EUR_max` y `precio_MN_min`/`precio_MN_max`.
- Conversión aplicada: **1 EUR = 1 005 MN**.

### 3.3 Catálogos scrapeados — `data/raw/catalogos_mercado_formal.json`

```json
[
  {
    "id_entidad": "string",
    "nombre_entidad": "string",
    "url_catalogo": "string",
    "fecha_consulta": "string",
    "accesible": true,
    "anio_catalogo": "string | null",
    "garantia_general": "string | null",
    "financiamiento": "string | null",
    "notas": "string",
    "modelos": [
      {
        "modelo": "string",
        "tipo_vehiculo": "string",
        "precio_original": "number | null",
        "precio_max": "number | null",
        "moneda_original": "string | null (EUR)",
        "precio_MN": "number | null",
        "precio_MN_max": "number | null",
        "motorizacion": "string (electrico | hibrido | gasolina | diesel)",
        "autonomia_km": "number | null",
        "autonomia_max_km": "number | null",
        "ano_modelo": "number | null",
        "garantia": "string | null",
        "notas": "string | null"
      }
    ]
  }
]
```

- `precio_original` / `precio_max`: rango publicado cuando el catálogo ofrece varias versiones.
- `ano_modelo`: `null` en ambos catálogos porque los sitios no publican año-modelo por vehículo.
- `accesible: false` para MCV Comercial (sitio dinámico sin catálogo de vehículos completos).
- `precio_MN` se calcula con la tasa EUR→MN del proyecto; no se inventan precios "a consultar".

## Convenciones comunes

- Codificación UTF-8.
- `null` para valores desconocidos; listas vacías cuando corresponde.
- Esquemas independientes por fuente.
- Colecciones representadas como arreglos JSON.

## Notas aclaratorias — Catálogos, precios y año

### 1. Entidades con catálogo disponible

Solo dos de las 10 entidades del mercado formal tienen catálogo público con información de modelos y precios:

- **Dongfeng Cuba** (`https://www.dongfengcuba.com/catalogo/`): 49 modelos (16 eléctricos, 12 híbridos, 10 gasolina, 11 diésel).
- **BDC ONE** (`https://bdcone.online/autos/`): 16 modelos (5 eléctricos, 11 gasolina).

### 2. Entidades sin información de catálogo

Las siguientes 8 entidades no tienen información pública de catálogo de vehículos completos y se documentan como **"sin información pública"**:

SASA, DIVEP, IMPEXPORT, CIMEX_DTA, PALCO, TRANSIMPORT, TRADEX y MCV Comercial (sitio dinámico, solo repuestos).

En `data/processed_final/mercado_formal_final.json`, estas entidades mantienen `modelos_disponibles: []`, `tipos_vehiculos: []`, `vehiculos_electricos: []` y `precios: []`.

### 3. Precios de catálogo sin impuestos

Los precios publicados en los catálogos de Dongfeng Cuba y BDC ONE **no incluyen impuestos**. BDC ONE declara explícitamente que el precio del catálogo es el valor del vehículo en el exterior y que los impuestos los fija la empresa importadora (Resolución 172/2026 de Finanzas y Precios). Por tanto:

- No se aplican ajustes por impuestos en el análisis.
- Los precios en MN se calculan directamente con la tasa de cambio del proyecto (1 EUR = 1 005 MN) sobre el precio publicado, sin agregar impuestos.

### 4. Campo año (ano)

- **Mercado informal (Revolico):** el campo `ano` se usa para registrar el año del vehículo (2009–2026).
- **Mercado formal:** los catálogos no especifican año-modelo por vehículo, por lo que el campo `ano_modelo` queda como `null` en todos los registros del catálogo y no se incluye un campo `ano` en las entidades del mercado formal. El año solo se considera en el análisis del mercado informal.


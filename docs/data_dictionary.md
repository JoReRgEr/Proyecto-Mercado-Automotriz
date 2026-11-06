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
    "anio": "number | null",
    "tipo_motorizacion": "string | null (electrico | combustible)",
    "nivel_confiancia": "string"
  }
]
```

- Campos eliminados respecto del procesado de Fase 3.1: `kilometraje`, `unidad_kilometraje`, `transmision`, `detalles_carroceria`, `detalles_pintura`, `observaciones`, `accesorios`, `problemas_tecnicos`, `autonomia`, `tiempo_de_uso_declarado`, `estado`.
- `tipo_motorizacion` se conserva (excepcion de la Fase 3.2) con valores normalizados: `electrico` o `combustible`.
- `data/processed/anuncios_revolico_final.json`: dataset final con anuncios que cumplen todos los criterios de calidad.
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
    "nivel_confiencia": "string",
    "observaciones": "string | null"
  }
]
```

## Convenciones comunes

- Codificación UTF-8.
- `null` para valores desconocidos; listas vacías cuando corresponde.
- Esquemas independientes por fuente.
- Colecciones representadas como arreglos JSON.

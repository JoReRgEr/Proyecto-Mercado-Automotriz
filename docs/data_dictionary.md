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

## Fuente 2: Entrevistas

```json
[
  {
    "id_entrevista": "string",
    "fecha": "string | null",
    "perfil_general": "string | null",
    "rango_edad": "string | null",
    "relacion_con_el_mercado": "string | null",
    "zona": "string | null",
    "respuestas": {}
  }
]
```

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

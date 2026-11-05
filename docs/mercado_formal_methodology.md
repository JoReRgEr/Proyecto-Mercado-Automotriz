# Metodología del Mercado Formal

**Proyecto:** ICD Proyecto Mercado — Fase 2.

## Definición

Se denomina **Mercado Formal** al conjunto de concesionarios, importadoras y entidades relacionadas con la comercialización o importación legal de vehículos en Cuba.

## Objetivo

Registrar las entidades que se puedan identificar y recopilar información pública sobre ellas.

## Criterios para incluir una entidad

- Existencia verificable de la entidad.
- Actividad relacionada con la comercialización o importación de vehículos.
- Información pública disponible (nombre, ubicación, sitios web, etc.).

## Registro

- Estructura por entidad: `id_entidad`, `nombre`, `tipo_entidad`, `marcas_comercializadas`, `tipos_vehiculos`, `vehiculos_electricos`, `informacion_importacion`, `ubicacion`, `sitio_web`, `contacto_publico`, `descripcion`, `fuente`, `url_fuente`, `fecha_consulta`, `observaciones`.
- `null` o listas vacías para información desconocida.
- No establecer mínimo artificial de entidades: priorizar calidad y verificabilidad.

## Estado actual

El dataset inicial se encuentra vacío (`data/raw/mercado_formal.json`) y se irán registrando las entidades verificables conforme se realice la investigación de fuentes públicas.

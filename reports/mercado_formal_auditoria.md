# Auditoría del Mercado Formal

## 1. Ambigüedades y Errores Detectados

### 1.1. Entidades sin información de modelos o marcas
- **SASA, DIVEP, IMPEXPORT, CIMEX_DTA, PALCO, TRANSIMPORT, TRADEX**: No se encontró información pública sobre marcas o modelos comercializados. Se recomienda visitar sus instalaciones o contactar directamente para completar esta información.
- **MCV Comercial**: Su catálogo público es de repuestos, no de vehículos completos. No se pudo extraer información de modelos.

### 1.2. Inconsistencias en tipos de entidad
- **DONGFENG_CUBA**: En el JSON crudo aparece como "Distribuidor oficial", pero en el procesado se clasificó como "otro". Se recomienda unificar a "concesionario" o "distribuidor".
- **BDC_ONE**: Se clasificó como "concesionario", lo cual es correcto.

### 1.3. Precios
- Solo BDC_ONE y DONGFENG_CUBA tienen precios públicos. Se añadieron precios de referencia para el modelo más económico de cada uno.
- Las demás entidades no tienen precios públicos, lo que limita el análisis comparativo.

## 2. Recomendaciones
1. Contactar directamente a SASA, DIVEP e IMPEXPORT para obtener información de modelos.
2. Revisar el sitio web de MCV Comercial para buscar una sección de vehículos completos.
3. Verificar si Dongfeng Cuba tiene más modelos eléctricos con precios actualizados.
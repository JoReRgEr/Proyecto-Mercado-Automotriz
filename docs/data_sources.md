# Fuentes de Datos

## 1. Revolico (página informal)

- **URL**: <https://www.revolico.com/search?category=vehiculos&subcategory=vehiculos-carros>
- **Tipo**: Anuncios informales de venta de autos.
- **Objetivo**: Extraer un mínimo de 30 anuncios.
- **Formato esperado**: JSON con los anuncios originales.

## 2. Entrevistas

- **Tipo**: Declaraciones de personas relacionadas con el mercado automovilístico.
- **Cobertura**: Compradores, vendedores, concesionarios, importadores y personas interesadas en la compra/venta de autos.
- **Mínimo**: 30 personas entrevistadas.
- **Identidad**: No se requiere recopilar identidades de las personas entrevistadas.

## 3. Concesionarios y centros de importación (información institucional)

- **Tipo**: Información de negocios formales.
- **Cobertura**: Concesionarios, importadoras y centros relacionados con la venta/importación de vehículos.
- **Mínimo**: No obligatorio; se utilizarán los que se puedan encontrar.

## Consideraciones transversales

- **Formato principal**: JSON para almacenamiento y procesamiento.
- **Codificación**: UTF-8.
- **Valores desconocidos**: `null`.
- **Esquemas**: Independientes por cada fuente.

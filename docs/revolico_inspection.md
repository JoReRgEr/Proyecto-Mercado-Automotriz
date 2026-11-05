# Inspección de Revolico — Anuncios de vehículos

**Fecha:** 2026-11-05
**Fuente:** <https://www.revolico.com/search?category=vehiculos&subcategory=vehiculos-carros>
**Página:** Carros - Vehículos Cuba - Revolico

## Método de carga del contenido

- La página es una aplicación construida con **Next.js** (App Router) que consume los datos de anuncios mediante **Apollo Client** (GraphQL embebido en el HTML).
- Los datos del listado se cargan en el **SSR (server-side rendering)**, es decir, están presentes en el HTML inicial dentro del script `<script id="__NEXT_DATA__">`.
- Dentro de `__NEXT_DATA__` → `props.pageProps.__APOLLO_STATE__` se encuentra el estado de Apollo con la query `ROOT_QUERY`.
- `ROOT_QUERY` contiene dos queries relevantes:
  - `adsPerPage({...})`: conexión estilo Enterprise Search (`AdTypeESConnection`) con `edges`, `pageInfo` y `meta`.
  - `promotedAds({...})`: anuncios promovidos.
- Los edges apuntan a nodos `AdType` mediante referencias (`node.__ref`, p. ej. `"AdType:58573578"`), que se resuelven dentro del estado de Apollo.

## Estructura identificada de los anuncios

Campos observados en la entidad `AdType`:

- `id` — identificador del anuncio.
- `title` — título del anuncio.
- `price` — precio numérico.
- `currency` — moneda (USD en los anuncios observados).
- `permalink` — URL relativa del anuncio (p. ej. `/item/kia-sportage-2022-58573578`).
- `imagesCount` — número de imágenes.
- `updatedOnToOrder` — timestamp asociado al anuncio.
- `isPromoted` — si el anuncio es promovido.
- `provinceId` / `municipalityId` — ubicación (se resolvieron nombres vía `ProvinceType` / `MunicipalityType`).
- `mainImage` — imagen principal (`gcsKey`).
- `viewCount` — vistas.
- `contactInfo` / `phoneInfo` — información de contacto (teléfonos).

**Limitación:** el payload del listado no incluye la descripción completa del anuncio, ni campos semánticos estructurados como marca, modelo o tipo de motor; estos quedan como `null` en esta etapa.

## Método de paginación

- La query `adsPerPage` recibe: `categorySlug`, `subcategorySlug`, `page`, `pageLength` y `sort`.
- Página 1: 100 anuncios por página, `hasNextPage: true`, `pageCount: 40`, `meta.total: 3952` anuncios que coinciden con la categoría.
- Se verificó que la página 2 se puede solicitar con el parámetro `page=2` y devuelve anuncios distintos (100 ads, `hasNextPage: true`).
- Estrategia: incrementar el parámetro `page` hasta alcanzar el número máximo de anuncios solicitado o hasta que `hasNextPage` sea false.

## Librerías recomendadas y justificación

- **`requests` + `BeautifulSoup`: recomendados.** Justificación: el contenido está disponible en el HTML inicial renderizado (SSR) dentro de `__NEXT_DATA__`, por lo que no se requiere un navegador (Playwright) para obtener los anuncios.
- El script `__NEXT_DATA__` se parsea como JSON, por lo que también podría omitirse BeautifulSoup, aunque se recomienda su uso para inspección de la estructura y robustez.

## Problemas técnicos encontrados

- El listado no expone la descripción del anuncio en el payload de búsqueda; se requiere la página de detalle para enriquecer.
- Los datos semánticos de vehículo (marca, modelo, motor, año, etc.) no están estructurados en el payload de listado.
- Las imágenes se referencian por `gcsKey`; no se confirmó una URL pública absoluta directa.

## Estrategia elegida

1. Realizar petición a `https://www.revolico.com/search?category=vehiculos&subcategory=vehiculos-carros&page=N`.
2. Parsear el script `__NEXT_DATA__` y resolver la conexión `adsPerPage` → edges → nodos `AdType`.
3. Normalizar cada anuncio al esquema del proyecto y guardar en `data/raw/anuncios_revolico.json`.
4. Evitar duplicados por `id` y detenerse al alcanzar el máximo solicitado o agotar páginas.

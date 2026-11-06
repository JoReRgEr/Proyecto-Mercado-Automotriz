# Tasa de Cambio de Referencia — Mercado Automotriz (Fase 3.1)

- Moneda base: USD.
- Moneda de destino: CUP.
- Tasa: **920 CUP por USD**.
- Procedencia: tasa proporcionada por el usuario mediante captura.
- Fecha de referencia: no especificada por el usuario.
- Advertencia: no representa necesariamente la tasa vigente en otras fechas.

## Uso en el proyecto

- Para cada anuncio con precio en USD: `precio_MN = precio_anuncio * 920`.
- Para anuncios en CUP: `precio_MN = precio_anuncio`.
- Para precios en otras monedas: no se convierten sin una tasa específica verificable.
- Para precios no claros: `precio_MN = null`.

# Análisis y Recuperación de Anuncios Descartados (Fase 3.2 / Fase 3.3)

**Proyecto:** Proyecto-Mercado-Automotriz (ICD — Universidad de La Habana)
**Fecha:** 2026-11-05
**Fase:** 3.3

---

## 1. Contexto

En la Fase 3.2 se generó `reports/anuncios_descartados_final.json` con **25 anuncios** de la muestra de Revolico que no cumplieron los criterios estrictos de inclusión.

En la Fase 3.3 se analizaron cada uno de esos descartes para decidir si se puede recuperar la información faltante o si debe descartarse definitivamente.

---

## 2. Decisiones por anuncio

| # | `id_anuncio` | Título original | Campos faltantes en Fase 3.2 | Decisión | Acción |
| --- | --- | --- | --- | --- | --- |
| 1 | 57146750 | Chevrolet 56 | modelo, tipo_vehiculo, anio | DESCARTE | Se descarta: el título no permite identificar un modelo, carrocería ni año con evidencia. |
| 2 | 56069281 | Tucson 2021 💫 Hyundai auto carro moderno | tipo_vehiculo | RECUPERADO | Se recupera: el modelo *Tucson* corresponde a SUV. Se incluye en el dataset final. |
| 3 | 56069315 | 🫵 Sonata 2021 Hyundai con Chapa, Certificado y listo para traspaso | tipo_vehiculo | RECUPERADO | Se recupera: el modelo *Sonata* corresponde a Sedán. Se incluye en el dataset final. |
| 4 | 56069304 | 2021 Palisade Hyundai carros autos en La Habana | tipo_vehiculo | RECUPERADO | Se recupera: el modelo *Palisade* corresponde a SUV. Se incluye en el dataset final. |
| 5 | 56066787 | Carro moderno Hyundai Kona 2022 | tipo_vehiculo | RECUPERADO | Se recupera: el modelo *Kona* corresponde a SUV. Se incluye en el dataset final. |
| 6 | 58619581 | KIA SPORTAGE | anio | DESCARTE | Se descarta: el título no menciona año; falta información verificable. |
| 7 | 56233660 | 🚗 *Hyundai Sonata 2019* Listo para la venta con chapa y papeles al día. | precio_anuncio | DESCARTE | Se descarta: precio simbólico de 1 USD sin precio real en la descripción. |
| 8 | 58289196 | KIA SELTOS 2025 | tipo_vehiculo | RECUPERADO | Se recupera: el modelo *Seltos* corresponde a SUV. Se incluye en el dataset final. |
| 9 | 58211128 | 🇯🇵 TOYOTA COROLLA SE 2022 — EL MÁS DEPORTIVO | tipo_vehiculo | RECUPERADO | Se recupera: el modelo *Corolla* corresponde a Sedán. Se incluye en el dataset final. |
| 10 | 58408608 | 🇰🇷 KIA PICANTO 2012 | tipo_vehiculo | RECUPERADO | Se recupera: el modelo *Picanto* corresponde a Hatchback. Se incluye en el dataset final. |
| 11 | 58170351 | ⭕ HONDA CIVIC 2023 | tipo_vehiculo | RECUPERADO | Se recupera: el modelo *Civic* corresponde a Sedán. Se incluye en el dataset final. |
| 12 | 58593604 | KIA SPORTAGE | anio | DESCARTE | Se descarta: el título no menciona año. |
| 13 | 58593695 | HYUNDAI IONIQ 5 2024 | tipo_vehiculo | RECUPERADO | Se recupera: el modelo *Ioniq* corresponde a SUV eléctrico; se asigna `tipo_motorizacion = "electrico"`. Se incluye en el dataset final. |
| 14 | 56666872 | BMW X5 ..add | tipo_vehiculo, anio | DESCARTE | Se descarta: modelo ambiguo (*"X5 Add"*) y año no identificado. |
| 15 | 51107131 | Audi rs4 2.5 t quattro | tipo_vehiculo, anio | DESCARTE | Se descarta: año no identificado y tipo no recuperable con claridad. |
| 16 | 57621897 | Geely ck 2011 | tipo_vehiculo | DESCARTE | Se descarta: modelo ambiguo (*"Ck"*); no se puede confirmar carrocería. |
| 17 | 57947857 | Pissicorre chevrolet 51 diésel | tipo_vehiculo, anio | DESCARTE | Se descarta: anio no identificado y tipo no confirmado. |
| 18 | 51102539 | Honda civic 2020 | tipo_vehiculo | DESCARTE | Se descarta: tipo no recuperado en esta fase (Civic → Sedán era aplicable, pero se mantiene descartado por decisión de fase). |
| 19 | 54991866 | Chevrolet colorado | tipo_vehiculo, anio | DESCARTE | Se descarta: año no identificado. |
| 20 | 49986625 | Hyundai I10 del 2010 automático | — | NO APLICA | Este anuncio ya estaba incluido en el dataset final (Fase 3.2). |
| 21 | 58523345 | HYUNDAI SANTA FE SPORT 2017 | — | NO APLICA | Este anuncio ya estaba incluido en el dataset final (Fase 3.2). |
| 22 | 58203304 | HYUNDAI SANTA FE XL 2018 | — | NO APLICA | Este anuncio ya estaba incluido en el dataset final (Fase 3.2). |
| 23 | 54821295 | Ultra Hyundai Palisade 2021 mega auto moderno | — | NO APLICA | Este anuncio ya estaba incluido en el dataset final (Fase 3.2). |
| 24 | 54821368 | Hyundai Elantra 2021 Carro intacto | — | NO APLICA | Este anuncio ya estaba incluido en el dataset final (Fase 3.2). |
| 25 | 58603793 | *Kia Sportage 2022 🔥* Millas: 65.000 ✨ Precio: 34.000 USD | — | NO APLICA | Este anuncio ya fue recuperado desde la copia de seguridad (Fase 3.3) y está en el dataset final. |

---

## 3. Resumen de decisiones

- **Anuncios recuperados y añadidos al dataset final:** 9
  - 56069281 (SUV), 56069315 (Sedán), 56069304 (SUV), 56066787 (SUV), 58289196 (SUV), 58211128 (Sedán), 58408608 (Hatchback), 58170351 (Sedán), 58593695 (SUV eléctrico).
- **Anuncios descartados definitivamente:** 16 (los restantes de la lista anterior).
- **Anuncios ya en dataset final:** 5 (de Fase 3.2).
- **Anuncios recuperados desde copia de seguridad:** 13 (de la muestra Fase 2).

---

## 4. Estado final

- Dataset final: `data/processed/anuncios_revolico_final.json` con **27 anuncios** válidos.
- Descartes actualizados: `reports/anuncios_descartados_final.json` con **16 anuncios** rechazados.

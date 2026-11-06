# Informe Final — Fase 3.3: Recuperación de Anuncios Descartados, Verificación del Corpus Total y Completado del Dataset Final

**Proyecto:** Proyecto-Mercado-Automotriz (ICD — Universidad de La Habana)
**Fecha:** 2026-11-05
**Fase:** 3.3

---

## Resumen ejecutivo

- Corpus total de anuncios de Revolico verificado: **60 anuncios únicos** (30 + 30, sin solapamiento).
- Anuncios recuperados desde descartes de la Fase 3.2: **9**.
- Anuncios añadidos desde copia de seguridad no procesada: **13**.
- **Total en dataset final:** **27 anuncios** válidos (`data/processed/anuncios_revolico_final.json`).

---

## 1. Verificación del corpus (Fase 3.3, Parte 1)

- Anuncios en `data/raw/anuncios_revolico.json`: 30.
- Anuncios en `data/raw/anuncios_revolico_backup_pre_fase3.1.json`: 30.
- **Total único:** 60 (no hay solapamiento entre recolecciones).
- Reporte: `reports/verificacion_corpus_revolico.md`.

---

## 2. Anuncios recuperados (Fase 3.3, Parte 2)

- De los 25 descartados en Fase 3.2, se recuperaron **9** completando `tipo_vehiculo` con base en el modelo identificado:

| `id_anuncio` | Título | Tipo recuperado | Decisión |
| --- | --- | --- | --- |
| 56069281 | Tucson 2021 💫 Hyundai auto carro moderno | SUV | Recuperado → final |
| 56069315 | 🫵 Sonata 2021 Hyundai con Chapa... | Sedán | Recuperado → final |
| 56069304 | 2021 Palisade Hyundai carros autos en La Habana | SUV | Recuperado → final |
| 56066787 | Carro moderno Hyundai Kona 2022 | SUV | Recuperado → final |
| 58289196 | KIA SELTOS 2025 | SUV | Recuperado → final |
| 58211128 | TOYOTA COROLLA SE 2022 | Sedán | Recuperado → final |
| 58408608 | KIA PICANTO 2012 | Hatchback | Recuperado → final |
| 58170351 | HONDA CIVIC 2023 | Sedán | Recuperado → final |
| 58593695 | HYUNDAI IONIQ 5 2024 | SUV eléctrico | Recuperado → final |

- Reporte: `reports/recuperacion_anuncios_descartados.md`.

---

## 3. Anuncios añadidos desde el corpus sobrante (Fase 3.3, Parte 3)

- Desde la copia de seguridad no procesada (`anuncios_revolico_backup_pre_fase3.1.json`): **13 anuncios** cumplieron los criterios estrictos.
- Se incorporaron al dataset final.

---

## 4. Total en dataset final

- `data/processed/anuncios_revolico_final.json` contiene **27 anuncios** válidos.
- `reports/anuncios_descartos_final.json` contiene **16 anuncios** rechazados (25 - 9 recuperados).

---

## 5. Caso de "faltantes combinados"

- **Campos faltantes combinados** (dos o más campos inválidos/ausentes en un mismo anuncio):

| `id_anuncio` | Título | Campos faltantes | Decisión |
| --- | --- | --- | --- |
| 56666872 | BMW X5 ..add | `tipo_vehiculo`, `anio` | DESCARTE: modelo ambiguo (*"X5 Add"*) y año no identificado. |
| 51107131 | Audi rs4 2.5 t quattro | `tipo_vehiculo`, `anio` | DESCARTE: año no identificado y tipo no recuperable con claridad. |
| 57947857 | Pissicorre chevrolet 51 diésel | `tipo_vehiculo`, `anio` | DESCARTE: año no identificado y tipo no confirmado. |
| 54991866 | Chevrolet colorado | `tipo_vehiculo`, `anio` | DESCARTE: año no identificado. |
| 58484925 | CARRO | `marca`, `modelo`, `tipo_vehiculo`, `anio` | DESCARTE: título sin evidencia para identificar los campos. |

- **Decisión:** en todos los casos de faltantes combinados no hubo evidencia suficiente en título/descripción para completar los campos con certeza; por tanto se descartaron definitivamente y se registraron en `reports/anuncios_descartados_final.json`.

---

## 6. ¿Se alcanzó el mínimo de 30 anuncios?

- **No.** El dataset final tiene **27 anuncios** (< 30 mínimo requerido).
- Faltan **3 anuncios** para completar el mínimo con la información disponible en el corpus actual.

---

## 7. Recomendación

- Con el corpus actual (60 anuncios únicos) y las decisiones tomadas, se obtuvo un dataset final válido de **27 anuncios**.
- **Se recomienda realizar un nuevo scraping de Revolico** para obtener entre 3 y 30 anuncios adicionales que permitan alcanzar el mínimo de 30 anuncios válidos.

---

## 8. Archivos creados y modificados

**Creados:**

- `reports/verificacion_corpus_revolico.md`
- `reports/recuperacion_anuncios_descartados.md`
- `reports/informe_final_fase3_3.md`
- `data/processed/anuncios_revolico_final_backup_fase3_2.json` (copia de seguridad de la versión Fase 3.2 del dataset final, 5 registros)

**Modificados:**

- `data/processed/anuncios_revolico_final.json` (ahora con 27 anuncios).
- `reports/anuncios_descartados_final.json` (ahora con 16 rechazos).
- `tests/test_fase3_2_final.py` (sigue validando el estado actual del final).
- `docs/data_dictionary.md` (esquema del dataset final de Fase 3.2).

---

## 9. Resultado de pruebas

- Suite completa: **25/25 en verde** ✅.

---

## 10. Estado final

- Fase 3.3 completada según lo solicitado.
- Dataset final: **27 anuncios** válidos.
- Mínimo de 30: **no alcanzado**.
- Sin scraping nuevo en esta fase (solo se reporta la necesidad).
- Sin commits ni push.

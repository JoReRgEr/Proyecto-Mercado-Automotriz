# Verificación del Corpus de Anuncios Revolico (Fase 3.3)

**Proyecto:** Proyecto-Mercado-Automotriz (ICD — Universidad de La Habana)
**Fecha:** 2026-11-05
**Fase:** 3.3 — Recuperación de anuncios descartados, verificación del corpus total y completado del dataset final

---

## 1. Resultado de la verificación del corpus

### 1.1. Anuncios crudos de Revolico encontrados

| Archivo | Tipo | Número de registros |
| --- | --- | ---: |
| `data/raw/anuncios_revolico.json` | Anuncios Revolico (muestra Fase 3.1) | 30 |
| `data/raw/anuncios_revolico_backup_pre_fase3.1.json` | Anuncios Revolico (copia de seguridad / muestra Fase 2) | 30 |
| `data/raw/entrevistas.json` | Entrevistas | 30 |
| `data/raw/mercado_formal.json` | Mercado Formal | 10 |

### 1.2. Total de anuncios crudos únicos

- **Anuncios de Revolico únicos en el corpus:** **60** (30 del archivo actual + 30 del backup).
- **Sin solapamiento** entre ambas recolecciones: 0 anuncios compartidos por `id_anuncio` o por URL.
- Por lo tanto, el corpus total de anuncios de Revolico contiene **60 anuncios únicos**.

### 1.3. Cobertura del dataset final

- `data/processed/anuncios_revolico_final.json` (Fase 3.2): 5 anuncios validados sobre la muestra Fase 3.1.
- `reports/anuncios_descartados_final.json` (Fase 3.2): 25 anuncios descartados de la muestra Fase 3.1.
- La copia de seguridad (Fase 2) no había sido procesada hasta la Fase 3.3; de ella se aprobaron **13 anuncios** que se incorporaron al dataset final.

---

## 2. Conclusión

- El corpus total de anuncios de Revolico del repositorio contiene **60 anuncios únicos**.
- Las dos recolecciones no se solapan.
- Tras el procesamiento de la copia de seguridad y las recuperaciones, el dataset final quedó en **27 anuncios válidos**.
- El mínimo de **30 anuncios** **no fue alcanzado** con la información disponible.

# Metodología de Entrevistas

**Proyecto:** ICD Proyecto Mercado — Fase 2.

## Objetivo

Recoger declaraciones de al menos 30 personas relacionadas con el mercado automotriz cubano, orientadas a comprender la modernización del automóvil en La Habana.

## Diseño

- Entrevistas individuales o grupales pequeñas.
- Preguntas: ver `docs/interview_questionnaire.md`.

## Consideraciones éticas y de datos

- Participación voluntaria.
- Almacenamiento de respuestas **anónimo**.
- No recopilar nombres, teléfonos, direcciones personales ni datos identificativos.
- Solo información declarativa de las personas.

## Registro

- Cada entrevista se registra con `id_entrevista`, `fecha`, `perfil_general`, `rango_edad` (opcional), `relacion_con_el_mercado`, `zona` y `respuestas`.
- Las respuestas se organizan por identificadores de preguntas (`question_id`).
- El dataset inicial está vacío (`data/raw/entrevistas.json`) hasta completar las entrevistas.

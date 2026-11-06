# Metodología de Entrevistas

**Proyecto:** ICD Proyecto Mercado — Fase 2 y Fase 4.

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

- Cada entrevista se registra con `id_entrevista`, `zona`, `ocupacion`, `relacion_con_el_mercado`, `propietario_vehiculo`, `experiencia_vehiculos_electricos` y `respuestas`.
- Las respuestas se organizan en el campo `respuestas` con los identificadores de los temas tratados (`tipo_vehiculo_observado`, `marcas_modernas_observadas`, `opinion_vehiculos_electricos`, `predominio_autos_clasicos`).
- El dataset de entrevistas contiene las 30 entrevistas registradas (`data/raw/entrevistas.json` y `data/processed/entrevistas.json`).
- Las respuestas se registran de forma declarativa y anónima; no se recopilan datos personales identificativos.

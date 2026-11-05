# AGENTS.md

Instrucciones para agentes de IA (y desarrolladores) trabajando en este repositorio.

## Proyecto

- **Nombre**: Proyecto-Mercado-Automotriz
- **Tema**: Mercado de venta de automóviles en La Habana, Cuba.
- **Asignatura**: Introducción a Ciencia de Datos (ICD).
- **Objetivo**: Extraer ≥30 anuncios informales, recolectar concesionarios formales y entrevistas (≥30 personas), estructurar los datos y hacer un análisis exploratorio del mercado.

## Estructura de carpetas

```
data/raw/           # Salida del scraper (JSON con anuncios originales)
data/processed/     # JSON limpio y estructurado
reports/figures/    # Gráficas del EDA
src/                # Código fuente (scraper, procesamiento, EDA, DB)
notebooks/          # Notebooks de Jupyter
docs/               # Documentación
tests/              # Pruebas
```

## Convenciones

- Python 3.10+, con type hints y docstrings en los módulos de `src/`.
- Los datos viven en `data/`; los artefactos generados en `reports/figures/` y `data/processed/`.
- Los notebooks viven en `notebooks/` y el código que sustenta análisis complejos debe moverse a `src/`.
- Mantener el flujo: `raw` → `processed` → análisis → base de datos.

## Comandos

```bash
python -m venv .venv
pip install -r requirements.txt
python -m pytest       # pruebas
jupyter lab            # notebooks
```

## Estado actual

Fase de **setup inicial**. El scraper **no** ha sido desarrollado todavía; primero se prepara la estructura, dependencias y pruebas.

## Reglas para agentes

- No hacer commits ni push a GitHub sin confirmación explícita del usuario.
- No subir datos personales ni información sensible de entrevistados al repositorio.
- Mantener el alcance del proyecto pequeño: terminar la semana 1 con la estructura funcional.

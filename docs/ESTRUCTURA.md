# Estructura del proyecto ICD Proyecto Mercado

Proyecto-Mercado-Automotriz/
├── data/
│   ├── raw/          # Anuncios scrapeados de páginas informales (JSON)
│   └── processed/    # Datos limpios y transformados (JSON)
├── reports/
│   └── figures/      # Gráficas del análisis exploratorio
├── src/              # Código fuente (scraper, procesamiento, EDA, DB)
├── notebooks/        # Notebooks de análisis exploratorio
├── docs/            # Documentación y notas del proyecto
├── tests/           # Pruebas automatizadas
├── README.md
├── AGENTS.md
└── requirements.txt

- **`data/raw/`**: Salida del scraper. Un JSON por página o fuente con los anuncios originales.
- **`data/processed/`**: JSON con anuncios, concesionarios y entrevistas ya normalizados y limpios.
- **`reports/figures/`**: Gráficas generadas por el análisis exploratorio.
- **`src/`**: Módulos de Python (scraper, limpieza, análisis, conexión a base de datos).
- **`notebooks/`**: Notebooks de Jupyter para el EDA visual.
- **`docs/`**: Notas, decisiones de diseño y documentación del proyecto.
- **`tests/`**: Pruebas unitarias y de estructura.

El flujo de trabajo esperado es: `raw/` (scraper) → `processed/` (limpieza) → `reports/figures/` (EDA) → base de datos.

# Proyecto-Mercado-Automotriz

Repositorio dedicado a la recopilación y análisis de datos sobre el mercado automotriz en La Habana, Cuba.

Proyecto de primer semestre de la asignatura **Introducción a Ciencia de Datos**.

## Objetivo

Analizar el mercado de venta de automóviles en La Habana a partir de:

- **Scraping**: extracción de anuncios de venta desde páginas informales (mínimo 30 anuncios).
- **Datos formales**: información de concesionarios y empresas formales del mercado.
- **Entrevistas**: declaraciones de al menos 30 personas sobre la compra y venta de autos.

Con esos datos se busca estructurar la información, realizar un análisis exploratorio del mercado y llegar a conclusiones sobre la modernización del automóvil en Cuba.

## Estructura del proyecto

```
Proyecto-Mercado-Automotriz/
├── data/
│   ├── raw/          # Anuncios scrapeados (JSON) - revolico, entrevistas, mercado formal
│   └── processed/    # Datos limpios y normalizados (JSON)
├── reports/
│   └── figures/      # Gráficas del análisis exploratorio
├── src/              # Código fuente (scraper, procesamiento, EDA, DB)
├── notebooks/        # Notebooks de Jupyter para el EDA
├── docs/            # Documentación del proyecto
├── examples/        # Ejemplos de esquemas JSON
├── tests/           # Pruebas automatizadas
├── README.md
├── AGENTS.md
└── requirements.txt
```

- `data/raw/`: salida del scraper y de las fuentes en colecciones JSON (anuncios, entrevistas, mercado formal).
- `data/processed/`: JSON con anuncios, concesionarios y entrevistas ya limpios y estructurados.
- `reports/figures/`: gráficas generadas por el análisis exploratorio.
- `src/`: módulos de Python para cada fase del proyecto.
- `notebooks/`: notebooks de Jupyter con el análisis exploratorio.
- `docs/`: documentación, decisiones y notas del proyecto.
- `tests/`: pruebas del proyecto.
- `examples/`: ejemplos de esquemas JSON por fuente.

## Flujo de datos

```
scraping (data/raw) → limpieza (data/processed) → análisis (reports/figures)
        → base de datos ← JSON procesado
```

1. El **scraper** guarda los anuncios obtenidos en `data/raw/` como JSON.
2. El **procesamiento** normaliza y estructura los datos en `data/processed/`.
3. El **análisis exploratorio** genera gráficas en `reports/figures/`.
4. Todo se carga en una **base de datos** y se analiza con Python.

## Requisitos

- Python 3.10 o superior
- pip

## Instalación

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
source .venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

## Uso

### Scraper de Revolico

```bash
python src/scraper_revolico.py --max-anuncios 30
```

Guarda los anuncios en `data/raw/anuncios_revolico.json`. El parámetro `--max-anuncios` permite configurar el máximo de anuncios a recolectar.

### Procesamiento

```bash
python src/process_revolico.py
```

Copia los anuncios procesados a `data/processed/anuncios_revolico.json` conservando los campos originales.

### Pruebas

```bash
python -m pytest        # ejecutar pruebas
```

## Estado del proyecto

Fase actual: **Fase 3 — Integración del Mercado Formal y procesamiento de los anuncios de Revolico**.

La Fase 3 incorpora:

1. Auditoría de fuentes del Mercado Formal (repositorio del compañero): `docs/mercado_formal_source_audit.md`.
2. Construcción de datasets JSON del Mercado Formal: `data/raw/mercado_formal.json` y `data/processed/mercado_formal.json`.
3. Procesamiento de los 30 anuncios de Revolico: `src/process_revolico.py`, `data/processed/anuncios_revolico.json`, `reports/ambiguedades_revolico.json`, `reports/data_quality_summary.json`.

Próximas fases:

1. Análisis exploratorio (EDA) sobre los datos procesados.
2. Ampliación de entrevistas (mínimo 30 personas).
3. Carga en base de datos.
4. Gráficas y conclusiones definitivas.

## Autor

Jorge Luis Bolaño Perdomo

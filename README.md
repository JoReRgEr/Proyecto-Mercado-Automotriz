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

- `data/raw/`: salida del scraper y de las fuentes en colecciones JSON (anuncios, entrevistas, mercado formal).
- `data/processed/`: JSON con anuncios, concesionarios y entrevistas ya limpios y estructurados.
- `reports/figures/`: gráficas generadas por el análisis exploratorio.
- `src/`: módulos de Python para cada fase del proyecto.
- `notebooks/`: notebooks de Jupyter con el análisis exploratorio.
- `docs/`: documentación, decisiones y notas del proyecto.
- `tests/`: pruebas del proyecto.
- `examples/`: ejemplos de esquemas JSON por fuente.

## Flujo de datos

scraping (data/raw) → limpieza (data/processed) → análisis (reports/figures)
        → base de datos ← JSON procesado

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

El scraper excluye automaticamente publicaciones que no corresponden a la venta de un automovil completo (baterias, piezas, accesorios, servicios, transporte) y registra los descartes en el archivo indicado por `--descartados`.

### Procesamiento

```bash
python src/process_revolico.py
```

Genera `data/processed/anuncios_revolico_processed_update.json` con la estructura definitiva de Fase 3.1 (precios normalizados, conversion USD -> CUP con tasa de referencia de 920, unidad de kilometraje, tipo de vehiculo, etc.).

- Tasa de conversion: `docs/exchange_rate_reference.md` (1 USD = 920 CUP).
- Descartes del scraper: `reports/anuncios_descartes_revolico.json`.
- Ambiguedades: `reports/ambiguedades_revolico_update.json` y `reports/ambiguedades_revolico_update.md`.
- Resumen de calidad: `reports/data_quality_summary_update.json` y `reports/data_quality_summary_update.md`.

### Pruebas

```bash
python -m pytest        # ejecutar pruebas
```

## Estado del proyecto

Fase actual: **Fase 4 — Consolidación de fuentes y preparación para el análisis exploratorio (EDA)**.

Las tres fuentes de datos están listas para el análisis:

1. **Revolico**: `data/raw/anuncios_revolico.json` (nueva muestra Fase 3.1 de 30 anuncios validos + respaldo + descartes) y `data/processed/anuncios_revolico_processed_update.json` (estructura definitiva con conversion USD -> CUP y tasa de referencia de 920).
2. **Mercado Formal**: `data/raw/mercado_formal.json` y `data/processed/mercado_formal.json` (10 entidades).
3. **Entrevistas**: `data/raw/entrevistas.json` y `data/processed/entrevistas.json` (30 entrevistas registradas).

Próximas fases:

1. Análisis exploratorio (EDA) sobre los datos procesados (gráficas en `reports/figures/`, notebooks en `notebooks/`).
2. Carga en base de datos.
3. Gráficas y conclusiones definitivas.

> En la Fase 4 no se realizaron nuevos escaneos ni recolecciones; solo se consolidaron las fuentes existentes.

## Autor

Jorge Luis Bolaño Perdomo

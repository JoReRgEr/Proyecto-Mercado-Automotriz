# Proyecto-Mercado-Automotriz

Repositorio dedicado a la recopilación y análisis de datos sobre el mercado automotriz en La Habana, Cuba.

Proyecto de primer semestre de la asignatura **Introducción a Ciencia de Datos**.

## Objetivo

Analizar el mercado de venta de automóviles en La Habana a partir de:

- **Scraping**: extracción de anuncios de venta desde páginas informales (mínimo 30 anuncios).
- **Datos formales**: información de concesionarios y empresas formales del mercado.
- **Entrevistas**: declaraciones de al menos 30 personas sobre la compra y venta de autos.

Con esos datos se estructura la información, se realiza un análisis exploratorio del mercado y se llegan a conclusiones sobre la modernización del automóvil en Cuba.

## Estructura del proyecto

```
Proyecto-Mercado-Automotriz/
├── data/
│   ├── raw/              # Datos crudos (JSON): anuncios, catálogos, mercado formal
│   ├── processed/        # Datos intermedios y de trabajo (JSON)
│   ├── processed_final/  # DataSets finales (JSON) - no se modifican
│   │   ├── anuncios_revolico_final.json
│   │   ├── mercado_formal_final.json
│   │   └── entrevistas_final.json
│   └── data_backup/      # Copias de seguridad (JSON)
├── reports/
│   ├── figures/          # Gráficas del EDA (PNG)
│   ├── informe_final_fase4_1.md
│   ├── informe_final_fase4_2.md
│   ├── catalagos_analisis_extra.md
│   ├── modelos_a_consultar_dongfeng.md
│   └── otros informes...
├── src/                  # Código fuente (scraper, procesamiento)
├── notebooks/            # Notebooks de Jupyter
│   ├── 00_setup_and_overview.ipynb          # Entrada técnica
│   ├── 01_analisis_revolico.ipynb           # Apoyo: mercado informal
│   ├── 02_analisis_mercado_formal.ipynb     # Apoyo: mercado formal
│   ├── 03_analisis_entrevistas.ipynb        # Apoyo: entrevistas
│   └── 04_integracion_y_conclusiones.ipynb  # PRINCIPAL (para presentar)
├── docs/                 # Documentación
│   ├── data_dictionary.md
│   ├── eda_plan.md
│   ├── conclusiones.md
│   └── otros documentos...
├── examples/             # Ejemplos de esquemas JSON
├── tests/                # Pruebas automatizadas
├── requirements.txt
├── README.md
└── AGENTS.md
```

- `data/raw/`: salida del scraper y de las fuentes en colecciones JSON (anuncios, entrevistas, mercado formal, catálogos).
- `data/processed_final/`: dataSets finales listos para el EDA (no se modifican).
- `data/data_backup/`: copias de seguridad de versiones previas.
- `reports/figures/`: gráficas generadas por el análisis exploratorio.
- `src/`: módulos de Python para cada fase del proyecto.
- `notebooks/`: notebooks de Jupyter con el análisis exploratorio.
- `docs/`: documentación, decisiones, diccionario de datos y conclusiones.
- `tests/`: pruebas automatizadas del proyecto.
- `examples/`: ejemplos de esquemas JSON por fuente.

## Estructura de notebooks (importante para la presentación)

- **`notebooks/04_integracion_y_conclusiones.ipynb`**: NOTEBOOK PRINCIPAL (MAESTRO). Es el que se abre para la presentación y defensa del proyecto. Recorre toda la historia: tema, preguntas de investigación, metodología, hallazgos de cada mercado, integración, tendencias y conclusiones finales.
- **`notebooks/01_analisis_revolico.ipynb`**: notebook de apoyo con el análisis detallado del mercado informal.
- **`notebooks/02_analisis_mercado_formal.ipynb`**: notebook de apoyo con el análisis detallado del mercado formal.
- **`notebooks/03_analisis_entrevistas.ipynb`**: notebook de apoyo con el análisis detallado de las entrevistas.
- **`notebooks/00_setup_and_overview.ipynb`**: punto de entrada técnico; carga y describe los tres dataSets finales.

## Flujo de datos

scraping (data/raw) → limpieza (data/processed) → análisis (reports/figures) → notebooks → base de datos

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

### Ejecutar los notebooks

Abrir en Jupyter Lab o Jupyter Notebook:

```bash
jupyter lab notebooks/
```

El notebook principal para la presentación es **`04_integracion_y_conclusiones.ipynb`**.

### Ejecutar las pruebas

```bash
python -m pytest        # ejecutar pruebas (35 pruebas, todas pasando)
```

## Resultados principales del EDA (Fase 5)

### Mercado informal (Revolico - 30 anuncios)

- Hyundai domina con 63% de los anuncios.
- SUV es el tipo más frecuente (50%).
- Solo 10% son vehículos eléctricos.
- Rango de precios: 10.000 – 100.000 USD (mediana 31.000 USD).

### Mercado formal (10 entidades)

- Solo 2 entidades tienen catálogo público: Dongfeng Cuba (49 modelos) y BDC ONE (16 modelos).
- 21 de 65 modelos en catálogos son eléctricos.
- Precios formales: 14.849 – 99.000 EUR (sin impuestos).

### Entrevistas (30 personas)

- 83% creen que predominan los autos clásicos.
- 87% tienen opinión negativa sobre vehículos eléctricos.
- Kia y Hyundai son las marcas modernas más mencionadas.

## Limitaciones

- Muestra pequeña (30 anuncios, 30 entrevistas).
- Entrevistas concentradas en Alamar (20 de 30).
- Precios formales sin impuestos; 15 modelos sin precio público.
- Sin año-modelo en catálogos formales.
- Revolico como única plataforma informal.

## Trabajo futuro

- Ampliar la muestra de anuncios y entrevistas.
- Incluir más plataformas de venta informal.
- Estudiar el impacto de los precios de combustibles.
- Analizar políticas de importación y aranceles.
- Estudiar la infraestructura de carga eléctrica.

## Autor

Jorge Luis Bolaño Perdomo

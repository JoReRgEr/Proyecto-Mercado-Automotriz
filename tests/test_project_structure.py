"""Pruebas de estructura del proyecto ICD Proyecto Mercado."""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

REQUIRED_DIRECTORIES = [
    "data/raw",
    "data/processed",
    "reports/figures",
    "src",
    "notebooks",
    "docs",
    "tests",
    "examples",
]

REQUIRED_FILES = [
    "README.md",
    "AGENTS.md",
    "requirements.txt",
]


def test_required_directories_exist() -> None:
    """Verifica que las carpetas base del proyecto existan."""
    for rel_path in REQUIRED_DIRECTORIES:
        assert (PROJECT_ROOT / rel_path).is_dir(), f"Falta el directorio requerido: {rel_path}"


def test_required_files_exist() -> None:
    """Verifica que los archivos base del proyecto existan."""
    for file_name in REQUIRED_FILES:
        assert (PROJECT_ROOT / file_name).is_file(), f"Falta el archivo requerido: {file_name}"

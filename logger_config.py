import logging
import os

# Crear carpeta logs si no existe
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/sistema.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    encoding="utf-8"
)

logger = logging.getLogger(__name__)
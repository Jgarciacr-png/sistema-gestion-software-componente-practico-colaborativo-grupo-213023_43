from interfaz.app import AppSistema
from logger_config import logger


def main():

    logger.info("===== Inicio del sistema =====")

    app = AppSistema()
    app.ejecutar()

    logger.info("===== Cierre del sistema =====")


if __name__ == "__main__":
    main()
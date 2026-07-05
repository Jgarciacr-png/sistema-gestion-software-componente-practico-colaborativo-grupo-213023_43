from datetime import datetime

from excepciones import (
    FechaInvalidaError,
    ReservaError
)


class Reserva:

    def __init__(self, cliente, servicio, fecha):

        self._cliente = cliente
        self._servicio = servicio

        self.fecha = fecha

        self._estado = "Pendiente"

    @property
    def cliente(self):
        return self._cliente

    @property
    def servicio(self):
        return self._servicio

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, nueva_fecha):

        try:

            datetime.strptime(nueva_fecha, "%Y-%m-%d")

        except ValueError as error:

            raise FechaInvalidaError(
                "La fecha debe tener formato YYYY-MM-DD."
            ) from error

        self._fecha = nueva_fecha

    @property
    def estado(self):
        return self._estado

    def confirmar_reserva(self):

        try:

            if self.estado == "Cancelada":

                raise ReservaError(
                    "No se puede confirmar una reserva cancelada."
                )

            self._estado = "Confirmada"

        except ReservaError as error:

            print(f"Error: {error}")

        finally:

            print("Proceso de confirmación finalizado.")

    def cancelar_reserva(self):

        self._estado = "Cancelada"

    def mostrar_info(self):

        return (
            f"Cliente: {self.cliente.nombre}\n"
            f"Servicio: {self.servicio.nombre}\n"
            f"Fecha: {self.fecha}\n"
            f"Estado: {self.estado}"
        )
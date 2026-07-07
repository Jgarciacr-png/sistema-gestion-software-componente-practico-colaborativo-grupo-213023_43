from excepciones import (
    FechaInvalidaError,
    ReservaError
)


class Reserva:
    """
    Representa una reserva realizada por un cliente
    para un servicio determinado.
    """

    def __init__(self, cliente, servicio, fecha):

        self._cliente = cliente
        self._servicio = servicio
        self._fecha = fecha
        self._estado = "Pendiente"

    # ==========================
    # PROPIEDADES
    # ==========================

    @property
    def cliente(self):
        return self._cliente

    @property
    def servicio(self):
        return self._servicio

    @property
    def fecha(self):
        return self._fecha

    @property
    def estado(self):
        return self._estado

    # ==========================
    # MÉTODOS
    # ==========================

    def confirmar_reserva(self):
        """
        Confirma una reserva si la fecha es válida.
        """

        try:

            if not self.fecha.strip():

                raise FechaInvalidaError(
                    "La fecha no puede estar vacía."
                )

            self._estado = "Confirmada"

        except FechaInvalidaError as error:

            raise ReservaError(
                f"Error al confirmar la reserva: {error}"
            ) from error

        else:

            print("Reserva confirmada correctamente.")

        finally:

            print("Proceso de confirmación finalizado.")

    def cancelar_reserva(self):
        """
        Cancela una reserva previamente creada.
        """

        try:

            if self.estado == "Cancelada":

                raise ReservaError(
                    "La reserva ya fue cancelada."
                )

            self._estado = "Cancelada"

        except ReservaError as error:

            raise ReservaError(
                f"Error al cancelar la reserva: {error}"
            ) from error

        else:

            print("Reserva cancelada correctamente.")

        finally:

            print("Proceso de cancelación finalizado.")

    def mostrar_info(self):
        """
        Devuelve la información completa de la reserva.
        """

        return (
            f"Cliente : {self.cliente.nombre}\n"
            f"Servicio: {self.servicio.nombre}\n"
            f"Costo   : ${self.servicio.calcular_costo():,.0f}\n"
            f"Fecha   : {self.fecha}\n"
            f"Estado  : {self.estado}"
        )

    def __str__(self):
        """
        Representación en texto de la reserva.
        """

        return self.mostrar_info()
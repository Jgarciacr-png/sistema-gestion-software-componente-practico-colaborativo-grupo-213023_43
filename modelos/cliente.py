from modelos.entidad import Entidad


class Cliente(Entidad):
    """
    Representa un cliente del sistema de reservas.
    """

    def __init__(self, id_entidad, nombre, correo, telefono):

        super().__init__(id_entidad, nombre)

        self.correo = correo
        self.telefono = telefono

    # ==========================
    # PROPIEDADES
    # ==========================

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, nuevo_correo):

        if (
            "@" not in nuevo_correo
            or "." not in nuevo_correo
        ):
            raise ValueError(
                "Correo electrónico inválido."
            )

        self._correo = nuevo_correo

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, nuevo_telefono):

        if not nuevo_telefono.isdigit():
            raise ValueError(
                "El teléfono solo debe contener números."
            )

        if len(nuevo_telefono) != 10:
            raise ValueError(
                "El teléfono debe tener exactamente 10 dígitos."
            )

        self._telefono = nuevo_telefono

    # ==========================
    # MÉTODOS
    # ==========================

    def mostrar_info(self):
        """
        Devuelve la información del cliente.
        """

        return (
            f"ID       : {self.id_entidad}\n"
            f"Nombre   : {self.nombre}\n"
            f"Correo   : {self.correo}\n"
            f"Teléfono : {self.telefono}"
        )

    def __str__(self):

        return self.mostrar_info()
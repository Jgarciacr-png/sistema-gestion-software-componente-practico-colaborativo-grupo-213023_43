from modelos.entidad import Entidad


class Cliente(Entidad):

    def __init__(self, id_entidad, nombre, correo, telefono):
        super().__init__(id_entidad, nombre)

        self._correo = correo
        self._telefono = telefono

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, nuevo_correo):

        if "@" not in nuevo_correo:
            raise ValueError("Correo inválido.")

        self._correo = nuevo_correo

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, nuevo_telefono):

        if not nuevo_telefono.isdigit():
            raise ValueError("El teléfono solo debe contener números.")

        self._telefono = nuevo_telefono

    def mostrar_info(self):

        return (
            f"ID: {self.id_entidad}\n"
            f"Nombre: {self.nombre}\n"
            f"Correo: {self.correo}\n"
            f"Teléfono: {self.telefono}"
        )
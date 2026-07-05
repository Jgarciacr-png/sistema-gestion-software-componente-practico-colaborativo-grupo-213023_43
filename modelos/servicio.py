from modelos.entidad import Entidad


class Servicio(Entidad):

    def __init__(self, id_entidad, nombre, precio):
        super().__init__(id_entidad, nombre)
        self._precio = precio

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, nuevo_precio):

        if nuevo_precio < 0:
            raise ValueError("El precio no puede ser negativo.")

        self._precio = nuevo_precio

    def calcular_costo(self):

        return self._precio

    def describir_servicio(self):

        return f"Servicio: {self.nombre} - Precio: ${self.precio}"

    def mostrar_info(self):

        return (
            f"ID: {self.id_entidad}\n"
            f"Servicio: {self.nombre}\n"
            f"Precio: ${self.precio}"
        )
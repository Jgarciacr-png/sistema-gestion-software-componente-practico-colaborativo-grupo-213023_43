from modelos.servicio import Servicio


class Equipo(Servicio):

    def __init__(self, id_entidad, nombre, costo_base, tipo):

        super().__init__(id_entidad, nombre, costo_base)

        self._tipo = tipo

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, nuevo_tipo):

        if not nuevo_tipo.strip():
            raise ValueError(
                "El tipo no puede estar vacío."
            )

        self._tipo = nuevo_tipo

    def calcular_costo(self):

        return self.costo_base * 1.15

    def describir_servicio(self):

        return (
            f"Equipo: {self.nombre}\n"
            f"Tipo: {self.tipo}\n"
            f"Costo: ${self.calcular_costo():,.0f}"
        )

    def mostrar_info(self):

        return self.describir_servicio()
from modelos.servicio import Servicio


class Sala(Servicio):

    def __init__(self, id_entidad, nombre, costo_base, capacidad):

        super().__init__(id_entidad, nombre, costo_base)

        self._capacidad = capacidad

    @property
    def capacidad(self):
        return self._capacidad

    @capacidad.setter
    def capacidad(self, nueva_capacidad):

        if nueva_capacidad <= 0:
            raise ValueError(
                "La capacidad debe ser mayor que cero."
            )

        self._capacidad = nueva_capacidad

    def calcular_costo(self):

        return self.costo_base * 1.10

    def describir_servicio(self):

        return (
            f"Sala: {self.nombre}\n"
            f"Capacidad: {self.capacidad} personas\n"
            f"Costo: ${self.calcular_costo():,.0f}"
        )

    def mostrar_info(self):

        return self.describir_servicio()
from modelos.servicio import Servicio


class Asesoria(Servicio):

    def __init__(self, id_entidad, nombre, costo_base, especialista):

        super().__init__(id_entidad, nombre, costo_base)

        self._especialista = especialista

    @property
    def especialista(self):
        return self._especialista

    @especialista.setter
    def especialista(self, nuevo_especialista):

        if not nuevo_especialista.strip():
            raise ValueError("El especialista no puede estar vacío.")

        self._especialista = nuevo_especialista

    def calcular_costo(self):

        return self.costo_base * 1.25

    def describir_servicio(self):

        return (
            f"Asesoría: {self.nombre}\n"
            f"Especialista: {self.especialista}\n"
            f"Costo: ${self.calcular_costo()}"
        )

    def mostrar_info(self):

        return self.describir_servicio()
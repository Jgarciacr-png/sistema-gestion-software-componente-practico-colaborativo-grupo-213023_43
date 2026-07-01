from abc import ABC, abstractmethod
from modelos.entidad import Entidad


class Servicio(Entidad, ABC):

    def __init__(self, id_entidad, nombre, costo_base):
        super().__init__(id_entidad, nombre)

        self._costo_base = costo_base

    @property
    def costo_base(self):
        return self._costo_base

    @costo_base.setter
    def costo_base(self, nuevo_costo):

        if nuevo_costo <= 0:
            raise ValueError("El costo debe ser mayor que cero.")

        self._costo_base = nuevo_costo

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def describir_servicio(self):
        pass
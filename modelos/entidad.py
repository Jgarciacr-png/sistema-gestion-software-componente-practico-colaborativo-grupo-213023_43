from abc import ABC, abstractmethod


class Entidad(ABC):
    """
    Clase abstracta, base para las entidades del sistema.
    """

    def __init__(self, id_entidad, nombre):
        self._id_entidad = id_entidad
        self._nombre = nombre

    @property
    def id_entidad(self):
        return self._id_entidad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if not nuevo_nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = nuevo_nombre

    @abstractmethod
    def mostrar_info(self):
        """
        Método abstracto que deberán implementar las clases hijas.
        """
        pass
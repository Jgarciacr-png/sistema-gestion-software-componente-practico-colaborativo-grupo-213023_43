from abc import ABC, abstractmethod


class Entidad(ABC):
    """
    Clase abstracta que representa una entidad genérica del sistema.
    Sirve como clase base para Cliente y Servicio.
    """

    def __init__(self, id_entidad, nombre):

        if not str(id_entidad).strip():
            raise ValueError(
                "El identificador no puede estar vacío."
            )

        self._id_entidad = id_entidad
        self.nombre = nombre

    # ==========================
    # PROPIEDADES
    # ==========================

    @property
    def id_entidad(self):
        return self._id_entidad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):

        if not nuevo_nombre.strip():
            raise ValueError(
                "El nombre no puede estar vacío."
            )

        self._nombre = nuevo_nombre

    # ==========================
    # MÉTODOS ABSTRACTOS
    # ==========================

    @abstractmethod
    def mostrar_info(self):
        """
        Devuelve la información de la entidad.
        """
        pass

    def __str__(self):
        return self.mostrar_info()
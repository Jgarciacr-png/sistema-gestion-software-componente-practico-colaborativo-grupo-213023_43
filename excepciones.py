class ClienteError(Exception):
    """Excepción para errores relacionados con clientes."""
    pass


class ServicioError(Exception):
    """Excepción para errores relacionados con servicios."""
    pass


class ReservaError(Exception):
    """Excepción para errores relacionados con reservas."""
    pass


class FechaInvalidaError(ReservaError):
    """Error cuando la fecha es inválida."""
    pass


class ServicioNoDisponibleError(ServicioError):
    """Error cuando un servicio no está disponible."""
    pass
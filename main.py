from modelos.cliente import Cliente
from modelos.sala import Sala
from modelos.reserva import Reserva


def main():

    print("=== SISTEMA DE GESTIÓN DE RESERVAS ===\n")

    # Crear cliente
    cliente1 = Cliente(
        1,
        "Jonathan Garcia",
        "jonathan@gmail.com",
        "3001234567"
    )

    # Crear servicio
    sala1 = Sala(
        101,
        "Sala Principal",
        200000,
        30
    )

    # Crear reserva
    reserva1 = Reserva(
        cliente1,
        sala1,
        "2026-07-10"
    )

    # Confirmar reserva
    reserva1.confirmar_reserva()

    # Mostrar información
    print(reserva1.mostrar_info())


if __name__ == "__main__":
    main()
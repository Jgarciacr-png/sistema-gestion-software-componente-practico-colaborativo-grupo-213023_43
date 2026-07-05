import tkinter as tk
from tkinter import messagebox

from modelos.cliente import Cliente
from modelos.servicio import Servicio
from modelos.reserva import Reserva


class AppSistema:

    def __init__(self):

        self.ventana = tk.Tk()
        self.ventana.title("Sistema de Gestión de Reservas")
        self.ventana.geometry("700x500")

        titulo = tk.Label(
            self.ventana,
            text="Sistema de Gestión de Reservas",
            font=("Arial", 24, "bold")
        )
        titulo.pack(pady=20)

        # Nombre cliente
        tk.Label(
            self.ventana,
            text="Nombre del cliente:"
        ).pack()

        self.entry_nombre = tk.Entry(
            self.ventana,
            width=40
        )
        self.entry_nombre.pack(pady=5)

        # Correo
        tk.Label(
            self.ventana,
            text="Correo:"
        ).pack()

        self.entry_correo = tk.Entry(
            self.ventana,
            width=40
        )
        self.entry_correo.pack(pady=5)

        # Teléfono
        tk.Label(
            self.ventana,
            text="Teléfono:"
        ).pack()

        self.entry_telefono = tk.Entry(
            self.ventana,
            width=40
        )
        self.entry_telefono.pack(pady=5)

        # Botón
        boton = tk.Button(
            self.ventana,
            text="Crear Reserva",
            font=("Arial", 14),
            command=self.crear_reserva
        )

        boton.pack(pady=20)

        # Resultado
        self.label_resultado = tk.Label(
            self.ventana,
            text="",
            font=("Courier", 14),
            justify="left"
        )

        self.label_resultado.pack(pady=20)

    def crear_reserva(self):

        try:

            nombre = self.entry_nombre.get()
            correo = self.entry_correo.get()
            telefono = self.entry_telefono.get()

            cliente = Cliente(
                "C001",
                nombre,
                correo,
                telefono
            )

            servicio = Servicio(
                "S001",
                "Sala Principal",
                150000
            )

            reserva = Reserva(
                cliente,
                servicio,
                "2026-07-10"
            )

            reserva.confirmar_reserva()

            self.label_resultado.config(
                text=reserva.mostrar_info()
            )

            messagebox.showinfo(
                "Éxito",
                "Reserva creada correctamente."
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    def ejecutar(self):

        self.ventana.mainloop()
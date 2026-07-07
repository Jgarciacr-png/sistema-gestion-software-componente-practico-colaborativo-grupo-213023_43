import tkinter as tk
from tkinter import ttk, messagebox

from tkcalendar import DateEntry

from modelos.cliente import Cliente
from modelos.reserva import Reserva
from modelos.sala import Sala
from modelos.equipo import Equipo
from modelos.asesoria import Asesoria

from interfaz.catalogo import SERVICIOS

from excepciones import ReservaError
from logger_config import logger


class AppSistema:

    def __init__(self):

        # ==============================
        # VENTANA
        # ==============================

        self.ventana = tk.Tk()
        self.ventana.title("Sistema de Gestión de Reservas")
        self.ventana.geometry("980x700")
        self.ventana.configure(bg="#F4F6F7")
        self.ventana.resizable(False, False)

        self.reserva_actual = None

        # ==============================
        # TÍTULO
        # ==============================

        titulo = tk.Label(
            self.ventana,
            text="SISTEMA DE GESTIÓN DE RESERVAS",
            font=("Arial", 22, "bold"),
            bg="#F4F6F7",
            fg="#1F618D"
        )

        titulo.pack(pady=15)

        # ==============================
        # CONTENEDOR PRINCIPAL
        # ==============================

        contenedor = tk.Frame(
            self.ventana,
            bg="#F4F6F7"
        )

        contenedor.pack(fill="both", expand=True, padx=20)

        # ======================================
        # PANEL IZQUIERDO
        # ======================================

        frame_formulario = tk.LabelFrame(
            contenedor,
            text="Datos del Cliente",
            font=("Arial", 12, "bold"),
            padx=15,
            pady=15,
            bg="white"
        )

        frame_formulario.grid(
            row=0,
            column=0,
            sticky="n"
        )

        # ======================================
        # NOMBRE
        # ======================================

        tk.Label(
            frame_formulario,
            text="Nombre",
            bg="white",
            font=("Arial", 10, "bold")
        ).grid(row=0, column=0, sticky="w")

        self.entry_nombre = tk.Entry(
            frame_formulario,
            width=35,
            font=("Arial", 10)
        )

        self.entry_nombre.grid(
            row=1,
            column=0,
            pady=5
        )

        # ======================================
        # CORREO
        # ======================================

        tk.Label(
            frame_formulario,
            text="Correo",
            bg="white",
            font=("Arial", 10, "bold")
        ).grid(row=2, column=0, sticky="w", pady=(10,0))

        self.entry_correo = tk.Entry(
            frame_formulario,
            width=35,
            font=("Arial",10)
        )

        self.entry_correo.grid(
            row=3,
            column=0,
            pady=5
        )

        # ======================================
        # TELÉFONO
        # ======================================

        tk.Label(
            frame_formulario,
            text="Teléfono",
            bg="white",
            font=("Arial",10,"bold")
        ).grid(row=4,column=0,sticky="w",pady=(10,0))

        self.entry_telefono = tk.Entry(
            frame_formulario,
            width=35,
            font=("Arial",10)
        )

        self.entry_telefono.grid(
            row=5,
            column=0,
            pady=5
        )

        # ======================================
        # CATEGORÍA
        # ======================================

        tk.Label(
            frame_formulario,
            text="Categoría",
            bg="white",
            font=("Arial",10,"bold")
        ).grid(row=6,column=0,sticky="w",pady=(15,0))

        self.combo_categoria = ttk.Combobox(
            frame_formulario,
            width=32,
            state="readonly"
        )

        self.combo_categoria["values"] = (
            "Sala",
            "Equipo",
            "Asesoría"
        )

        self.combo_categoria.current(0)

        self.combo_categoria.grid(
            row=7,
            column=0,
            pady=5
        )

        self.combo_categoria.bind(
            "<<ComboboxSelected>>",
            self.actualizar_servicios
        )

        # ======================================
        # SERVICIO
        # ======================================

        tk.Label(
            frame_formulario,
            text="Servicio",
            bg="white",
            font=("Arial",10,"bold")
        ).grid(row=8,column=0,sticky="w",pady=(15,0))

        self.combo_servicio = ttk.Combobox(
            frame_formulario,
            width=32,
            state="readonly"
        )

        self.combo_servicio.grid(
            row=9,
            column=0,
            pady=5
        )

        self.combo_servicio.bind(
            "<<ComboboxSelected>>",
            self.actualizar_detalle_servicio
        )

        # ======================================
        # FECHA
        # ======================================

        tk.Label(
            frame_formulario,
            text="Fecha",
            bg="white",
            font=("Arial",10,"bold")
        ).grid(row=10,column=0,sticky="w",pady=(15,0))

        self.calendario = DateEntry(
            frame_formulario,
            width=33,
            background="#2E86C1",
            foreground="white",
            borderwidth=2,
            date_pattern="yyyy-mm-dd"
        )

        self.calendario.grid(
            row=11,
            column=0,
            pady=5
        )

        # ======================================
        # BOTONES
        # ======================================

        frame_botones = tk.Frame(
            frame_formulario,
            bg="white"
        )

        frame_botones.grid(
            row=12,
            column=0,
            pady=20
        )

        self.boton_crear = tk.Button(
            frame_botones,
            text="Crear Reserva",
            width=15,
            bg="#2E86C1",
            fg="white",
            command=self.crear_reserva
        )

        self.boton_crear.grid(
            row=0,
            column=0,
            padx=5
        )

        self.boton_cancelar = tk.Button(
            frame_botones,
            text="Cancelar",
            width=15,
            bg="#CB4335",
            fg="white",
            command=self.cancelar_reserva
        )

        self.boton_cancelar.grid(
            row=0,
            column=1,
            padx=5
        )

        self.boton_limpiar = tk.Button(
            frame_botones,
            text="Limpiar",
            width=15,
            bg="#7DCEA0",
            command=self.limpiar_formulario
        )

        self.boton_limpiar.grid(
            row=0,
            column=2,
            padx=5
        )
        # ======================================
        # PANEL DERECHO
        # ======================================

        frame_info = tk.LabelFrame(
            contenedor,
            text="Información del Servicio",
            font=("Arial", 12, "bold"),
            padx=15,
            pady=15,
            bg="white",
            width=350,
            height=430
        )

        frame_info.grid(
            row=0,
            column=1,
            padx=20,
            sticky="n"
        )

        frame_info.grid_propagate(False)

        self.label_info = tk.Label(
            frame_info,
            text="Seleccione un servicio.",
            justify="left",
            bg="white",
            font=("Courier New", 11),
            anchor="nw"
        )

        self.label_info.pack(
            fill="both",
            expand=True
        )

        # ======================================
        # RESULTADO DE LA RESERVA
        # ======================================

        frame_resultado = tk.LabelFrame(
            self.ventana,
            text="Detalle de la Reserva",
            font=("Arial", 12, "bold"),
            padx=15,
            pady=15,
            bg="white"
        )

        frame_resultado.pack(
            fill="both",
            padx=20,
            pady=15
        )

        self.text_resultado = tk.Text(
            frame_resultado,
            height=9,
            width=100,
            font=("Courier New", 11),
            state="disabled"
        )

        self.text_resultado.pack()

        # ======================================
        # PIE
        # ======================================

        pie = tk.Label(
            self.ventana,
            text="Fundamentos de Programación - UNAD",
            bg="#F4F6F7",
            fg="gray"
        )

        pie.pack(
            pady=5
        )

        # ======================================
        # CARGAR INFORMACIÓN INICIAL
        # ======================================

        self.actualizar_servicios()

    # ============================================================
    # ACTUALIZAR LISTA DE SERVICIOS
    # ============================================================

    def actualizar_servicios(self, event=None):

        categoria = self.combo_categoria.get()

        if categoria == "Sala":

            servicios = [
                nombre
                for nombre, servicio in SERVICIOS.items()
                if isinstance(servicio, Sala)
            ]

        elif categoria == "Equipo":

            servicios = [
                nombre
                for nombre, servicio in SERVICIOS.items()
                if isinstance(servicio, Equipo)
            ]

        else:

            servicios = [
                nombre
                for nombre, servicio in SERVICIOS.items()
                if isinstance(servicio, Asesoria)
            ]

        self.combo_servicio["values"] = servicios

        if servicios:

            self.combo_servicio.current(0)

        self.actualizar_detalle_servicio()

    # ============================================================
    # MOSTRAR INFORMACIÓN DEL SERVICIO
    # ============================================================

    def actualizar_detalle_servicio(self, event=None):

        nombre = self.combo_servicio.get()

        if nombre == "":
            return

        servicio = SERVICIOS[nombre]

        texto = servicio.describir_servicio()

        self.label_info.config(
            text=texto
        )

    # ============================================================
    # CREAR RESERVA
    # ============================================================

    def crear_reserva(self):

        try:

            cliente = Cliente(
                "C001",
                self.entry_nombre.get(),
                self.entry_correo.get(),
                self.entry_telefono.get()
            )

            servicio = SERVICIOS[
                self.combo_servicio.get()
            ]

            fecha = self.calendario.get_date().strftime("%Y-%m-%d")

            self.reserva_actual = Reserva(
                cliente,
                servicio,
                fecha
            )

            self.reserva_actual.confirmar_reserva()

            self.mostrar_reserva()

            logger.info(
                f"Reserva creada para {cliente.nombre}"
            )

            messagebox.showinfo(
                "Reserva",
                "Reserva creada correctamente."
            )

        except ReservaError as error:

            logger.error(str(error))

            messagebox.showerror(
                "Reserva",
                str(error)
            )

        except ValueError as error:

            logger.error(str(error))

            messagebox.showerror(
                "Validación",
                str(error)
            )
    # ============================================================
    # MOSTRAR RESERVA
    # ============================================================

    def mostrar_reserva(self):

        if self.reserva_actual is None:
            return

        self.text_resultado.config(
            state="normal"
        )

        self.text_resultado.delete(
            "1.0",
            tk.END
        )

        self.text_resultado.insert(
            tk.END,
            self.reserva_actual.mostrar_info()
        )

        self.text_resultado.config(
            state="disabled"
        )

    # ============================================================
    # CANCELAR RESERVA
    # ============================================================

    def cancelar_reserva(self):

        try:

            if self.reserva_actual is None:

                messagebox.showwarning(
                    "Reserva",
                    "No existe una reserva para cancelar."
                )

                return

            self.reserva_actual.cancelar_reserva()

            self.mostrar_reserva()

            logger.info(
                f"Reserva cancelada para {self.reserva_actual.cliente.nombre}"
            )

            messagebox.showinfo(
                "Reserva",
                "Reserva cancelada correctamente."
            )

        except ReservaError as error:

            logger.error(str(error))

            messagebox.showerror(
                "Reserva",
                str(error)
            )

    # ============================================================
    # LIMPIAR FORMULARIO
    # ============================================================

    def limpiar_formulario(self):

        self.entry_nombre.delete(
            0,
            tk.END
        )

        self.entry_correo.delete(
            0,
            tk.END
        )

        self.entry_telefono.delete(
            0,
            tk.END
        )

        self.combo_categoria.current(0)

        self.actualizar_servicios()

        self.calendario.set_date("today")

        self.label_info.config(
            text="Seleccione un servicio."
        )

        self.text_resultado.config(
            state="normal"
        )

        self.text_resultado.delete(
            "1.0",
            tk.END
        )

        self.text_resultado.config(
            state="disabled"
        )

        self.reserva_actual = None

    # ============================================================
    # EJECUTAR
    # ============================================================

    def ejecutar(self):

        logger.info(
            "Sistema iniciado."
        )

        self.ventana.mainloop()

        logger.info(
            "Sistema finalizado."
        )
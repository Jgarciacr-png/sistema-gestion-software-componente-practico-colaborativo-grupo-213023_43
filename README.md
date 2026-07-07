# Sistema de Gestión de Reservas

## Descripción

Este proyecto corresponde al desarrollo del componente práctico colaborativo de la asignatura **Fundamentos de Programación** de la **Universidad Nacional Abierta y a Distancia (UNAD)**.

El sistema fue desarrollado en **Python** utilizando los principios de la **Programación Orientada a Objetos (POO)**, permitiendo gestionar clientes, servicios y reservas mediante una interfaz gráfica desarrollada con **Tkinter**. Además, incorpora manejo de excepciones personalizadas, registro de eventos mediante logs y control de versiones con Git y GitHub.

---

# Objetivos

## Objetivo general

Desarrollar un sistema de gestión de reservas aplicando los principios de la Programación Orientada a Objetos y las buenas prácticas de desarrollo de software.

## Objetivos específicos

- Implementar clases utilizando abstracción, herencia, encapsulamiento y polimorfismo.
- Gestionar clientes, servicios y reservas mediante una interfaz gráfica.
- Implementar manejo de excepciones para controlar errores del sistema.
- Registrar eventos importantes utilizando el módulo `logging`.
- Gestionar el proyecto mediante Git y GitHub.

---

# Tecnologías utilizadas

- Python 3
- Tkinter
- Git
- GitHub
- Logging
- Visual Studio Code

---

# Funcionalidades implementadas

El sistema permite:

- Registrar clientes.
- Gestionar diferentes tipos de servicios.
- Crear reservas.
- Confirmar reservas.
- Cancelar reservas.
- Validar datos ingresados por el usuario.
- Manejar excepciones personalizadas.
- Registrar eventos importantes del sistema.
- Ejecutar el sistema mediante una interfaz gráfica.

---

# Principios de Programación Orientada a Objetos

Durante el desarrollo del proyecto se aplicaron los siguientes conceptos:

- Abstracción
- Herencia
- Encapsulamiento
- Polimorfismo

---

# Estructura del proyecto

```text
sistema-gestion-software-componente-practico-colaborativo-grupo-213023_43/

│
├── interfaz/
│   ├── __init__.py
│   └── app.py
│
├── modelos/
│   ├── __init__.py
│   ├── entidad.py
│   ├── servicio.py
│   ├── cliente.py
│   ├── sala.py
│   ├── equipo.py
│   ├── asesoria.py
│   └── reserva.py
│
├── logs/
│   └── sistema.log
│
├── excepciones.py
├── logger_config.py
├── main.py
├── README.md
└── .gitignore
```

---

# Manejo de excepciones

El sistema implementa excepciones personalizadas para controlar diferentes tipos de errores:

- ClienteError
- ServicioError
- ReservaError
- FechaInvalidaError
- ServicioNoDisponibleError

Estas excepciones permiten mantener un control adecuado de errores y mejorar la estabilidad del sistema.

---

# Registro de eventos

El sistema registra automáticamente eventos importantes mediante el módulo `logging`.

Los registros se almacenan en:

```text
logs/sistema.log
```

Entre los eventos registrados se encuentran:

- Inicio del sistema.
- Creación de reservas.
- Cancelación de reservas.
- Errores de validación.
- Errores de ejecución.

---

# Ejecución del proyecto

Desde la carpeta principal ejecutar:

```bash
python3 main.py
```

---

# Integrantes

- Jonathan Garcia Cruz

---

# Repositorio del proyecto

https://github.com/Jgarciacr-png/sistema-gestion-software-componente-practico-colaborativo-grupo-213023_43

---

# Licencia

Proyecto desarrollado con fines académicos para la asignatura **Fundamentos de Programación** de la **Universidad Nacional Abierta y a Distancia (UNAD)**.

---

# Estado del proyecto

**Versión:** 1.0

**Estado:** Finalizado para entrega.
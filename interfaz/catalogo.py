from modelos.sala import Sala
from modelos.equipo import Equipo
from modelos.asesoria import Asesoria

SERVICIOS = {

    # ==========================
    # SALAS
    # ==========================

    "Sala Principal": Sala(
        "S001",
        "Sala Principal",
        350000,
        80
    ),

    "Sala Segunda": Sala(
        "S002",
        "Sala Segunda",
        220000,
        40
    ),

    "Sala Tercera": Sala(
        "S003",
        "Sala Tercera",
        150000,
        20
    ),

    # ==========================
    # EQUIPOS
    # ==========================

    "Cámara Profesional": Equipo(
        "E001",
        "Cámara Profesional",
        180000,
        "Cámara"
    ),

    "Video Beam": Equipo(
        "E002",
        "Video Beam",
        120000,
        "Proyector"
    ),

    "Computador Portátil": Equipo(
        "E003",
        "Computador Portátil",
        90000,
        "Computador"
    ),

    # ==========================
    # ASESORÍA
    # ==========================

    "Asesoría Técnica": Asesoria(
        "A001",
        "Asesoría Técnica",
        180000,
        "Ingeniero de Sistemas"
    )

}
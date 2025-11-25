# __init__.py

from .jugador import ataque_jugador, mostrar_jugador
from .enemigo import generar_enemigo, ataque_enemigo, mostrar_enemigo

__all__ = [
    "ataque_jugador", "mostrar_jugador",
    "generar_enemigo", "ataque_enemigo", "mostrar_enemigo",
]

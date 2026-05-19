# HECHO POR FERCHO
from typing import TypeVar, Callable
from utils import EsNatural

T = TypeVar("T")


def LeerEntrada(
    prompt: str,
    tipo: Callable[[str], T],
    *,
    condicion: Callable[[T], bool] | None = None,
    msg_condicion: str = "La entrada no cumple el formato especificado.",
    intentos: int | None = None,
) -> T | None:

    restantes = intentos

    while True:
        entrada = input(f"{prompt}\n>>> ").strip()

        try:
            valor = tipo(entrada)

            if condicion is None or condicion(valor):
                return valor
            print(f"\n{msg_condicion}")
        except Exception:
            print("\nLa entrada no se pudo procesar. Por favor revisela.")

        if restantes is not None:
            restantes -= 1
            if restantes <= 0:
                return None
            print(f"\nLe quedan: {restantes} intento/s.")
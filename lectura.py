# HECHO POR FERCHO

from utils import EsNatural

def _leer(prompt):
    print(prompt)
    entrada = input(">>> ")
    return entrada

def LeerEntero(prompt):
    entrada = _leer(prompt)
    try:
        return int(entrada)
    except Exception as e:
        return e

def LeerFlotante(prompt):
    entrada = _leer(prompt)
    try:
        return float(entrada)
    except Exception as e:
        return e

def LeerConIntentosEntero(prompt, intentos):
    while True:
        entrada = LeerEntero(prompt)
        if isinstance(entrada, int) and EsNatural(entrada):
            return entrada
        else:
            
            intentos -= 1
            if intentos <= 0:
                print("Has agotado todos los intentos.")
                return None
            else:
                print(f"Entrada no válida. Te quedan {intentos} intentos.")
                print("Presiona Enter para intentar de nuevo...")
                input()


def LeerConIntentosFlotante(prompt, intentos):
    while True:
        entrada = LeerFlotante(prompt)
        if isinstance(entrada, float) and EsNatural(entrada):
            return entrada
        else:
            
            intentos -= 1
            if intentos <= 0:
                print("Has agotado todos los intentos.")
                return None
            else:
                print(f"Entrada no válida. Te quedan {intentos} intentos.")
                print("Presiona Enter para intentar de nuevo...")
                input()
        
def LeerConIntentos(prompt, condicion,intentos):
    while True:
        entrada = _leer(prompt)

        if condicion(entrada):
            return entrada.upper()
        else:
            
            intentos -= 1
            if intentos <= 0:
                print("Has agotado todos los intentos.")
                return None
            else:
                print(f"Entrada no válida. Te quedan {intentos} intentos.")
                print("Presiona Enter para intentar de nuevo...")
                input()

# HECHO POR FERCHO

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
        if isinstance(entrada, int):
            return entrada
        else:
            print(f"Entrada no válida. Te quedan {intentos} intentos.")
            print("Presiona Enter para intentar de nuevo...")
            input()
            intentos -= 1
            if intentos <= 0:
                print("Has agotado todos los intentos.")
                return None

def LeerConIntentosFlotante(prompt, intentos):
    while True:
        entrada = LeerFlotante(prompt)
        if isinstance(entrada, float):
            return entrada
        else:
            print(f"Entrada no válida. Te quedan {intentos-1} intentos.")
            print("Presiona Enter para intentar de nuevo...")
            input()
            intentos -= 1
            if intentos <= 0:
                print("Has agotado todos los intentos.")
                return None
        
def LeerConIntentos(prompt, condicion,intentos):
    while True:
        entrada = _leer(prompt)

        if condicion(entrada):
            return entrada
        else:
            print(f"Entrada no válida. Te quedan {intentos-1} intentos.")
            print("Presiona Enter para intentar de nuevo...")
            input()
            intentos -= 1
            if intentos <= 0:
                print("Has agotado todos los intentos.")
                return None

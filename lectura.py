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

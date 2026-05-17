def BorrarPantalla():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def EsNatural(valor):
    return valor >= 0 and valor < 300
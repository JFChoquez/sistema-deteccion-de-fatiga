from menu import Menu
from lectura import LeerEntero

def main():
    numero = LeerEntero("Ingrese un numero")
    if isinstance(numero, int):
        print(numero*numero)
    else:
        print("eres un sano")

if __name__ == "__main__":
    try:
        Menu()
    except KeyboardInterrupt as kbi:
        print("\nGracias por usar el programa.")
# HECHO POR Pacheco Arnao Kristopher Williams
from lectura import LeerEntero
from utils import BorrarPantalla
from znog import DeteccionFatiga
# primera parte del menu
def Menu():
    continuar = True
    intentos = 3
    while continuar:
        BorrarPantalla()
        print("""
    =========================================================================
    |       SISTEMA INTELIGENTE DE DETECCION DE FATIGA EN CONDUCTORES       |
    =========================================================================
    |   1. Iniciar sistema de detección de fatiga                           |
    |   2. Informacion sobre el programa                                    |
    |   3. Salir del programa                                               |
    =========================================================================
    """)

        opcion = LeerEntero("Ingrese una opción:")
        match opcion:
            case 1:
                print("Iniciando sistema de detección de fatiga...")
                intentos = 3
            case 2:
                print("""
    |  Este sistema evalua si el conductor esta en condiciones para         |
    |  continuar conduciendo.                                               |
    |   (Horas continuas de conduccion)                                     |
    |   (Velocidad promedio del viaje)                                      |
    |   (Numero de pausas realizadas durante el viaje)                      |
    """)
                print("Regresando al menu principal...")
                intentos = 3
            case 3:
                print("Saliendo del programa...")
                continuar = False
            case _:
                intentos -= 1
                if intentos != 0:
                    print(f"Lo sentimos es invalido, le quedan: {intentos}")
                else:
                    print("Demasiados intentos fallidos. Saliendo del programa.")
                    continuar = False
        print("Presione enter para continuar...")
        input()
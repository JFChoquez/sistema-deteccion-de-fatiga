# HECHO POR Pacheco Arnao Kristopher Williams
from lectura import LeerEntero, LeerEntrada
from utils import BorrarPantalla
from znog import DeteccionFatiga


# primera parte del menu
def Menu():
    continuar = True
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

        opcion = LeerEntrada("Ingrese una opción:", int, intentos=3)
        match opcion:
            case 1:
                print("Iniciando sistema de detección de fatiga...")
                DeteccionFatiga()
            case 2:
                print("""
    =========================================================================                   
    |  Este sistema evalua si el conductor esta en condiciones para         |
    |  continuar conduciendo.                                               |
    |   (Horas continuas de conduccion)                                     |
    |   (Velocidad promedio del viaje)                                      |
    |   (Numero de pausas realizadas durante el viaje)                      |
    =========================================================================
    """)
                print("Regresando al menu principal...")
                input()
            case 3 | None:
                print("Saliendo del programa...")
                continuar = False

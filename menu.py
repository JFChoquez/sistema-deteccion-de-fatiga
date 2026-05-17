# HECHO POR Pacheco Arnao Kristopher Williams
from lectura import LeerEntero
import time

def Menu():
    continuar = True
    while continuar:
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
        if not isinstance(opcion, int):
            print("Lo sentimos es invalido")
        else:
            match opcion:
                case 1:
                    print("Iniciando sistema de detección de fatiga...")
                    time.sleep(2)
                case 2:
                    print("""
        |  Este sistema evalua si el conductor esta en condiciones para         |
        |  continuar conduciendo.                                               |
        |   (Horas continuas de conduccion)                                     |
        |   (Velocidad promedio del viaje)                                      |
        |   (Numero de pausas realizadas durante el viaje)                      |
        """)
                    print("Regresando al menu principal...")
                    time.sleep(2)
                case 3:
                    return

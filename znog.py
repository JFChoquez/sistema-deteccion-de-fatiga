# HECHO POR KRISTOPHER PACHECO, GONZALO TASAYCO
from lectura import LeerEntrada
from utils import BorrarPantalla


def DeteccionFatiga():
    BorrarPantalla()
    # Vamos a calcular si el conductor esta en riesgo, seguros, peligro
    Tseguros = 0
    Triesgos = 0
    Tpeligro = 0
    continuar = True
    Tconductores = 0
    Sumvelocidad = 0

    while continuar:
        BorrarPantalla()

        print("Registro de conductor N°", Tconductores + 1)

        velocidad = LeerEntrada(
            "Ingrese la velocidad del conductor (km/h):",
            float,
            intentos=3,
            condicion=lambda v: 0 < v < 300,
            msg_condicion="La velocidad es incoherente.",
        )
        if velocidad is None:
            print(
                "Se han agotado los intentos para la velocidad. Mostrando el reporte."
            )
            input()
            break

        horas = LeerEntrada(
            "Ingrese las horas de conducción continuas: ",
            float,
            intentos=3,
            condicion=lambda v: 0 < v < 30,
            msg_condicion="Las horas conducidas son incoherentes.",
        )
        if horas is None:
            print(
                "Se han agotado los intentos para las horas de conducción. Mostrando el reporte."
            )
            input()
            break

        pausa = LeerEntrada(
            "Ingrese el número de pausas: ",
            int,
            intentos=3,
            condicion=lambda p: 0 <= p,
            msg_condicion="El numero de pausas es incoherente.",
        )
        if pausa is None:
            print(
                "Se han agotado los intentos para la conducción. Mostrando el reporte."
            )
            input()
            break

        if horas <= 4 and velocidad <= 80 and pausa >= 1:
            Tseguros += 1
            estado = "Conductor Seguro"

        elif (5 <= horas <= 7) or (80 < velocidad <= 100) and (pausa == 0):
            Triesgos += 1
            estado = "Conductor en riesgo"

        elif horas >= 8 or velocidad > 100 or (horas >= 6 and pausa == 0):
            Tpeligro += 1
            estado = "Conductor peligroso"

        else:
            estado = "Indeterminado"

        Tconductores += 1
        Sumvelocidad += velocidad

        print(f"El conductor está clasificado como: {estado}")

        opcion = LeerEntrada(
            "¿Desea registrar otro conductor? (S/N):",
            str,
            intentos=3,
            condicion=lambda o: o.strip().upper() == "S" or o.strip().upper() == "N",
        )

        if opcion is None:
            print("Demasiados intentos. Mostrando el reporte.")
            input()
            break
        else:
            continuar = opcion.upper() == "S"

    if Tconductores > 0:
        Promvelocidad = Sumvelocidad / Tconductores
    else:
        Promvelocidad = 0.0
    BorrarPantalla()
    print(f"""
    =================================================================================================
      REPORTE FINAL:                                                                                
        Total de conductores registrados: {Tconductores}                                            
        La Velocidad Promedio de los conductores es: {Promvelocidad:.2f} Km/H                       
        Conductores en estado Seguro: {Tseguros}                                                    
        Conductores en estado de Riesgo: {Triesgos}                                                 
        Conductores en estado de Peligro: {Tpeligro}                                                
    =================================================================================================
     """)
    print("\nPresione enter para volver al menu principal...")
    input()

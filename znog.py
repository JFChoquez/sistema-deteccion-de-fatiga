# HECHO POR KRISTOPHER PACHECO, FERNANDO CHOQUEZ, GONZALO TASAYCO
from lectura import LeerFlotante, LeerEntero, LeerConIntentosEntero, LeerConIntentosFlotante, LeerConIntentos
from utils import BorrarPantalla 

def DeteccionFatiga():
    BorrarPantalla()
    #Vamos a calcular si el conductor esta en riesgo, seguros, peligro
    Tseguros= 0
    Triesgos= 0
    Tpeligro= 0
    continuar = True
    intentos = 3
    Tconductores= 0
    Sumvelocidad= 0

    while continuar:
        if intentos == 0:
            print("Se han agotado los intentos. Mostrando el reporte.")
            break

        print("Registro de conductor N°", Tconductores + 1)

        velocidad = LeerConIntentosFlotante("Ingrese la velocidad del conductor (km/h):", 3)
        if velocidad is None:
            print("Se han agotado los intentos para la velocidad. Mostrando el reporte.")
            break

        horas = LeerConIntentosFlotante("Ingrese las horas de conducción continuas:", 3) 
        if horas is None:
            print("Se han agotado los intentos para la conducción. Mostrando el reporte.")
            break

        pausa = LeerConIntentosEntero("Ingrese el número de pausas:", 3)
        if pausa is None:
            print("Se han agotado los intentos para la conducción. Mostrando el reporte.")
            break
            
        if horas <=4 and velocidad <= 80 and pausa >= 1:
            Tseguros += 1
            estado= "Seguro"

        elif (5<=horas<=7) or (80<velocidad<=100) or (pausa == 0):
            Triesgos += 1
            estado= "En Riesgo"
        
        elif horas >= 8 or velocidad > 100 or (horas>=6 and pausa == 0):
            Tpeligro += 1
            estado= "En Peligro"
        
        else:
            estado= "Indeterminado"
        
        Tconductores += 1
        Sumvelocidad += velocidad

        print(f"El conductor está clasificado como: {estado}")

        opcion = LeerConIntentos("¿Desea registrar otro conductor? (S/N):", lambda entrada: entrada.upper == "S" or entrada.upper == "N", 3)
        
        if opcion is None:
            break
        else:
            opcion = (opcion == "S")


    
    if Tconductores > 0:
        Promvelocidad = Sumvelocidad/Tconductores
    else:
        Promvelocidad = 0.0
    print(f"""
    ==========================================================================
     | REPORTE FINAL:
     |   Total de conductores registrados: {Tconductores}
     |   La Velocidad Promedio de los conductores es: {Promvelocidad:.2f} Km/H  
     |   Conductores en estado Seguro: {Tseguros}
     |   Conductores en estado de Riesgo: {Triesgos}  
     |   Conductores en estado de Peligro: {Tpeligro}  
          """)

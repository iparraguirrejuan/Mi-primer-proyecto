import sys
import mysql.connector
from funciones import App


while True:
    print("""
Bienvenido Dr/a a la calculadora antropometrica

1 - Ingrese un nuevo paciente
2 - Hacer una antropometria
3 - Ver pacientes
4 - Salir
        """)
        
    opcion = int (input("Seleccione el numero de la operacion a realizar "))

    
    if opcion == 1:
        
        acciones = App
        acciones.__init__()
        acciones.Posicion_pacientes()
        acciones.Insertar_paciente()

        

    elif opcion == 2:
        print("")
        print(">>>> Hacer una antropometria <<<<")
        # Poner todos los datos que vamos a utilizar para una antropometira, todas las variables que vamos a utilizar, luego hacer todas las funciones 

    elif opcion == 3:
        acciones.listar_pacientes()
        

    elif opcion == 4:
        acciones.__del__()
        print("Muchas gracias por usar nuestro programa")
        sys.exit()

    else:
        print("La opcion es incorrecta.... Por favor ingrese una opcion correcta")

        

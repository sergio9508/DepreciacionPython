# Se ingresa al menu para ver que metodo de deprreciacion se usara
import funciones
activos = []
menu = 0


while menu != 6:
    menu = int(input("1- Agregar registro de activos \n 2- Modificar registro de activos \n 3- Borrar registro de activos \n 4- Consultar registro de activos \n 5- Visualizar tabla de depreciacion por activos \n 6- Salir del programa\n "))
    if menu == 1:
        numeroActivos = int(input("Numero de activos a ingresar: \n"))
        activos = funciones.AgregarActivos(numeroActivos)
    elif menu == 2:
        posicion = int(input("Ingrese la posicion del activo a modificar"))
        activos = funciones.ModificarActivo(activos, posicion)
    elif menu == 3:
        posicion = int(input("Ingrese la posicion del activo que quiere borrar"))
        activos = funciones.BorrarRegistro(activos, posicion)
    elif menu == 4:
        funciones.ConsultarActivos(activos)
    elif menu == 5:
        funciones.ConsultarDepreciacion
    elif menu > 6:
        print("Error elija una opcion del menu \n")

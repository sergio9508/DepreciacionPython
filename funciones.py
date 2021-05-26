def AgregarActivos(numeroActivos):
    activos = []
    for i in range(numeroActivos):
        codigoActivo = input("Ingrese el codigo del activo \n")
        nombreActivo = input("Ingrese el nombre del activo \n")
        costo = float(input("Ingrese el costo del activo \n"))
        vidaUtil = float(input("Ingrese la vida util del activo (en años)\n"))
        valorRecuperacion = float(input("Ingrese el valor de recuperacion \n"))
        activos.append([codigoActivo, nombreActivo, costo,
                       vidaUtil, valorRecuperacion])
    return activos

def ModificarActivo(activos, posicion):
    codigoActivo = input("Ingrese el codigo del activo \n")
    nombreActivo = input("Ingrese el nombre del activo \n")
    costo = float(input("Ingrese el costo del activo \n"))
    vidaUtil = float(input("Ingrese la vida util del activo (en años)\n"))
    valorRecuperacion = float(input("Ingrese el valor de recuperacion \n"))
    activos[posicion-1] = [codigoActivo, nombreActivo,
                         costo, vidaUtil, valorRecuperacion]
    return activos

def BorrarRegistro(activos, posicion):
    for i in posicion:
        activos.pop(i)
    return activos

def ConsultarActivos(activos):
    print("Activos")
    for activo in activos:
        print("{:<5} {:<10} {:<15} {:<20} {:<25}".format(
            activo[0], activo[1], str(activo[2]), str(activo[3]), str(activo[4])))

def ConsultarDepreciacion(activos):
    return activos
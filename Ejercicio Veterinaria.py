import os, time, msvcrt as ms, numpy as np, statistics as stats, random

### VARIABLES
errorText = "\nError: Ha ocurrido un error.\nHa ocurrido un error no especificado.\n\nInténtelo nuevamente en"
errorRange = range(3,0,-1)
dogCount = 0
catCount = 0

### FLAGS
sw = True
swName = False
swOwner = False
swType = False
matchSearch = False

### LISTAS / DICCIONARIOS
listaRegistro = []
# diccionarioRegistro = []

### FUNCIONES
def errorMessage_v1():
    global errorText, errorRange
    
    for i in errorRange:
        os.system("cls")
        print(f"{errorText} {i}.")
        time.sleep(1)
    os.system("cls")

def errorMessage_v2():
    global errorText, errorRange

    for i in errorRange:
        os.system("cls")
        print(f"{errorText}.")
        time.sleep(1)
    os.system("cls")

def Menu1():
    global errorText, errorRange, op1, sw, diccionarioRegistro
    print("\n- =  M E N Ú  = -\n\n[1] Registar Mascotas   [4] Ver Registro (Filtrado)\n[2] Ver Registros       [5] Salir\n[3] Buscar Mascotas")
    op1 = int(input("\nSeleccione una opción: (1 - 5)\n> "))

    if op1 < 1 or op1 > 5:
        errorText = "\nError: Valor fuera de rango.\nIngrese un valor que se encuentre dentro del rango especificado.\n\nInténtelo nuevamente en"
        errorRange = range(3,0,-1)
        errorMessage_v1()
    else:
        match op1:
            case 1: # REGISTRAR MASCOTAS
                RegistrarMascota()

            case 2: # VER REGISTROS
                VerRegistros()

            case 3: # BUSCAR MASCOTA
                BuscarMascotas()

            case 4: # VER REGISTRO SEGÚN TIPO DE MASCOTA
                VerRegistrosFiltrados()

            case 5: # SALIR DEL SISTEMA
                errorText = "\nSaliendo del sistema.\n\nPor favor, espere unos segundos"
                errorRange = range(2,0,-1)
                errorMessage_v2()

                os.system("cls")
                sw = False

def RegistrarMascota():
    global errorText, errorRange, matchSearch, swName, swOwner, swType
    
    os.system("cls")

    regID = str(input("\nRegistro de Mascotas\n\n(1/4)\n\nIngrese el ID de la mascota:\n> "))
    
    matchSearch = False

    if len(listaRegistro) > 0:
        for diccionarioRegistro in listaRegistro:
            if diccionarioRegistro['ID'] == regID:
                matchSearch = True
        
        if matchSearch == True:
            errorText = "\nError: Código Repetido.\nYa existe un registro con el código ingresado.\n\nInténtelo nuevamente en"
            errorRange = range(3,0,-1)
            errorMessage_v1()
        else:
            if len(regID) < 5 or len(regID) > 5:
                errorText = "\nError: Largo de código erróneo.\nEl largo del código ingresado es distinto de 5.\n\nInténtelo nuevamente en"
                errorRange = range(3,0,-1)
                errorMessage_v1()
            elif regID.isdigit() == False:
                errorText = "\nError: Código no numérico.\nEl código ingresado debe estar compuesto solamente por números.\n\nInténtelo nuevamente en"
                errorRange = range(3,0,-1)
                errorMessage_v1()
            else:
                swName = True

    else:
        if len(regID) < 5 or len(regID) > 5:
            errorText = "\nError: Largo de código erróneo.\nEl largo del código ingresado es distinto de 5.\n\nInténtelo nuevamente en"
            errorRange = range(3,0,-1)
            errorMessage_v1()
        elif regID.isdigit() == False:
            errorText = "\nError: Código no numérico.\nEl código ingresado debe estar compuesto solamente por números.\n\nInténtelo nuevamente en"
            errorRange = range(3,0,-1)
            errorMessage_v1()
        else:
            swName = True

    if swName == True:
        os.system("cls")

        regNamePet = str(input("\nRegistro de Mascotas\n\n(2/4)\n\nIngrese el Nombre de la mascota:\n> "))

        if len(regNamePet) < 1:
            errorText = "\nError: Nombre vacío.\nDebe ingresar el nombre de la mascota para continuar.\n\nInténtelo nuevamente en"
            errorRange = range(3,0,-1)
            errorMessage_v1
            swName = False
        else:
            swOwner = True
            swName = False

    if swOwner == True:
        os.system("cls")

        regNameOwner = str(input("\nRegistro de Mascotas\n\n(3/4)\n\nIngrese el Nombre del Dueño de la mascota:\n> "))

        if len(regNameOwner) < 1:
            errorText = "\nError: Nombre vacío.\nDebe ingresar el nombre del dueño de la mascota para continuar.\n\nInténtelo nuevamente en"
            errorRange = range(3,0,-1)
            errorMessage_v1
            swOwner = False
        else:
            swType = True
            swOwner = False

    if swType == True:
        os.system("cls")

        regType = int(input("\nRegistro de Mascotas\n\n(4/4)\n\nSeleccione el tipo de Mascota:\n\n[1] Perro\n[2] Gato\n\n> "))

        if regType < 1 or regType > 2:
            errorText = "\nError: Valor fuera de rango.\nIngrese un valor que se encuentre dentro del rango especificado.\n\nInténtelo nuevamente en"
            errorRange = range(3,0,-1)
            errorMessage_v1()
        else:
            if regType == 1:
                PetType = "Perro"
            elif regType == 2:
                PetType = "Gato"
            
            VacPend = random.randint(1,10)

            diccionarioRegistro = {'ID': regID, 'PetName': regNamePet, 'OwnerName': regNameOwner, 'Tipo': PetType, 'VacPend': VacPend}
            listaRegistro.append(diccionarioRegistro)

            swType = False

def VerRegistros():
    global errorText, errorRange

    if len(listaRegistro) == 0:
        errorText = "\nError: Sin registros.\nNo hay registros en el sistema, cree al menos un registro para poder verlo.\n\nInténtelo nuevamente en"
        errorRange = range(3,0,-1)
        errorMessage_v1()
    else:
        os.system("cls")
        print("\nRegistros de Mascotas:\n")

        for diccionarioRegistro in listaRegistro:
            print(f"ID: {diccionarioRegistro['ID']}\tNombre Mascota: {diccionarioRegistro['PetName']}\tNombre Dueño: {diccionarioRegistro['OwnerName']}\tTipo: {diccionarioRegistro['Tipo']}\tVacunas Pendientes: {diccionarioRegistro['VacPend']}")
        print("\nPresione una tecla para continuar.")
        ms.getch()

def BuscarMascotas():
    global errorText, errorRange, matchSearch

    if len(listaRegistro) == 0:
        errorText = "\nError: Sin registros.\nNo hay registros en el sistema, cree al menos un registro para poder verlo.\n\nInténtelo nuevamente en"
        errorRange = range(3,0,-1)
        errorMessage_v1()
    else:
        os.system("cls")
        searchID = input("\nIngrese ID de mascota a buscar\n> ")
        matchSearch = False

        os.system("cls")

        print("\nResultados de Búsqueda:\n")
        for diccionarioRegistro in listaRegistro:
            if diccionarioRegistro['ID'] == searchID:
                matchSearch = True

                print(f"ID: {diccionarioRegistro['ID']}\tNombre Mascota: {diccionarioRegistro['PetName']}\tNombre Dueño: {diccionarioRegistro['OwnerName']}\tTipo: {diccionarioRegistro['Tipo']}\tVacunas Pendientes: {diccionarioRegistro['VacPend']}")
        if matchSearch == False:
            errorText = "\nError: Sin Resultados.\nNo se han encontrado resultados de búsqueda.\n\nInténtelo nuevamente en"
            errorRange = range(3,0,-1)
            errorMessage_v1()
        else:
            print("\nPresione una tecla para continuar.")
            ms.getch()

def VerRegistrosFiltrados():
    global errorText, errorRange, matchSearch

    if len(listaRegistro) == 0:
        errorText = "\nError: Sin registros.\nNo hay registros en el sistema, cree al menos un registro para poder verlo.\n\nInténtelo nuevamente en"
        errorRange = range(3,0,-1)
        errorMessage_v1()
    else:
        os.system("cls")
        op2 = int(input("\nSeleccione tipo de mascota a buscar:\n\n[1] Perro\n[2] Gato\n\n> "))
        matchSearch = False
        dogCount = 0
        catCount = 0

        if op2 < 1 or op2 > 2:
            errorText = "\nError: Valor fuera de rango.\nIngrese un valor que se encuentre dentro del rango especificado.\n\nInténtelo nuevamente en"
            errorRange = range(3,0,-1)
            errorMessage_v1()
        else:
            os.system("cls")

            print("\nRegistros de Mascotas:\n")

            match op2:
                case 1:
                    for diccionarioRegistro in listaRegistro:
                        if diccionarioRegistro['Tipo'] == "Perro":
                            print(f"ID: {diccionarioRegistro['ID']}\tNombre Mascota: {diccionarioRegistro['PetName']}\tNombre Dueño: {diccionarioRegistro['OwnerName']}\tTipo: {diccionarioRegistro['Tipo']}\tVacunas Pendientes: {diccionarioRegistro['VacPend']}")
                            dogCount += 1
                            matchSearch = True

                    if matchSearch == False:
                        errorText = "\nError: Sin Resultados.\nNo se han encontrado resultados de búsqueda.\n\nInténtelo nuevamente en"
                        errorRange = range(3,0,-1)
                        errorMessage_v1()
                    else:
                        print(f"\n{dogCount} resultados de búsqueda.\n\nPresione una tecla para continuar.")
                        ms.getch()

                case 2:
                    for diccionarioRegistro in listaRegistro:
                        if diccionarioRegistro['Tipo'] == "Gato":
                            print(f"ID: {diccionarioRegistro['ID']}\tNombre Mascota: {diccionarioRegistro['PetName']}\tNombre Dueño: {diccionarioRegistro['OwnerName']}\tTipo: {diccionarioRegistro['Tipo']}\tVacunas Pendientes: {diccionarioRegistro['VacPend']}")
                            catCount += 1
                            matchSearch = True

                    if matchSearch == False:
                        errorText = "\nError: Sin Resultados.\nNo se han encontrado resultados de búsqueda.\n\nInténtelo nuevamente en"
                        errorRange = range(3,0,-1)
                        errorMessage_v1()
                    else:
                        print(f"\n{catCount} resultados de búsqueda.\n\nPresione una tecla para continuar.")
                        ms.getch()

while sw == True:
    try:
        os.system("cls")

        Menu1()

    except ValueError:
        errorText = "\nError: Carácter inválido.\nIngrese un valor que se encuentre dentro del rango especificado.\n\nInténtelo nuevamente en"
        errorRange = range(3,0,-1)
        errorMessage_v1()
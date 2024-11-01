def get_input():
    entrada = input('Ingrese el codigo de la golosina: ')
    return int(entrada)

def check_legajo(legajo, empleados:dict):
    for e in empleados:
        if legajo == e:
            return True
    print('Uted no es empleado de la empresa.')
    return False

def get_golosina(codigo, golosinas):
    for g in golosinas:
        if g[0] == codigo:
            if check_stock(g) == False:
                return False
            return g

def dism_golosina(codigo:list, lista_golosinas:list, retiros:list):
    golosina = get_golosina(codigo, lista_golosinas)
    if get_golosina(codigo, lista_golosinas) == False:
        return False
    golosina.append((lambda lista: lista[2] - 1)(golosina))
    golosina.pop(2)
    retiros.append(golosina)
    if golosina in lista_golosinas:
        lista_golosinas.pop((golosina[0]-1))
        lista_golosinas.insert(golosina[0]-1, golosina)
    return True

def recargar_golosina(codigo:list, lista_golosinas:list, cantidad:int):
    golosina = get_golosina(codigo, lista_golosinas)
    if get_golosina(codigo, lista_golosinas) == False:
        return False
    golosina.append((lambda lista: lista[2] + cantidad)(golosina))
    golosina.pop(2)
    if golosina in lista_golosinas:
        lista_golosinas.pop((golosina[0]-1))
        lista_golosinas.insert(golosina[0]-1, golosina)
    return True

def check_stock(golosina):
    if golosina[2] == 0:
        print(f'Lo sentimos la golosina {golosina[1]} no se encuentra disponible, seleccione otra golosina o ingresa salir si no desea otra golosina')
        return
    elif golosina[2] > 0: 
        return golosina[2]
        
def pedir_golosina(lista_empleados, lista_golosinas, retiros):
    legajo_ingresado = int(input('Ingrese su legajo: '))
    if not check_legajo(legajo_ingresado, lista_empleados):
        return
    golosina_seleccionada = get_input()
    golosina = get_golosina(golosina_seleccionada, lista_golosinas)
    if dism_golosina(golosina_seleccionada, lista_golosinas, retiros):
        print(f'Se retiró {golosina[1]} de la máquina')
    else: 
        print(f'No se pudo retirar {golosina[1]} de la máquina')
        
def mostrar_golosinas(golosinas):
    for golosina in golosinas:
        print(golosina)

def ingreso_tecnico(claves):
    contrasenia1 = input('Ingresa la contraseña de técnico 1: ')
    if contrasenia1 != claves[0]:
        return False
    contrasenia2 = input('Ingresa la contraseña de técnico 2: ')
    if contrasenia2 != claves[1]:
        return False
    contrasenia3 = int(input('Ingresa la contraseña de técnico 3: '))
    if contrasenia3 != claves[2]:
        return False
    return True
    
def rellenar_golosinas(claves_tecnico, lista_golosinas):
    if ingreso_tecnico(claves_tecnico):
        print('\nIngreso correctamente\n')
        codigo = int(input('¿Qué golosina quiere rellenar?: '))
        cantidad = int(input('¿Cuantas quiere recargar?: '))
        recargar_golosina(codigo, lista_golosinas, cantidad)
    else:
        print('No tiene permiso para ejecutar la función de recarga')

def get_golosinas_pedidas(lista_pedidos:list, retiradas, lista_golosinas):
    cantidad = {}
    for g in retiradas:
        if g[0] in cantidad:
            cantidad[g[0]] +=1
        else:
            cantidad[g[0]] = 1
    
    for cod, count in cantidad.items():
        desc_golosina = get_golosina(cod, lista_golosinas)[1]
        linea = [cod, desc_golosina, count]
        lista_pedidos.append(linea)
    
    for l in lista_pedidos:
        print(l)
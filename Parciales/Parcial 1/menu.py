from helpers import *
from maquina_golosinas import *


while True:
    entrada:int = int(input('\n¿Qué quiere realizar?\n1. Pedir Golosinas\n2. Mostrar Golosinas\n3. Rellenar Golosinas\n4. Apagar Maquina\n-->   '))
    if entrada == 1:
        pedir_golosina(empleados, golosinas, retiros)
    elif entrada == 2:
        mostrar_golosinas(golosinas)
    elif entrada == 3:
        rellenar_golosinas(claves_tecnico, golosinas)
    elif entrada == 4:
        get_golosinas_pedidas(golosinas_pedidas, retiros, golosinas)
        print('\n----La Máquina se apagó----\n')
        break


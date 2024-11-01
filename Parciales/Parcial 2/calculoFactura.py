from helpers import *
from classes import *

fecha_factura = ''
numero_factura = int()
letra_factura = ''
total_factura = float()
monto_iva = float()
cliente_factura = ''
detalle_factura = []
detalle_factura_txt = [
    ['Código Articulo', 'Nombre Articulo', 'Cantidad', 'Precio Unitario', 'Subtotal']
    ]
cuit_cliente = int()
subtotal = float()
articulos = [
            (101, 'Leche', 250),
            (102, 'Gaseosa', 300),
            (103, 'Fideos', 150),
            (104, 'Arroz', 280),
            (105, 'Vino', 1200),
            (106, 'Manteca', 200),
            (107, 'Lavandina', 180),
            (108, 'Detergente', 460),
            (109, 'Jabón en Polvo', 960),
            (110, 'Galletas', 600)
            ]
clientes = {
            20110425417: 'Rodolfo Fernandez',
            30527419655: 'Los Pollos Hnos',
            27289425478: 'Andrea Pereira',
            33536549878: 'Multimarca Repuestos',
            20291122568: 'Luis Peric'
}

def get_fecha_factura():
    fecha = input('Ingrese la fecha de la factura (DD-MM-AAAA): ')
    return fecha

def get_num_factura():
    'Realiza un ingreso manual para seguir los requisitos, también podria ser secuencial con una función'
    num = input('Ingrese el numero de la factura: ')
    return num

def get_cuit_cliente():
    cuit_ingresado = int(input('Ingrese el cuit del cliente: '))
    while check_cuit(cuit_ingresado) == False:
        print('Ingrese un CUIT válido: ')
        cuit_ingresado = int(input('Ingrese el cuit del cliente: '))
    if cuit_ingresado in clientes:
        cliente_factura = clientes[cuit_ingresado]
    else:
        cliente_factura = 'Consumidor Final'

def get_articulos():
    get_articulo(articulos, detalle_factura, LineaDetalle)

def calcular_total(detalle_factura):
    total = float()
    for l in detalle_factura:
        total = total + l[4]
    return total

def print_factura():
    print(f'Fecha:              {fecha_factura}')
    print(f'Numero:             {numero_factura}')
    print(f'Letra:              {letra_factura}')
    print(f'Ciente:             {cliente_factura}')
    print(detalle_factura_txt)
    for l in detalle_factura:
        print(l)
    print(f'                IVA:{monto_iva}')
    print(f'                IVA:{total_factura}')



def main():

    cuit_cliente = get_cuit_cliente()
    numero_factura = get_num_factura()
    #get_letra_factura(cuit_cliente)
    get_articulos()
    print(detalle_factura)
    subtotal = calcular_total(detalle_factura)
    monto_iva = get_monto_iva(cuit_cliente, subtotal)
    total_factura = get_total_factura(calcular_total(detalle_factura), monto_iva)
    print_factura()

main()
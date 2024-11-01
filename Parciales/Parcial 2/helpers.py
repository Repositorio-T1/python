def check_cuit(cuit:int):
    cuit_validos = [20, 27, 30, 33]
    if int(str(cuit)[0:2]) not in cuit_validos:
        return False
    return True

def get_monto_iva(cuit:int, subtotal:float):
    inscripto = [30, 33]
    if int(str(cuit)[0:2]) not in inscripto:
        return subtotal
    else:
        return subtotal * 0.21
 
def get_letra_factura(cuit:int):
    inscripto = [30, 33]
    if int(str(cuit)[0:2]) in inscripto:
        return 'A'
    else:
        return 'B'
    
def get_total_factura(subtotal:float, letra:str, monto_iva):
    total = float()
    if letra == 'B':
        total = subtotal + monto_iva
    else:
        total = subtotal
    return total

def get_articulo(articulos:list, detalle:list, builder):
    while True:
        cod_articulo = int(input('Ingrese el código del articulo (XXX) o 0000 para terminar la carga:'))
        if cod_articulo == 0000:
            return
        for a in articulos:
            if cod_articulo == a[0]:
                cant = int(input('Ingrese la cantidad: '))
                linea_detalle = builder(a, cant)
                detalle.append(linea_detalle.get_as_list())
                break
            else:
                print('Código incorrecto')

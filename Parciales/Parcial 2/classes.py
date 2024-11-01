class LineaDetalle:
    def __init__(self, articulo, cantidad):
        #Código Articulo', 'Nombre Articulo', 'Cantidad', 'Precio Unitario', 'Subtotal
        self.codigo = articulo[0]
        self.nombre = articulo[1]
        self.cantidad = cantidad
        self.precio_uni = articulo[2]
        self.subtotal = int(cantidad * self.precio_uni)
    
    def get_as_list(self):
        como_lista = [self.codigo, self.nombre, self.cantidad, self.precio_uni, self.subtotal]
        return como_lista
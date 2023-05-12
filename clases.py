class Cliente:
    """Clase que representa a un cliente en la tienda"""
    def __init__(self, id_usuario, nombre, apellido, correo, fecha_registro, __saldo):
        self.id = id_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.fecha = fecha_registro
        self.__saldo = __saldo
        self.fecha_nacimiento = None
    @property
    def saldo(self):
        """Obtiene el saldo del cliente"""
        return(self.__saldo)
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    def obtenerCliente(self, id):
        return self.nombre if id == self.id else None

class Producto:
    """Clase que representa a un producto en la tienda"""
    def __init__(self, sku, nombre, categoria, proveedor, stock, valor_neto, *prioritario):
        self.sku = sku
        self.nombre = nombre
        self.categoria = categoria
        self.proveedor = proveedor
        self.stock = stock
        self.valor_neto = valor_neto
        self.prioritario = prioritario[0] if prioritario else False

    def comisionPrioritario(self, cantidad) -> float: 
        if self.prioritario is False:
            return self.valor_neto * cantidad * 0.005
        return self.valor_neto * cantidad * 0.01

    def cambiarValorProducto(self, nuevo_valor):
        self.valor_neto = nuevo_valor
        print(
            f'El valor del producto {self.nombre} fue cambiado a ${self.valor_neto}')

    def agregarStockProducto(self, cantidad):
        self.stock += cantidad
        print(f'Se agregaron {cantidad} unidades al producto {self.nombre}')
        
class Vendedor:
    """Clase que representa a un vendedor en la tienda"""
    def __init__(self, run, nombre, apellido, seccion, __comision, ventas):
        self.run = run
        self.nombre = nombre
        self.apellido = apellido
        self.seccion = seccion
        self.__comision = __comision
        self.ventas = 0

    @property
    def comision(self):
        """Obtiene la comisión por defecto del vendedor"""
        return(self.__comision)
    
    @comision.setter
    def comision(self, comision):
        self.__comision = comision

    def vender(self, producto, cliente, cantidad):
        if producto.stock >= cantidad:
            if cliente.saldo >= producto.valor_neto * cantidad:
                producto.stock -= cantidad
                self.comision += producto.comisionPrioritario(cantidad)
                cliente.saldo -= producto.valor_neto * cantidad
                self.ventas += producto.valor_neto * cantidad
                print(
                    f'El producto {producto.nombre} fue vendido exitosamente, el saldo del cliente es {cliente.saldo}')
            else:
                print(
                    f'El cliente {cliente.nombre} {cliente.apellido} no tiene saldo suficiente para comprar el producto {producto.nombre}')
        else:
            print(f'El producto {producto.nombre} no tiene stock disponible')
        
    def consultarVentas(self):
        print(f'Las ventas del vendedor {self.nombre} son ${self.ventas}')

class Proveedor:
    """Clase que representa a un proveedor en la tienda"""
    
    def __init__(self, rut, nombre_legal, razon_social, pais, es_persona_juridica):
        self.rut = rut
        self.nombre_legal = nombre_legal
        self.razon_social = razon_social
        self.pais = pais
        self.es_persona_juridica = True


cliente1 = Cliente(1, 'Juan', 'Perez', 'juan@juan.com', '2020-01-01', 1000000)
vendedor1 = Vendedor(1, 'Juan', 'Perez', 'Abarrotes', 0, 1)

producto1 = Producto(1, 'Arroz', 'Abarrotes', 'Tia Rica', 500, 1000)

vendedor1.vender(producto1, cliente1, 10)

vendedor1.consultarVentas()
print(f'El total acumulado de las comisiones del vendedor {vendedor1.nombre} es igual a ${vendedor1.comision}')

vendedor1.vender(producto1, cliente1, 10)

vendedor1.consultarVentas()
print(f'El total acumulado de las comisiones del vendedor {vendedor1.nombre} es igual a ${vendedor1.comision}')

proveedor1 = Proveedor(1, 'Tia Rica', 'Tia Rica', 'Chile', True)

print(f'El stock actual {producto1.stock}')

proveedor1.agregarStockProducto(producto1, 100)

print(f'El nuevo stock {producto1.stock}')
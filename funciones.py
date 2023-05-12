import os
from clases import *
# Bodega
productos = {
    "zapatillas": 20,
    "poleras": 10,
    "zapatos": 15,
    "poleron": 3,
    "chaqueta": 5,
    "guantes": 4
}


clientes = [Cliente(1, 'Juan', 'Pérez', 'jp@gmail.com', '21/03/2022', 50000)]
clientes.append(Cliente(2, 'Pedro', 'García',
                'pg@gmail.com', '15/06/2022', 100000))
clientes.append(Cliente(3, 'Diego', 'López',
                'dl@gmail.com', '30/09/2022', 75000))
clientes.append(Cliente(4, 'Javiera', 'Rodríguez',
                'jr@gmail.com', '02/12/2022', 30000))
clientes.append(Cliente(5, 'Francisca', 'Sánchez',
                'fs@gmail.com', '05/02/2023', 90000))


def nuevo_stock():
    """Agrega un nuevo producto al stock"""
    producto = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad del producto: "))
    productos[producto] = cantidad
    print(productos)


def actualizar_producto():
    """Actualiza el stock de un producto"""
    producto = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad del producto: "))
    productos[producto] += cantidad
    print(productos)


def nombre_productosbodega():
    """Muestra los nombres de los productos en bodega"""
    producto = input("Ingrese el nombre del producto: ")
    if producto in productos:
        print(f'En bodega quedan: {productos[producto]} {producto}')
    else:
        print("El producto no existe")


def todos_productostienda():
    """Muestra todos los productos en la tienda"""
    print('Productos disponibles en la tienda:')
    for producto in productos:
        print(producto)


def productos_enstock():
    """Muestra los productos con stock mayor a 1"""
    stock = "".join(
        f"{producto}, " for producto in productos if productos[producto] >= 1
    )
    print(f'Los productos con stock mayor a 1 es bodega son: {stock}')


def adm_compra():
    """Permite realizar una compra"""
    try:
        id_cliente = int(input("Ingrese el id del cliente: "))
        producto = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad del producto: "))
        realizar_compra(producto, id_cliente, cantidad)
    except Exception:
        realizar_compra(producto, id_cliente, 1)


def realizar_compra(producto, id_cliente, cantidad):
    for _ in clientes:
        if id_cliente == _.id:
            cliente = _.nombre
            break
    if producto in productos:
        if productos[producto] >= cantidad:
            productos[producto] -= cantidad
            print(f"Estimado {cliente}: Compra aprobada y en camino")
        else:
            print(f"Estimado {cliente}, lo sentimos mucho. Compra cancelada")
    else:
        print("El producto no existe, pruebe nuevamente")


def ver_saldo_cliente():
    id_cliente = int(input('Ingrese ID del cliente: '))
    for _ in clientes:
        if id_cliente == _.id:
            return _.saldo


def cambiar_saldo_cliente():
    id_cliente = int(input('Ingrese ID del cliente: '))
    nuevo_saldo = int(input('Ingrese nuevo saldo: '))
    for _ in clientes:
        if id_cliente == _.id:
            _.saldo = nuevo_saldo
            return _.saldo


def mostrar_clientes():
    print('ID   Nombre  Apellido    Correo Electrónico  Fecha de Registro')
    for _ in clientes:
        print(_.id, _.nombre, _.apellido, _.correo, _.fecha)
    print(f'Hay {len(clientes)} usuarios registrados.')


def crear_cliente(nombre, apellido, correo, fecha_registro, saldo_inicial):
    pass


def limpiarTerminal():
    os.system("cls")

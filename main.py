from funciones import *
from clases import *

###########################################
########## CONTROL DE BODEGA ##############
###########################################

def adm_bodega():
    print("\nControl de bodega\n")
    menu_admbodega = 0
    while menu_admbodega != 7:
        print("""\nIngrese el número de la opción que desea realizar
        1. Almacenar nuevos productos
        2. Actualizar el stock de productos en la bodega virtual
        3. Mostrar y retornar las unidades disponibles por producto
        4. Mostrar y retornar las unidades disponibles de un producto en particular
        5. Mostrar y todos los productos de la tienda
        6. Mostrar y retornar los productos que tienen más de un número de unidades
        7. Salir\n""")
        menu_admbodega = int(input("Ingrese el número de la opción que desea realizar: "))
        if menu_admbodega == 1:
            limpiarTerminal() 
            nuevo_stock()
        elif menu_admbodega == 2:
            limpiarTerminal()
            actualizar_producto()
        elif menu_admbodega == 3:
            limpiarTerminal()
            print(productos)
        elif menu_admbodega == 4:
            limpiarTerminal()
            nombre_productosbodega()
        elif menu_admbodega == 5:
            limpiarTerminal()
            todos_productostienda()
        elif menu_admbodega == 6:
            limpiarTerminal()
            productos_enstock()
        elif menu_admbodega == 7:
            limpiarTerminal()
            print("Gracias por utilizar el sistema de control de bodega")
            break

###########################################
########## CONTROL DE VENTAS ##############
###########################################

def adm_ventas():
    print("\nSistema de ventas\n")
    menu_ventas = 0
    while menu_ventas != 3:
        print("""\nIngrese el número de la opción que desea realizar
        1. Mostrar y retornar el número de clientes registrados en la tienda
        2. Ir a comprar
        3. Salir\n""")
        menu_ventas = int(input("Ingrese el número de la opción que desea realizar: "))
        if menu_ventas == 1:
            limpiarTerminal()
            print(clientes)
        elif menu_ventas == 2:
            limpiarTerminal()
            adm_compra()
        elif menu_ventas == 3:
            limpiarTerminal()
            print("Gracias por utilizar el sistema de ventas")
            break

###########################################
########## CONTROL DE CLIENTES ############
###########################################

def adm_clientes():
    print("\nAdministración de clientes\n")
    menu_clientes = 0
    while menu_clientes != 5:
        print("""\nIngrese el número de la opción que desea realizar
        1. Mostrar y retornar el número de clientes registrados en la tienda
        2. Crear cliente
        3. Mostrar saldo de cliente
        4. Modificar saldo de cliente
        5. Salir\n""")
        menu_clientes = int(input("Ingrese el número de la opción que desea realizar: "))
        if menu_clientes == 1:
            limpiarTerminal()
            mostrar_clientes()
        elif menu_clientes == 2:
            limpiarTerminal()
            crear_cliente()
        elif menu_clientes == 3:
            limpiarTerminal()
            ver_saldo_cliente()
        elif menu_clientes == 4:
            limpiarTerminal()
            cambiar_saldo_cliente()
        elif menu_clientes == 5:
            limpiarTerminal()
            print("Gracias por utilizar el sistema de administración de clientes")
            break

###########################################
########## MENU GENERAL ###################
###########################################

print("\nBienvenido al sistema de control y ventas\n")
opcion = 0
while opcion != 3:
    print("""Ingrese el número de la opción que desea realizar
    1. Control de bodega
    2. Administración de clientes
    3. Sistema de ventas
    4. Salir""")
    opcion = int(input("Ingrese el número de la opción que desea realizar: "))
    if opcion == 1:
        limpiarTerminal()
        adm_bodega()
    elif opcion == 2:
        limpiarTerminal()
        adm_clientes()
    elif opcion == 3:
        limpiarTerminal()
        adm_ventas()
    elif opcion == 4:
        limpiarTerminal()
        print("Gracias por utilizar el sistema de control y ventas")
        break



msg="""
===BIENVENIDO AL SISTEMA===
para continuar, por favor ingrese una opcion:
1.Sumar 2 numeros
2.Crea una coleccion
3.agregar un producto
4.Precio de mas bajo costo de la coleccion
5.ver productos de la coleccion
0.Salir
==========================
"""
def sumar():
    n1=int(input("ingrese el primer valor: "))
    n2=int(input("ingrese el segundo valor: "))
    resultado = n1+n2
    print(f"el resultado de la suma es: {resultado}")
def crear_coleccion():
    print("Nueva colecion de prodructos creada")
    return []
def agregar(coleccion):
    nombre_del_producto = input("ingrese el nombre del producto: ")
    precio_del_producto = float(input("ingrese el precio del producto: "))
    coleccion.append({"nombre":nombre_del_producto,"precio":precio_del_producto})
    print(f"{nombre_del_producto} agregado con exito")
def precio_mas_bajo(coleccion):
    if not coleccion:
        print("la coleccion esta vacia")
        return
    else:
        poducto_mas_barato = min(coleccion, key=lambda p : p['precio'])
        print(f"el producto mas barato es: {poducto_mas_barato['nombre']} con un precio de: {poducto_mas_barato['precio']}")
def ver_productos(coleccion):
    if not coleccion:
        print("la coleccion esta vacia")
        return
    else:
        print("Productos en la coleccion:")
        for i, p in enumerate(coleccion, 1):
            print(f"{i}. {p['nombre']}  Precio: {p['precio']}")

productos = []
coleccion = []



while True:
    print(msg)
    option= int(input("ingrese una opcion: "))
    if option ==1:
        sumar()
    elif option ==2:
        crear_coleccion()
    elif option ==3:
        agregar(coleccion)
    elif option ==4:
        precio_mas_bajo(coleccion)
    elif option ==5:
        ver_productos(coleccion)
    elif option == 0:
        break
    else:
        print("ingrese una opcion valida")
inventario = {
        "Mercedez": 5000,
        "Toyota": 2500,
        "BMW": 4300,
        "Porsche": 7000,
        "Kia": 1200
        }

def menu():
    print("""
               1) Agregar marcas al inventario:
               2) Mostrar los datos del inventario:
               3) Filtrar por nombre:
               4) Filtrar por precio:
               5) Salir
    """)

def agregar_marcas():
    marca = input("Ingrese el nombre de la marca: ")
    precio = int(input("Ingrese el precio de la marca: "))
    inventario[marca] = precio

def mostrar_inventario():
    print("Su inventario es el siguiente: ")
    for marca, precio in inventario.items():
        print("Marca:", marca)
        print("Precio:", precio)
        print("- - - - - -")

def buscar_marca():
    filtro = input("Ingrese el nombre de la marca que busca: ")
    resultados = []
    for marca, precio in inventario.items():
        if filtro.lower() in marca.lower():
            resultados.append((marca, precio))

    if resultados:
        print("Los resultados de su búsqueda son los siguientes:")
        for marca, precio in resultados:
            print("Marca:", marca)
            print("Precio:", precio)
            print("- - - - - -")
    else:
        print("No se encontraron resultados para su búsqueda.")

def despedida():
    print("Gracias por usar la aplicación.")

opcion = -1

while opcion != 0:
    menu()
    opcion = int(input("Ingrese el número del menú que desea realizar: "))

    if opcion == 1:
        agregar_marcas()
    elif opcion == 2:
        mostrar_inventario()
    elif opcion == 3:
        buscar_marca()
    elif opcion == 5:
        despedida()
        break
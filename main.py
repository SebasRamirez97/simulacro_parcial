from funciones.carga_productos import carga_inventario as carga
from funciones.busqueda_por_nombre import buscar_producto as buscar
from funciones.ordenar_inventario import orden_ascendente_precios as orden
from funciones.mostrar_segun import mostrar_maximo as maximo
from funciones.mostrar_segun import mostrar_minimo as minimo


matriz = [[]]
opcion = 0

while(opcion != 7):
    print("MENU PRINCIPAL")
    print("1. Carga productos\n" \
    "2. Buscar productos\n" \
    "3. Ordenar inventario\n" \
    "4. Mostrar progructo mas caro\n" \
    "5. Mostrar producto mas barato\n" \
    "6. Mostrar productos con precio mayor a 15000\n" \
    "7. Salir")


    opcion = int(input("Seleccione una opcion: "))
    respuesta = ""
    match opcion:
        case 1: 
            while(respuesta != "n" and respuesta != "N"):
                carga(matriz)
                print("¿Quiere seguir cargando?s/n:")
        case 2:
            print(buscar(matriz))
        case 3:
            print(orden(matriz))
        case 4:
            print(maximo(matriz))
        case 5:
            print(minimo(matriz))
        
    


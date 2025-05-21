def mostrar_maximo(matriz):
    maximo = -float("inf")
    for i in range(len(matriz)):
        if matriz[i][1] > maximo:
            maximo = matriz[i][1]
            producto_maximo_precio = matriz[i]
    return producto_maximo_precio

def mostrar_minimo(matriz):
    minimo = float("inf")
    for i in range(len(matriz)):
        if matriz[i][1] < minimo:
            minimo = matriz[i][1]
            producto_minimo_precio = matriz[i]
    return producto_minimo_precio

def mostrar_mayores_15000(matriz):
    nueva_matriz = []
    for i in range(len(matriz)):
        if matriz[i][1] > 15000:
            nueva_matriz += matriz[i]
    return nueva_matriz
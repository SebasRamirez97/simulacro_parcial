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


matriz = [["zanahoria", 25000, 3], ["hamburguesa", 2000, 4], ["Pepino",15000, 6]]


print(mostrar_maximo([["zanahoria", 25000, 3], ["hamburguesa", 2000, 4], ["Pepino",15000, 6]]))
print(mostrar_minimo([["zanahoria", 25000, 3], ["hamburguesa", 2000, 4], ["Pepino",15000, 6]]))
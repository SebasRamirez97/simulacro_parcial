def orden_ascendente_precios(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)-1):
            if matriz[j][1] > matriz[j+1][1]:
                aux = matriz[j+1]
                matriz[j+1] = matriz[j]
                matriz[j] = aux

    return matriz

print(orden_ascendente_precios([["zanahoria", 25000, 3], ["algodon", 2000, 6], ["hamburguesa", 20000, 4], ["Pepino",15000, 6], ["Salchicha", 1600, 5]]))
def buscar_producto(matriz):
    
    producto = input("Ingrese el nombre del producto que desea buscar: ")
    for i in range(len(matriz)):
        if(matriz[i][0] == producto):
            return matriz[i]
        else:
            return "No se encontro el producto"
        



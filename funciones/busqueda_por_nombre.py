from .matriz_vacia import vacia

def buscar_producto(matriz: list)->list|str: 
    """Recibe una matriz, en primer instancia 
    revisa si la matriz esta vacia, en caso de 
    estarlo nos dara un mensaje de matriz vacia. 
    En caso de no estar vacia nos pédira que ingresemos el producto que necesitamos
    y en el caso de existir nos devolvera el produuto que buscamos junto a su precio 
    y cantidad en caso de no existir nos devolvera un mensaje de producto no encontrado.
     
    ### Args:
        matirz: list
    ### Returns:
        str | list
    """
    if(vacia(matriz)):
        return "La matriz esta vacia ingrese datos antes seleccionar esta opcion\n"
    else:
        producto = input("Ingrese el nombre del producto que desea buscar: ")
        for i in range(len(matriz)):
            if(matriz[i][0] == producto):
                return matriz[i]
            else:
                return "No se encontro el producto\n"
        



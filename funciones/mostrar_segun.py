from .matriz_vacia import vacia

def mostrar_maximo(matriz: list)->str|list:
    """Recibe una matriz, en primer instancia 
    revisa si la matriz esta vacia, en caso de 
    estarlo nos dara un mensaje de matriz vacia. 
    Sino nos devuelve el producto con el precio maximo.
     
    ### Args:
        matriz: list
    ### Returns:
        str | list
    """
    if(vacia(matriz)):
        return "La matriz esta vacia ingrese datos antes seleccionar esta opcion\n"
    else:
        maximo = -float("inf")
        for i in range(len(matriz)):
            if matriz[i][1] > maximo:
                maximo = matriz[i][1]
                producto_maximo_precio = matriz[i]
        return producto_maximo_precio

def mostrar_minimo(matriz: list)->str|list:
    """Recibe una matriz, en primer instancia 
    revisa si la matriz esta vacia, en caso de 
    estarlo nos dara un mensaje de matriz vacia. 
    Sino nos devuelve el producto con el precio minimo.
     
    ### Args:
        matriz: list
    ### Returns:
        str | list

    """
    if(vacia(matriz)):
        return "La matriz esta vacia ingrese datos antes seleccionar esta opcion\n"
    else:
        minimo = float("inf")
        for i in range(len(matriz)):
            if matriz[i][1] < minimo:
                minimo = matriz[i][1]
                producto_minimo_precio = matriz[i]
        return producto_minimo_precio

def mostrar_mayores_15000(matriz):
    """Recibe una matriz, en primer instancia 
    revisa si la matriz esta vacia, en caso de 
    estarlo nos dara un mensaje de matriz vacia. 
    Devuelve una nueva matriz con los productos 
    con el precio mayor a 15000.
     
    ### Args:
        matriz: list
    ### Returns:
        str | list

    """
    if(vacia(matriz)):
        return "La matriz esta vacia ingrese datos antes seleccionar esta opcion\n"
    else:
        nueva_matriz = []
        for i in range(len(matriz)):
            if matriz[i][1] > 15000:
                nueva_matriz += matriz[i]
        return nueva_matriz
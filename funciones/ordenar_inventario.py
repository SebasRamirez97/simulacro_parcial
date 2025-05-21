from .matriz_vacia import vacia

def orden_ascendente_precios(matriz: list)->list:
    """Recibe una matriz, en primer instancia 
    revisa si la matriz esta vacia, en caso de 
    estarlo nos dara un mensaje de matriz vacia. 
    Sino nos ordena la matriz segun el precio de 
    manera ascendente y la devuelve.
    
    ### Args:
        matriz: list
    ### Returns:
        list
    """
    if(vacia(matriz)):
        return "La matriz esta vacia ingrese datos antes seleccionar esta opcion\n"
    else:
        for i in range(len(matriz)):
            for j in range(len(matriz)-1):
                if matriz[j][1] > matriz[j+1][1]:
                    aux = matriz[j+1]
                    matriz[j+1] = matriz[j]
                    matriz[j] = aux

        return matriz


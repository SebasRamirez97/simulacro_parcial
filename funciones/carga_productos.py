def carga_inventario(matriz:list)->None:
      """Recibe una matriz y nos pedira cargar un producto,
        por nombre, precio y cantidad
        
        ### Args:
            matriz: list
        ### Returns:
            None
        """
      nombre_producto = input("Ingrese el nombre del producto: ")
      precio_producto = float(input("Ingrese el precio del producto: "))
      cantidad = int(input("Ingrese la cantidad de productos: "))

      matriz += [[nombre_producto, precio_producto, cantidad]]


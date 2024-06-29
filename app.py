from funciones import agregar_producto, listar_productos, buscar_por_categoria, calcular_promedio, guardar_productos

def main():
    productos = []
    
    while True:
        print("1. Registrar producto")
        print("2. Listar todos los productos")
        print("3. Buscar productos por categoría")
        print("4. Calcular el precio promedio de los productos")
        print("5. Guardar lista de productos en archivo")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_producto(productos)
        elif opcion == "2":
            listar_productos(productos)
        elif opcion == "3":
            buscar_por_categoria(productos)
        elif opcion == "4":
            calcular_promedio(productos)
        elif opcion == "5":
            guardar_productos(productos)
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    main()

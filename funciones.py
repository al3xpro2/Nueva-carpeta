import math
import random

def agregar_producto(productos):
    try:
        nombre = input("Ingresar producto: ")
        categoria = input("Ingrese categoría del producto: ")
        cantidad = int(input("Ingresar cantidad del producto: "))
        precio = random.uniform(10, 1000)

        producto = {
            "nombre": nombre,
            "categoria": categoria,
            "cantidad": cantidad,
            "precio": precio
        }

        productos.append(producto)
        print("Producto registrado exitosamente!")
    except ValueError:
        print("Error: La cantidad debe ser un número entero.")

def listar_productos(productos):
    if productos:
        for producto in productos:
            print(f'Nombre: {producto["nombre"]}, Categoría: {producto["categoria"]}, Cantidad: {producto["cantidad"]}, Precio: {producto["precio"]:.2f}')
    else:
        print("No hay productos registrados.")

def buscar_por_categoria(productos):
    categoria = input("Ingrese la categoría que desea buscar: ")
    encontrados = [producto for producto in productos if producto["categoria"].lower() == categoria.lower()]
    
    if encontrados:
        for producto in encontrados:
            print(f'Nombre: {producto["nombre"]}, Cantidad: {producto["cantidad"]}, Precio: {producto["precio"]:.2f}')
    else:
        print("No se encontraron productos en esta categoría.")

def calcular_promedio(productos):
    precios = [producto["precio"] for producto in productos]
    if precios:
        promedio = math.fsum(precios) / len(precios)
        print(f'El precio promedio de todos los productos es: {promedio:.2f}')
    else:
        print("No hay precios registrados para calcular el promedio.")

def guardar_productos(productos):
    with open("productos.txt", "w") as archivo:
        for producto in productos:
            archivo.write(f'{producto}\n')
    print("Lista de productos guardada exitosamente en productos.txt")

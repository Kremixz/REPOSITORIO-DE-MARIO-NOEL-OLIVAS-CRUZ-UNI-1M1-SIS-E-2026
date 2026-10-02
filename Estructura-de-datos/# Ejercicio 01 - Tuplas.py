# Ejercicio 01 - Tuplas
# Estudiante: Mario Noel Olivas Cruz   Carnet: 6B76F959

# Una tupla es una colección ordenada e INMUTABLE
producto = ("Arroz", "libra", 18.50)      # (nombre, unidad, precio en C$)

# 1. Acceso por índice
print("Producto:", producto[0])
print("Precio:   C$", producto[2])

# 2. Desempaquetado
nombre, unidad, precio = producto
print(f"{nombre} por {unidad}: C$ {precio:.2f}")

# 3. Tupla de tuplas: compra en la pulpería
compra = (
    ("Arroz", 5, 18.50),
    ("Frijoles", 3, 32.00),
    ("Azúcar", 2, 20.00),
)

total = 0
for articulo, cantidad, precio_unitario in compra:
    subtotal = cantidad * precio_unitario
    total = total + subtotal
    print(f"{articulo:<10} {cantidad} x C$ {precio_unitario:6.2f} = C$ {subtotal:7.2f}")

print(f"Total a pagar: C$ {total:.2f}")
print("Artículos distintos:", len(compra))

# 4. Inmutabilidad: quita el # de la siguiente línea y observa el error
# producto[2] = 20.00
#Tuplas10_Ferreteria:Catagolo_Factura

# Parte A del ejercicio:

catalogo = (
    ("P01", "Martillo", 250.00),
    ("P02", "Clavos 2 pulg (lb)", 45.00),
    ("P03", "Cinta métrica 5 m", 180.00),
    ("P04", "Brocha 3 pulg", 95.00),
    ("P05", "Lija #100", 15.00),
)


def buscar_producto(codigo):
    for producto in catalogo:
        if producto[0] == codigo:
            return producto
    return None


print(buscar_producto("P03"))
print(buscar_producto("P09"))
      
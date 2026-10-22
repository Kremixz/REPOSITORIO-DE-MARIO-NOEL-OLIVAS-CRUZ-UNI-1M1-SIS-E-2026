# Intercambio de dos posiciones de una lista
precios = [85, 30, 120]
print("Antes:", precios)

# Forma 1: asignación múltiple de Python
precios[0], precios[1] = precios[1], precios[0]
print("Después:", precios)

# Forma 2: con variable auxiliar (válida en cualquier lenguaje)
temporal = precios[1]
precios[1] = precios[2]
precios[2] = temporal
print("Con auxiliar:", precios)
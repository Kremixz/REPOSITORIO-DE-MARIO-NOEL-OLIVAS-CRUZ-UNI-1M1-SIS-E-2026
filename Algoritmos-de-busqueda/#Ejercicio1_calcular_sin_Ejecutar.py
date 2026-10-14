def busqueda_lineal(lista, objetivo):
    comparaciones = 0
    for posicion, valor in enumerate(lista):
        comparaciones += 1
        if valor == objetivo:
            return posicion, comparaciones
    return -1, comparaciones


n = 8000
codigos = list(range(1, n + 1))

# Mejor caso: el objetivo es el primer elemento
pos, comp = busqueda_lineal(codigos, 1)
print("Mejor caso:   ", comp, "comparaciones")

# Peor caso: el objetivo no existe (ningún código es 0)
pos, comp = busqueda_lineal(codigos, 0)
print("Peor caso:    ", comp, "comparaciones")

# Caso promedio: buscar cada código una vez y promediar
total = 0
for valor in codigos:
    pos, comp = busqueda_lineal(codigos, valor)
    total = total + comp
print("Caso promedio:", total / n, "comparaciones")
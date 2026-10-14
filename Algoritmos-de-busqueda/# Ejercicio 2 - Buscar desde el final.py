# Ejercicio 2 - Buscar desde el final

def busqueda_inversa(lista, objetivo):
    comparaciones = 0
    for i in range(len(lista) - 1, -1, -1):
        comparaciones = comparaciones + 1
        if lista[i] == objetivo:
            return i, comparaciones
    return -1, comparaciones


n = 1000
codigos = list(range(1, n + 1))

# Mejor caso: el objetivo es el ÚLTIMO elemento (ahora se revisa primero)
pos, comp = busqueda_inversa(codigos, n)
print("Mejor caso:   ", comp, "comparaciones")

# Peor caso: el objetivo no existe (ningún código es 0)
pos, comp = busqueda_inversa(codigos, 0)
print("Peor caso:    ", comp, "comparaciones")

# Caso promedio: buscar cada código una vez y promediar
total = 0
for valor in codigos:
    pos, comp = busqueda_inversa(codigos, valor)
    total = total + comp
print("Caso promedio:", total / n, "comparaciones")

# Respuestas:
# - ¿Qué objetivo produce ahora el mejor caso? El último elemento (1000),
#   porque es el primero que se revisa. Antes era el primero (1).
# - ¿Cambia el promedio? No: sigue siendo (n + 1) / 2 = 500.5. Cada posición
#   sigue teniendo la misma probabilidad; solo se invierte el orden: el
#   elemento del final cuesta 1, el penúltimo 2, ... y el primero n, y
#   la suma 1 + 2 + ... + n es la misma.
# - ¿Cambia el peor caso? No: sigue siendo n = 1000. Si el objetivo no
#   existe, se revisan los n elementos sin importar la dirección.
# - Conclusión: la dirección solo cambia qué objetivo es el afortunado
#   (mejor caso), pero no el costo promedio ni el peor caso: ambos siguen
#   siendo O(n).
# Ejercicio 3 - Su propia tabla de crecimiento
import time


def busqueda_lineal(lista, objetivo):
    comparaciones = 0
    for i in range(len(lista)):
        comparaciones = comparaciones + 1
        if lista[i] == objetivo:
            return i, comparaciones
    return -1, comparaciones


tamanos = [1000, 10000, 100000, 1000000, 2000000]
tiempo_1M = 0

for n in tamanos:
    codigos = list(range(1, n + 1))
    inicio = time.perf_counter()
    pos, comp = busqueda_lineal(codigos, 0)     # peor caso
    fin = time.perf_counter()
    print(f"n = {n:>9} | comparaciones = {comp:>9} | tiempo = {fin - inicio:.5f} s")

    if n == 1000000:
        tiempo_1M = fin - inicio
        # Predicción: la lista se duplica, el trabajo se duplica (O(n))
        prediccion = tiempo_1M * 2
        print(f"  Predicción para 2 000 000: {prediccion:.5f} s")
    if n == 2000000:
        print(f"  Resultado real:            {fin - inicio:.5f} s")

# Explicación de la diferencia:
# Con O(n), al duplicar n se espera que el tiempo se duplique (≈ 2 × el
# tiempo de 1 000 000). Las comparaciones sí se duplican exactamente
# (1 000 000 -> 2 000 000), pero el tiempo medido casi nunca coincide
# con la predicción: el reloj tiene variaciones, hay otros programas
# usando el procesador, y el uso de memoria y de caché cambia con
# listas más grandes. Por eso la predicción es aproximada.
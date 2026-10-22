def ordenar_burbuja(lista):
    n = len(lista)
    comparaciones = 0
    intercambios = 0
    i = 0
    hubo_intercambio = True

    while i < n - 1 and hubo_intercambio:
        hubo_intercambio = False
        for j in range(n - 1 - i):           # mejora 1
            comparaciones += 1
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambios += 1
                hubo_intercambio = True          # mejora 2
        i += 1
        print(f"Pasada {i}: {lista}")

    return comparaciones, intercambios


precios = [85, 30, 120, 45, 60]
print("Original:", precios)
comp, inter = ordenar_burbuja(precios)
print("Ordenada:", precios)
print("Comparaciones:", comp, "| Intercambios:", inter)
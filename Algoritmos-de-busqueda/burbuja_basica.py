def ordenar_burbuja(lista):
    n = len(lista)
    for i in range(n - 1):           # pasadas
        for j in range(n - 1):       # pares (j, j + 1)
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]


precios = [85, 30, 120, 45, 60]
print("Original:", precios)
ordenar_burbuja(precios)
print("Ordenada:", precios)
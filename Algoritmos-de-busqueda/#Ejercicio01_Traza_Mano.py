
def busqueda_lineal(lista, objetivo):
    i = 0
    while i < len(lista):
        if lista[i] == objetivo:
            return i          
        i = i + 1
    return -1                


lista=[4,15,8,15,23]
posicion = busqueda_lineal(lista, 7)

print("Buscar 15:", busqueda_lineal(lista, 15))
print("Buscar 23:", busqueda_lineal(lista, 23))
print("Buscar 7:", busqueda_lineal(lista, 7))
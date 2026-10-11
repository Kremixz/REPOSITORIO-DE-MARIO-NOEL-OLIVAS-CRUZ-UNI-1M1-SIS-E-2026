#Ejercicio03_Inventario_Agotado
def busqueda_lineal(lista, objetivo):
    i = 0
    while i < len(lista):
        if lista[i] == objetivo:
            return i
        i = i + 1
    return -1

existencias = [12, 7, 0, 25, 0, 3]
posicion = busqueda_lineal(existencias, 0)

if posicion != -1:
    print("Primer producto agotado en la posición:", posicion)
else:
    print("No hay productos agotados")
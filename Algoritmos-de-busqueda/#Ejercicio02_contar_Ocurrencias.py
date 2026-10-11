#Ejercicio02_contar_Ocurrencias
def contar(lista, objetivo):
    cantidad = 0
    for i in range(len(lista)):
        if lista[i] == objetivo:
            cantidad = cantidad + 1
    return cantidad

notas = [78, 92, 65, 92, 88]

print("Cantidad de veces que aparece 92:", contar(notas, 92))
print("Cantidad de veces que aparece 100:", contar(notas, 100))
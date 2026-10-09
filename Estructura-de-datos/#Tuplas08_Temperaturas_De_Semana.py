#Tuplas08_Temperaturas_De_Semana
temp_managua = (31, 33, 32, 34, 30, 29, 32)
temp_esteli = (24, 26, 25, 23, 27, 25, 24)


def resumen(datos):
    minima = datos[0]
    maxima = datos[0]
    suma = 0
    for dato in datos:
        if dato < minima:
            minima = dato
        if dato > maxima:
            maxima = dato
        suma = suma + dato
    promedio = suma / len(datos)
    return (minima, maxima, promedio)


minima, maxima, promedio = resumen(temp_managua)
print(f"Managua -> mínima: {minima} °C, máxima: {maxima} °C, promedio: {promedio:.1f} °C")

minima, maxima, promedio = resumen(temp_esteli)
print(f"Estelí -> mínima: {minima} °C, máxima: {maxima} °C, promedio: {promedio:.1f} °C")
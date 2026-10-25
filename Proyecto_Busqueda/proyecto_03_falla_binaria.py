# Proyecto 3 · ¿Por qué falla la binaria?
# Nombre: Mario Noel Olivas Cruz
# Carné: 6B76F959

# ---------------------------------------------------------------
# DATOS
# La lista de facturas NO esta ordenada (llegan en el orden de caja)
# ---------------------------------------------------------------
facturas = [4821, 1307, 9654, 2290, 7716, 3348, 5012, 8875,
            1180, 6433, 2957, 7041, 3895, 9210, 5568]

buscados = [8875, 4821, 2290, 7041, 9210, 1180]


# ---------------------------------------------------------------
# BUSQUEDAS (iguales a las de los proyectos anteriores, sin cambios)
# ---------------------------------------------------------------
def busqueda_lineal(lista, buscado):
    comparaciones = 0
    for i in range(len(lista)):
        comparaciones = comparaciones + 1    # se cuenta antes de comparar
        if lista[i] == buscado:
            return i, comparaciones
    return -1, comparaciones


def busqueda_binaria(lista, buscado):
    izq = 0
    der = len(lista) - 1
    posicion = -1
    comparaciones = 0
    while izq <= der and posicion == -1:
        medio = (izq + der) // 2
        comparaciones = comparaciones + 1    # una comparacion por cada medio examinado
        if lista[medio] == buscado:
            posicion = medio
        elif lista[medio] < buscado:
            izq = medio + 1
        else:
            der = medio - 1
    return posicion, comparaciones


# ---------------------------------------------------------------
# FUNCIONES NUEVAS DEL PROYECTO
# ---------------------------------------------------------------
def binaria_con_traza(lista, buscado):
    # Igual que la binaria, pero imprime lo que pasa en cada vuelta del ciclo
    izq = 0
    der = len(lista) - 1
    posicion = -1
    comparaciones = 0
    while izq <= der and posicion == -1:
        medio = (izq + der) // 2
        comparaciones = comparaciones + 1
        print(f"izq = {izq:>2}  der = {der:>2}  medio = {medio:>2}  lista[medio] = {lista[medio]}")
        if lista[medio] == buscado:
            posicion = medio
        elif lista[medio] < buscado:
            izq = medio + 1
        else:
            der = medio - 1
    return posicion, comparaciones


def esta_ordenada(lista):
    # Compara cada elemento con el siguiente. Si encuentra uno mayor que el
    # que sigue, ya sabe que la lista no esta ordenada.
    ordenada = True
    for i in range(len(lista) - 1):    # el -1 es para no salirnos de la lista con i + 1
        if lista[i] > lista[i + 1]:
            ordenada = False
    return ordenada


def busqueda_segura(lista, buscado):
    # Solo usa la binaria si la lista esta ordenada; si no, usa la lineal
    if esta_ordenada(lista):
        return busqueda_binaria(lista, buscado)
    else:
        return busqueda_lineal(lista, buscado)


def mostrar_tabla(titulo, usar_segura):
    # Imprime la tabla del paso 3. Si usar_segura es True, usa busqueda_segura
    # en lugar de la binaria normal.
    print(titulo)
    print("Buscado   Real   Binaria   Comparaciones   Veredicto")
    print("-------   ----   -------   -------------   ---------")
    fallas = 0
    for valor in buscados:
        pos_real, comp_real = busqueda_lineal(facturas, valor)
        if usar_segura:
            pos_bin, comp_bin = busqueda_segura(facturas, valor)
        else:
            pos_bin, comp_bin = busqueda_binaria(facturas, valor)

        if pos_bin == pos_real:
            veredicto = "CORRECTO"
        else:
            veredicto = "FALLA"
            fallas = fallas + 1
        print(f"{valor:>7}   {pos_real:>4}   {pos_bin:>7}   {comp_bin:>13}   {veredicto}")
    print(f"Total de fallas: {fallas} de {len(buscados)}")


# ---------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ---------------------------------------------------------------

# Paso 3: la binaria sobre la lista desordenada
mostrar_tabla("=== BINARIA SOBRE LISTA DESORDENADA ===", False)

# Paso 4: la traza buscando 7041
print()
print("=== TRAZA DE LA BINARIA BUSCANDO 7041 ===")
pos, comp = binaria_con_traza(facturas, 7041)
print(f"Resultado: posición {pos}, {comp} comparaciones")

# Paso 5: comprobar si las listas estan ordenadas
print()
print("=== ESTA ORDENADA? ===")
print("facturas:", esta_ordenada(facturas))

# Paso 6: la busqueda segura
print()
mostrar_tabla("=== BUSQUEDA SEGURA SOBRE LA MISMA LISTA ===", True)

# Paso 7: copia ordenada
# sorted() crea una lista NUEVA, por eso facturas queda igual que antes
facturas_ordenadas = sorted(facturas)
print()
print("=== BINARIA SOBRE LA COPIA ORDENADA ===")
print("facturas_ordenadas:", facturas_ordenadas)
print("facturas sigue igual:", facturas)
print("Buscado   En la copia   Real en facturas")
print("-------   -----------   ----------------")
for valor in buscados:
    pos_copia, comp_copia = busqueda_binaria(facturas_ordenadas, valor)
    pos_real, comp_real = busqueda_lineal(facturas, valor)
    # Las dos posiciones casi nunca coinciden porque la copia tiene otro orden
    print(f"{valor:>7}   {pos_copia:>11}   {pos_real:>16}")

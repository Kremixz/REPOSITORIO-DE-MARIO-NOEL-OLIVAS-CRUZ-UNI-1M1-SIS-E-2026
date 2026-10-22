# Proyecto 1 · Tipo de cambio del BCN
# Nombre: (tu nombre completo)
# Carné: (tu carné)

# ---------------------------------------------------------------
# DATOS
# Dos listas paralelas: tasas[i] es el tipo de cambio del dia fechas[i]
# ---------------------------------------------------------------
fechas = [
    "2023-10-02", "2023-10-03", "2023-10-04", "2023-10-05", "2023-10-06",
    "2023-10-09", "2023-10-10", "2023-10-11", "2023-10-12", "2023-10-13",
    "2023-10-16", "2023-10-17", "2023-10-18", "2023-10-19", "2023-10-20",
    "2023-10-23", "2023-10-24", "2023-10-25", "2023-10-26", "2023-10-27",
    "2023-10-30", "2023-10-31"
]

tasas = [
    36.4330, 36.4340, 36.4350, 36.4360, 36.4370,
    36.4400, 36.4410, 36.4420, 36.4430, 36.4440,
    36.4470, 36.4480, 36.4490, 36.4500, 36.4510,
    36.4540, 36.4550, 36.4560, 36.4570, 36.4580,
    36.4610, 36.4620
]


# ---------------------------------------------------------------
# FUNCIONES DE BUSQUEDA
# Las dos retornan (posicion, comparaciones) y no imprimen nada
# ---------------------------------------------------------------
def busqueda_lineal(lista, buscado):
    comparaciones = 0
    for i in range(len(lista)):
        comparaciones = comparaciones + 1    # se cuenta antes de comparar
        if lista[i] == buscado:
            return i, comparaciones
    # Si el for termino sin retornar, el valor no esta en la lista
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
            izq = medio + 1                  # descarta la mitad izquierda
        else:
            der = medio - 1                  # descarta la mitad derecha
    return posicion, comparaciones


# ---------------------------------------------------------------
# FUNCIONES DEL MENU
# ---------------------------------------------------------------
def mostrar_menu():
    print()
    print("=== TIPO DE CAMBIO OFICIAL · OCTUBRE 2023 ===")
    print("1. Consultar tipo de cambio de una fecha")
    print("2. Convertir dólares a córdobas")
    print("3. Convertir córdobas a dólares")
    print("4. Salir")


def pedir_monto(mensaje):
    # Retorna el monto como float, o -1 si no es valido (texto, cero o negativo)
    texto = input(mensaje)
    try:
        monto = float(texto)
    except ValueError:
        # Si el usuario escribe letras, float() da error y lo atrapamos aqui
        print("Monto inválido. Debe escribir un número.")
        return -1
    if monto <= 0:
        print("El monto debe ser mayor que cero.")
        return -1
    return monto


def consultar_fecha():
    fecha = input("Fecha (AAAA-MM-DD): ")
    pos_lin, comp_lin = busqueda_lineal(fechas, fecha)
    pos_bin, comp_bin = busqueda_binaria(fechas, fecha)

    if pos_bin == -1:
        print("No hay registro para esa fecha (fin de semana o fuera del período).")
        print(f"Búsqueda lineal : {comp_lin} comparaciones")
        print(f"Búsqueda binaria: {comp_bin} comparaciones")
    else:
        print(f"Tipo de cambio: C$ {tasas[pos_bin]:.4f} por US$ 1")
        print(f"Búsqueda lineal : posición {pos_lin}, {comp_lin} comparaciones")
        print(f"Búsqueda binaria: posición {pos_bin}, {comp_bin} comparaciones")


def dolares_a_cordobas():
    fecha = input("Fecha (AAAA-MM-DD): ")
    # Aqui solo usamos la binaria, como pide el enunciado
    pos, comp = busqueda_binaria(fechas, fecha)
    if pos == -1:
        print("No hay registro para esa fecha (fin de semana o fuera del período).")
    else:
        monto = pedir_monto("Monto en dólares: ")
        if monto != -1:
            resultado = monto * tasas[pos]    # dolares por la tasa = cordobas
            print(f"US$ {monto:.2f} equivalen a C$ {resultado:.2f}")


def cordobas_a_dolares():
    fecha = input("Fecha (AAAA-MM-DD): ")
    pos, comp = busqueda_binaria(fechas, fecha)
    if pos == -1:
        print("No hay registro para esa fecha (fin de semana o fuera del período).")
    else:
        monto = pedir_monto("Monto en córdobas: ")
        if monto != -1:
            resultado = monto / tasas[pos]    # cordobas entre la tasa = dolares
            print(f"C$ {monto:.2f} equivalen a US$ {resultado:.2f}")


# ---------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ---------------------------------------------------------------
opcion = ""
while opcion != "4":
    mostrar_menu()
    opcion = input("Elija una opción: ")

    if opcion == "1":
        consultar_fecha()
    elif opcion == "2":
        dolares_a_cordobas()
    elif opcion == "3":
        cordobas_a_dolares()
    elif opcion == "4":
        print("Hasta luego.")
    else:
        print("Opción inválida. Elija un número del 1 al 4.")

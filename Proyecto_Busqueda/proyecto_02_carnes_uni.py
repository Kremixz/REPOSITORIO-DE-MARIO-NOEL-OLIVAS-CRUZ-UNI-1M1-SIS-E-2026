# Proyecto 2 · Consulta de estudiantes por carné UNI
# Nombre: Mario Noel Olivas Cruz
# Carné: 6B76F959

# ---------------------------------------------------------------
# DATOS
# Tres listas paralelas: la posicion i de las tres es el mismo estudiante
# ---------------------------------------------------------------
carnes = [
    "2023-0118U", "2023-0274U", "2023-0391U", "2023-0456U", "2023-0582U",
    "2023-0647U", "2023-0733U", "2023-0819U", "2023-0905U", "2023-1042U",
    "2024-0063U", "2024-0127U", "2024-0215U", "2024-0298U", "2024-0344U",
    "2024-0410U", "2024-0487U", "2024-0535U", "2024-0619U", "2024-0702U",
    "2024-0788U", "2024-0861U", "2025-0034U", "2025-0109U", "2025-0186U",
    "2025-0252U", "2025-0329U", "2025-0413U", "2025-0497U", "2025-0560U"
]

nombres = [
    "María José Rivas Zeledón",
    "Carlos Andrés Mairena López",
    "Ana Gabriela Espinoza Rugama",
    "Luis Fernando Obando Castillo",
    "Kevin Josué Blandón Pérez",
    "Fernanda Isabel Rocha Gutiérrez",
    "José Daniel Talavera Ruiz",
    "Valeria Sofía Centeno Aráuz",
    "Bryan Alexander Chavarría Mendoza",
    "Katherine Lucía Herrera Picado",
    "Jorge Luis Moncada Úbeda",
    "Daniela Alejandra Somarriba Cruz",
    "Eduardo Josué Castellón Vega",
    "Mariela Auxiliadora Lanuza Torres",
    "Óscar Danilo Pineda Hernández",
    "Ximena Carolina Galeano Molina",
    "Francisco Javier Ortega Zamora",
    "Heydi Massiel Matamoros Sáenz",
    "Ernesto Rafael Dávila Membreño",
    "Gissell Marcela Arana Quintero",
    "Axel Mauricio Jarquín Salgado",
    "Scarleth Yahoska Romero Huete",
    "Josué David Sequeira Bermúdez",
    "Camila Fernanda Urbina Narváez",
    "Héctor Manuel Ponce Largaespada",
    "Yaritza Lisseth Morales Duarte",
    "Marvin Antonio Sandino Flores",
    "Nohelia Patricia Cerda Valle",
    "Wilber Josué Vílchez Martínez",
    "Andrea Belén Guevara Mejía"
]

carreras = [
    "Ingeniería en Sistemas", "Ingeniería Civil", "Ingeniería Industrial",
    "Ingeniería Eléctrica", "Ingeniería en Computación", "Arquitectura",
    "Ingeniería en Sistemas", "Ingeniería Química", "Ingeniería Mecánica",
    "Ingeniería Electrónica", "Ingeniería Agrícola", "Ingeniería en Sistemas",
    "Ingeniería Civil", "Ingeniería Industrial", "Ingeniería Eléctrica",
    "Ingeniería en Computación", "Arquitectura", "Ingeniería en Sistemas",
    "Ingeniería Química", "Ingeniería Civil", "Ingeniería Mecánica",
    "Ingeniería Electrónica", "Ingeniería en Sistemas", "Ingeniería Industrial",
    "Ingeniería Agrícola", "Ingeniería en Computación", "Ingeniería Civil",
    "Ingeniería en Sistemas", "Ingeniería Eléctrica", "Arquitectura"
]


# ---------------------------------------------------------------
# VALIDACION DEL CARNE
# ---------------------------------------------------------------
def carne_valido(carne):
    # Formato esperado: AAAA-NNNNU (10 caracteres en total)
    if len(carne) != 10:
        return False
    # Con rebanadas (slices) sacamos cada parte del carne
    anio = carne[0:4]
    guion = carne[4]
    numero = carne[5:9]
    letra = carne[9]
    if anio.isdigit() and guion == "-" and numero.isdigit() and letra == "U":
        return True
    return False


# ---------------------------------------------------------------
# FUNCIONES DE BUSQUEDA
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


def buscar_nombre(lista, buscado):
    # Busqueda lineal que no distingue mayusculas de minusculas
    comparaciones = 0
    for i in range(len(lista)):
        comparaciones = comparaciones + 1
        # Se pasan a minuscula los DOS lados: el elemento y lo que escribio el usuario
        if lista[i].lower() == buscado.lower():
            return i, comparaciones
    return -1, comparaciones


def buscar_todos(lista, buscado):
    # Recorre TODA la lista y guarda cada posicion donde aparece el valor
    posiciones = []
    comparaciones = 0
    for i in range(len(lista)):
        comparaciones = comparaciones + 1
        if lista[i] == buscado:
            posiciones.append(i)    # no hay return aqui, el for sigue hasta el final
    return posiciones, comparaciones


# ---------------------------------------------------------------
# FUNCIONES DEL MENU
# ---------------------------------------------------------------
def mostrar_menu():
    print()
    print("=== REGISTRO ACADÉMICO UNI · CONSULTA ===")
    print("1. Buscar por carné")
    print("2. Buscar por nombre completo")
    print("3. Listar estudiantes de una carrera")
    print("4. Salir")


def opcion_buscar_carne():
    carne = input("Carné: ")
    if not carne_valido(carne):
        print("Formato inválido. Ejemplo de carné: 2024-0153U")
    else:
        # La binaria sirve aqui porque la lista de carnes esta ordenada
        pos_bin, comp_bin = busqueda_binaria(carnes, carne)
        pos_lin, comp_lin = busqueda_lineal(carnes, carne)
        if pos_bin == -1:
            print("No existe un estudiante con ese carné.")
            print(f"Búsqueda lineal : {comp_lin} comparaciones")
            print(f"Búsqueda binaria: {comp_bin} comparaciones")
        else:
            print(f"Estudiante: {nombres[pos_bin]}")
            print(f"Carrera   : {carreras[pos_bin]}")
            print(f"Búsqueda lineal : posición {pos_lin}, {comp_lin} comparaciones")
            print(f"Búsqueda binaria: posición {pos_bin}, {comp_bin} comparaciones")


def opcion_buscar_nombre():
    nombre = input("Nombre completo: ")
    # Aqui NO se puede usar la binaria porque los nombres no estan ordenados
    pos, comp = buscar_nombre(nombres, nombre)
    if pos == -1:
        print("No existe un estudiante con ese nombre.")
        print(f"Búsqueda lineal: {comp} comparaciones")
    else:
        # Como las listas son paralelas, la misma posicion sirve para las otras dos
        print(f"Carné   : {carnes[pos]}")
        print(f"Carrera : {carreras[pos]}")
        print(f"Búsqueda lineal: posición {pos}, {comp} comparaciones")


def opcion_listar_carrera():
    carrera = input("Carrera: ")
    posiciones, comp = buscar_todos(carreras, carrera)
    if len(posiciones) == 0:
        print("No se encontraron estudiantes en esa carrera.")
        print(f"Total: 0 estudiantes · {comp} comparaciones")
    else:
        for p in posiciones:
            print(f"  {carnes[p]}  {nombres[p]}")
        print(f"Total: {len(posiciones)} estudiantes · {comp} comparaciones")


# ---------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ---------------------------------------------------------------
opcion = ""
while opcion != "4":
    mostrar_menu()
    opcion = input("Elija una opción: ")

    if opcion == "1":
        opcion_buscar_carne()
    elif opcion == "2":
        opcion_buscar_nombre()
    elif opcion == "3":
        opcion_listar_carrera()
    elif opcion == "4":
        print("Hasta luego.")
    else:
        print("Opción inválida. Elija un número del 1 al 4.")

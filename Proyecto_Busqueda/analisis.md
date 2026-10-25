# Análisis · Algoritmos de búsqueda

**Nombre:** Mario Noel Olivas Cruz

**Carné:** 6B76F959

**Unidad:** Algoritmos de búsqueda · Programación Estructurada

## Contenido

1. [Proyecto 1 · Tipo de cambio del BCN](#proyecto-1--tipo-de-cambio-del-bcn)
2. [Proyecto 2 · Consulta de estudiantes por carné UNI](#proyecto-2--consulta-de-estudiantes-por-carné-uni)
3. [Proyecto 3 · ¿Por qué falla la binaria?](#proyecto-3--por-qué-falla-la-binaria)

---

## Proyecto 1 · Tipo de cambio del BCN

### Pregunta 1

> **Enunciado:** Completa una tabla con las comparaciones de cada algoritmo al buscar 2023-10-02, 2023-10-20, 2023-10-31 y 2023-10-07. ¿En cuál de las cuatro la lineal le gana o empata con la binaria, y por qué?

**Respuesta:**

| Fecha buscada | Comparaciones lineal | Comparaciones binaria |
|---------------|----------------------|-----------------------|
| 2023-10-02    | 1                    | 4                     |
| 2023-10-20    | 15                   | 4                     |
| 2023-10-31    | 22                   | 5                     |
| 2023-10-07    | 22                   | 4                     |

La lineal le gana a la binaria solamente al buscar 2023-10-02, porque necesitó 1 comparación contra 4 de la binaria. Esto pasa porque esa fecha está en la posición 0, o sea es el primer elemento de la lista, y la lineal empieza justo por ahí, así que es su mejor caso. La binaria en cambio no empieza por el principio sino por el medio, y tiene que ir descartando mitades hasta llegar al inicio de la lista, por eso hizo 4. En ninguna de las cuatro fechas empataron.

### Pregunta 2

> **Enunciado:** ¿Cuál es el peor caso de cada algoritmo con estas 22 fechas? Comprueba tu respuesta buscando fechas que no existan.

**Respuesta:**

Con 22 fechas, el peor caso de la lineal es 22 comparaciones, que pasa cuando la fecha está de última (como 2023-10-31) o cuando no existe (como 2023-10-07). Lo comprobé buscando fechas que no existen y la lineal siempre dio 22.

El peor caso de la binaria es 5 comparaciones. Lo comprobé porque al buscar todas las fechas que sí existen el máximo fue 5 (por ejemplo con 2023-10-31), y al buscar fechas que no existen como 2023-10-14, 2023-10-15 y 2023-11-01 también dio 5. Ninguna búsqueda dio 6 o más. Esto coincide con la calculadora de la sesión: se divide 22 entre 2 hasta llegar a 0 (22, 11, 5, 2, 1) y salen 5 divisiones.

### Pregunta 3

> **Enunciado:** Las fechas se comparan como texto. Ejecuta en Python `"2023-10-09" < "2023-10-16"` y luego `"31/10/2023" < "02/11/2023"`. Explica por qué el formato AAAA-MM-DD permite usar la binaria y qué pasaría si las fechas se guardaran como DD/MM/AAAA.

**Respuesta:**

Cuando ejecuté en Python `"2023-10-09" < "2023-10-16"` me dio `True`, y cuando ejecuté `"31/10/2023" < "02/11/2023"` me dio `False`.

Python compara los textos caracter por caracter de izquierda a derecha, parando en el primer caracter que sea distinto. Con el formato AAAA-MM-DD lo primero que se compara es el año, luego el mes y luego el día, que es el mismo orden de importancia de una fecha, entonces el orden alfabético del texto coincide con el orden cronológico. Por eso la lista de fechas queda ordenada y se puede usar la binaria.

Con DD/MM/AAAA pasa lo contrario: lo primero que se compara es el día. En el segundo ejemplo, el 31/10/2023 es anterior al 02/11/2023 en la vida real, pero Python dice que no porque compara el "3" con el "0" y el "3" es mayor. Entonces la lista no quedaría ordenada por fecha y la binaria fallaría, podría decir que una fecha no existe aunque sí esté.

### Pregunta 4

> **Enunciado:** La lista tasas también está ordenada de menor a mayor. ¿A qué se debe en este registro? Desde 2024 el BCN mantiene fijo el tipo de cambio: si el registro fuera de un mes de 2025, ¿tendría sentido buscar una fecha a partir de una tasa?

**Respuesta:**

La lista tasas está ordenada de menor a mayor porque en 2023 el córdoba se deslizaba un poco cada día, o sea que el tipo de cambio subía todos los días. Como las fechas van avanzando en orden, las tasas también van subiendo en orden.

Si el registro fuera de un mes de 2025 no tendría sentido buscar una fecha a partir de una tasa, porque desde 2024 el BCN mantiene el tipo de cambio fijo. Eso significa que todas las tasas serían el mismo número repetido, entonces una tasa no identifica a un solo día: la misma tasa le correspondería a todas las fechas del mes y no podríamos saber cuál fecha es la que se quiere. Además, una lista con todos los valores iguales no sirve para ir descartando mitades.

### Pregunta 5

> **Enunciado:** Si el registro tuviera los días hábiles de diez años (unas 2,600 fechas), ¿cuántas comparaciones haría cada algoritmo en el peor caso?

**Respuesta:**

Con unas 2,600 fechas:

- Lineal: 2,600 comparaciones en el peor caso, porque revisa todos los elementos.
- Binaria: 12 comparaciones en el peor caso. Dividiendo 2,600 entre 2 varias veces (2600, 1300, 650, 325, 162, 81, 40, 20, 10, 5, 2, 1) salen 12 divisiones. Lo comprobé también con un while en Python y dio 12.

Se nota que la lineal creció muchísimo (de 22 a 2,600) y la binaria casi no cambió (de 5 a 12).

---

## Proyecto 2 · Consulta de estudiantes por carné UNI

### Pregunta 1

> **Enunciado:** Completa una tabla con las comparaciones de cada algoritmo al buscar 2023-0118U, 2024-0344U, 2025-0560U y 2024-0999U. Uno de ellos se encuentra con una sola comparación binaria: ¿por qué?

**Respuesta:**

| Carné buscado | Comparaciones lineal | Comparaciones binaria |
|---------------|----------------------|-----------------------|
| 2023-0118U    | 1                    | 4                     |
| 2024-0344U    | 15                   | 1                     |
| 2025-0560U    | 30                   | 5                     |
| 2024-0999U    | 30                   | 5                     |

El carné que se encontró con una sola comparación binaria es 2024-0344U. Esto pasa porque la lista tiene 30 elementos (posiciones 0 a 29) y la binaria siempre empieza calculando el medio con (0 + 29) // 2 = 14, y justo ese carné está en la posición 14. Entonces el primer medio que revisa ya es el que buscamos. Es como un mejor caso de la binaria, y fue por la posición en que está el dato, no porque el algoritmo haya hecho algo especial.

### Pregunta 2

> **Enunciado:** ¿Por qué la búsqueda por nombre no puede ser binaria con estas listas? Si quisieras usar la binaria para buscar nombres, ¿qué tendrías que hacerle a las tres listas y qué cuidado debes tener para que sigan siendo paralelas?

**Respuesta:**

La búsqueda por nombre no puede ser binaria porque la lista de nombres no está en orden alfabético. La binaria solo funciona si la lista está ordenada, ya que cada vez que compara con el medio descarta una mitad pensando que ahí no puede estar el dato. Con los nombres desordenados esa decisión sería incorrecta y podría decir que no existe un estudiante que sí está.

Para usar la binaria con nombres tendría que ordenar la lista de nombres alfabéticamente. El cuidado es que las tres listas son paralelas, entonces no basta con ordenar solo nombres: si lo hago, el nombre de la posición 0 ya no sería el del carné de la posición 0 y los datos quedarían mezclados (le saldría la carrera de otro estudiante). Tendría que reordenar las tres listas juntas, de manera que cada nombre siga con su carné y su carrera. Otro problema es que al reordenar así, la lista de carnés dejaría de estar ordenada y ya no podría usar la binaria para carnés, por lo que lo mejor sería trabajar con copias.

### Pregunta 3

> **Enunciado:** buscar_todos siempre hace 30 comparaciones. ¿Por qué no puede detenerse en la primera coincidencia, como la lineal normal?

**Respuesta:**

buscar_todos no puede detenerse en la primera coincidencia porque el valor puede aparecer más de una vez. Por ejemplo, en carreras hay 3 estudiantes de Arquitectura. Si la función hiciera return al encontrar el primero, solo daría una posición y se perderían los otros dos. Además, el programa no sabe de antemano cuántas veces aparece el valor, y la única forma de estar seguro de que ya encontró todos es revisar toda la lista hasta el final. Por eso siempre hace 30 comparaciones, y también cuando la carrera no existe.

### Pregunta 4

> **Enunciado:** Si la UNI tuviera 12,000 estudiantes en esta lista, ¿cuántas comparaciones haría cada algoritmo en el peor caso? ¿Y con 24,000? Explica qué observas al duplicar la cantidad de estudiantes.

**Respuesta:**

Con 12,000 estudiantes, en el peor caso:

- Lineal: 12,000 comparaciones.
- Binaria: 14 comparaciones (12000 se divide entre 2 catorce veces hasta llegar a 0).

Con 24,000 estudiantes:

- Lineal: 24,000 comparaciones.
- Binaria: 15 comparaciones.

Lo que observo es que al duplicar la cantidad de estudiantes la lineal también duplica su trabajo (de 12,000 a 24,000), pero la binaria solo aumenta una comparación (de 14 a 15). Eso confirma que la lineal crece al mismo ritmo que los datos y la binaria crece muy despacio.

### Pregunta 5

> **Enunciado:** Un estudiante de nuevo ingreso recibe el carné 2026-0001U. ¿En qué posición debe agregarse para que la binaria siga funcionando? ¿Qué pasaría si se insertara al inicio de la lista?

**Respuesta:**

El carné 2026-0001U debe agregarse al final de la lista, en la posición 30, porque la lista está ordenada por año de ingreso y luego por número, y 2026 es mayor que todos los años que ya hay (2023, 2024 y 2025). Así la lista sigue ordenada. Hay que agregarlo en la misma posición en las tres listas (carnes, nombres y carreras) para que sigan siendo paralelas. Lo probé y con el carné al final la binaria lo encuentra en la posición 30 con 5 comparaciones.

Si se insertara al inicio, la lista dejaría de estar ordenada porque 2026-0001U es mayor que el resto y quedaría primero. Lo probé y la binaria ya no encontró al estudiante nuevo, devolvió -1 aunque sí estaba en la lista. Los 30 estudiantes anteriores sí los siguió encontrando, pero eso fue suerte con estos datos y no se puede confiar en ello, porque en general una lista desordenada hace que la binaria descarte la mitad equivocada. Además, al insertar al inicio todas las posiciones se corren una casilla.

---

## Proyecto 3 · ¿Por qué falla la binaria?

### Pregunta 1 (tabla del paso 3)

> **Enunciado:** Copia la tabla del paso 3. ¿Cuántos valores falló la binaria, si todos existen en la lista?

**Respuesta:**

```
=== BINARIA SOBRE LISTA DESORDENADA ===
Buscado   Real   Binaria   Comparaciones   Veredicto
-------   ----   -------   -------------   ---------
   8875      7         7               1   CORRECTO
   4821      0        -1               4   FALLA
   2290      3         3               2   CORRECTO
   7041     11        -1               4   FALLA
   9210     13        13               3   CORRECTO
   1180      8        -1               4   FALLA
```

La binaria falló en 3 de los 6 valores (4821, 7041 y 1180), y eso que todos existen en la lista. En los tres casos devolvió -1, o sea que dijo "no encontrado" cuando el valor sí estaba.

### Pregunta 2 (traza de 7041)

> **Enunciado:** Con la traza de 7041, explica paso a paso en qué momento la binaria descartó la parte de la lista donde estaba el valor y por qué tomó esa decisión.

**Respuesta:**

La traza que mostró el programa fue:

```
izq =  0  der = 14  medio =  7  lista[medio] = 8875
izq =  0  der =  6  medio =  3  lista[medio] = 2290
izq =  4  der =  6  medio =  5  lista[medio] = 3348
izq =  6  der =  6  medio =  6  lista[medio] = 5012
```

En la primera vuelta el medio es la posición 7 y ahí está 8875. Como 8875 es mayor que 7041, el algoritmo decidió que 7041 tenía que estar a la izquierda y cambió der a 6. En ese momento descartó las posiciones 7 a 14, y justo en la posición 11 estaba el 7041. Ahí fue donde se perdió el valor, desde la primera comparación.

El algoritmo tomó esa decisión porque supone que la lista está ordenada: si el del medio es mayor que el buscado, todo lo que está a la derecha también sería mayor. Pero en esta lista eso no es cierto, a la derecha del 8875 hay números más chicos como 7041. Después de eso siguió buscando solo en las posiciones 0 a 6, donde el 7041 no existe, hasta que izq pasó a der y terminó con -1.

### Pregunta 3

> **Enunciado:** Uno de los valores se encontró con una sola comparación. ¿Fue mérito del algoritmo o casualidad? Explica.

**Respuesta:**

El valor que se encontró con una sola comparación fue 8875, y fue casualidad. La lista tiene 15 elementos y el primer medio que calcula la binaria siempre es (0 + 14) // 2 = 7. Resulta que el 8875 está justo en la posición 7, entonces lo encontró de una. No fue mérito del algoritmo ni significa que la lista esté bien para la binaria, simplemente el dato estaba en el lugar donde la binaria mira primero. Con otra lista desordenada habría fallado.

### Pregunta 4

> **Enunciado:** Que la binaria encuentre algunos valores, ¿demuestra que funciona en listas desordenadas? ¿Qué condición necesita y qué supone cada vez que descarta una mitad?

**Respuesta:**

No, que la binaria encuentre algunos valores no demuestra que funcione con listas desordenadas. En la tabla encontró 3 de 6, y esos aciertos dependieron de dónde estaban los valores (8875 estaba en el primer medio, y 2290 y 9210 quedaron en el camino por suerte). Un algoritmo que falla la mitad de las veces no sirve.

La condición que necesita es que la lista esté ordenada. Cada vez que descarta una mitad, está suponiendo que el valor no puede estar ahí, porque todos los elementos de esa mitad son menores (o mayores) que el buscado. Si la lista no está ordenada esa suposición puede ser falsa y el algoritmo descarta justo la parte donde estaba el dato, sin avisar ni dar ningún error.

### Pregunta 5

> **Enunciado:** Después de sorted(), la posición que devuelve la binaria ya no coincide con la de facturas. ¿Qué significa ese número? ¿Cuándo sería un problema, por ejemplo si existiera una lista paralela de montos en córdobas?

**Respuesta:**

Después de usar sorted(), el número que devuelve la binaria es la posición del valor dentro de facturas_ordenadas, que es otra lista con otro orden, no la posición en facturas. Por ejemplo, el 1180 está en la posición 0 de la copia pero en la posición 8 de facturas, y el 8875 está en la 12 de la copia pero en la 7 de facturas. Solo el 9210 coincidió (13 en las dos), y fue casualidad.

Sería un problema si existiera una lista paralela de montos en córdobas, porque montos[i] pertenece a la factura facturas[i]. Si uso la posición de la copia ordenada para buscar en montos, me daría el monto de otra factura. Por ejemplo, para la factura 1180 la binaria me daría 0 y montos[0] sería el monto de la factura 4821, que no es la que busqué. Para evitar eso habría que usar la posición real (con la lineal sobre facturas) o reordenar también la lista de montos de la misma manera.

### Pregunta 6

> **Enunciado:** Si solo vas a buscar una factura una vez, ¿conviene ordenar primero y usar la binaria, o usar la lineal? ¿Y si vas a hacer 1,000 búsquedas sobre la misma lista? Pista: para ordenar hay que revisar todos los elementos al menos una vez.

**Respuesta:**

Si solo voy a buscar una factura una vez, conviene usar la lineal. Para ordenar hay que revisar todos los elementos al menos una vez, o sea que ordenar ya cuesta tanto como hacer la búsqueda lineal completa en el peor caso (15 comparaciones aquí), y después todavía faltaría hacer la binaria. Ordenar primero y buscar con la binaria hace más trabajo en total que la lineal sola.

Si voy a hacer 1,000 búsquedas sobre la misma lista, conviene ordenar una sola vez y usar la binaria. El costo de ordenar se paga una vez y después cada búsqueda es muy barata: con esta lista de 15, la binaria hace como máximo 4 comparaciones, contra hasta 15 de la lineal. Haciendo 1,000 búsquedas serían unas 4,000 comparaciones contra unas 15,000 en el peor caso de la lineal, y la diferencia crece mientras más grande sea la lista. Otra cosa a tener en cuenta es que habría que mantener la lista ordenada si se le agregan datos.

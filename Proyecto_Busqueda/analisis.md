# Análisis · Algoritmos de búsqueda

Nombre: (tu nombre completo)

Carné: (tu carné)

## Proyecto 1 · Tipo de cambio del BCN

### Pregunta 1

| Fecha buscada | Comparaciones lineal | Comparaciones binaria |
|---------------|----------------------|-----------------------|
| 2023-10-02    | 1                    | 4                     |
| 2023-10-20    | 15                   | 4                     |
| 2023-10-31    | 22                   | 5                     |
| 2023-10-07    | 22                   | 4                     |

La lineal le gana a la binaria solamente al buscar 2023-10-02, porque necesitó 1 comparación contra 4 de la binaria. Esto pasa porque esa fecha está en la posición 0, o sea es el primer elemento de la lista, y la lineal empieza justo por ahí, así que es su mejor caso. La binaria en cambio no empieza por el principio sino por el medio, y tiene que ir descartando mitades hasta llegar al inicio de la lista, por eso hizo 4. En ninguna de las cuatro fechas empataron.

### Pregunta 2

Con 22 fechas, el peor caso de la lineal es 22 comparaciones, que pasa cuando la fecha está de última (como 2023-10-31) o cuando no existe (como 2023-10-07). Lo comprobé buscando fechas que no existen y la lineal siempre dio 22.

El peor caso de la binaria es 5 comparaciones. Lo comprobé porque al buscar todas las fechas que sí existen el máximo fue 5 (por ejemplo con 2023-10-31), y al buscar fechas que no existen como 2023-10-14, 2023-10-15 y 2023-11-01 también dio 5. Ninguna búsqueda dio 6 o más. Esto coincide con la calculadora de la sesión: se divide 22 entre 2 hasta llegar a 0 (22, 11, 5, 2, 1) y salen 5 divisiones.

### Pregunta 3

Cuando ejecuté en Python `"2023-10-09" < "2023-10-16"` me dio `True`, y cuando ejecuté `"31/10/2023" < "02/11/2023"` me dio `False`.

Python compara los textos caracter por caracter de izquierda a derecha, parando en el primer caracter que sea distinto. Con el formato AAAA-MM-DD lo primero que se compara es el año, luego el mes y luego el día, que es el mismo orden de importancia de una fecha, entonces el orden alfabético del texto coincide con el orden cronológico. Por eso la lista de fechas queda ordenada y se puede usar la binaria.

Con DD/MM/AAAA pasa lo contrario: lo primero que se compara es el día. En el segundo ejemplo, el 31/10/2023 es anterior al 02/11/2023 en la vida real, pero Python dice que no porque compara el "3" con el "0" y el "3" es mayor. Entonces la lista no quedaría ordenada por fecha y la binaria fallaría, podría decir que una fecha no existe aunque sí esté.

### Pregunta 4

La lista tasas está ordenada de menor a mayor porque en 2023 el córdoba se deslizaba un poco cada día, o sea que el tipo de cambio subía todos los días. Como las fechas van avanzando en orden, las tasas también van subiendo en orden.

Si el registro fuera de un mes de 2025 no tendría sentido buscar una fecha a partir de una tasa, porque desde 2024 el BCN mantiene el tipo de cambio fijo. Eso significa que todas las tasas serían el mismo número repetido, entonces una tasa no identifica a un solo día: la misma tasa le correspondería a todas las fechas del mes y no podríamos saber cuál fecha es la que se quiere. Además, una lista con todos los valores iguales no sirve para ir descartando mitades.

### Pregunta 5

Con unas 2,600 fechas:

- Lineal: 2,600 comparaciones en el peor caso, porque revisa todos los elementos.
- Binaria: 12 comparaciones en el peor caso. Dividiendo 2,600 entre 2 varias veces (2600, 1300, 650, 325, 162, 81, 40, 20, 10, 5, 2, 1) salen 12 divisiones. Lo comprobé también con un while en Python y dio 12.

Se nota que la lineal creció muchísimo (de 22 a 2,600) y la binaria casi no cambió (de 5 a 12).

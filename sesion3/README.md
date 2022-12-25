# Tipos de objetos en Python
En Python todo son objetos. Tenemos los siguientes tipos de datos:

* Enteros
* Decimales
* Cadenas de texto
* Booleanos
* Listas
* Tuplas
* Diccionarios
* Conjuntos

## Dinamismo
Python sabe identificar el tipo de dato de forma dinámica. Podemos saber qué tipo de dato es un objeto usando type(objeto).

```py
print(type(a))
# salida: <class 'int'>

a = 'h'
print(type(a))
# salida: <class 'str'>


a = 1.2
print(type(a))
# salida: <class 'float'>

```

## Inmutabilidad
Los valores de algunos tipos de datos en Python son inmutables. 

Si asignamos el valor 5 a una variable, guardará el valor en una dirección de memoria y la variable apuntará a ese valor.

Si modifico el valor de a y lo cambio por 6, ahora la variable apunta a otra dirección de memoria.

```py
a = 5
print(id(a))
# salida: 4487598456
print(getsizeof(a))

a = 6
print(id(a))
# salida: 4561363352

a = 5
print(id(a))
#salida: 4561363320

```

### Tipos de datos inmutables
* Números: 1, 1.3,...
* Cadenas de texto: 'texto'
* Tuplas: tupla = (valor1, valor2,...)

Si intentamos cambiar sus valores, vamos a obtener un error. Por ejemplo:
```py
saludo = 'hola'
saludo[0] = 'f'
# salida: TypeError: 'str' object does not support item assignment
```

Sí podemos asignar una nueva cadena de texto, pero se guardará en otra zona de memoria.

## Tipos de datos mutables
* **Listas**: lista = [valor1, valor2, ...]
  
* **Diccionarios**: diccionario = {clave1: valor1, clave2: valor2,...}
  * Acceder a un valor: diccionario['clave']
  * Modificar un valor: diccionario['clave'] = nuevoValor

* **Conjunto** (set: no tiene valores duplicados. Si los hay, los elimina): conjunto = {1, 2, 3, 4}


## Tipos de datos y sus métodos
* **Objetos**
  * type(): devuelve el tipo de dato
  * getsizeof(): devuelve el tamaño de la variable

* **Números**

* **Cadenas de texto**
  * upper(): convierte a mayúsculas todas las letras
  * lower(): convierte a minúsculas todas las letras
  * capitalize(): convierte a mayúscula la primera
  * title(): convierte a mayúscula la primera de cada palabra
  * count(): devuelve el número de veces que aparece una subcadena de texto
  * find(): devuelve el índice en el que aparece la subcadena. Si no aparece, devuelve -1
  * rfind(): igual que find pero empezando por el final
  * isdigit(): devuelve True si todos los elementos de la cadena son números
  * isalnum(): True si todos los caracteres son alfanuméricos
  * isalpha(): True si todos los caracteres son alfabéticos
  * islower(), isupper(), istitle(), isspace()
  * startswith(): True si la cadena empieza con la subcadena indicada
  * endswith(): True si la cadena acaba con la subcadena indicada
  * split(): separa una cadena por sus espacios y devuelve una lista
  * join(): une todos los elementos de una cadena de texto a partir del caracter indicado
  * strip(): borra todos los espacios o los caracteres indicados por delante y detrás de una cadena
  * replace(): reemplaza una subcadena por otra

* **Booleanos**

* **Listas**
  * len(): devuelve la longitud de la tupla
  * append(): añade elementos al dinal de la lista
  * insert(): agrega un elemento en una posición concreta de la lista (0: primera posición, -1: penúltima posición, fuera de rango: al final de la lista)
  * pop(): extrae un elemento y lo borra
  * remove(): elimina el elemento de la lista con el valor indicado
  * clear(): elimina todos los elementos de la lista, la vacía
  * extend(): une una lista a otra
  * count(): cuenta el número de veces que aparece un ítem
  * index(): devuelve el índice en el que está un elemento
  * reverse(): le da la vuelta a la lista
  * sort(): ordena una lista por valor de menor a mayor

* **Tuplas**
  * len(): devuelve la longitud de la tupla
  * index(): busca un elemento y devuelve su índice
  * count(): cuenta el número de veces que aparece un elemento en la tupla

* **Conjuntos**
  * add(): añade un elemento
  * discard(): borra el elemento con el valor indicado
  * copy(): devuelve una copia del conjunto
  * clear(): borra todos los elementos
  * isdisjoint(): comprueba si es disjunto
  * issubset(): comprueba si es subconjunto
  * issuperset(): comprueba si contiene un subconjunto
  * union(): une conjuntos. ( Operador: | )
  * update(): une un conjunto a otro dentro del propio conjunto
  * difference(): encuentra los elementos no comunes de dos conjuntos. ( Operador: - )
  * difference_update(): guarda en el conjunto los elementos no comunes de dos conjuntos
  * intersection(): devuelve un conjunto con la intersección de otros dos. ( Operador: & )
  * intersection_update()
  * symmetric_difference(): devuelve todos los elementos no comunes entre dos conjuntos. ( Operador: ^ )

* **Diccionarios**
  * get(): busca un elemento por su clave
  * keys(): genera una lista con las claves del diccionario
  * values(): genera una lista con los valores del diccionario
  * items(): genera una lista con los pares clave-valor
  * pop(): extrae un registro por su clave y lo elimina
  * clear(): borra todos los elementos

* **Pilas**
  * append(): añadie elementos al final de la pila
  * pop(): extrae el último elemento y eliminarlo 

* **Colas ( deque() )**
  * append(): añade elementos al final de la pila
  * popleft(): extrae el primer elemento de la cola

## Librería Math
* ceil(): redondea hacia arriba
* floor(): redondea hacia abajo
* lcm(): devuelve el mínimo común múltiplo
* trun(): elimina la parte decimal y deja solo la parte entera
* pow(x, y): devuelve x elevado a y
* sqrt(): raíz cuadrada
* pi: número pi
* e: número e

## Operadores 
* Sumar: +
* Restar: -
* Multiplicar: *
* Dividir: /
* Dividir enteros: //
* Calcular la potencia: **
* Calcular el módulo: %


### Relacionales
* Igual que: ==
* Distinto que: !=
* Mayor que: >
* Menor que: <
* Mayor o igual que: >=
* Menor o igual que: <=
  
### Lógicos
* Devuelve True si se cumplen todas las condiciones: and
* Devuelve True si se cumple alguna condición: or
* Niega el valor: not

### Asignación
* Asignar un valor: =
* Sumar un valor y asignarlo a la variable: +=
* Restar un valor y asignarlo a la variable: -=
* Multiplicar un valor y asignarlo a la variable: *=
* Dividir un valor y asignarlo a la variable: /=
* Devolver el módulo  y asignarlo a la variable: %=
* Calcular la potencia y asignarlo a la variable: **=



## FUENTES

https://docs.hektorprofe.net/python/
https://docs.python.org/es/3/library/math.html

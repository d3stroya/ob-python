# Estructuras de control de flujo
Guían la ejecución del programa:
* Si se cumplen unas condiciones
* Mientras se cumplan unas condiciones

Normalmente la condición va a consistir en una variable, un operador y un valor:
```py
a == 5
b < 3
c != null and c < 100
d == 7 or e = 9
```

## Condicional
Utiliza **if** seguido de la condición y dos puntos. Debajo, identadas, las acciones.

Podemos combinar varios operadores dentro de la condición.

También podemos combinar varias combinaciones con **elif**.

E incluso definir una acción distinta cuando no se cumpla ninguna condición.

```py
# if <condicion>:
#    <acciones>

if a > 0 and b > 0:
    print("a y b son mayores que 0") 
elif a > 0 or b > 0:
    print("solo una variable es mayor que 0")
else:
    print("ninguna variable es mayor que 0")

```

## Bucle foreach (for ... in ...)
Recorre un valor, repitiendo la ejecución mientras no se llegue al final de ese valor (puede ser un string, un array,...).  Iteran un número de veces predefinido.

La palabra reservada **break** permite parar la iteración cuando se cumple una condición. 

Por su parte, **continue** se salta el bloque de código que falte por ejecutar y salta directamente a la siguiente iteración.

```py
for <variable> in <iterable>:
    <acciones>

text = 'Python'
for i in text:
    print(i)
    if i == h:
        break

for i in text:
    if i == 'h':
        continue
    print(i)


```

## Bucles while
Ejecuta las acciones indicadas mientras se cumpla la condición. Iteran un número de veces predefinido.

Es importante incrementar o aumentar la variable para no crear un bucle infinito. Es decir, el while debe ser falso en algún momento, debe terminar después de X iteraciones.

La palabra reservada **break** permite parar la iteración cuando se cumple una condición. 
```py
while <condicion>:
    <acciones>

count = 5
while count > 0:
    print(count)
    count -= 1

count2 = 5
while count2 > 0:
    print('Count2 = ', count2)
    count2 -= 1
    if count2 == 2:
        break
```

## Swhitch case
Es nuevo en Python y evita un uso repetitivo de sentencias if - elif. Ofrece unas acciones para distintas condiciones:

```py
match <variable>:
    case <condición 1>:
        <acciones 1>
    case <condición 2>:
        <acciones 2>
    ...

day = 'Saturday'

match day:
    case 'Saturday':
        print('It`s your free day, enjoy!')
    case 'Sunday':
        print('It`s sunday')
    case 'Monday':
        print('Work to do!')
```

## zip()
Crea una lista que contiene a otras que se pasen por parámetro. Es como una cremallera que junta dos listas. Es muy útil para iterar a la vez varias listas.

```py
students = ['Laura', 'Álvaro', 'Esther', 'Enrique']
points = [10, 23, 34, 21]

for student, point in zip(students, points):
    print(student, ' has ', point, ' points')
```

## enumerate()
Permite añadir el índice de cada elemento iterado.

## Referncias
https://ellibrodepython.com/estructuras-control-python
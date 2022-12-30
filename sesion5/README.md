# Funciones
Permiten escribir código reutilizable, tanto en el mismo proyecto como en proyectos distintos.

Una función está pensada para hacer una única tarea y tenrdá un nombre acorde a la tarea que realiza.

```py
def <nombreFunción>(<parámetros>):
    acciones
```

Python necesita interpretar primero las funciones antes de poder ejecutarlas. Es decir, hay que definir la función antes de llamarla.

```py
def miFuncion():
    pass

miFuncion()
```

Cuando el intérprete encuentra una función, paraliza la ejecución del programa y salta al cuerpo de la función. Cuando acaba, sigue la ejecución del programa por donde iba.

## Parámetros
Son variables que usan las funciones y van entre los paréntesis de la función.
```py
def misParametros(nombre):
    print("Mi parametro nombre es: ", nombre)
```
## Funciones con variables
También podemos crear variables dentro de las funciones. Estas variables solo son accesibles desde dentro de la función, que es su ámbito; no podemos llamarlas desde fuera de la función. Si queremos llamarla desde fuera, tenemos que crearla como una variable global (fuera de la función) en lugar de declararla en el ámbito local de la función.


```py
def saludo(nombre):
    texto = 'Hola, '
    print(texto, nombre)
```

**Variable shadowing**: Si tenemos una variable global y la declaramos de nuevo dentro de una función, prevalece la local.
```py
temperatura = 12

def tPoloNorte():
    temperatura = -42
    print(temperatura)
```

**global**: es una palabra reservada que permite manipular una variable global desde dentro de una función.
```py
temperatura = 12

def tPoloNorte():
    global temperatura  # la variable global pasa a tener el valor de -42
    temperatura = -42
    print(temperatura)
```

**Parámetros opcionales**: Python permite crear parámetros opcionales a los que asignamos valores por defecto. No puede haber después ningún parámetmro obligatorio. Si un parámetro es opcional, siempre será el último o irá seguido de otros parámetros opcionales. Además, podemos modificar el valor de un parámetro opcional sin necesidad de mantener el orden escribiendo la variable, un igual y el valor.
```py
def usuario(estado='Online'):
    print(estado)
```

## Parámetros variables
Designa un número variable de parámetros. Lo usamos escribiendo *args como parámetro, que se convertirá en una lista
```py
def suma(*args):
    res = 0
    for arg in args:
        res += arg
    print(res)
```

También podemos usarlo con pares clave-valor (diccionarios) con la expresión **kwargs.

## return
Es la expresión para indicar el valor que devuelve la función
```py
def multiplicar(a, b):
    return a * b
````

Podemos devolver un valor o varios (devuelve una tupla).

```py
def operaciones(a, b):
    return a + b, a - b, a * b, a / b

# Devuelve (10, 0, 25, 1.0)
```

## Funciones lambda
Simplifican el código de las funciones. Se declaran asignándolas a una variable y con la palabra reservada lambda seguida de los parámetros, dos puntos y las acciones.
```py
<variable> = lambda <parametros> : <acciones>

multiplicarLambda = lambda a, b : a * b

```
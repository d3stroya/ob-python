# Características de Python

## Dinamismo
Python sabe identificar el tipo de dato de forma dinámica.
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
Los valores en Python son inmutables. 

Si asignamos el valor 5 a una variable, guardará el valor en una dirección de memoria y la variable apuntará a ese valor.

Si modifico el valor de a y lo cambio por 6, ahora la variable apunta a otra dirección de memoria.

```py
a = 5
print(id(a))
# salida: 4487598456

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
* Listas: lista = [valor1, valor2, ...]
  * append(): añade elementos al dinal de la lista
  * remove(): elimina elementos
* Diccionarios: diccionario = {clave1: valor1, clave2: valor2,...}
  * Acceder a un valor: diccionario['clave']
  * Modificar un valor: diccionario['clave'] = nuevoValor
  * Extraer valor de elemento y eliminar el elemento: diccionario.pop('clave')
* Conjunto (set: no tiene valores duplicados. Si los hay, los elimina): conjunto = {1, 2, 3, 4}
  * Unión de conjuntos: a | b
  * Intersección: a & b
  * Diferencia simétrica: a ^ b



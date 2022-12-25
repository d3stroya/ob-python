# 1. Datos inmutables
from sys import getsizeof


print('1. TIPOS DE DATOS INMUTABLES')
a = 5
print('Posición en memoria: ', id(a))

a = 6
print('Posición en memoria: ', id(a))

a = 5
print('Posición en memoria: ', id(a))

saludo = 'hola'
#saludo[0] = 'f'

# 2. Datos mutables
print('2. TIPOS DE DATOS MUTABLES')

# 2.1. Listas
print('2.1. LISTAS')

lista = [1, 2, 3]
print(lista)

lista.append(4)
print(lista)

lista.remove(2)
print(lista)

lista[0] = 9
print(lista)

letras = ['a', 'b', 'c']

lista.append(letras)
print(lista)

# 2.2. Diccionarios
print('2.2. DICCIONARIOS')

diccionario = {
    'clave1': 'valor1', 
    'clave2': 'valor2'
}

print(diccionario)
print(diccionario['clave1'])
diccionario['clave1'] = 1
print(diccionario['clave1'])

personaje = {
    'nombre': 'Francesca',
    'apodo': 'Franky',
    'apellido': 'Doyle',
    'edad': 31,
    'situacion': 'reculsa'
}
print(personaje)
personaje.pop('situacion')
print(personaje)

# 2.3. Conjuntos (set)
print('2.3. CONJUNTOS')

conjunto = {1, 2, 3, 2, 4}
print(conjunto)

conjunto2 = {2, 4, 6, 8}
print('Unión: ', conjunto | conjunto2)
print('Intersección: ', conjunto & conjunto2)
print('Diferencia:', conjunto - conjunto2)
print('Diferencia simétrica:', conjunto ^ conjunto2)

# 3. Dinamismo
print('3. DINAMISMO')
print(type(a))
print(getsizeof(a))

a = 'h'
print(type(a))
print(getsizeof(a))


a = 1.2
print(type(a))
print(getsizeof(a))

# TODO: Algunos ejercicios --> https://docs.hektorprofe.net/python/metodos-de-las-colecciones/ejercicios/



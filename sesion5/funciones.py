# Definición de funciones
def miFuncion():
    print("hola desde miFuncion")

    for i in range(1, 6):
        print(i)

print("antes")
miFuncion()
print("después")


# Funciones con parámetros
def imprimeNombre(nombre):
    print(nombre)

imprimeNombre("Franky")

def saludo(nombre, apellido):
    print("Hola, ", nombre, apellido)

saludo('Franky', 'Doyle')

# Funciones con variables
def saludo(nombre):
    texto = 'Hola, '
    print(texto, nombre)

saludo('Franky')

# Variable shadowing
temperatura = 12
print('Variable global: ', temperatura)

def tPoloNorte():
    #global temperatura
    temperatura = -42
    print('Variable local: ', temperatura)

tPoloNorte()

print('Variable global: ', temperatura)

def usuario(nombre, alias, seguidores=0, estado='Online'):
    print(nombre, '(' + alias + ') con ', seguidores, 'seguidores está ', estado)

usuario('Bridget', 'Gidge', 86392)
usuario('Joan', 'callMeGovernor', estado='Offline')

# Parámetros variables
def suma(*args):
    res = 0
    for arg in args:
        res += arg
    print(res)

suma(1, 2, 3, 4, 5, 6, 7)

def coche(**kwargs):
    print(kwargs)
    #for key, value in kwargs.items():
    #    print(key , ': ', value)

coche(modelo='Golf', alias='golfy', color='rojo', ac=True)
coche(modelo='Clio', alias='clippy')

# Return
def multiplicar(a, b):
    return a * b

print(multiplicar(5, 5))

def operaciones(a, b):
    return a + b, a - b, a * b, a / b

print(operaciones(5, 5))

# Funciones lambda
multiplicarLambda = lambda a, b : a * b

print('Función lambda: ', multiplicar(3, 3))
# 1. Condicionales
print('1. CONDICIONALES')

# Condicional simple
a = 6

if a % 2 == 0:
    print(a, "es par") 

# Condicional doble
b = 5
c = 8

if b % 2 == 0:
    print(b, "es par") 
elif c > 0:
    print(b, "es mayor que 0")

# Condicional y excepción
if b % 2 == 0:
    print (b, "es par")
else:
    print(b, "es impar")   

# Condicional combinando operadores
if a > 0 and b > 0:
    print("a y b son mayores que 0") 
elif a > 0 or b > 0:
    print("solo una variable es mayor que 0")
else:
    print("ninguna variable es mayor que 0")

# Operador ternario
print('Esto es un operador ternario' if a > 0 else 'a es negativo')

# 2. Bucle for
print('2. BUCLE FOR')

for i in range(10):
    print(i)

names = ['Franky', 'Bridget', 'Tess']
for name in names:
    print(name)

text = 'Python'
for i in text:
    print(i)

for i in text:
    if i == 'h':
        continue
    print(i)

print('Imprime Python al revés: ')
for i in text[::-1]:
    print(i)

print('Imprime números pares entre el 0 y el 9:')
for i in range(10)[::2]:
    print(i)

# Imagina que tienes invitados en casa y todos te piden un vaso de agua.
def servirAgua():
    print("Coger vaso")
    print("Abrir botella de agua")
    print("Echar agua al vaso")
    print("Colocar el vaso en la mesa frente al invitado")

invitados = ['Laura', 'Álvaro', 'Esther', 'Enrique']

for invitado in invitados:
    print()
    print("Preparando vaso para", invitado)
    servirAgua()

matrix = [
    [1, 3, 5],
    ['a', 'b', 'c']
]

for i in matrix:
    #print(i)
    for j in i:
        print(j)
        if j == 'b':
            break

# 3. Bucles while
print('3. BUCLE WHILE')
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

# Dibuja un árbol de navidad
x = 7
y = 1
z = 2

while x > 0:
    print(' ' * x + '*' * y + ' ' * x)
    x -= 1
    y += 2

while z > 0:
    print(' ' * 6 + '| ' * 2 + ' ' * 6)
    z -= 1

# Fibonacci
a, b = 0, 1


while b < 20:
    print(b)
    a, b = b, a + b

# Switch case
print('4. SWITCH CASE')

day = 'Saturday'

match day:
    case 'Saturday':
        print('It`s your free day, enjoy!')
    case 'Sunday':
        print('It`s sunday')
    case 'Monday':
        print('Work to do!')

# 4. Zip
print('4. ZIP')

students = ['Laura', 'Álvaro', 'Esther', 'Enrique']
points = [10, 23, 34, 21]

for student, point in zip(students, points):
    print(student, ' has ', point, ' points')


# 5. Enumerate
print('5. ENUMERATE')
for i in enumerate(students):
    print(i)
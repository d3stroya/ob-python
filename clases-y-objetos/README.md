# Clases y objetos
Definición de una clase:
```py
class <NombreClase>:
    <atributos>
    <métodos>
```

Cuando queremos que una variable no se modifique, le añadimos un guion bajo al principio:
```py
_nariz = True
```

Instanciar una clase (crear un objeto):
```py
<nombreObjeto> = <NombreClase>() 
```

Acceder a métodos y atributos de la clase:
```py
<nombreObjeto>.<atributo>
<nombreObjeto>.<método>
```

Ejemplo:
```py
class MrPotato():
    # Atributos
    numOjos = 2
    numBrazos = 2
    numZapatos = 2
    nariz = True

    # Métodos
    def caminar():
        print('Mr Potato en movimiento')
```

## Self
El parámetro self permite referirnos a métodos o atributos de la propia clase:
```py
    def quitarBrazo(self):
        if(self.numBrazos > 0):
            self.numBrazos -= 1
        else:
            print('Mr. Potato no tiene brazos, así que no le puedes quitar ninguno.')
    
    def agregarBrazo(self):
        if(self.numBrazos < 2):
            self.numBrazos += 1
        else:
            print('Mr. Potato ya tiene 2 brazos, no puedes añadir más.')

```
## Clases estáticas
Comparten un mismo espacio de memoria, así que si se modifica un valor, se modifica en toda la clase.

En las clases dinámicas se crean objetos en espacios de memoria distintos, por lo que mrPotato1 es indepediente a mrPotato2; si cambio un valor en mrPotato1 no se cambia en mrPotato2.

Las clásicas dinámicas utilizan self. Las dinámicas no usan self, sino el nombre de la clase.

```py
class Estatica():
    contador = 0

    def incrementar():
        contador += 1
```

Las clases estáticas pueden usarse como listas de opciones.
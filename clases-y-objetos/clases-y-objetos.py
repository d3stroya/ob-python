# 1. Crear un clase
class MrPotato():
    # Atributos
    numOjos = 2
    numBrazos = 2
    numZapatos = 2
    nariz = True

    # Métodos
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

# 2. Crear un objeto
mrPotato1 = MrPotato()

# 3. Acceder a un método
print(mrPotato1.numBrazos)

# 4. Acceder a un método
mrPotato1.quitarBrazo()

print(mrPotato1.numBrazos)
mrPotato1.quitarBrazo()
print(mrPotato1.numBrazos)
mrPotato1.quitarBrazo()


# 4. Clase estática
print('CONTADOR')
class Estatica():
    contador = 0

    def incrementar():
        Estatica.contador += 1

print(Estatica.contador)
Estatica.incrementar()
print(Estatica.contador)
Estatica.incrementar()
print(Estatica.contador)
Estatica.incrementar()
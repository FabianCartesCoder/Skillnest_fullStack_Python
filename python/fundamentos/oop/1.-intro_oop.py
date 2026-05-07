# Creación de la clase usuario - Entidad
class Usuario:
    def __init__(self):
        self.nombre = "Nariyoshi"
        self.apellido = "Miyagi"
        self.email = "miyagi@codingdojo.la"
        self.limite_credito = 30000
        self.saldo_pagar = 0
# Instancias de una clase
miyagi = Usuario()
daniel = Usuario()
fabian = Usuario()

#Accedemos a los atributos de la instancia
print(miyagi.nombre) #Imprime: Nariyoshi
print(miyagi.apellido) #Imprime: Nariyoshi
print(miyagi.email) #Imprime: miyagi@codingdojo.la
print(miyagi.limite_credito) #Imprime: 30000
print(miyagi.saldo_pagar) #Imprime: 0

# Nuevos valores asignados a atributos de la instancia
daniel.nombre = "Daniel"
daniel.apellido = "Larusso"
daniel.email = "daniel@gmail.com"
daniel.limite_credito = 50000
daniel.saldo_pagar = 10000

print(daniel.nombre) #Imprime: Daniel
print(daniel.apellido) #Imprime: Larusso
print(daniel.email) #Imprime: daniel@gmail.com
print(daniel.limite_credito) #Imprime: 50000
print(daniel.saldo_pagar) #Imprime: 10000


fabian.nombre = "Fabian"
fabian.apellido = "Cartes"
fabian.email = "fabian@gmail.com"
fabian.limite_credito = 40000
fabian.saldo_pagar = 5000

print(fabian.nombre) #Imprime: Fabian
print(fabian.apellido) #Imprime: Cartes
print(fabian.email) #Imprime: fabian@gmail.com
print(fabian.limite_credito) #Imprime: 40000
print(fabian.saldo_pagar) #Imprime: 5000
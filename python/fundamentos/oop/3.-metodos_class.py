class Usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = 30000
        self.saldo_pagar = 0

    def hacer_compra(self, monto):  #recibe como argumento el monto de la compra
        self.saldo_pagar += monto   #el saldo a pagar del usuario aumenta en la cantidad del valor recibido

    def aumentarCredito(self, aumento):
        self.limite_credito += aumento

    def cambiarCorreo(self, email):
        self.email = email

miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la")
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la")

miyagi.hacer_compra(2000)
print(f"Primera compra de: {miyagi.nombre}: {miyagi.saldo_pagar}")
miyagi.hacer_compra(300)
print(f"Segunda compra de: {miyagi.nombre}: {miyagi.saldo_pagar}")
# Imprimir cuanto credito de queda a Miyagi
print(f"Credito disponible de: {miyagi.nombre}: {miyagi.limite_credito - miyagi.saldo_pagar}")

# Compras de Daniel 2 compras y muestra saldo apagar--------
print("-----------------Compras de Daniel-----------------")
daniel.hacer_compra(45)
print(daniel.saldo_pagar)

# Tarea
'''
Crear un nuevo metodo que permita aumentar el limite de credito.
Imprimir el nuevo limite de credito.

2.- Crear un metodo que permita cambiar el correo de instancia.
Mostrar el nuevo correo.
'''
miyagi.aumentar_credito(2000)
print(f"Nuevo limite de credito de: {miyagi.nombre}: {miyagi.limite_credito}")

miyagi.cambiarCorreo("miyagi@codingdojo.la")
print(f"Nuevo correo de: {miyagi.nombre}: {miyagi.email}")
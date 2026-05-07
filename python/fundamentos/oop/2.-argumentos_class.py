class Usuario:
   def __init__(self, nombre, apellido, email, limite_credito, saldo_pagar):
       self.nombre = nombre
       self.apellido = apellido
       self.email = email
       self.limite_credito = limite_credito
       self.saldo_pagar = saldo_pagar

# Creación de las instancias
miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la", 30000, 0)
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la", 50000, 10000)
fabian = Usuario("Fabian", "Cartes", "fabian@codingdojo.la", 40000, 5000)
# Imprimimos los valores
print(miyagi.nombre) #Imprime: Nariyoshi
print(daniel.nombre) #Imprime: Daniel
print(fabian.nombre) #Imprime: Fabian

#--------------------------------------------------------------------------------------
# Tarea rápida
'''
Crear una clase ESTUDIANTE, y asignarle los siguientes atributos:
(rut, nombre, apellido, especialidad, fecha_nac)
- Crear 3 instancias para la clase con distintos estudiantes.
- Imprimir el nombre y  apellido concatenado + especialidad
'''
class Estudiante:
    def __init__(self, rut, nombre, apellido, especialidad, fecha_nac):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.especialidad = especialidad
        self.fecha_nac = fecha_nac

estudiante1 = Estudiante("23345678-9", "Juan", "Pérez", "Logistica", "24-10-2008")
estudiante2 = Estudiante("22765432-1", "María", "Gómez", "RR.HH", "15-05-2007")
estudiante3 = Estudiante("21678912-3", "Carlos", "Rodríguez", "Programación", "20-08-2006")

print(f"{estudiante1.nombre} {estudiante1.apellido} - {estudiante1.especialidad}")
print(f"{estudiante2.nombre} {estudiante2.apellido} - {estudiante2.especialidad}")
print(f"{estudiante3.nombre} {estudiante3.apellido} - {estudiante3.especialidad}")

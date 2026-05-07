#Atributos, metodos de clase, metodos estaticos

#DEFINICION DE LA CLASE
class Estudiante:
    #Atributo de Clase
    colegio = "Liceo Vate Vicente Huidobro"
    #Lista en donde esten todos los estudiantes
    estudiantes = []

    #Metodo constructor
    def __init__(self, nombre, nota):
        #Atributos de instancia
        self.nombre = nombre
        self.nota = nota
        
        #Agregar elementoss a la lista de estudiantes (objeto)
        Estudiante.estudiantes.append(self)

    #Metodo de instancia
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")

    #Metodo de clase
    # Usa "CLS" porque trabaja con la informacion de la clase, no de la instancia
    @classmethod
    def cambiar_colegio(cls, nuevo_colegio):
        cls.colegio = nuevo_colegio
        print(f"El colegio ha sido cambiado a: {cls.colegio}")

    @classmethod #Contar la cantidad de estudiantes existentes
    def cantidad_estudiantes(cls):
        return len(cls.estudiantes)
    
    #Metodo estatico
    #Este no usa CLS ni SELF porque no trabaja con la informacion de la clase ni de la instancia, es independiente
    @staticmethod
    def es_aprobado(nota):
        if nota >= 4.0:
            return True
        else:
            return False
        
#Creacion de objetos (Instanccias)
e1 = Estudiante("Donovan", 4.0)
e2 = Estudiante("Randy", 6.7)
e3 = Estudiante("Martin", 3.9)

# Uso de metodos de instancia
print("== METODO DE INSTANCIA ==")
e1.mostrar_info()
print()
e2.mostrar_info()
print()

#Usar atributos de clase
print("== ATRIBUTO DE CLASE ==")
print(f"El colegio de {e1.nombre} es: {e1.colegio}")
print(f"El colegio de {e2.nombre} es: {e2.colegio}")
print()

#Uso de metodos de clase
print("== METODO DE CLASE ==")
Estudiante.cambiar_colegio("Purkuyen")
e1.colegio = "VVH" # mODIFICA EL ATRIBUTO DE INSTANCIA EN LA CLASE, NO EN LA INSTANCIA
print(f"El colegio de {e2.nombre} es: {e2.colegio}")
print()

#Contar la cantidad de estudiantes
print("== CANTIDAD DE ESTUDIANTES ==")
print(f"Total de estudiantes: {Estudiante.cantidad_estudiantes()}")
print()

#Metodo estatico
print("== METODO ESTATICO ==")

print(f"¿{e1.nombre} aprueba?")
print(Estudiante.es_aprobado(e1.nota))

print(f"¿{e2.nombre} aprueba?")
print(Estudiante.es_aprobado(e2.nota))

print(f"¿{e3.nombre} aprueba?")
print(Estudiante.es_aprobado(e3.nota))

def validador(user, password):
    if user == "matias123" and password == "matias123":
        print(f"Bienvenido, {user}!")
        return True
    else:
        print("Usuario o contraseña incorrectos.")
        return False
    
def enviarDatos():
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    validador(username, password)

enviarDatos()
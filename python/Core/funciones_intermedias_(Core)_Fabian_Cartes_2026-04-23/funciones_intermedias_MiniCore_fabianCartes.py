# 🎯 MINI DESAFÍO (nivel core)
datos = [
   {"nombre": "Carlos", "puntaje": 80},
   {"nombre": "María", "puntaje": 95},
   {"nombre": "Pedro", "puntaje": 70}
]

# 1. Cambiar el puntaje de Pedro a 75
datos[2]["puntaje"] = 75
print(f"Nombre: {datos[2]['nombre']} - {datos[2]['puntaje']}")

# 2. Crear función que imprima:
#    "Carlos obtuvo 80 puntos"

def imprimir_informacion(datos):
    for nombre in datos:
        print(f"{nombre['nombre']} obtuvo {nombre['puntaje']} puntos")

# 3. Crear función que reciba "nombre" o "puntaje" e imprima solo esos valores
def imprimir_valores(nombre):
    for nombre in datos:
        if nombre == "nombre":
            print(f"Nombre: {nombre} - Puntaje: {datos[1]["puntaje"]}")
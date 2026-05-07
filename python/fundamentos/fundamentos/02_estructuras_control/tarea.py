'''
Crear una función que reciba una lista de edades y clasifique a las personas en tres grupos: menores de edad, adultos y adultos mayores (60+).
 Debe mostrar la cantidad de personas en cada grupo.
'''
def contar_mayores_de_edad(edades):
    menores = 0
    adultos = 0
    adultos_mayores = 0
    for edad in edades:
        if edad >= 60:
            adultos_mayores += 1
        elif edad >= 18:
            adultos += 1
        else: 
            menores += 1
    return menores, adultos, adultos_mayores

def ejercicio6():
    edades_input = input("Ingrese cuantas edades desea ingresar: ")
    edades = []
    for _ in range(int(edades_input)):
        edad = int(input("Ingrese una edad: "))
        edades.append(edad)
    cantidad_mayores = contar_mayores_de_edad(edades)
    print(f"La cantidad de personas menores de edad es: {cantidad_mayores[0]}")
    print(f"La cantidad de personas mayores de edad es: {cantidad_mayores[1]}")
    print(f"La cantidad de personas adultas mayores es: {cantidad_mayores[2]}")

'''
Crear una función que reciba una lista de números y genere una nueva lista sin elementos repetidos.
 Luego debe mostrar la lista original y la lista resultante.
'''

def crear_lista_original(lista):
    lista_sin_repetidos = []
    for numero in lista:
        if numero not in lista_sin_repetidos:
            lista_sin_repetidos.append(numero)
    return lista_sin_repetidos
lista_original = [1, 2, 3, 4, 2, 5, 1, 6]
lista_resultante = crear_lista_original(lista_original)


def ejercicio():
    resultado = crear_lista_original(lista_original)
    print(f"Lista original: {lista_original}")
    print(f"Lista resultante sin elementos repetidos: {resultado}")
   

'''
Crear una función que reciba una lista de notas (decimales) y genere dos listas: una con aprobados (≥ 4.0) y otra con reprobados (< 4.0).
 Debe mostrar ambas listas y la cantidad de estudiantes en cada grupo.
'''

def separarnotas(lista_notas):
    aprobados = []
    reprobados = []
    for nota in lista_notas:
        if nota >= 4.0:
            aprobados.append(nota)
        else:
            reprobados.append(nota)
    return aprobados, reprobados

def mostrar_resultados():
    entrada = input("Ingrese las notas separadas por espacio: ")
    notas = []
    for nota in entrada.split():
        notas.append(float(nota))
    aprobados, reprobados = separarnotas(notas)
    print("Lista de aprobados:", aprobados)
    print("Cantidad de aprobados:", len(aprobados))
    print("Lista de reprobados:", reprobados)
    print("Cantidad de reprobados:", len(reprobados))


continuar = True
while continuar:
    opcion = input("\n--- Elige una opción: (1-3) (0 para salir) --- ")
    if opcion == "0":
        continuar = False
    elif opcion == "1":
        ejercicio6()
    elif opcion == "2":
        ejercicio()
    elif opcion == "3":
        mostrar_resultados()
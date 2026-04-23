# Funciones basicas 2

# Ejercicio 1
# Calcula experiencia
def multiplica_por_2(n):
    return [i * 2 for i in range(n + 1)]

def ejercicio1():
    resultado = multiplica_por_2(5)
    print(resultado)
    # Debe retornar: [0, 2, 4, 6, 8, 10]
# Debe retornar: [0, 2, 4, 6, 8, 10]

# Ejercicio 2
# Analiza publicaciones
def suma_y_resta(lista):
    suma = sum(lista)
    resta = lista[0] - lista[1]
    print(suma)

    return resta

def ejercicio2():
    resultado = suma_y_resta([10, 5])
    print(f"Resultado: {resultado}")
    # Imprime: 15 y retorna: 5
    resultado2 = suma_y_resta([20, 10])
    print(f"Resultado 2: {resultado2}")
    # Imprime: 30 y retorna: 10
    resultado3 = suma_y_resta([100, 50])
    print(f"Resultado 3: {resultado3}")
# Imprime: 235 y retorna: 5

# Ejercicio 3
# Puntaje ajustado
def sumatoria_menos_longitud(lista):
    suma = sum(lista)
    longitud = len(lista)
    return suma - longitud

def ejercicio3():
    resultado = sumatoria_menos_longitud([10, 5, 3, 7])
    print(f"Resultado: {resultado}")
    # Suma total = 25, longitud = 4, debe retornar: 21
    resultado2 = sumatoria_menos_longitud([1, 2, 3])
    print(f"Resultado 2: {resultado2}")
    # Suma total = 6, longitud = 3, debe retornar: 3
    resultado3 = sumatoria_menos_longitud([100, 50])
    print(f"Resultado 3: {resultado3}")
# Suma total = 25, longitud = 4, debe retornar: 21

# Ejercicio 4
# Ajusta visualizaciones
def valores_multiplicados_segundo(lista):
    if len(lista) < 2:
        print(len(lista))
        return []
    else:
        seEle = lista[1]
        nuevaLista = []
        for i in lista:
            nuevaLista.append(i * seEle)
            long = len(nuevaLista)
        print(long)
        return nuevaLista
def ejercicio4():
    result1 = valores_multiplicados_segundo([100, 3, 50, 20])
    print(result1)
    print()
    # Imprime 4 y retorna: [300, 9, 150, 60]
    result2 = valores_multiplicados_segundo([100])
    print(result2)
    # Imprime 1 y retorna: []


# Ejercicio 5
def valor_multiplicado_longitud(a, b):
    multList = []
    for i in range(b):
        multList.append(a * b)
        return multList

def ejercicio5():
    result1 = valor_multiplicado_longitud(5, 2)
    print(f"Resultado 1: {result1}")
    # debe retornar: [10, 10]
    result2 = valor_multiplicado_longitud(7, 5)
    print(f"Resultado 2: {result2}")
    # debe retornar: [35, 35, 35, 35, 35]

continuar = True
while continuar:
    opcion = input("\n--- Elige una opción: (1-15) (0 para salir) --- ")
    if opcion == "0":
        continuar = False
    elif opcion == "1":
        ejercicio1()
    elif opcion == "2":
        ejercicio2()
    elif opcion == "3":
        ejercicio3()
    elif opcion == "4":
        ejercicio4()
    elif opcion == "5":
        ejercicio5()
    
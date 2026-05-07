'''
Instrucciones generales

Deberá desarrollar un programa en Python que contenga un menú interactivo utilizando la estructura while, permitiendo
al usuario seleccionar distintas opciones para ejecutar funciones previamente definidas.

Cada opción del menú deberá llamar a una función diferente, la cual resolverá una situación
específica utilizando distintos tipos de datos como enteros, decimales, cadenas de texto, listas y diccionarios.

En aquellos casos donde sea necesario, deberá solicitar información al usuario mediante input().
Además, se deberá trabajar con arreglos (listas) para recorrer información utilizando ciclos for,
junto con estructuras condicionales como if, elif y else.

El programa deberá incluir una opción para salir correctamente del sistema.
-------------------------------------------------------------------------------------------------------
'''

'''
REQUISITOS OBLIGATORIOS
Su trabajo debe cumplir con lo siguiente:

Uso de funciones con parámetros
Uso de menú con ciclo while
Uso de input() para solicitar datos
Uso de listas (arreglos)
Uso de diccionarios
Uso de ciclos for
Uso de estructuras condicionales (if, elif, else)
Código ordenado, comentado y correctamente indentado
Opción de salida del programa (0. Salir)
'''

'''
-------------------------------------------------------------------------------------------------------
Ejercicios a desarrollar

Su programa deberá considerar las siguientes funciones:
'''
# Crear una función que reciba una lista de números enteros y muestre cuál es el número mayor y cuál es el menor.
def numeroMayorMenor(listado):
    menor = min(listado)
    mayor = max(listado)
    print(f"El número mayor es: {mayor} y el número menor es: {menor}")

def ejercicio1():
    limit = int(input("Ingrese la cantidad de números a ingresar: "))
    listadoNum = []
    i = 1
    while i <= limit:
        num = input("Ingrese un número entero con decimales: ")
        if "." in num:
            num = float(num)
        else:
            num = int(num)
        listadoNum.append(num)
        i += 1
    numeroMayorMenor(listadoNum)
# Crear una función que reciba una cadena de texto y cuente cuántas vocales contiene.
def contar_vocales(texto):
    vocales = "aeiouAEIOUáéíóúÁÉÍÓÚ"
    contador = 0
    for letra in texto:
        if letra in vocales:
            contador += 1
    return contador

def ejercicio2():
    texto = input("Ingrese una cadena de texto: ")
    cantidad_vocales = contar_vocales(texto)
    print(f"La cantidad de vocales en el texto es: {cantidad_vocales}")
    
# Crear una función que reciba una lista de nombres y muestre únicamente aquellos que tengan más de 5 letras.
def nombres_mas_de_cinco_letras(nombres):
    resultado = []
    for nombre in nombres:
        if len(nombre) > 5:
            resultado.append(nombre)
    return resultado

def ejercicio3():
    nombres = input("Ingrese una lista de nombres separados por comas: ").split(", ")
    nombres_filtrados = nombres_mas_de_cinco_letras(nombres)
    print("Nombres con más de 5 letras:")
    for nombre in nombres_filtrados:
        print(nombre.strip())

# Crear una función que reciba una lista de notas (números decimales), calcule el
# promedio e indique si el estudiante aprueba (promedio mayor o igual a 4.0).
def calcular_promedio(notas):
    if len(notas) == 0:
        return 0
    promedio = sum(notas) / len(notas)
    return promedio

def ejercicio4():
    notas_input = input("Ingrese cuantas notas desea ingresar: ")
    notas = []
    for _ in range(int(notas_input)):
        nota = float(input("Ingrese una nota: "))
        notas.append(nota)
    promedio = calcular_promedio(notas)
    print(f"El promedio es: {promedio:.2f}")
    if promedio >= 4.0:
        print("El estudiante aprueba.")
    else:
        print("El estudiante no aprueba.")
# Crear una función que reciba una lista de precios de productos y aplique un descuento del 10%,
# mostrando el valor original y el nuevo valor.
def aplicar_descuento(precios):
    precios_con_descuento = []
    for precio in precios:
        nuevo_precio = precio * 0.9
        precios_con_descuento.append((precio, nuevo_precio))
    return precios_con_descuento

def ejercicio5():
    cantidad = int(input("Cuantos precios desea ingresar? "))
    precios = []
    for i in range(cantidad):
        precio = float(input("Ingrese un precio: "))
        precios.append(precio)
    precios_descuento = aplicar_descuento(precios)
    print("Precio original - Precio con descuento:")
    for original, descuento in precios_descuento:
        print(f"{original:.2f} - {descuento:.2f}")
# Crear una función que reciba un número entero y determine si es par o impar.
def es_par_o_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"
def ejercicio6():
    numero = int(input("Ingrese un número entero: "))
    resultado = es_par_o_impar(numero)
    print(f"El número {numero} es {resultado}.")
# Crear una función que reciba una lista de edades y muestre cuántas personas son mayores de edad (18 años o más).
def contar_mayores_de_edad(edades):
    contador = 0
    for edad in edades:
        if edad >= 18:
            contador += 1
    return contador
def ejercicio7():
    edades_input = input("Ingrese cuantas edades desea ingresar: ")
    edades = []
    for _ in range(int(edades_input)):
        edad = int(input("Ingrese una edad: "))
        edades.append(edad)
    cantidad_mayores = contar_mayores_de_edad(edades)
    print(f"La cantidad de personas mayores de edad es: {cantidad_mayores}")
# Crear una función que reciba una lista de palabras y permita buscar
# cuántas veces aparece una palabra específica ingresada por el usuario.
def contar_palabra(palabras, palabra_buscada):
    contador = 0
    for palabra in palabras:
        if palabra == palabra_buscada:
            contador += 1
    return contador
def ejercicio8():
    palabras_input = input("Ingrese cuantas palabras desea ingresar: ")
    palabras = []
    for _ in range(int(palabras_input)):
        palabra = input("Ingrese una palabra: ")
        palabras.append(palabra)
    palabra_buscada = input("Ingrese la palabra que desea buscar: ")
    cantidad = contar_palabra(palabras, palabra_buscada)
    print(f"La palabra '{palabra_buscada}' aparece {cantidad} veces en la lista.")
# Crear una función que reciba una lista de números y genere
# una nueva lista que contenga únicamente los números positivos.
def filtrar_positivos(numeros):
    positivos = []
    for numero in numeros:
        if numero > 0:
            positivos.append(numero)
    return positivos

def ejercicio9():
    cantidad = int(input("Ingrese cuántos números desea ingresar: "))
    numeros = []
    for _ in range(cantidad):
        numero = float(input("Ingrese un número: "))
        numeros.append(numero)
    numeros_positivos = filtrar_positivos(numeros)
    print("Números positivos:")
    for numero in numeros_positivos:
        print(numero)
# Crear una función que reciba una lista de productos (utilizando diccionarios con nombre y stock)
# y muestre cuáles tienen un stock menor a 5 unidades.
def productos_con_stock_bajo(productos):
    productos_bajos = []
    for producto in productos:
        if producto["stock"] < 5:
            productos_bajos.append(producto)
    return productos_bajos
def ejercicio10():
    cantidad = int(input("Ingrese cuántos productos desea ingresar: "))
    productos = []
    for _ in range(cantidad):
        nombre = input("Ingrese el nombre del producto: ")
        stock = int(input("Ingrese el stock del producto: "))
        productos.append({"nombre": nombre, "stock": stock})
    productos_bajos = productos_con_stock_bajo(productos)
    print("Productos con stock menor a 5 unidades:")
    for producto in productos_bajos:
        print(f"{producto['nombre']} - Stock: {producto['stock']}")


continuar = True
while continuar:
    opcion = input("\n--- Elige una opción: (1-10) (0 para salir) --- ")
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
    elif opcion == "6":
        ejercicio6()
    elif opcion == "7":
        ejercicio7()
    elif opcion == "8":
        ejercicio8()
    elif opcion == "9":
        ejercicio9()
    elif opcion == "10":
        ejercicio10()



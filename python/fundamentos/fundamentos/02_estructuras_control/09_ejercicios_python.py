'''
1. Números Pares Dinámicos
Desarrolla un programa que solicite al usuario cuántos números pares desea ver ($n$).
El programa debe imprimir los primeros $n$ números pares positivos.
'''

def numerosDinamicos():
    n = int(input("¿Cuántos números pares deseas ver? "))
    for i in range(1, n + 1):
        print(i * 2)

'''
2. Verificador de Edad y Acceso
Pide al usuario su año de nacimiento. Calcula su edad y muestra si es mayor de edad (18+). 
Si tiene menos de 18, indica cuántos años le faltan para la mayoría de edad.
'''

def verificadorEdad():
    año_nacimiento = int(input("¿Cuál es tu año de nacimiento? "))
    año_actual = int(input("¿Cuál es el año actual? "))
    edad = año_actual - año_nacimiento
    if edad >= 18:
        print(f"Eres mayor de edad. Tienes {edad} años.")
    else:
        años_faltantes = 18 - edad
        print(f"Eres menor de edad. Te faltan {años_faltantes} años para la mayoría de edad.")

'''
3. Calculadora de Descuentos
Solicita el precio de un producto y la cantidad comprada.
Si el total supera los $100, aplica un 15% de descuento. Muestra el subtotal, 
el descuento aplicado y el total final.
'''

def calculadoraDescuentos():
    precio = float(input("¿Cuál es el precio del producto? "))
    cantidad = int(input("¿Cuánta cantidad deseas comprar? "))
    subtotal = precio * cantidad
    descuento = subtotal * 0.15 if subtotal > 100 else 0
    total = subtotal - descuento
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Descuento: ${descuento:.2f}")
    print(f"Total final: ${total:.2f}")

'''
4. Clasificador de Números
Pide un número al usuario e indica si es: Positivo-Par, 
Positivo-Impar, Negativo-Par, Negativo-Impar o Cero.
'''

def clasificadorNumeros():
    numero = int(input("Ingresa un número: "))
    if numero == 0:
        print("Cero")
    elif numero > 0:
        print("Positivo-Par" if numero % 2 == 0 else "Positivo-Impar")
    else:
        print("Negativo-Par" if numero % 2 == 0 else "Negativo-Impar")

'''
II. Iteraciones y Bucles (Intermedio)
5. Tabla de Multiplicar Personalizada
Solicita un número entero y muestra su tabla de multiplicar del 1 al 12, 
pero solo muestra los resultados que sean múltiplos de 3.
'''

def tablaMultiplicar():
    numero = int(input("Ingresa un número: "))
    for i in range(1, 13):
        resultado = numero * i
        if resultado % 3 == 0:
            print(f"{numero} x {i} = {resultado}")

'''
6. Sumatoria con Centinela
Crea un programa que pida números continuamente y los sume. El ciclo debe terminar cuando 
el usuario ingrese un número negativo. Al final, muestra la suma total (sin incluir el negativo).
'''

def sumatoriaCentinela():
    total = 0
    while True:
        num = int(input("Ingresa un número (negativo para terminar): "))
        if num < 0:
            break
        total += num
    print(f"Suma total: {total}")

'''
7. Contador de Vocales
Pide al usuario una frase o palabra. Utiliza un bucle para 
recorrer la cadena y contar cuántas vocales tiene en total.
'''

def contadorVocales():
    frase = input("Ingresa una frase o palabra: ")
    vocales = "aeiouáéíóuAEIOUÁÉÍÓU"
    cantidad = sum(1 for letra in frase if letra in vocales)
    print(f"Total de vocales: {cantidad}")

'''
8. Validación de Contraseña
Define una contraseña en una variable. Pide al usuario que la intente adivinar. 
Tienes un máximo de 3 intentos; si falla los 3, bloquea el acceso.
'''

def validacionContrasena():
    clave = "python123"
    intentos = 3
    while intentos > 0:
        entrada = input("Ingresa la contraseña: ")
        if entrada == clave:
            print("¡Acceso concedido!")
            break
        intentos -= 1
        if intentos > 0:
            print(f"Contraseña incorrecta. Te quedan {intentos} intentos.")
        else:
            print("Acceso bloqueado. Has agotado los 3 intentos.")

'''
III. Manejo de Arreglos / Listas (Avanzado)
9. Registro de Nombres
Crea un arreglo vacío. Pide al usuario que ingrese 5 nombres. 
Guárdalos en el arreglo y, al final, imprímelos en orden inverso al que fueron ingresados.
'''

def registroNombres():
    nombres = []
    for _ in range(5):
        nombre = input("Ingresa un nombre: ")
        nombres.append(nombre)
    print("Nombres en orden inverso:")
    for nombre in reversed(nombres):
        print(nombre)

'''
10. Promedio de Notas
Solicita al usuario cuántas notas desea ingresar. Almacena cada nota en un arreglo. 
Al finalizar, calcula y muestra el promedio, la nota más alta y la más baja.
'''

def promedioNotas():
    cantidad_notas = int(input("¿Cuántas notas deseas ingresar? "))
    notas = [float(input("Ingresa una nota: ")) for _ in range(cantidad_notas)]
    print(f"Promedio: {sum(notas)/len(notas):.2f}")
    print(f"Nota más alta: {max(notas):.2f}")
    print(f"Nota más baja: {min(notas):.2f}")

'''
11. Filtro de Arreglos
Dado un arreglo de números generado por el usuario, crea un nuevo arreglo que 
contenga solo los números que sean mayores a 50. Muestra ambos arreglos.
'''

def filtroArreglos():
    cantidad_numeros = int(input("¿Cuántos números deseas ingresar? "))
    numeros = [float(input("Ingresa un número: ")) for _ in range(cantidad_numeros)]
    filtrados = [num for num in numeros if num > 50]
    print(f"Arreglo original: {numeros}")
    print(f"Arreglo filtrado (mayores a 50): {filtrados}")

'''
12. Buscador de Elementos
Crea una lista de 10 ciudades. Pide al usuario que ingrese el nombre de una ciudad y 
el programa debe decir si la ciudad se encuentra en la lista y en qué índice (posición) está
'''

def buscadorElementos():
    ciudades = ["Santiago", "La Serena", "Coquimbo", "Chillán", "Temuco", "Concepción", "Valparaíso", "Antofagasta", "Iquique", "Puerto Montt"]
    ciudad = input("Ingresa el nombre de una ciudad: ").capitalize()
    if ciudad in ciudades:
        print(f"La ciudad {ciudad} se encuentra en la lista en el índice {ciudades.index(ciudad)}.")
    else:
        print(f"La ciudad {ciudad} no se encuentra en la lista.")

'''
IV. Retos de Lógica Combinada
13. Simulación de Inventario
Crea dos arreglos: uno para nombres_productos y otro para precios. Permite al usuario ingresar 3 productos con sus precios. Luego, muestra una lista formateada: Producto: [Nombre] - Precio: $[Valor].
'''

def simulacionInventario():
    nombres_productos, precios_productos = [], []
    for _ in range(3):
        nombre = input("Ingresa el nombre del producto: ")
        precio = float(input("Ingresa el precio del producto: "))
        nombres_productos.append(nombre)
        precios_productos.append(precio)
    print("\nLista de productos:")
    for nombre, precio in zip(nombres_productos, precios_productos):
        print(f"Producto: {nombre} - Precio: ${precio:.2f}")

'''
14. Generador de Lista de Compras
Usa un bucle while para que el usuario agregue artículos a una lista de compras. El proceso termina cuando el usuario escribe "terminar". Al final, muestra la lista ordenada alfabéticamente.
'''

def generadorListaCompras():
    lista_compras = []
    while True:
        articulo = input("Ingresa un artículo para la lista de compras (o escribe 'terminar' para finalizar): ")
        if articulo == "terminar":
            break
        lista_compras.append(articulo)
    lista_compras.sort()
    print("Lista de compras ordenada alfabéticamente:")
    for articulo in lista_compras:
        print(f"- {articulo}")

'''
15. Análisis de Temperaturas
Solicita las temperaturas de los 7 días de la semana y guárdalas en un arreglo. Muestra:
El promedio semanal.
Cuántos días la temperatura fue superior a 25 grados.
El día con la temperatura más baja (asumiendo que el índice 0 es Lunes).
'''

def analisisTemperaturas():
    temperaturas = []
    for i in range(7):
        temp = float(input(f"Ingresa la temperatura del día {i+1}: "))
        temperaturas.append(temp)
    print(f"Promedio semanal: {sum(temperaturas)/len(temperaturas):.2f}")
    print(f"Días con temperatura superior a 25: {len([t for t in temperaturas if t > 25])}")
    print(f"Día con temperatura más baja: {temperaturas.index(min(temperaturas)) + 1}")
    
continuar = True
while continuar:
    opcion = input("\n--- Elige una opción: (1-15) (0 para salir) --- ")
    if opcion == "0":
        continuar = False
    elif opcion == "1":
        numerosDinamicos()
    elif opcion == "2":
        verificadorEdad()
    elif opcion == "3":
        calculadoraDescuentos()
    elif opcion == "4":
        clasificadorNumeros()
    elif opcion == "5":
        tablaMultiplicar()
    elif opcion == "6":
        sumatoriaCentinela()
    elif opcion == "7":
        contadorVocales()
    elif opcion == "8":
        validacionContrasena()
    elif opcion == "9":
        registroNombres()
    elif opcion == "10":
        promedioNotas()
    elif opcion == "11":
        filtroArreglos()
    elif opcion == "12":
        buscadorElementos()
    elif opcion == "13":
        simulacionInventario()
    elif opcion == "14":
        generadorListaCompras()
    elif opcion == "15":
        analisisTemperaturas()
# Ranking de puntajes de un torneo de eSports
#En puntajes, cambia el valor 300 por 600 (ajuste en los puntajes de la primera ronda). Resultado esperado:
# puntajes = [[1000, 1500, 2000], [600, 700, 1400]]

puntajes = [ [1000, 1500, 2000], [300, 700, 1400] ]
def actualizar_puntajes(puntajes):
    puntajes[1][0] = 600
    return puntajes
puntajes = actualizar_puntajes(puntajes)
print(puntajes)

# Lista de creadores de contenido en una plataforma de streaming
# En streamers, cambia el nombre de ”GameNinjaPro” a ”EliteGamerX”.
streamers = [
   {"nombre": "GameNinjaPro", "seguidores": 250000},
   {"nombre": "PixelWarrior", "seguidores": 180000}
]
def actualizar_streamers(streamers):
    streamers[0]["nombre"] = "EliteGamerX"
    return streamers
streamers = actualizar_streamers(streamers)
print(streamers)

# Eventos en distintas ciudades del mundo
#En eventos, cambia la ciudad “Las Vegas” por “San Francisco”.
eventos = {
   "Estados Unidos": ["Los Ángeles", "Nueva York", "Las Vegas"],
   "España": ["Madrid", "Barcelona", "Valencia"]
}
def actualizar_eventos(eventos):
    eventos["Estados Unidos"][2] = "San Francisco"
    return eventos
eventos = actualizar_eventos(eventos)
print(eventos)

# Coordenadas de la sede de un torneo internacional
# En ubicacion, cambia el valo de ”latitud” a 40.712776 (cambiando la sede del torneo a Nueva York).
ubicacion = [
   {"latitud": 34.052235, "longitud": -118.243683}
]
def actualizar_ubicacion(ubicacion):
    ubicacion[0]["latitud"] = 40.712776
    return ubicacion
ubicacion = actualizar_ubicacion(ubicacion)
print(ubicacion)

'''
Crea la función iterar_diccionario(lista) que reciba una lista de diccionarios (como streamers) y recorra cada uno, imprimiendo sus claves y valores.
Formatea la salida para que cada diccionario se imprima en una sola línea, con el formato.
nombre - EliteGamerX, seguidores - 250000
'''
animales = [
   {"animal": "león", "velocidad": "40 km/h"},
   {"animal": "pollo", "velocidad": "8 km/h"}
]
def iterar_diccionario(lista):
    for diccionario in lista:
        print(f"animal - {diccionario["animal"]}, velocidad - {diccionario["velocidad"]}")
iterar_diccionario(animales)

# ---------------------------------------------

streamers = [
   {"nombre": "EliteGamerX", "seguidores": 250000},
   {"nombre": "PixelWarrior", "seguidores": 180000}
]

def obtener_valores(clave, lista):
    for diccionario in lista:
        print(diccionario[clave])
obtener_valores("nombre", streamers)
print() 
obtener_valores("seguidores", streamers)
print("-" * 20)

# --------------------------------------------------------------------

categorias = {
   "juegos_populares": ["Fortnite", "Minecraft", "Valorant", "GTA V"],
   "ciudades_eventos": ["Nueva York", "Madrid", "Tokio"]
}

def mostrar_informacion(diccionario):
    for clave, lista in diccionario.items():
        print(f"{len(lista)} {clave.upper()}")
        for elemento in lista:
            print(elemento)
        print() 
mostrar_informacion(categorias)
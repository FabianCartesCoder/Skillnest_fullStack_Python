'''
🗂️ Define la clase UsuarioStreaming, que debe incluir:

Atributos:
nombre
email
suscripcion (Gratis, Estándar o Premium)
lista_reproduccion (lista de títulos agregados por el usuario).
Métodos:
agregar_a_lista(self, titulo) agrega un contenido a la lista de reproducción.
ver_contenido(self, titulo) simula que el usuario reproduce un contenido.
cambiar_suscripcion(self, nueva_suscripcion) modifica el tipo de suscripción del usuario.
mostrar_info_usuario(self) muestra los datos del usuario y su lista de reproducción.
🧪 Realizar las siguientes pruebas con instancias:

Crea 3 usuarios de la plataforma de streaming.
Haz que el primer usuario agregue dos títulos a su lista y los vea.
Haz que el segundo usuario agregue un título, lo vea y cambie su suscripción.
Haz que el tercer usuario agregue tres títulos, los vea y cambie su suscripción dos veces.
'''

class UsuarioStreaming:
    def __init__(self, nombre, email, suscripcion="Gratis"):
        self.nombre = nombre
        self.email = email
        self.suscripcion = suscripcion
        self.lista_reproduccion = []

    def agregar_a_lista(self, titulo):
        self.lista_reproduccion.append(titulo)
        print(f'"{titulo}" se agregó a la lista de {self.nombre}.')

    def ver_contenido(self, titulo):
        if titulo in self.lista_reproduccion:
            print(f'{self.nombre} está viendo "{titulo}".')
        else:
            print(f'"{titulo}" no está en la lista de {self.nombre}. Agrégalo primero.')

    def cambiar_suscripcion(self, nueva_suscripcion):
        susAntigua = self.suscripcion
        self.suscripcion = nueva_suscripcion
        print(f'Suscripción de {self.nombre} cambiada de {susAntigua} a {self.suscripcion}.')

    def mostrar_info_usuario(self):
        print("----- Información del usuario -----")
        print(f"Nombre: {self.nombre}")
        print(f"Email: {self.email}")
        print(f"Suscripción: {self.suscripcion}")
        print("Lista de reproducción:")
        if self.lista_reproduccion:
            for titulo in self.lista_reproduccion:
                print(f" - {titulo}")
        else:
            print(" (vacía)")
        print("----------------------------------")


def crear_usuarios():
    usuarios = []
    for i in range(3):
        print(f"\nRegistro del usuario {i + 1}")
        nombre = input("Nombre: ").strip()
        email = input("Email: ").strip()
        suscripcion = input("Suscripción (Gratis, Estándar, Premium) [Gratis]: ").strip()
        if suscripcion == "":
            suscripcion = "Gratis"
        usuarios.append(UsuarioStreaming(nombre, email, suscripcion))
    return usuarios


def seleccionar_usuario(usuarios):
    print("\nUsuarios disponibles:")
    for numero, usuario in enumerate(usuarios, start=1):
        print(f"{numero}. {usuario.nombre} ({usuario.suscripcion})")

    seleccion = input("Selecciona el número del usuario o escribe 0 para salir: ").strip()

    if seleccion == "0":
        return None

    if seleccion.isdigit():
        numero_seleccionado = int(seleccion)
        if 1 <= numero_seleccionado <= len(usuarios):
            return usuarios[numero_seleccionado - 1]

    return None


def menu():
    usuarios = crear_usuarios()

    while True:
        usuario = seleccionar_usuario(usuarios)
        if usuario is None:
            print("Saliendo...")
            break

        while True:
            print(f"\nUsuario seleccionado: {usuario.nombre}")
            print("1. Agregar un título a la lista")
            print("2. Ver un contenido")
            print("3. Cambiar suscripción")
            print("4. Mostrar información del usuario")
            print("5. Volver a seleccionar usuario")
            print("0. Salir")

            opcion = input("Elige una opción: ").strip()

            if opcion == "1":
                titulo = input("Título a agregar: ").strip()
                usuario.agregar_a_lista(titulo)
            elif opcion == "2":
                titulo = input("Título a ver: ").strip()
                usuario.ver_contenido(titulo)
            elif opcion == "3":
                nueva = input("Nueva suscripción (Gratis, Estándar, Premium): ").strip()
                if nueva == "":
                    nueva = usuario.suscripcion
                usuario.cambiar_suscripcion(nueva)
            elif opcion == "4":
                usuario.mostrar_info_usuario()
            elif opcion == "5":
                break
            elif opcion == "0":
                print("Saliendo...")
                return
            else:
                print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    menu()
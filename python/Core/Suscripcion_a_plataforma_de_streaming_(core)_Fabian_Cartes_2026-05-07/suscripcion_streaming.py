'''
 Instrucciones
 Crea un archivo de Python llamado suscripcion_streaming.py.

 Define la clase SuscripcionStreaming, que debe incluir:

Atributos:
usuario (nombre del usuario asociado a la suscripción)
tipo_suscripcion (Gratis, Estándar, Premium)
costo_mensual (según el tipo de suscripción)
saldo_pendiente (monto acumulado que debe pagar el usuario)
Métodos:
realizar_pago(self, monto) reduce el saldo pendiente según el monto pagado.
cambiar_suscripcion(self, nuevo_tipo) cambia el tipo de suscripción y ajusta el costo mensual.
ver_contenido_exclusivo(self) permite el acceso a contenido según el tipo de suscripción. La suscripción “Gratis” no tiene acceso a contenido exclusivo.
mostrar_info_suscripcion(self) muestra el estado actual de la suscripción del usuario.
 Realizar las siguientes pruebas con instancias:

Crea 3 usuarios con diferentes tipos de suscripción.
Haz que el primer usuario intente ver contenido exclusivo, mejore su suscripción y pague su saldo.
Haz que el segundo usuario vea contenido exclusivo, cambie su suscripción a Premium y pague dos veces.
Haz que el tercer usuario intente pagar una cantidad menor a su saldo pendiente y vea contenido exclusivo.
'''

class SuscripcionStreaming:
   costos_suscripcion = {"Gratis": 0, "Estándar": 5.99, "Premium": 10.99}


   def __init__(self, usuario, tipo_suscripcion="Gratis"):
         self.usuario = usuario
         self.tipo_suscripcion = tipo_suscripcion
         self.costo_mensual = self.costos_suscripcion[tipo_suscripcion]
         self.saldo_pendiente = 0

   def realizar_pago(self, monto):
       if monto > 0:
           self.saldo_pendiente -= monto
           if self.saldo_pendiente < 0:
               self.saldo_pendiente = 0
           print(f"{self.usuario} pagó ${monto}. Saldo pendiente: ${self.saldo_pendiente:.2f}")
       else:
           print("El monto debe ser mayor a 0")

   def cambiar_suscripcion(self, nuevo_tipo):
       if nuevo_tipo in self.costos_suscripcion:
           self.tipo_suscripcion = nuevo_tipo
           self.costo_mensual = self.costos_suscripcion[nuevo_tipo]
           self.saldo_pendiente += self.costo_mensual
           print(f"{self.usuario} cambió a suscripción {nuevo_tipo}. Nuevo saldo pendiente: ${self.saldo_pendiente:.2f}")
       else:
           print("Tipo de suscripción inválido")

   def ver_contenido_exclusivo(self):
       if self.tipo_suscripcion == "Gratis":
           print(f"{self.usuario} con suscripción Gratis no tiene acceso a contenido exclusivo.")
       elif self.tipo_suscripcion == "Estándar":
           print(f"{self.usuario} con suscripción Estándar puede ver contenido exclusivo estándar.")
       elif self.tipo_suscripcion == "Premium":
           print(f"{self.usuario} con suscripción Premium puede ver todo el contenido exclusivo.")

   def mostrar_info_suscripcion(self):
       print(f"\n--- Información de Suscripción ---")
       print(f"Usuario: {self.usuario}")
       print(f"Tipo de Suscripción: {self.tipo_suscripcion}")
       print(f"Costo Mensual: ${self.costo_mensual:.2f}")
       print(f"Saldo Pendiente: ${self.saldo_pendiente:.2f}")
       print(f"-----------------------------------\n")


# Pruebas con instancias
# Usuario 1: Gratis -> Estándar -> Pago
usuario1 = SuscripcionStreaming("Juan", "Gratis")
print("=== USUARIO 1: JUAN ===")
usuario1.ver_contenido_exclusivo()
usuario1.cambiar_suscripcion("Estándar")
usuario1.realizar_pago(5.99)
usuario1.mostrar_info_suscripcion()

# Usuario 2: Estándar -> Premium -> Dos pagos
usuario2 = SuscripcionStreaming("María", "Estándar")
print("=== USUARIO 2: MARÍA ===")
usuario2.saldo_pendiente += usuario2.costo_mensual
usuario2.ver_contenido_exclusivo()
usuario2.cambiar_suscripcion("Premium")
usuario2.realizar_pago(10.99)
usuario2.realizar_pago(5.98)
usuario2.mostrar_info_suscripcion()

# Usuario 3: Premium -> Pago parcial -> Ver contenido
usuario3 = SuscripcionStreaming("Carlos", "Premium")
print("=== USUARIO 3: CARLOS ===")
usuario3.saldo_pendiente += usuario3.costo_mensual
usuario3.realizar_pago(5.00)
usuario3.ver_contenido_exclusivo()
usuario3.mostrar_info_suscripcion()  
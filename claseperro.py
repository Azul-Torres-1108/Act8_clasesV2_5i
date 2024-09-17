print("Clases version 2 el Constructor")

class Perro:
    # Funcion del constructor 
    def __init__(self,color,edad):
        self.color=color
        self.edad=edad
    # Funciones creadas por el usuario
    def muerde(self):
        print("Chale el perro me mordio")
    def chatperro(self,mensaje):
        print(f"chatperro: {mensaje}")
    def chatperra(self,mensajepe):
        print(f"chatperro: {mensajepe}")
    def datos(self):
        print(f"color: {self.color} edad: {self.edad}")
# Crear el objeto
chihuas = Perro("Negro", 2)
# Llamadas a funciones
chihuas.datos()
chihuas.muerde()
chihuas.chatperro("Hola canina")
chihuas.chatperra("Hola bobby")
chihuas.chatperro("Quieres ser mi guagua? ")
chihuas.chatperra("gRRRRrrr.................")
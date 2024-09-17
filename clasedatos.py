class Informacion:
# -----------------------------------------------------
    def mi_lista(self):
        lista_Nomperros={"bobby", "Dollar", "fany"}
        for x in lista_Nomperros:
            print(x)
# -----------------------------------------------------
    def mi_tupla(self):
        tupla = ("Husky", "Chihuahua", "Dalmata")
        for x in tupla:
            print(x)
# -----------------------------------------------------
    def mi_diccionario(self):
        diccionario = {
        "Raza": "Chihuahua", 
        "Nombre": "Bobby",
        "Edad": "2"
        }
        for x, y in diccionario.items():
            print(x, y)
# -----------------------------------------------------
    def mi_conjunto(self):
        set_edades = (5, 1, 3)
        for e in set_edades:
            print(e)
# Creando el objeto
datos=Informacion()
print("Listado de nombre de perros:")
datos.mi_lista()
print("# -----------------------------------------------------")
print("Listado de Tupla:")
datos.mi_tupla()
print("# -----------------------------------------------------")
print("Informacion de el perro")
datos.mi_diccionario()
print("# -----------------------------------------------------")
print("Edad de los perros:")
datos.mi_conjunto()

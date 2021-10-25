from Bots import Terminator


class Usuario:
    def __init__(self, nombre):
        self.nombre = "@"+nombre
        self.mensajes = []

    def twittear(self):
        mensaje = input("¿Qué estás pensando? (Max: 15 palabras)\n")
        self.mensajes.append(mensaje)
        
        if len(mensaje.split()) > 15:
            return "Tweet demasiado largo"
        else:
            return "Tweet enviado"

    def verMensajes(self):
        return self.mensajes

#Pensar en mas propiedades o metodos

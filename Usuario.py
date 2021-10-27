class Usuario:
    def __init__(self, nombre):
        self.nombre = "@"+nombre
        self.mensajes = []

    def twittear(self, mensaje):
        if len(mensaje.split()) > 15:
            return "Tweet demasiado largo"
        else:
            self.mensajes.append(mensaje)
            return "Tweet enviado"
        
    def verMensajes(self):
        return self.mensajes


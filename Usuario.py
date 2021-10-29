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
        
    def verTodosLosMensajes(self):
        return self.mensajes

    def verMensajesAlVacio(self):
        listaMensajesAlVacio = [s for s in self.mensajes if not s.__contains__("@")]
        return listaMensajesAlVacio

    def verMensajesAUsuarios(self):
        listaMensajesAUsuarios = [s for s in self.mensajes if s.__contains__("@")]
        return listaMensajesAUsuarios


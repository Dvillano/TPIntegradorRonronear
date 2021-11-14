#Clase padre Bot
from Usuario import Usuario


class Bot:
    def __init__(self):
        pass
    
    def enviarRespuesta(mensaje):
        print(mensaje)
 

#Bot Terminator: No responden, pero se guardan información de todos los que twittean
#Y hereda los atributos de la clase padre Bot.
class Terminator(Bot):
    def __init__(self):
        Bot().__init__()
        self = self

    

    def guardarTweets(nombreUsuario, mensajes):
        try:
            archivo = open("tweetsGuardados/" + nombreUsuario + ".txt", "a")

            for mensaje in mensajes:
                archivo.write(mensaje + "\n")
            archivo.close()
        except IOError:
            input("Error al guardar los archivos de mensajes")


respuesta = Terminator()
respuesta.enviarRespuesta()


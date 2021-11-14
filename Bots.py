#Clase padre Bot
from Usuario import Usuario


class Bot:
    def __init__(self):
        pass
    
    def enviarRespuesta(usuario, mensaje):
        respuesta = usuario + " " + mensaje
        print(respuesta)
        return respuesta
 
 # responde al usuario que originó el tweet con un link publicitario si el tweet contiene una palabra puntual
class Wally(Bot):
    def _init_(self):
        self = self

    def publicidad(respuesta,usuario):
        if "auto" in respuesta:
            return Wally.enviarRespuesta(usuario, "Visita www.ford.com.ar y obtendras importantes  descuentos")
        if "agua" in respuesta:
            return Wally.enviarRespuesta(usuario, "El agua mineral de la mejor calidad www.glaciar.com")
        if "viaje" in respuesta:
            return Wally.enviarRespuesta(usuario, "La mayor variedad de destinos la encontras en www.despegar.com")
        
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


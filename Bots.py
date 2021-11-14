#Clase padre Bot
from os import close
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
        
# Bot Terminator: No responden, pero se guardan información de todos los que twittean
# Y hereda los atributos de la clase padre Bot.
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

# Bot Benito: revisa los mensajes de los usuarios y  los machea con una lista negra, la cual detecta si se encuentra
# coincidencias, haciendo que se guarde el mensaje, el usuario y dando parte a las autoridades

listaNegra = ["muerte", "matar","asesinar","acuchilla","violar", "secuestrar"]

class Benito(Bot):
    def __init__(self):
        self = self

    def revisarMensaje(usuario, respuesta):
        respuestaMinusculas = respuesta.lower()
        respuestaEnLista = respuestaMinusculas.split()

        for i in listaNegra:
            for j in respuestaEnLista:
                if i == j:
                    archivo = open("tweetsReportados/" + usuario + ".txt", "a")
                    print("Mesanje Guardado y reportado a la Policia")
                    archivo.write(respuesta +"\n")
                    archivo.close 
    

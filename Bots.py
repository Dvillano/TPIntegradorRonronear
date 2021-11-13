#Clase padre Bot
class Bot:
    def __init__(self):
        pass
    
    def enviarRespuesta(mensaje):
        print(mensaje)
 

#Bot Terminator: No responden, pero se guardan información de todos los que twittean
class Terminator():
    def __init__(self):
        self = self

    def guardarTweets(nombreUsuario, mensajes):
        try:
            archivo = open("tweetsGuardados/" + nombreUsuario + ".txt", "a")

            for mensaje in mensajes:
                archivo.write(mensaje + "\n")
            archivo.close()
        except IOError:
            input("Error al guardar los archivos de mensajes")



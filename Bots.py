#Bot Terminator: No responden, pero se guardan información de todos los que twittean
class Terminator:
    def __init__(self):
        self = self

    def guardarTweets(nombreUsuario, mensajes):
        archivo = open("tweetsGuardados/" + nombreUsuario + ".txt", "a")

        for mensaje in mensajes:
            archivo.write(mensaje + "\n")
        archivo.close()


#Por hacer: 
#Englobar bots en una clase padre
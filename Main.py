from App import App
from Bots import Terminator, Wally, Benito
from CasosPrueba import listaUsuariosPrueba

print("")
print("    ###################################")
print("    #                                 #")
print("    #   Hola!! Bienvenidos a          #")
print("    #        PdpTwitter!!             #")
print("    #                                 #")
print("    ###################################")


def start_tuitear():
    start = None
    while start != "S":
        start = input("¿Queres ingresar tu usuario?: [S/N] ")
        start = start.upper()
        if start == "N":
            print("En serio?? Somos mejores que Facebook!!!")
            exit()
        if start == "S":
            print("Bien!! Vamos a tuitear!!!")
           
start_tuitear()

#Instancias
Pdptwitter = App()
#Guardamos todos los usuarios de prueba y sus mensajes en la lista de usuarios
for user in listaUsuariosPrueba: 
    Pdptwitter.guardarUsuario(user)
    for mensaje in user.mensajes:
        Pdptwitter.guardarMensaje(mensaje)

#Verificamos que ya exista usuario
nombreUsuario = input("Por favor ingrese su nombre de usuario: ")
usuario = Pdptwitter.crearUsuario(nombreUsuario)

while (True):
    print("")
    print("###################### MENU DE USUARIO ##########################")
    print("Bienvenido " + usuario.nombre + " a Pdptwitter, ¿que desea hacer?")
    print("1. Ver todos mis tweets")
    print("2. Escribir un tweet")
    print("3. Ver mis Menciones")
    print("4. Cambiar de Sesion")
    print("5. Ver mensajes al vacio")
    print("6. Ver mensajes a otros usuarios")
    print("7. Cerrar Sesion")

    opcion = int(input())
    if opcion == 1:

        print("Estos son tus tweets: \n")
        for tweet in usuario.mensajes:
            print(tweet)

    elif opcion == 2:
        
        # Usuario envia su mensaje, se guarda en la lista de mensajes del usuario
        tweet = input("Que estas pensando? (Max: 15 palabras): \n")
        respuesta = usuario.twittear(tweet)
        print(respuesta)
        Pdptwitter.guardarMensaje(tweet)
        
        # Wally envia su respuesta y se guarda en las menciones al usuario
        respuestaWally = Wally.publicidad(tweet, usuario.nombre)
        if respuestaWally != None:
            Pdptwitter.guardarMensaje(respuestaWally)
        

        # Benito revisa el mensaje del usuario
        respuestaBenito = Benito.revisarMensaje(usuario.nombre,tweet)
        if respuestaBenito != None:
            Pdptwitter.guardarMensaje(respuestaBenito)
        
    elif opcion == 3:
        
        for mensaje in Pdptwitter.mostrarMensajes():
            if usuario.nombre in mensaje:
                print(mensaje)
            
    elif opcion == 4:

        nombreUsuario = input("Por favor ingrese su nombre de usuario: ")
        usuario = Pdptwitter.crearUsuario(nombreUsuario)
        
    elif opcion == 5:
        print(usuario.verMensajesAlVacio())

    elif opcion == 6:
        print(usuario.verMensajesAUsuarios())

    elif opcion == 7:
        break

    else:
        print("Ingrese una opcion valida")

# Accion del BOT Terminator
for user in Pdptwitter.listaUsuarios:
    Terminator.guardarTweets(user.nombre, user.mensajes)


from Usuario import Usuario
from Bots import Terminator
from CasosPrueba import usuarioMaria, usuarioPedro, usuarioJuan

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
        start = input("¿Queres ingresar tu usuario y contrasenia?: [S/N] ")
        start = start.upper()
        if start == "N":
            print("En serio?? Somos mejores que Facebook!!!")
            exit()
        if start == "S":
            print("Bien!! Vamos a tuitear!!!")
start_tuitear()

usuario = Usuario(input("Bienvenido a Pdptwitter, por favor ingrese su nombre de usuario: "))



while (True):

    print("Bienvenido " + usuario.nombre + " a Pdptwitter, ¿que desea hacer?")
    print("1. Ver mis tweets")
    print("2. Escribir un tweet")
    print("3. Ver mis Menciones")
    print("4. Cerrar Sesion")
    
    opcion = int(input())
    if opcion == 1:

        print("Estos son tus tweets: ")
        for tweet in usuario.mensajes:
            print(tweet)

    elif opcion == 2:
        tweet = input("Que estas pensando?: \n")
        respuesta = usuario.twittear(tweet)
        print(respuesta)
        
    elif opcion == 3:

        for tweet in usuarioPedro.verMensajesAUsuarioEspecifico(usuario.nombre):
            print(tweet)
        for tweet in usuarioJuan.verMensajesAUsuarioEspecifico(usuario.nombre):
            print(tweet)
        for tweet in usuarioMaria.verMensajesAUsuarioEspecifico(usuario.nombre):
            print(tweet)
        
        break

    elif opcion == 4:
        break



    else:
        print("Ingrese una opcion valida")




# Terminator.guardarTweets(usuario.nombre, usuario.mensajes)
Terminator.guardarTweets(usuarioPedro.nombre, usuarioPedro.mensajes)
Terminator.guardarTweets(usuarioJuan.nombre, usuarioJuan.mensajes)
Terminator.guardarTweets(usuarioMaria.nombre, usuarioMaria.mensajes)

#Por hacer:
# 1. Crear clase Aplicacion
# 	- Metodo para envio de mensaje
# 2. Crear casos prueba (3 ususarios, 3 tweet arroba y 3 arroba) ✓
# 3. Obtener listado de tweets que arroban al usuario ✓
# 4. Obtener listado de tweets que no arroban a nadie ✓

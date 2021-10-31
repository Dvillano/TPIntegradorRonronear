from Usuario import Usuario 

#Casos de prueba:
usuarioPedro = Usuario("Pedro")
usuarioMaria = Usuario("Maria")
usuarioJuan = Usuario("Juan")

#Tweets de pedro
usuarioPedro.twittear("Hola, estoy en Twitter")
usuarioPedro.twittear("Me gusta mucho la coca-cola con todas mis comidas")
usuarioPedro.twittear("No me gusta gusta mucho el chocolate ")
usuarioPedro.twittear("@Maria recuerda que el viernes es la fiesta de cumpleanios, ¿vamos a ir?")
usuarioPedro.twittear("@Juan ¿quieres una cerveza?")
usuarioPedro.twittear("@Maria podemos ir mas temprano asi no te pierdes de nada importante")

#Tweets de Maria
usuarioMaria.twittear("Que dia tan feo, espero que maniana sea mejor")
usuarioMaria.twittear("Quien para una salida al cine?")
usuarioMaria.twittear("El gato de mi vecina es tan lindo que podria secuestrarlo")
usuarioMaria.twittear("@Pedro, no se si este libre para ir al cumpleanios, dejame revisar mi agenda")
usuarioMaria.twittear("@Juan ¿Vas a ir a la fiesta tambien?")
usuarioMaria.twittear("@Pedro, dejame pensarlo, mi jefe es un idiota y tengo mucho que hacer")

#Tweets de Juan
usuarioJuan.twittear("Aguante bokita el mas grande de todos")
usuarioJuan.twittear("Adidas es mejor que Nike, nadie lo puede negar")
usuarioJuan.twittear("3-0!!!!!!!!")
usuarioJuan.twittear("@Pedro obvio amigo siempre listo para unas birras")
usuarioJuan.twittear("@Maria claaaroo sabes que no me pierdo ninguna fiesta")
usuarioJuan.twittear("@Maria recordame que llevo para el asado? ")

listaUsuariosPrueba = [usuarioPedro, usuarioMaria, usuarioJuan]
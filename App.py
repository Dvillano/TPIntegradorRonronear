from Usuario import Usuario

class App:
    def __init__(self):
        self.listaTodosLosMensajes = []
        self.listaUsuarios = []
        self.listaNombresUsuarios = []

    def guardarUsuario(self, usuario):
        self.listaUsuarios.append(usuario)
        self.listaNombresUsuarios.append(usuario.nombre)

    def guardarMensaje(self, mensaje):
        self.listaTodosLosMensajes.append(mensaje)

    def mostrarMensajes(self):
        return self.listaTodosLosMensajes
    
    def mostrarUsuarios(self):
        return self.listaNombresUsuarios

    def crearUsuario(self, nombre):
        for usuario in self.listaUsuarios:
            if usuario.nombre == "@"+nombre:
                return usuario
        #create user
        usuario = Usuario(nombre)
        self.guardarUsuario(usuario)
        return usuario
    
    
    

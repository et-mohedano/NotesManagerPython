import usuarios.usuario as modeloUser
import notas.acciones
class Acciones:
    def registro(self):
        print("\nOk, vamos a registrarte en el sistema...")
        nombre = input("¿Cuál es tu nombre?: ")
        apellidos = input("¿Cuáles son tus apellidos?: ")
        email = input("¿Cuál es tu email?: ")
        password = input("Ingresa tu contraseña: ")
        usuario = modeloUser.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()
        if registro[0] >= 1:
            print(f"\nPerfecto {usuario.getNombre()} te has registrado con el email: {usuario.getEmail()}") 
        else:
            print("\nNo te has registrado correctamente")  
    def login(self):
        print("Ok, identificate en el sistema...")
        try:
            email = input("¿Cuál es tu email?: ")
            password = input("Ingresa tu contraseña: ")
            usuario = modeloUser.Usuario('', '', email, password)
            login = usuario.identificar()
            if email == login[3]:
                print(f"\nBienvenido {login[1]}, te has registrado en el sistema el {login[5]}")
                self.proximasAcciones(login)
        except Exception as e:
            # print(type(e))
            # print(type(e).__name__)
            print("Login incorrecto, intentalo de nuevo")
    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles:
        - Crear nota (crear)
        - mostrar tus notas (mostrar)
        - Eliminar notas (eliminar)
        - Salir (salir)
        """)
        accion = input("¿Qué quieres hacer?: ")
        accionesNotas = notas.acciones.Acciones()
        if accion == "crear":
            accionesNotas.crear(usuario)
            self.proximasAcciones(usuario)
        elif accion == "mostrar":
            print("Vamos a mostrar")
            accionesNotas.mostrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == "eliminar":
            accionesNotas.borrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == "salir":
            print(f"Hasta pronto {usuario[1]}")
            exit()
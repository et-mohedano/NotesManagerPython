import datetime
import hashlib
import usuarios.conexion as conexion
connect = conexion.conectar()
database = connect[0]
cursor = connect[1]
class Usuario:
    """
     Atributos;
    nombre
    apellidos
    email
    password
    """
    # Constructor
    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password
    # Setters and getters
    def setNombre(self, nombre):
        self.nombre = nombre
    def getNombre(self):
        return self.nombre
    def setApellidos(self, apellidos):
        self.apellidos = apellidos
    def getApellidos(self):
        return self.apellidos
    def setEmail(self, email):
        self.email = email
    def getEmail(self):
        return self.email
    def setPassword(self, password):
        self.password = password
    def getPassword(self):
        return self.password
    def registrar(self):
        fecha = datetime.datetime.now()
        # Cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))
        sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fecha)
        try:    
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]
        return result
    def identificar(self):
        # Consulta para comprobar si existe el usuario
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s;"
        # Cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))
        # Datos para la consulta
        usuario = (self.email, cifrado.hexdigest())
        cursor.execute(sql, usuario)
        result = cursor.fetchone()
        return result
import usuarios.conexion as conexion
connect = conexion.conectar()
database = connect[0]
cursor = connect[1]
class Nota:
    """
    Atributos:
    - Usuario_id
    - Titulo
    - Descripción
    """
    # constructor
    def __init__(self, usuario_id, titulo = "", descripcion = ""):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion
    # Setters and Getters
    def getUsuarioId(self):
        return self.usuario_id
    def setUsuarioId(self, usuario_id):
        self.usuario_id = usuario_id

    def getTitulo(self):
        return self.titulo
    def setTitulo(self, titulo):
        self.titulo = titulo

    def getDescripcion(self):
        return self.descripcion
    def setDescripcion(self, descripcion):
        self.descripcion = descripcion
    # Métodos
    def guardar(self):
        sql = "INSERT INTO notas VALUES(null, %s, %s, %s, NOW());"
        nota = (self.usuario_id, self.titulo, self.descripcion)
        cursor.execute(sql, nota)
        database.commit()
        return [cursor.rowcount, self]
    def listar(self):
        sql = f"SELECT * FROM notas WHERE usuario_id = {self.usuario_id};"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    def eliminar(self):
        sql = f"DELETE FROM notas WHERE usuario_id = {self.usuario_id} AND titulo LIKE '%{self.titulo}%';"
        cursor.execute(sql)
        database.commit()
        return [cursor.rowcount, self]
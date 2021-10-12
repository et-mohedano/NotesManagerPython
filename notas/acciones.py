import notas.nota as modeloNota
class Acciones:
    def crear(self, usuario):
        print(f"ok {usuario[1]} vamos a crear una nueva nota...")
        titulo = input("Ingresa el titulo de tu nota: ")
        descripcion = input("Ingresa el contenido de tu nota: ")
        nota = modeloNota.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()
        if guardar[0] >= 1:
            print(f"\nNota guardada correctamente: {nota.getTitulo()}")
        else:
            print(f"\nNo se ha guardado la nota, lo siento {usuario[1]}")
    def mostrar(self, usuario):
        print(f"\nVale {usuario[1]} aquí tienes tus notas: ")
        nota = modeloNota.Nota(usuario[0])
        notas = nota.listar()
        for nota in notas:
            print("\n*************************************")
            print(nota[2])
            print(nota[3])
            print("*************************************")
    def borrar(self, usuario):
        print(f"\nOk {usuario[1]} vamos a borrar notas")
        titulo = input("Ingresa el titulo de la nota a borrar: ")
        nota = modeloNota.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()
        if eliminar[0] >= 1:
            print(f"Hemos borrado la nota: {nota.getTitulo()}")
        else:
            print(f"No se ha borrado la nota, intentalo de nuevo")
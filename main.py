"""
Proyecto Python y Mysql
- Abrir asistente
- Login o registro
- Si elegimos registro, creará un usuario en la bd
- Si elegimos login, identifica al usuario y nos preguntará por la psw
- Se podrá elegir: crear nota, mostrar notas, borrarlas
"""
from usuarios import acciones
objAcciones = acciones.Acciones()
# import usuarios.acciones
print("""
Acciones disponibles:
    - registro
    - login
""")
accion = input("\n¿Qué quieres hacer?: ")
if accion == "registro":
    objAcciones.registro()
elif accion == "login":
    objAcciones.login()
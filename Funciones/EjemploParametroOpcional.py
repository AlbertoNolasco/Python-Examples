
## Ejemplo 4
"""
Como usar los parametros opcionales


Al parametro se le asigna un valor iniciar desde su declaracion, al momento de invocar la funcion esta no tendra problemas

"""


print("##### Ejemplo 4 #####")

def getEmpleado(nombre, dni = None):
    print("\n##### Empleado #####")
    print(f"Nombre: {nombre}")

    if dni != None:
        print(f"DNI: {dni}")

getEmpleado("Alberto Nolasco", "172301")

getEmpleado("Laura")
## Ejemplo 6
"""
Crear una funcion dentro de otra funcion
"""
print("\n##### Ejemplo 6 #####")

def getNombre(nombre):
    texto = f"El nombre es: {nombre}"

    return texto


def getApellido(apellidos):
    texto = f"Los apellidos son: {apellidos}"

    return texto


def devuelveTodo(nombre, apellidos):
    cadena = getNombre(nombre) + " \n" + getApellido(apellidos) + "\n" 

    return cadena


print(devuelveTodo("José A.", "Alvarez"))
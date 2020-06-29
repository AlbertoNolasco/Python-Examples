"""
Las variables locales: se definen dentro de una funcion y no se puede usar fuera de ella,
solo esta disponible dentro. a no ser que se haga un return

Variables globales: Son las que se declaran fuera de una funcion y estan disponibles 
dentro y fuera de ellas

"""

# Variables globales

frase = "Podrán robarte las ideas, pero nunca el talento!!"

print(frase)

def holaMundo():
    frase = "Hola mundo!!"
    print("Dentro de la función: ")
    print(frase)

    # se puede hacer una variable global de la siguiente manera  
    global variableGlobal 
    variableGlobal = "Hola como estas"

    print(variableGlobal)

holaMundo()

print(variableGlobal)


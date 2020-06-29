## Ejemplo 5
"""
parametros opcionales y return o devolver datos
Crear una calculadora

Ejemplo para crear un return

def saludame(nombre):
    saludo = f"Hola, saludos {nombre}"

    return saludo


print(saludame("Alberto"))
"""
print("##### Ejemplo 5 ##### \n")

def calculadora (numero1, numero2, basicas = False):

    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    div = numero1 / numero2

    cadena = ""

    if basicas == True:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:
        cadena += "Multiplicación: " + str(multi)
        cadena += "\n"
        cadena += "Divición: " + str(div)
        cadena += "\n"

    return cadena


    ## con los dos parametros
print(calculadora(20,4,True))

    ## Sin el parametro opcional
print(calculadora(4,2))
    

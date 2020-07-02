"""
Set es un tipo de dato, para tener una coleccion de valores. 
pero no tiene ni indice ni orden.
"""

personas = {
    "Corina",
    "Alberto",
    "Sebastian"
}

personas.add("Arcelia")
print(personas)
print(type(personas))

personas.remove("Alberto")
print(personas)

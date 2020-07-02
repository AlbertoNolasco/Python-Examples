"""
Una lista multidimensional es una lista dentro de otra lista
(Que tiene varias dimensiones)

"""


#lista multidimensional

print("\n ########## Listado de contactos ##########")

contactos = [
    [
        'Alberto',
        'alberto@alberto.com'
    ],
    [
        'Corina',
        'corina@corina.com'
    ],
    [
        'Sebas',
        'sebas@sebas.com'
    ],
    [
        'Arcelia',
        'arcelia@arcelia.com'
    ]
]

print(contactos)

## sacar el imail de sebas 

##print(contactos[2][1])

for contacto in contactos:
    for elemento in contacto:
        #print(elemento)
        if contacto.index(elemento) == 0:
            print(f"Nombre: {elemento}")
        else:
            print(f"Correo: {elemento}")




    print("\n")


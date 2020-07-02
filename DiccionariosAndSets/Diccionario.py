"""
Un diccionario es un tipo de dato que almacena un conjunto de dato 
en formato clave : valor 
Es parecido a un array asociativo o un objeto json

"""

persona ={
    "nombre" : "Alberto",
    "apellido": "Alvarez",
    "profesion" : "Developer"
    
}

print(persona)

print(persona["nombre"])
print(persona["profesion"])

## Lista con diccionarios
print("\n################### listas con diccionarios ################")
contactos=[
    {
        'nombre' : 'Alberto',
        'email' : 'alberto.alberto@.com'
    },
    {
        'nombre' : 'Luis',
        'email' : 'luis.luis@.com'
    },
    {
        'nombre' : 'Sebastian',
        'email' : 'sebastian.sebastian@.com'
    }
]

print(contactos)

print(contactos[0]["nombre"])

## asignar valor a un campo en especifico
contactos[0]["nombre"] = "Albertito"

print(contactos[0]["nombre"])

## imprimir listado de contactos con formato

print("\n Listado de contactos: ")

for contacto in contactos:
    print(f"Nombre dek contacto: {contacto['nombre']}")
    print(f"Dirección de email: {contacto['email']}")
    print("----------------------------------------------")
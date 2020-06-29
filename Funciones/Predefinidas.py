"""
Existen varias funciones predefinidas en python
"""
texto = "Hola"

#funciones generales
print(texto)
print(type(texto))


# detectar el tipado
comprobar = isinstance(texto, str)

if comprobar:
    print("Esa variable es un string")
else:
    print("No es una cadena")

if not isinstance(texto,float):
    print("La variable no es un numero con decimales")


#limpiar espacios
frase = "    Mi contenido"
print(frase)

print(frase.strip())


## Eliminar variables
year = 2022

print(year)

#del year

#print(year)


# comprobar variable vacia

cadenaTexto = "Jo  "

if len(texto) <= 0:
    print("La variable esta vacia")
else:
    print("La variable tiene contenido: ", len(cadenaTexto))



# encontrar caracter
frase = "La vida es bella"

print(frase.find("vida"))

## remplazar palabras en un string 
nueva_frase = frase.replace("vida","moto")
print(nueva_frase)


## Mayusculas y minusculas

print(texto)

print(texto.lower())

print(texto.upper())
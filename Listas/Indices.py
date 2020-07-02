"""
Trabajar con los indices de una lista

"""


peliculas = ["Batman","Spiderman", "Los vengadores"]

cantantes = list(('2pac','Drake', 'Lopez'))

#indices 

print(peliculas[1])
print(peliculas[-2])

print(cantantes[1:3])

print(cantantes[0:1])

print(peliculas[0:])

peliculas[0] = "Tor"

print(peliculas)
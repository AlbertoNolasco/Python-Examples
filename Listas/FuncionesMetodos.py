"""
Funciones predefinidas en las listas

"""

#lisas

grupos_musica = list(('AC\DC','Audioslave', 'Europe'))

numeros = [1,4,7,12,22,5,9]


#funciones

#Ordenar
print(numeros)
numeros.sort()
print(numeros)

#Agregar elementos
print(grupos_musica)
grupos_musica.append("Van Halen")
print(grupos_musica)

grupos_musica.insert(1,"Helloween")
print(grupos_musica)

#eliminar elementos
grupos_musica.pop(1)
print(grupos_musica)

#eliminar elemento por nombre
grupos_musica.remove("Europe")
print(grupos_musica)


# dar vuelta a una lista
print(numeros)
numeros.reverse()
print(numeros)

# buscar dentro de una lista
print('Van Halen' in grupos_musica)

#contar elementos
print(grupos_musica)
print(len(grupos_musica))


## cuantas veces aparece un elemento en una lista
print(numeros.count(2))
numeros.append(2)
print(numeros.count(2))


# conseguir un indice
print(grupos_musica.index("Audioslave"))

# unir una lista
grupos_musica.extend(numeros)

print(grupos_musica)
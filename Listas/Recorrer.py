"""
recorrer lista con loops


"""

grupos_musica = list(('AC\DC','Audioslave', 'Europe'))


grupos_musica.append("Van Halen")
grupos_musica.append("Helloween")




nuevo_grupo = ""
while nuevo_grupo != "parar":
    nuevo_grupo = input("Introduce el nuevo grupo de musica: ")
    if nuevo_grupo != "parar":
        grupos_musica.append(nuevo_grupo)


print("#" * 8 + " Grupos de Rock " + "#" * 8)
for grupos in grupos_musica:
    print(f"{grupos_musica.index(grupos) + 1}.- {grupos}")



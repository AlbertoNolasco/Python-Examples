#Ejercicio 9: Mostrar la fecha de un evento almacenada en una tupla.

fecha_evento = (2023, 9, 14)

print(type(fecha_evento))


print(fecha_evento)


print('El evento programado es para la fecha: ', fecha_evento)

print('El evento programado es para la fecha: %i/%i/%i'% fecha_evento)

##tambien se puede desempaquetar la tupla 
agnio, mes, dia = fecha_evento

print('El evento programado es para la fecha:{}/{}/{}'.format(dia,mes,agnio))
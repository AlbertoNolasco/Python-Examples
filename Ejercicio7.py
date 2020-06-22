# Ejercicio 7: obtener la extensión de un archivo especificado por el usuario

nombre_archivo = input('Ingrese el nombre del archivo: ')

splitDoc = nombre_archivo.split('.')
nombreArchivo = splitDoc[0]
extArchivo = splitDoc[-1]


print(nombre_archivo)
print('Nombre del archivo: ',nombreArchivo)
print('Extensión del archivo: ', extArchivo)

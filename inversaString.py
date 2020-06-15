## Obtener la representación inversa de una cadena de caracter

# Python => nohtyp

cadena = 'Python'

for i in range(len(cadena)-1, -1, -1):
    print(cadena[i], end='')


print()

print(cadena[::1])
print(cadena[::-1])


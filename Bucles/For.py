## For
## for variable in elemento_iterable (lista, rango, etc)
##      bloque de instrucciones
##

contador = 0
resultado = 0

for contador in range(0,10):
    print("Voy por el " + str(contador) )

    resultado += contador
    #resultado = resultado + contador

print(f"El resultado es: {resultado}")


## Ejemplo tabla de multiplicar

print("\n#" * 8, "Ejemplo 1", "#" *8 )

numero_Usuario = int(input("De que numero quieres la tabla?: "))

if numero_Usuario < 1:
    numero_Usuario = 1

print(f"\n##### Tabla de multiplicar del número {numero_Usuario}#####")

for numero_tabla in range(1,11):
    if numero_Usuario == 111:
        print("Numero prohibido")
        break

    print(f"{numero_Usuario} x {numero_tabla} = {numero_Usuario * numero_tabla}")
else:
    print("Tabla finalizada")

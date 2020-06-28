"""
Ejercicio 9:
Hacer un programa que pida numeros al usuario indifinidamente 
hasta que el usuario ingrese el 111

"""


numero = 0

while numero != 111:
    numero = int(input("Ingrese un numero: "))
    print(f"\nNumero ingresado: {numero}")

else:
    print("Ingresaste el numero correcto Gracias!!")
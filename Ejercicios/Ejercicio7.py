"""
Ejercicio 7:
Hacer un programa que mestre todos los numeros impares entre dos numeros que decida el usuario.
"""

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))


if(numero1 < numero2):
    print(f"Los numeros impares entre el numero {numero1} y el numero {numero2} son: \n")
    
    for inpar in range(numero1,(numero2+1)):

        if inpar %2 != 0:
            print(inpar)

else:
    print("El primer numero debe de ser mas chico que el segundo numero.")

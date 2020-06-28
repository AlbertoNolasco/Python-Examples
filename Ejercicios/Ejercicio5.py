"""
Ejercicio 5:
Hacer un programa que muestre todos los numeros entre dos numeros que diga el usuario.

"""
print("Mostrar numeros")

contador1 = int(input("Ingrese el primer numero: "))
contador2 = int(input("Ingrese el segundo numero: "))

if contador1 < contador2:
    print(f"Los numeros entre el numero {contador1} y {contador2} son: ")
    for numeros in range(contador1,(contador2+1)):
        print(numeros)
else:
    print(f"Los numeros entre el numero {contador2} y {contador1} son: ")
    for numeros in range(contador2,(contador1+1)):
        print(numeros) 




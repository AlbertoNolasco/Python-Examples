"""
Ejercicio 3:
Escribir un programa que muestre los cuadrados (un numero multiplicado por si mismo) 
de los 60 primeros numeros naturales. 
- Resolverlo con un for y un while

"""

numero_cuadradoFor = []
numero_cuadradoWhile = []
numero_cuadradoForA = {}


contador = 1

for contador in range(61):
    numero_cuadradoFor.append(contador * contador)
    print(f"El cuadrado de {contador} es {contador * contador}")

contador = 0
while contador <= 60:
    numero_cuadradoWhile.append(contador *contador)
    print(f"El cuadrado de {contador} es {contador * contador}")
    contador += 1

print("*" *5, "Cuadrado de los numeros del 1 al 60 con For", "*"*5)
print(numero_cuadradoFor)
print("\n")

print("*" *5, "Cuadrado de los numeros del 1 al 60 con While", "*"*5)
print(numero_cuadradoWhile)



"""
Ejercicio 2:
Escribir un script que muestre por pantalla todos los numeros pares del 1 al 100

"""

numero = 1
numeros_pares = []

while numero <= 120:
    par = numero % 2 
    if par == 0:
        numeros_pares.append(numero)

    
    numero = numero + 1
else:
    print("*" * 8 , "Finaliza loop con while", "*" *8,"\n")
    print(numeros_pares)

contador_for = 1
numeros_paresFor = []
for contador_for in range(1,121):
   
    
    if contador_for % 2 == 0:
        numeros_paresFor.append(contador_for)

else:
    print("*" * 8 , "Finaliza loop con for", "*" *8,"\n")
    print(numeros_paresFor)
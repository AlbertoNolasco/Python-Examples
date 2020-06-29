## Ejemplo 3 
"""
Crear un programa que genere las tablas de multiplicar de un numero en especifico o de un rango de numeros

"""
print("##### Ejemplo 3 #####")

opcion = "ninguno"
numero1 = 0
numero2 = 0


def tablaMultiplicar(pNumero):
    print(f"\n##### Tabla de multiplicar del número {pNumero} #####")
    for contador in range(1,11):      
        print(f"{pNumero} x {contador} = {pNumero *contador}")


def tablaMultiplicarRango(pNumero1, pNumero2):
    for contador in range(pNumero1,(pNumero2+1)):
        tablaMultiplicar(contador)


while opcion != "s":
    print("################################")
    print("Oprima 1 si quiere saber la tabla de multiplicar de un numero")
    print("Oprima 2 si quiere saber la tabla de multiplicar de un rango de numeros")
    print("Oprima s si quiere salir del programa")
    print("################################\n")

    opcion = input("Seleccione una opcion por favor: ")

    if opcion == "1":
        print("##### Opcion uno #####")
        numero1 = int(input("Ingrese el numero por favor: "))
        tablaMultiplicar(numero1)
    elif opcion == "2":
        print("##### Opcion dos #####")
        numero1 = int(input("Ingrese el primer numero por favor: "))
        numero2 = int(input("Ingrese el segundo numero por favor: "))
        if numero1 > numero2:
            print("El numero uno debe de ser menor al numero dos !!")
        else:
            tablaMultiplicarRango(numero1,numero2)
    elif opcion == "s":
        print("A salido del programa !!")

    else:
        print("Opcion no valida")
    



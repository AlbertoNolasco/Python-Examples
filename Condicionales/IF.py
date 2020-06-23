# Condicional IF 
# if condicion:
#   instrucciones
# else
#   otras condiciones

## Operadores de comparación 
## == Igual
## != Diferente
## < Menor que
## > Mayor que
## <= Menor igual que
## >= Mayor igual que 

## if anidados

#Ejemplo 1 
print("#" * 8, "Ejemplo 1", "8" *8 )


color = "Rojo" #input("Adivina el color")

if color == "Rojo":
    print("Muy bien\n")
    print("El color es rojo")
else:
    print("El color no es rojo\n")
    print(":(")


#Ejemplo 2
print("\n#" * 8, "Ejemplo 2", "8" *8 )

year = 2020 ##int(input("En que año estamos: "))

if year >= 2021:
    print("Estamos de 2021 en adelante!!")
else :
    print("Es un año anterior al 2021")

#Ejemplo 3 if anidados comprobar mayoria de edad
print("\n#" * 8, "Ejemplo 3", "8" *8 )

nombre = "José" #input("Ingrese su nombre por favor: ")
nacionalidad = "Mexicano" #input("Ingrese su nacionalidad por favor: ")
ciudad = "Jalisco" ##input("Ingrese su ciudad: ")
edad = 21 ##int(input("Ingrese su edad por favor: "))


if edad >= 18:
    print(f"{nombre} es mayor de edad!! ")
    if nacionalidad != "Mexicano":
        print("No es mexican@")
    else:
        print(f"{nombre} es Mexicano y de {ciudad}")
else:
    print(f"{nombre} no es mayor de edad")

#Ejemplo 4 Imprime dia de la semana: por numero del 1 al 5
print("\n#" * 8, "Ejemplo 4", "8" *8 )

dia = 3 #int(input("Ingrese el numero de la semana: "))

if dia == 1:
    print("Lunes")
elif dia == 2:
    print("Martes")
elif dia == 3:
    print("Miercoles")
elif dia == 4:
    print("Jueves")
elif dia == 5:
    print("Viernes")
else:
    print("Es fin de semana")


#Ejemplo 5 multiples condiciones comprobar la edad de trabajar rango de edad de 18 a 65 años
# Operadores logicos
# and y 
# or o 
# ! negacion 
# not No

print("\n#" * 8, "Ejemplo 5", "8" *8 )

edad_minima = 18 
edad_maxima = 65
edad_oficial = 18 ##int(input("Introduce tu edad"))

if edad_oficial >= edad_minima and edad_oficial <= edad_maxima:
    print("Esta en el rango para trabajar")
else:
    print("Usted no cumple con la edad para trabajar") 


#Ejemplo 6 Mas ejemplos de IF
print("\n#" * 8, "Ejemplo 6", "8" *8 )

pais = "Mexico"

if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print(f"{pais} es un pais de habla hispana !!")
else:
    print(f"{pais} no es un pais de habla hispana")


#Ejemplo 6a Mas ejemplos de IF
print("\n#" * 8, "Ejemplo 6a", "8" *8 )

pais = "Alemania"

if not(pais == "Mexico" or pais == "España" or pais == "Colombia"):
    print(f"{pais} no es un pais de habla hispana")
else:    
    print(f"{pais} es un pais de habla hispana !!")

    
#Ejemplo 6b Mas ejemplos de IF
print("\n#" * 8, "Ejemplo 6a", "8" *8 )

pais = "Colombia"

if pais != "Mexico" and pais != "España" and pais != "Colombia":
    print(f"{pais} no es un pais de habla hispana")
else:    
    print(f"{pais} es un pais de habla hispana !!")
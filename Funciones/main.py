"""
Función es una conjunto de instrucciones agrupadas bajo un nombre en concreto 
que puede reutilizarse invocando a la función tantas veces como sea necesario

Ejemplo:

def nombreFuncion(parametros):
    #bloque de instrucciones

se llama la funcion de la siguiente manera

nombreFuncion(mi_parametro)

"""
print("##### Ejemplo 1 #####")
#Ejemplo 1 

#definir la funcion
def muestraNombres():
    print("Alberto")
    print("Corina")
    print("Arcelia")
    print("Sebastian")

    print("\n")


## invocar función

muestraNombres()


# Ejemplo 2 parametros
print("##### Ejemplo 2 #####")



def mostrarTuNombre(nombre, edad):
    #print(f"Tu nombre es: {nombre}")

    if edad >= 18:
        print(f"{nombre} tiene {edad} es mayor de edad")
    else:
        print(f"{nombre} tiene {edad} es menor de edad")


nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
#mostrarTuNombre("José Alberto")

mostrarTuNombre(nombre, edad)





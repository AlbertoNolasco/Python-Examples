"""
Ejercicio 1: 
    -Crear dos variables, uno pais otro continente
    -Mostrar su valor por pantalla 
    -poner un comentario diciendo el tipo de dato
"""

pais = input("¿De que país eres?: ")  #string 
continente = input("¿De que continente eres?: ") #string
year = int(input("¿Que año es: ")) #int

print(f"Tu continente es {continente} y tu país es {pais} el año es {str(year)}")
print(f"El tipo de dato de país es: {type(pais)} y el tipo de dato del continente es: {type(continente)}")
print(f"El tipo de dato del año es: {type(year)}")
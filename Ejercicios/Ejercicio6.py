"""
Ejercicio 6:
Mostrar todas las tablas de multiplicar del 1 al 10. 
mostrando el titulo de la tabla y luego las multiplicaciones del 1 al 10

"""
tabla = 1

while tabla <= 10:
    print("#"*40)
    print(f"Tabla de multiplicar del numero {tabla}")
    print("#"*40)

    for contador in range(1,11):
        print(f"{tabla} x {contador} : {tabla * contador} ")

    tabla += 1


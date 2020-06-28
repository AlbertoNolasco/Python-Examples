"""
Ejercicio 10:
El programa tiene que pedir la nota de 15 alumnos y sacar por pantalla cuantos han aprobado y cuantos han suspendido.

"""

calif_alumnos = []
for alumno in range(1,16):
    calificacion = int(input(f"\nIngrese la calificacion del alumno numero {alumno}: "))
    calif_alumnos.append(calificacion)

aprobado=0
reprobado=0
for alum in calif_alumnos:
    
    if (alum < 60):
        reprobado += 1
    else:
        aprobado += 1

print(f"El numero de reprobados es {reprobado} y el numero de aprobados es {aprobado}")

"""
Tambien se puede hacer de esta manera
"""
contador = 1
aprobado=0
reprobado=0

num_alumnos = int(input("¿Cuantos alumnos vas a ingresar?: "))

while  contador <= num_alumnos:
    alumno = int(input(f"Inserte la calificación del alumno numero {contador}: "))

    if alumno >= 60:
        aprobado += 1
    else:
        reprobado += 1
    
    contador += 1


print(f"El numero de reprobados es {reprobado} y el numero de aprobados es {aprobado}")
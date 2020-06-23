## Itera o repite la ejecucion n veces
##
## while condicion:
##  bloque de intrucciones
##  actualizacion de contador
##


contador = 1 

while contador <= 100:
    print(f"Estoy en el número: {contador} ")
    contador = contador + 1

print("#" * 10)
muestrame = str(0)
contador = 1 

while contador <= 100:
    print(f"Estoy en el número: {contador} ")
    muestrame = muestrame + ", " + str(contador)
    contador = contador + 1

print(muestrame)


## Ejemplo tabla de multiplicar

print("\n#" * 8, "Ejemplo 1", "#" *8 )

numero_usuario = int(input("¿De que numero quieres tu tabla?: "))

if numero_usuario < 1:
    numero_usuario = 1

print(f"#####Tabla del numero {numero_usuario}#####")

contador = 1 

while contador <= 10:
    print(f"{numero_usuario} x {contador} = {numero_usuario * contador}")
    contador += 1
else:
    print("#### Tabla terminada ####")


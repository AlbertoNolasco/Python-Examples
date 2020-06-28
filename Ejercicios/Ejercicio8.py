"""
Ejercicio 8:
¿Cuanto es el x por ciento de un numero? 

pedir el numero y pedir que porcentaje queremos obtener

"""

cantidad = float(input("Ingrese una cantidad: "))
porcentaje = float(input("Ingrese el porcentaje a obtener: ")) 


print(f"El {porcentaje}% de {cantidad} es : {cantidad * (porcentaje * .01)}")
#Ejercicio 10: Solicitar al usuario un número n y calcular n + nn + nnn

## ejemplo n = 5 + 55 + 555 = 615 

n = input('Ingrese un numero por favor: ')
valorString = {n,n+n,n+n+n}
vOne, vTwo, vThree = valorString
suma = int(vOne)+int(vTwo)+int(vThree)
print("El valor es: {} + {} + {} = {}".format(vOne,vTwo,vThree,suma))


#tambien se puede hacer de esta manera

print("********************************************")
nn = int('{}{}'.format(n,n))
nnn = int('%s%s%s'% (n,n,n))
n = int(n)
sumaV = n+nn+nnn

print('Suma2 : {} + {} + {} = {}'.format(n,nn,nnn,sumaV))

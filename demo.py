import sys
import datetime

print(sys.version)
print(sys.version_info)

## ejemplos basicos de print


print('Este es un print basico')

print('Este es un ejemplo basico.', end='')

print()

print('Python', 'es', 'muy bueno!!')
print('Python', 'es', 'muy bueno!!',sep='-')

print()

print('{} es {}'.format('Python','tremendo!!') )

print()

numero = [2,5,7,1,3]

print(numero)
print()
##diccionario

lugares = {'Oaxaca','Jalisco','veracruz'}
print(lugares)


## obtener la hora y fecha actual del sistema
print(datetime.datetime.now())

dateNow = datetime.datetime.now()

print(dateNow)

print(type(dateNow))
##formatear fecha y hora

print(dateNow.strftime('%d/%m/%Y %H:%M:%S'))


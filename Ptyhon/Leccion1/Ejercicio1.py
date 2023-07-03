'''
Ejercicio 1:
Deberemos plasmar la expresion en una expresion algoritmica, osea hacerlo en codigo
'''
'''
a= float(input('Digite el valor de a: '))
b= float(input('Digite el valor de b: '))
c= float(input('Digite el valor de a: '))

resultado= (a** 3 * (b** 2 - 2 * a * c)) / (2 *b)
print(f'El resultado es: {resultado}')
'''

'''Ejercicio 2:
Determinar la solucion logica de la siguente operacion'''
'''
a= float(input("Escribir el valor de a: "))
b= float(input("Escribir el valor de b: "))
resultado= ((3+ 5 * 8) < 3 and ((-6/3*4) /2 <2 )) or (a>b)
print(f"El resultado es: {resultado}")
'''

'''
Ejercicio 3: 
Intercambiar el valor de dos variables 
'''
'''
a= 12
b= 5

aux= a
a=b
b=aux

print(f'El valor nuevo de a es: {a}')
print(f'El valor nuevo de b es: {b}')
'''
'''
Ejercicio 4: Area y longitud de un circulo

Hacer un programa para ingresar el radio de un circulo y se reporte su area y la longitud
de la circunferencia.
'''
'''
import math

radio= float(input("ingresar el radio: "))
area= math.pi *(radio**2)
longitud = 2 * math.pi * radio

print(f'El area del circulo es: {area}')
print(f'La longitud de a circunferencia es: {longitud}')
'''


'''
Ejercicio n°3: Calcular la estacion del año

Pedir al usuario que ingrese un mes del año, el valor debe ser entre 1 y 12, luego le decimos
en que estacion del año esta.
'''
'''
mesActual= int(input("Ingresa en forma numerica el mes del año: "))
if mesActual ==1 or mesActual ==2 or mesActual ==3:
    estacion = "Verano"
elif mesActual ==4 or mesActual==5 or mesActual==6:
    estacion = "Otonio"
elif mesActual ==7 or mesActual==8 or mesActual==9:
    estacion = "Invierno"
elif mesActual ==10 or mesActual==11 or mesActual==12:
    estacion = "Primavera"
else:
    estacion= "ingrese un valor valido"

print(f"En el mes {mesActual} la estacion es: {estacion} ")

'''

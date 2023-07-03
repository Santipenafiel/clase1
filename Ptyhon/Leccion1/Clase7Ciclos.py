'''
Ciclo While
imprmir numeros del 0 al 5 con el ciclo while
'''

'''
maximo =5
contador= 0
while contador <=maximo:
    print(contador)
    contador+= 1
'''
'''
minimo= 1
contador = 5
while contador>= minimo:
    print(contador)
    contador -=1
'''
#Palabra reservada break

'''
for letra in 'Alemania':
    if letra == 'a':
        print(f'La letra encontrada es: {letra}')
        break
        # una vez llegue al elemento que busca se corta el ciclo
else:
     print("Fin del ciclo for")
'''
'''
#Palabra reservada continue

for i in range(6):
    if i % 2 == 0:
        print(f'Valor: {i}')

for i in range(6):
    if i % 2 != 0:
        continue
    print(f'Valor: {i}')
'''


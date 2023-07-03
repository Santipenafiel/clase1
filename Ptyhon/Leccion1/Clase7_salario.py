'''
Dadas las horas trabajadas de 5 personas y la tarifa de pago, calcular el salario y el total de todos los salarios
'''

'''
persontasTotal=5
salarioTotal=0

for i in range(persontasTotal):
    horasTotales =float(input(f'Ingrese la cantidad de horas trabajadas de la persona {i+1} :'))
    pagoHoras= float(input(f'Ingrese la tarifa de pago por hora de la persona {i+1}: '))

    salario=horasTotales * pagoHoras
    salarioTotal += salario

    print(f'El salario de la persona {i+1} es: {salario}')
print("El total de todos los saliarios es: ", salarioTotal)
'''

#Año bisiesto

'''
respuesta="s"
while respuesta == "s":
    anio= int(input("Ingrese un año"))

    if (anio % 4 == 0 and anio % 100 !=0) or anio % 400 ==0:
        print(f"el año {anio}, es año bisiesto")

'''

cadena= "Hola"
for letra in cadena:
    print(letra)
else:
    print("fin del ciclo for")
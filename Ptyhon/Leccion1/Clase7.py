'''
Ejercicio n°4: Etapas de la vida
Haremos un programa que cuando el usuario ingrese su edad le diga,
o imprima la etapa de su vida en una breve oracion:
0 a 10 = la infancia es increible y bella
10 a 19 = Tienes muchos cambios, mucho que estudiar
20 a 29 = Amor y comienza el trabajo
para las siguientes etapas ,deberas completarlo
'''
'''
edad = int(input("Ingrese su edad en numeros: "))
mensaje= None

if 0 <= edad <10:
    mensaje= "La infancia es increible y bella"
elif 10 <= edad <19:
    mensaje= "Tienes muchos cambios, mucho que estudiar"
elif 19 <= edad <29:
    mensaje= "Amor y comienza el trabajo"
elif 29 <= edad <39:
    mensaje= "Comienzas a hacer lo que te apasiona"
elif 39 <= edad <49:
    mensaje= "construccion de vivienda propia y de una familia "
else:
    mensaje= "Comienzan a volver los frutos de todo el esfuerzo de la vida "
print(f'La edad ingresada es {edad} : {mensaje}')
'''
'''
Ejercicio n°5: Sistema de calificaciones
Crear un sistema de calificaciones de la siguiente manera: le pedimos al usuario que ingrese un valor entre 0 y 10

'''

calificacion =int(input("Ingrese la calificacion con valores de 0 a 10: "))
if 9<= calificacion <=10:
    print("A")
elif 8<= calificacion <9:
    print("B")
elif 7<= calificacion <8:
    print("C")
elif 6<= calificacion <7:
    print("D")
elif 0<= calificacion <6:
    print("F")
else:
    print("Ingreso un valor incorrecto")
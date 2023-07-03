'''
miVariable = 3
print(miVariable)
miVariable = "a"
print(miVariable)
miVariable = 3.5
print(miVariable)

x = 10
y = 2
z = x + y
print(id(x))

# Las literales se escriben x624
print(id(y))
print(id(z))


a= "Hola alumnos"
print(type(a))

b:str = 54 # :str es solo para usar una referencia en la variable, pero la misma puede contener distinto tipo de dato
print(type(b))

# Tipos int, float, String, bool

x=10
print(x)
print(type(x))
x=14.5
print(x)
print(type(x))
x= "Hola alumnos"
print(x)
print(type(x))
x= True
print(x)
print(type(x))
x= False
print(x)
print(type(x))

# Manejos de cadenas (String)
miGrupoFavorito: str = "The letter black"
caracteristicas = "The Best Rock band"
print("Mi grupo favorito es:" + miGrupoFavorito + caracteristicas)
print("Mi grupo favorito es:" , miGrupoFavorito , caracteristicas) # otra forma de concatenar

numero1 = "7"
numero2 = "8"
print(int (numero1) + int(numero2))

'''

num =  int(input("Digite un numero en el rango del 1 al 3: "))
numTexto = ''
if num == 1:
    numTexto = 'Numero uno'
elif num == 2:
    numTexto = 'Numero dos'
elif num == 3:
    numTexto = 'Numero tres'
else:
    numTexto = 'Has ingresado un numero fuera de rango'

print(f'El numero ingresado es: {num} - {numTexto}')
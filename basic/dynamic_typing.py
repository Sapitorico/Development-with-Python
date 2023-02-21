#!/usr/bin/python3
""" Python determina automáticamente el tipo de la variable en tiempo de ejecución. """
number = 10
string = "sapitorico"
number2 = 10.4
character = 'c'

print(number)
print(string)
print(number2)
print(character)

a = 42
b = -13
c = 0

print(a, b, c)

a = 0
print(a + 1)

pi = 3.1416
e = 2.7182

print(pi, e)


a = "sapo"
a = 4 > 3
print(a)

a = 5
print(a)
a = "Hola mundo"
print(a)

a = 5
b = "7"
print(a + int(b)) # podemos pedirle a python qu haga la converion explicita de tipo

nombre = "Juan"
apellido = 'Pérez'

print("Mi nombre es " + nombre + " " + apellido) # podemos concatenar strings asi de simple

""" variables booleanas (bool) """
es_verdadero = True
es_falso = False

if es_verdadero:
    print("Es verdadero")
else:
    print("Es falso")

"""  Las listas son colecciones ordenadas de elementos que pueden contener elementos de diferentes tipos. """
numeros = [1, 2, 3, 4, 5]
palabras = ['hola', 'mundo']

print(numeros)
print(palabras)

""" podemos definir un diccionario con valores a traves de un id """
persona = {'nombre': 'Juan', 'apellido': 'Pérez', 'edad': 35}

print(persona['nombre'])
print(persona['apellido'])
print(persona['edad'])

""" define una variable de tipo tupla """
punto = (3, 4)

print(punto[0])
print(punto[1])

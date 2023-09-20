# Variables
my_variable= 'My String variable'
print(my_variable)

my_int_variable = 5
print(my_int_variable)

#Tambien se le puede cambiar el valor a otro tipo ejemplo
my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

#Concatenacion de variables en print
print('Hola' + 'como esta esta: ', my_variable, my_int_to_str_variable, my_bool_variable )

#Funciones del sistema
print(len(my_variable))

#Variables en una sola linea

"""Es una manera de declarar variables, pero no es una buena practica"""
name, surname, alias, age = "Frank", "Chango", "-Changito-", 20
print   ("Hola mi nombre es:",name, surname,". Mi edad: ",age, ". Mi alias es: ",alias)

#Inputs()
"""
name=input('Cual es tu nombre: ')
age=input(f'Cual es tu edad {name}: ')
print(f"Hola {name} bienvenido.... tu edad es?: {age}")
"""
#Cambiamos su tipo

name=0.5
age="Hola que hace"
print(name, age)

#¿Forzamos un tipo?

address: str = "Como estas?"
address= 32
address= False
address= 5.7
print(type(address))







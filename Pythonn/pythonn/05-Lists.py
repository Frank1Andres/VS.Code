################################################ lISTAS ##########################################

my_list = list()
my_other_list =[]

print(len(my_list))

my_list=[20,35,30,62,95,54,17]
print(my_list)
print(len(my_list))

my_other_list=[20, 1.56,"Frank", "Chango"]
print(type(my_other_list))
print(type(my_list))

print(my_other_list[-1])
print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-4])
print(my_list.count(30)) #nos sirve para saber cuantos elementos se repiten
#print(my_other_list[-5]) IndexError
#print(my_other_list[-4]) IndexError

age, height, name, surname = my_other_list
print(surname)

"No es una buena practica realizar esto"
# name, height,surname,age = my_other_list[2], my_other_list[1], my_other_list[3], my_other_list[0]
# print(age)
print(my_list + my_other_list)

"Funciones con las listas"

# agregar un nuevo elemento a la lista
my_other_list.append("Yeca")
print(my_other_list)

#agrega un elemento a lista con su indice
my_other_list.insert(1, "Azul")
print(my_other_list)

#elimina un elemento de la lista
my_other_list.remove("Yeca")
print(my_other_list)

my_list.remove(20)
print(my_list)

# my_list.pop() #el ultimo de la lista
print(my_list.pop())
print(my_list)
#agregando lo que saca el pop a una variable
my_pop_list=my_list.pop(2)
print(my_pop_list)
print(my_list)

del my_list[2]
print(my_list)

my_new_list = my_list.copy()
print(my_new_list)

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

print(my_new_list[1:2])

my_list = "Hola Python"
print(my_list)
print(type(my_list))

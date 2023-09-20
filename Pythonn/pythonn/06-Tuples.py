################################################ TUPLAS ##########################################
#Conjunto de valores!!

my_tuple = tuple()
my_other_tuple = ()

my_tuple=(20, 1.56, "Frank", "Chango", "Frank")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[4]) IndexError
# print(my_tuple[-6]) IndexError

print(my_tuple.count("Frank"))
print(my_tuple.index(1.56))



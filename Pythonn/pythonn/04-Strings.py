### Strings ###

my_string= "Mi String "
my_other_string= "Mi otro String"

print(len(my_string))
print(len(my_other_string))
print(my_string + " pero sabes que? tambien " + my_other_string)

"""Tenemos caracteres especiales en tipos strings: \n 
--este va al inicio\t 
"""

my_line_string="Este string\ncon salto de linea"
print(my_line_string)

my_tabulation_string="\tEste string lleva tabulacion"
print(my_tabulation_string)

my_scape_string="\\tEste es un string lleva \\n escapado"
print(my_scape_string)

#FORMATEO

name, surname, age="Frank", "Chango", 20

# Esta es una de las peores maneras en las que se puede imprimir en formateo de código
print("Mi nombre es " + name + " " + surname + " xd. y mi edad es " + str(age))
"""Mejores manera de formatear codigo"""
print("Mi nombre es {} {} y mi edad es {} ". format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
#tambien tenemos este que aprendimos en Hola Mundo jeje
print(f"Mi nombre es {name} {surname} y mi edad es de {age}")

# Desempaquetado de caracteres

language = "python"
a,b,c,d,e,f=language
print(a)
print(b)

# División

language_slice=language[1:3]
print(language_slice)

language_slice=language[1:]
print(language_slice)

language_slice=language[:]
print(language_slice)

language_slice=language[-2]
print(language_slice)

language_slice=language[0:6:2]
print(language_slice)

#Reverse

reversed_language = language[::-1]
print(reversed_language)

#Funciones

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.lower().isupper())
print(language.startswith("PY")) 
# no es lo mismo colocarlo con mayus y minusculas
print("Py"=="py")

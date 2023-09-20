### Operadores Aritmericos ###

print(5+6)
print(5-6)
print(5*6)
print(5/3)
print(10//3)
print("Division con numeros pares: ",
      10%2 ,"Ahora con impares: ", 10%3)
print(10**3) #Potencia

print("Que mas"+" " + "ve"+ " " + "Con catenacion con '+' ")
print("Hola" + str(5))
print("Hola" * 3)
print("Vamos bien" * (2**3))

my_float=(2.5*2)
print("agua "* int(my_float))

### Operadores Comparativos###

print(3>4)
print(3<4)
print(3<=4)
print(3>=4)
print(3==4)
print(3!=4)

print(""" Comparacion con Strings""")

print("Hola" > "Python")
print("Hola" < "Python")
print("Hola" >= "Python")
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")
print("Cango">"Aezer")#Realiza una comparacion alfabetica
print(len("BOLA")<len("COLA")) #Comparacion de caracteres

### OPERADORES LÓGICOS ###
print("/////////////////////////////")
# Todo negativo tanto en AND como en OR
print(3>4 and "Hola" > "Python")
print(3>4 or "Hola" > "Python")
# Todo positivo AND y OR
print(3<4 and "Hola"< "Python")
print(3<4 or "Hola" < "Python")
print(3<4 or "Hola" > "Python")
print(3<4 or "Hola" < "Python" and 4==4)
print( not(3>4))
#EJERCICIO
#Simular los 6 números del Loto entre 1 y 41
""" (Decima para el desafio) """

import random

print (random.random())#entre 0 y 1
print (random.randint(1,6))#dado
print (random.randrange(111, 1111, 3))#Numeros aleatorios de 3 cifras

caracteres= "abcdefghijklmnopqrstuxwxyz0123456789"
password =""
for i in range(8):
    password += random.choice(caracteres)

print("La contraseña generada es:", password)

alumnos = ["Juan", "Andres", "Massiel"]

print("El alumno seleccionado es:", random.choice(alumnos))
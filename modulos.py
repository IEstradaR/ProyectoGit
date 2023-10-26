#Importar un modulo local 
import funciones as fun
#as se utiliza para crear alias 

#importar un módulo interno de Python
import math

#Importar una funcion especifica del modulo
from funciones import restar, variable

print(variable)

numero1= int(input("Ingrese un numero"))
numero2 = int(input("Ingrese otro numero"))

print(fun.sumar(numero1, numero2))

print(restar(numero1,numero2))


#MODULOS DE TERCEROS

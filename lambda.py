lista = [1, 2, 3 ,4 ,5]
#La funcion map aplica la funcion lambda 
# a una lista
cuadrado = list(map(lambda x:x**2, lista))
print(cuadrado)

#Funcion Filter para filtrar los numeros pares
pares = list(filter(lambda x:x%2==0, lista))
print("pares",pares)

farenheit = [0, 32, 70, 98.6, 212]
#La funcion map aplica la funcion lambda 
# a una lista
celcius = list(map(lambda f:(f-32)/1.8, farenheit))
print(celcius)


















radio=float(input("Ingrese el radio \n"))

area= lambda r : 3.14*(r**2)
print(area(radio))
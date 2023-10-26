#Creando un diccionario
semana={1:"lunes", 2:"martes" }

#Imprimir diccionario
print(semana.items())
print(semana.keys())
print(semana.values())

#Buscar un elemento
print(semana.get(1))

#Agregar un elemento
semana[3]="Miercoles"
print(semana.values())

#Modificar un elemento
semana[2]="Tuesday"
print(semana.values())

#Eliminar un elemento
semana.pop(2)
print(semana.values())
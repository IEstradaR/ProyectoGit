""" nota=0
iterador=0 #Contador
suma =0 #Acumulador
while iterador<3:
    nota=int(input("Ingrese la nota \n"))
    iterador+=1 #Cuento las repeticiones
    suma +=nota #Acumulo las notas(las sumo)
print("La suma es", suma) """

#Crea un programa para contar votos de 2 cantidatos, 
# al finalizar debe imprimir la cantidad de votos por cada 
#candidato y la cantidad de votos totales.
cain=0 #Contador
abel=0 #Contador
TotalVotos=0 #Acumulador
voto="blanco"
while voto!="":
    voto=input("Ingrese su voto \n")
    if voto=="cain":
        cain +=1
    elif voto=="abel":
        abel+=1
    TotalVotos+=1
print("Total",TotalVotos-1)
print("Cain",cain)
print("Abel",abel)




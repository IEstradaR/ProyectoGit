
#identifique los 5 errores en el archivo y corrijalos

def miFuncion():
    print("Hola Mundo")
          
def calcularArea(alto, ancho):
    return alto*ancho

def perimetro(alto, ancho):
    return (alto+ancho)*2

a=int(input("Ingrese el ancho del rectangulo: \n"))
h=int(input("Ingrese la altura del rectangulo: \n"))

print("El Área es: ", calcularArea(h,a))

print("El Perimetro es: ", perimetro(h,a))

""" *********************************************************************** """
#Maneje los siguientes errores lógicos en Python

def division(num, div):
    return num/div

try:
    n=int(input("Ingrese un numero: \n"))
    d=int(input("Ingrese su divisor: \n"))
    resultado=division(n,d)
    print("el resultado de la división es: ", resultado)
except:
    print("Se indetermino por dividir por cero")

""" SEGUNDA FUNCION """
def ingresoRut(rut):
    return rut

r=int(input("Ingrese su rut \n"))
rut=ingresoRut(r)
print("Su rut es: ", rut)


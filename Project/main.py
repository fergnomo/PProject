import clases as cd
import listas as li

#Print Hola Mundo
print("Hola Mundo")

#Print con variable
mi_nombre = 'Fernando'
print(mi_nombre)

#Algo guapo
a = 0
for i in range(5):
    a += 1
    print(a)
#Nuevo comentario pull

#nuevo comentario push

#Operadores
numero = 5

mensaje = """esto es un mensaje
con tres saltos
de linea"""
print(mensaje)

numero1 = 5
numero2 = 7
if numero1 > numero2:
    print("El número 1 es mayor")
else:
    print("El numero 2 es mayor")

def mensaje1():
    print("Hola")
    print("Y")
    print("Adios")
 
    
def sumar():
    num1 = 6
    num2 = 7
    resultado = num1 + num2
    return(resultado)

def restar(a, b):
    resultado = a - b
    return (resultado)

resultado_suma = sumar()
resultado_resta = restar(20,5)
resultado_multiplicar = cd.multiplicar(7,3)

print(resultado_suma)
print(resultado_resta)
print(resultado_multiplicar)
print(li.primeraLista)
mensaje1()

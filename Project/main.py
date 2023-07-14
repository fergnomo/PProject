import clases as cd

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
    return(num1 + num2)

def restar(a, b):
    return (a - b)

print(sumar())
print(restar(17,2))
print(cd.multiplicar(3,2))
mensaje1()

# excepciones parte 1
# las excepciones son errores que ocurren durante la ejecución de un programa. La sintaxis del código es correcta pero durante la ejecución del programa ocurre un error inesperado
# para solucionar esto se hace un captura de la excepción

#ejemplo descargado del curso, si no tuviera una captura de excepción al intentar una división por 0 este código fallaría
def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):		
    try:
        return num1/num2 
    except ZeroDivisionError: #se añade una captura de excepción para que la división por cero no produzca que el programa falle
        print("No se puede dividir entre 0")
        return "Operación errónea"

op1 = 0
op2 = 0
while True:
    try: #se añade una captura de instrucción para que recoja las dos variables que pueden causar errores al insertar valores que no sean int
        op1=(int(input("Introduce el primer numero: ")))
        op2=(int(input("Introduce el segundo numero: ")))
        break
    
    except ValueError:
        print("Error en los datos introducidos. Intentalo de nuevo.")
    
operacion=input("Introduce la operacion a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operacion no contemplada")


print("Operacion ejecutada. Continuacion de ejecucion del programa ")



#excepciones segundo ejemplo
#como capturar varias excepciones en un solo try
def divide2():
    try:
        op1 = float(input("Introduce el primer numero: "))
        op2 = float(input("Introduce el segundo numero: "))
    
        print("La división es: " + str(op1/op2))
    except ValueError:
        print("El valor introducido es erróneo")
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
    #except: de esta manera se recogen las excepciones de manera general, sin especificar cual es el error. No es muy recomendable
    
    finally: #lo que se ponga dentro de esta función siempre se va a ejecutar, entre o no entre por except
        print("Cálculo finalizado")
    
    # si ponemos una bloque try sin el except se ejecuta lo que hay dentro pero no se recoge ninguna excepción en el except pero se ejecuta lo que haya en el finally. 
    # Siempre tiene que haber un finally si utilizamos un try sin except.
divide2()


#parte 2 de Excepciones
#vemos la instrucción raise, para poder lanzar nuestra propias excepciones según las definamos nosotros a voluntad
def evaluaEdad(edad):

    if edad <0:
       raise ZeroDivisionError("La edad no puede ser menor que cero") #esta es una forma de lanzar nuestro propio error
    
    if edad < 20:
        return "Eres muy joven"
    elif edad < 40:
        return "Eres joven"
    elif edad < 65:
        return "Eres maduro"
    elif edad < 100:
        return "Cuídate..."
    
print(evaluaEdad(int(input("Indica tu edad: "))))


#nuevo ejemplo
import math

def calculaRaiz(num1):
    
    if num1<0:
        raise ValueError ("El número no puede ser negativo")
    
    else:
        return math.sqrt(num1)
    
op1 = int(input("Introduce un número: "))

try:
    print(calculaRaiz(op1))
except ValueError as ErrorNumeroNegativo: #de esta manera recogemos nuestro propio error y este no da un error por tener un error con un nombre no definido
    print(ErrorNumeroNegativo)
    
print("Programa terminado")

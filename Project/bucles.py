# vamos a empezar a hablar de los bucles
# bucles determinados, se sabe solamente leyendo el codigo cuantas veces se va a repetir
# bucles indeterminados, no sabemos cuantas veces lo va a repetir dependiendo de las circunstancias de la ejecución del programa

# bucles FOR (determinado)
#for VARIABLE in ELEMENTO A RECORER
    #mensaje dentro del codigo con identación

#hace el bucle tantas veces como elementos tenga la lista
for i in [1, 2, 3]:
    print("Hola")

#a la variable i mientras recorre la lista se le asigna cada valor dentro de la lista
for i in ["Primavera", "Verano", "Otoño", "Invierno"]:
    print(i)

#mas bucles for
email = False
mi_email = input("Introduce tu email: ")

for i in mi_email:
    if i == "@":
        email=True
   
if email==True:
    print ("El correo es valido.")
else:
    print ("El correo no es valido.")

#nuevo bucle 
contador = 0
mi_email2 = input("Introduce tu email: ")

for j in mi_email2: 

    if (j == "@" or j=="."):
        contador = contador+1

if contador==2:
    print ("Email Valido!")
else:
    print ("Email Invalido! Debe tener al menos un caracter especial (@ o.) y")
 

#----------------- parte 3 de los bucles   
    #nuevo bucle in range y notaciones especiales con el print
    
for i in range(5):
    print("Hola")

for i in range(5):    #imprime del 0 al 4
    print(i)
    
for i in range (5):
    print(f"Valor de la variable {i}")   #la f se utiliza para que el print entienda que lo que hay entre llaves es una notación especial que una texto con los valores que toma la variable

for i in range(5, 50, 3):
    print(f"Valor de la variable {i}")   #la i va del 5 al 49 y va de 3 en 3


valido=False
email = input("Introduce tu email: ")

for i in range(len(email)):
    if email[i] == "@":  #con esta sentencia se valida si la variable i durante el for coge el valor que se esta buscando
        valido = True
        
if valido:
    print("Email correcto")
    
#----------------- parte 4 de los bucles
        #ejemplos con while
i=1

while i<=10:
    print("Ejecución" + str(i))
    i+=1

print("Terminó la ejecución")

#ejemplo de inicio de sesión con re intentos limitados, si quitamos la condición de la i == 15, tendríamos intentos infinitos
edad = int(input("Escribe tu edad: "))
sesión = True
i = 0

while edad<5 or edad>100:
    print("Has introducido una edad errónea. Vuelve a intentarlo")
    edad = int(input("Escribe tu edad: "))
    i += 1
    if i == 5:
        print("Se ha bloqueado la sesión")
        sesión = False
        break
    
if sesión == True:
    print("Gracias por colaborar. Puedes pasar")
    print(f"Edad del participante {edad}")
    
#----------------- parte 5 de los bucles
        #instrucciones continue, pass y else
for letra in "Python":
    
    if letra == "h":
        continue #se salta una iteración del bucle 
    print("Viendo la letra: " + letra)

#ejercicio con una aplicación mas practica
nombre="Pildoras Informaticas"
contador = 0
print(len(nombre))

for letra in nombre:
    if letra == " ":
        continue
    contador+=1
    
print(contador)

#instrucción pass: sirve para que el programa cargue sin hacer nada y no rompa el programa

#instrucción else
email=input("Email: ")

for i in email:
    if i=="@":
        arroba = True
        break   
else:
    arroba = False
    
print(arroba)
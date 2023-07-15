#---------------------Ejercicios Condicionales

#Ejercicio 1
num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el primer numero: "))

def DevuelveMax (n1, n2):
    if n1 < n2:
        print(n2)
    elif n2 < n1:
        print(n1)
    else:
        print ("Son iguales")
    
print("El numero mas alto es: ")
DevuelveMax(num1, num2)

#Ejercicio 2
nombre = input("Escribe tu nombre: ")
direccion = input("Escribe tu direccion: ")
telefono = input("Escribe tu telefono: ")

listaDirecciones=[nombre, direccion, telefono]
print("Los datos personales son: " + listaDirecciones[0] + " " + listaDirecciones[1] + " " + listaDirecciones[2])

#Ejercicio 3
num1 = int(input("Primer Valor "))
num2 = int(input("Segundo Valor "))
num3 = int(input("Tercer Valor "))

lista = [num1, num2, num2]
media = (lista[0] + lista[1] + lista[2])/len(lista)
print("La media es " + str(media))

#Ejercicio 4 ---- FALLIDO
#while len(lista) < 11:
#   for i in range(len(lista)):
#       lista.append(int(input("Escribe un numero: ")))
#media = sum(lista[0:])/len(lista)
#print("La media es: " + str(media))
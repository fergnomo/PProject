
#ejer1
#crear un programa que pida infinitamente numeros mayores que el anterior, si metemos un numero menor se acaba el programa

num1 = int(input("Introduce un número: ")) 
num2 = int(input(f"Introduce un número mayor que {num1}: ")) 

while num2 > num1:
    num1 = num2
    num2 = int(input(f"Escribe un numerin crack mayor que {num1}: ")) 

print()
print(num2, "no es mayor que", str(num1))


#ejer2
#se piden infinitos números positivos, en el momento de que sean negativos se sale del programa. Cuando salga del programa suma todos los valores positivos anteriores
lista = []

while True:
    num3 = int(input("Escribe un numero: "))
    if num3 < 0:
        break
    lista.append(num3)
    
print (f"La suma es: {sum(lista[0:])}")

#otra forma de hacer el mismo ejercicio que antes, los while true no son una muy buena cosa
numero = int(input("Numero: "))
suma = 0
while numero > 0:
    suma = suma+numero
    numero = int(input("Numero: "))
    
print(suma)
#Ejercicio 4 ---- FALLIDO
lista=[]
num = int(input("De cuantos numeros vas a hacer la media: "))
while len(lista) < num:
#   for i in range(len(lista)):
    lista.append(int(input("Escribe un numero: ")))
media = int(sum(lista[0:])/len(lista))
print("La media es: " + str(media))
#Ejercicio 4 ---- Resolucion temporal
lista=[]
while True:
    lista.append(int(input("Escribe un numero: ")))
    confirmacion = input("¿Quieres continuar? Escribe s o n: ")
    if confirmacion == "n":
        break
media = sum(lista[0:])/len(lista)
print("La media es: " + str(media))

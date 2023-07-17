#Ejercicio 4 ---- Resolucion temporal
#lista=[]
#while True:
#    lista.append(int(input("Escribe un numero: ")))
#    confirmacion = input("¿Quieres continuar? Escribe s o n: ")
#    if confirmacion == "n":
#        break
#media = sum(lista[0:])/len(lista)
#print("La media es: " + str(media))

#Ejercicio 4 ---- Solucion

lista=[]
while True:
    num = input("Escribe un numero (c para terminar): ")
    if num == "c":
        break
    else:
        lista.append(int(num))
if len(lista) != 0:
    media = round(sum(lista[0:])/len(lista), 3)
    print("La media es: " + str(media))
else:
    print ("No hay datos")


primeraLista=["Primero", "Segundo", "Tercero", "Cuarto"]

print(primeraLista[:])
print(primeraLista[-2])
print(primeraLista[1:3])
print(primeraLista[:2])
print(primeraLista[2:])

#Agrega al final
primeraLista.append("Quinto")

#Agrega en un punto intermedio
primeraLista.insert(1,"Usurpador")

#Agregar varios elementos
primeraLista.extend(["Sexto","Séptimo","Octavo"])

#Devolver el indice de un elemento de la lista
print(primeraLista.index("Segundo"))

#Comprobar si el elemento se encuentra en la lista
print("Noveno" in primeraLista)

#Pueden almacenar todo tipo de datos
segundaLista=["Azul", 36, "Rojo", 42.3]

#Eliminar elementos de la lista
primeraLista.remove("Usurpador")

#Eliminar ultimo elemento agregado a la lista
segundaLista.pop()

#Juntar dos listas diferentes
terceraLista = primeraLista[:] + segundaLista[:]

#Repetir las lista
cuartaLista = primeraLista[:] * 2

print(primeraLista[:])
print(segundaLista[:])
print(terceraLista[:])
print(cuartaLista[:])

#Estructuras de datos como las listas y las tuplas, con la diferencia de que estos se almacenan asociados a una clave:valor y no tienen ningún orden
#clave:valor significa que a cada valor que almacenamos se le asigna una clave única. Dentro de los diccionarios se pueden almacenar listas, tuplas y otros diccionarios

#Crear un diccionario
primerDiccionario={"Spain":"Madrid", "Varsovia":"Tirana", "Colombia":"Bogota"}

#Añadir un elemento nuevo a un diccionario existente
primerDiccionario["Japon"]="Roma"
print(primerDiccionario["Japon"])

#Sobreescribir en un elemento ya añadido al diccionario
primerDiccionario["Japon"]="Tokyo"
print(primerDiccionario["Japon"])

#Borrar elementos del diccionario
del primerDiccionario["Varsovia"]
print(primerDiccionario)

#Se pueden crear diccionarios con elementos de varios tipos
segundoDiccionario={"Spain":"Madrid", 7:"Cristiano Ronaldo", "CR": 7}

#Incluir tuplas en un diccionario como claves
otraTupla=["Spain", "Italia", "Reino Unido", "Alemania"]
tercerDiccionario={otraTupla[0]:"Madrid", otraTupla[1]:"Roma", otraTupla[2]:"Londres", otraTupla[3]:"Berlin"}
print(tercerDiccionario)

#Asignar un tupla de valores, no de clave
cuartoDiccionario={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "Anillos":[1991, 1992, 1993, 1996, 1997, 1998]}
print(cuartoDiccionario["Equipo"])
print(cuartoDiccionario["Anillos"])

#Guardar diccionario dentro de un diccionario
quintoDiccionario={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "Anillos":{"temporadas":[1991, 1992, 1993, 1996, 1997, 1998]}}
print(quintoDiccionario)

#Metodo keys, devuelve las claves
print(quintoDiccionario.keys())

#Metodo Values, devuelve los valores
print(quintoDiccionario.values())

#Devuelve la longitud del diccionario
print("Longitud: ", len(quintoDiccionario))


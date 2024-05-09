# Las tuplas son listas inmutables, por lo que las acciones que se pueden hacer en las listas aquí no funcionan, salvo extraer porciones. Tampoco se puede consultar en ellas
# Tienen la utilidad de que son más rápidas y ocupan menos espacio. 
# Permiten formatear strings y pueden utilizarse como claves en un diccionario


primeraTupla=("Fernando", 12, 5, 1996)

#Convertir una tupla en una lista
lista=list(primeraTupla)
print(lista)

#Convertir una lista en una tupla
tupla=tuple(lista)
print(tupla)

#Como ver si esta el elemento que busco en una tupla
print("Fernando" in tupla)

#Averiguar cuantos elementos de los que le preguntamos se encuentran en la tupla
print(tupla.count(12))

#Averiguar la longitud de una tupla
print(len(tupla))

#Se puede crear tuplas con un solo elemento. Es muy importante añadir la coma detrás del único elemento para que sea una tupla unitaria
segundaTupla=("Carmen",)

#Se puede crear una tupla si utilizar paréntesis. Puede llegar a confusión, es recomendable ponerlos. Se conoce como empaquetado de tupla
terceraTupla="Fernando", 12, 5, 1996
print(terceraTupla)

#Desempaquetado de tupla. Asigna los valores de la tupla a las variables que hemos creado
cuartaTupla=("Fernando", 12, 5, 1996)
nombre, dia, mes, anho = cuartaTupla

print(nombre)
print(anho)
print(dia)
print(mes)

#Recordar que no se pueden utilizar acciones que modifiquen las tuplas

print(anho)

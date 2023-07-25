# Generadores Parte 1
# estructuras que extraen valores de una función y se almacena en objetos iterables (que se pueden recorrer)
# estos se almacenan de uno en uno 
# cada vez que se almacena un valor este se queda en estado pausado hasta que se solicita el siguiente

#ejemplo de generador
def generaNumeros():
    numeros = 0
    yield numeros

# son mas eficientes que las funciones tradicional
# muy útiles con listas de valores infinitos, por ejemplo una función que genera direcciones IP aleatorias a petición
# bajo determinados escenarios, será muy útil que un generador devuelva los valores de uno en uno

#practica diferenciar funciones y generadores

def generaPares(limite):
    num = 1
    miLista=[]
    while num<limite:
        miLista.append(num*2)
        num+=1
    return miLista

print(generaPares(10))

#generador que haga lo mismo

def generaPares2(limite):
    num = 1
    
    while num<limite:
        yield num*2
        num+=1

devuelvePares=generaPares2(10)

#si quiere que me devuelve la lista entera
#for i in devuelvePares:
#       print(i)

#si quiero que me imprima solo una parte de la lista que genera
print(next(devuelvePares))

print("Aquí puede haber mas cosas") #añadido unicamente para ver el orden del flujo

print(next(devuelvePares)) #entre llamada y llamada entra en suspensión y ahorra recursos

print("Aquí puede haber mas cosas")

print(next(devuelvePares))


# Generadores Parte 2
# nueva instrucción yield from 
# se usa para simplificar bucles anidados

def devuelveCiudades(*ciudades): #cuando se informa un asterisco antes del argumento se indica que va a recibir indefinidos argumentos y que le van a llegar en forma de tupla
    for elemento in ciudades:
        for subElemento in elemento:
            yield subElemento

ciudades_devueltas = devuelveCiudades("Madrid", "Bilbao", "Barcelona", "Talavera de la Reina")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))

#ejemplo simplificado

def devuelveCiudades2(*ciudades): #cuando se informa un asterisco antes del argumento se indica que va a recibir indefinidos argumentos y que le van a llegar en forma de tupla
    for elemento in ciudades:
        yield from elemento

ciudades_devueltas = devuelveCiudades("Madrid", "Bilbao", "Barcelona", "Talavera de la Reina")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))

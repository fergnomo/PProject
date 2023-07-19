#Condicionales IF - Condicionales 
print("Evaluacion notas de alumno")

#código para introducir los valores por teclado
#para utilizar esta función hay que definir a que valor el programa tiene que transformar el valor que escribimos por consola
nota_alumno=int(input("Introduce la nota del alumno: "))

def evaluacion(nota):
    valoracion = "no presentado"
    if nota < 5 and nota >= 0:
        valoracion = "suspenso"
    elif nota >= 5 and nota <10:
        valoracion = "aprobado"
    elif nota == 10:
        valoracion = "matricula de honor"
    else:
        valoracion = "ha copiado"
    return valoracion

print("Valoracion:",evaluacion(nota_alumno))

#---------------------------------------------- Parte 2

print("Verificacion de acceso")

edad_usuario=int(input("Introduce tu edad: "))

#if edad_usuario<18:
#    print("No puedes pasar")
#else:
#    print("Adelante maquinaria")
    
if edad_usuario<18:
    print("No puedes pasar")
elif edad_usuario>100:
    print("No te lo crees ni tu hermano")
else:
    print("Pasen y vean, el circo de los horrores")

#---------------------------------------------- Parte 3
# Instruccion SWITCH no existe en Python

#Concatenacion de operadores
edad = 7
if 0 < edad < 100:
    print("Edad correcta")
else:
    print("Edad incorrecta")
    
#Nuevo ejercicio comparación salarios
salario_presidente = int(input('Ingrese salario presidente: '))
print("Salario presidente: " + str(salario_presidente))

salario_director = int(input('Ingrese salario director: '))
print("Salario director: " + str(salario_director))

salario_jefe_area = int(input('Ingrese salario jefe de area: '))
print("Salario jefe de area: " + str(salario_jefe_area))

salario_administrativo = int(input('Ingrese salario administrativo: '))
print("Salario administrativo: " + str(salario_administrativo))

if salario_administrativo < salario_jefe_area < salario_director < salario_director:
    print("Bien")
else:
    print("Mal")
#---------------------------------------------- Parte 4
#uso de los operadores logicos AND y OR

print("Becas 2023")
distancia = int(input("Distancia de tu casa a la escuela: "))
hermanos = int(input("Número de hermanos en el centro: "))
salario_familiar = int(input("Salario anual bruto: "))

if distancia > 40 and hermanos > 2 and salario_familiar <= 20000:
    print("Tiene beca")
else:
    print("Que te la paguen tus padres crack")

if (distancia > 40 and hermanos > 2) or salario_familiar <= 20000:
    print("Tiene beca")
else:
    print("Que te la paguen tus padres crack")
    
#uso del operador IN
asignaturas=["matematicas", "ingles", "lengua", "fisica", "quimica"]
print(asignaturas[:])

eleccion = input("Elige la asignatura a cursar")
#lo inputado en la variable anterior lo transforma en minusculas
eleccionLower = eleccion.lower()

if eleccionLower in asignaturas[:]:
    print("Asignatura elegida " + eleccion)
else:
    print("Asignatura elegida erronea")
    
#Python es case sensitive, por lo que si ponemos alguna palabra de la lista con una mayuscula que no esta configurada va a dar error
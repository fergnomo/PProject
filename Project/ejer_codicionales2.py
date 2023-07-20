#ejercicios de condicionales

#ejer 1
key = "contrasena"
password = input("Cual es la contraseña: ")

if password == key:
    print("La contraseña es correcta")
else:
    print("Esto va a petar corre")

#ejer 2

a = int(input("Escribe el dividendo: "))
b = int(input("Escribe el divisor: "))

if b == 0:
    print("ERROR")
else:
    print(a/b)
    
#ejer 3

ent = int(input("Escribe un numero entero: "))
if ent % 2 == 0:
    print(f"El numero {ent} es par")
else:
    print(f"El numero {ent} es impar")

#ejer 4
nombre = input("Escribe tu nombre: ")
sexo = input("Escribe el sexo (Hombre o Mujer): ")
nombreUpper = nombre.upper()
sexoUpper = sexo.upper()

if (nombreUpper[1] <= "M" and sexoUpper == "MUJER") or (nombreUpper[1] >= "N" and sexoUpper == "HOMBRE"):
    print("Te toca el grupo A")
else:
    print("Te toca el grupo B")

#ejer 5
salario = int(input("Salario anual: "))
if salario < 10000:
    print("Tipo impositivo: 5%")
elif 10000 < salario < 20000:
    print("Tipo impositivo: 15%")
elif 20000 < salario < 35000:
    print("Tipo impositivo: 20%")
elif 35000 < salario < 60000:
    print("Tipo impositivo: 30%")
elif 60000 < salario:
    print("Tipo impositivo: 45%")
else:
    pass

#ejer 10
alim_veg = ["pimiento", "tofu", "falafel"]
alim_no_veg = ["peperoni", "jamon", "salmon"]

conf = input("¿Te gustaria una pizza vegetariana? ")
if conf.lower() == "si":
    ing = input(f"Elige tu ingrediente {alim_veg}: ").lower()
    if ing in alim_veg:
        print(f"Tu pizza vegetariana lleva tomate, mozzarella y {ing}")
    else:
        print("No disponemos de ese ingrediente vegetariano")
else:
    ing = input(f"Elige tu ingrediente {alim_no_veg}: ").lower()
    if ing in alim_no_veg:
        print(f"Tu pizza no es vegetariana lleva tomate, mozzarella y {ing}")
    else:
        print("No disponemos de ese ingrediente")

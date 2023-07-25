# POO Parte 1 - ¿Que es la programación orientada a objetos? 
    # Consiste en trasladar la naturaleza de los objetos de la vida real al código de programación
    # Los objetos tienen un estado, un comportamiento y unas propiedades
    # Lenguajes que hacen esto C++, Java, Visual.net, etc
    # Programas divididos en "trozos"
    # Muy re utilizable. Herencia
    # Si existe fallo en alguna línea de código, el programa continuará con su funcionamiento. Tratamiento de excepciones
    # Encapsulamiento

# Desventajas programación orientada a procedimientos
    # Las lineas de código son muchas
    # En aplicaciones completas son difíciles de descifrar
    # Poco re utilizable
    # Si existe fallo en alguna linea del código, es muy probable que el programa caiga
    # Aparición frecuente de código espagueti
    # Difícil de depurar por otros programadores en caso de necesidad o error

# POO Parte 2 - Conceptos o términos de la POO
    # Clase: Modelo donde se redactan las características comunes de un grupo de objetos
    # Ejemplar/instancia/objeto de clase
    # Modularización: Cuando creas una aplicación compleja, lo normal es que este formada por varias clases. Y el concepto deriva de que una aplicación puede estar compuesta por distintas clases
        # Si no funciona una de las clases de la Modularización  el programa seguirá funcionando aunque la parte rota no lo haga
    # Encapsulamiento: Lo que se encuentra dentro de una clase es independiente al resto de lo que tiene las clases y no saben una de la otra
    # Métodos de acceso: Con esto se consiguen conectar las clases de un programa
    # Para poder acceder a la propiedades y comportamiento de un objeto se utiliza la nomenclatura del punto

#Poo Parte 3 - Ejemplo de código
#Construcción de una clase

class Coche():
   
# los objetos que creemos en esta clase todos tendrán las mismas características
# si queremos que esas características comunes sean por defecto estas formaran un estado inicial y se especifican con un CONSTRUCTOR
    def __init__(self): #Constructor que agrupa las características de la clase. este tiene doble barras bajas antes y después

        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4 #esta variable esta encapsulada. se necesita tener dos guiones bajos delante
        self.__enMarcha = False #las variables encapsuladas solo se pueden modificar mediante un método

    def arrancar(self, arrancamos): #este método se utiliza para indicar a la clase si vamos a poner enMarcha el coche o no, pasandole por parámetros True o False, si lo arrancamos o no
        
        self.__enMarcha=arrancamos
        
        if (self.__enMarcha):
            chequeo=self.__chequeo_interno()
        
        if(self.__enMarcha and chequeo): 
            return "El coche está encendido."
        
        elif(self.__enMarcha and chequeo == False):
            return "No podemos arrancar"
        
        else:
            return "El coche esta parado"
        
    def estado(self): #con este método únicamente se imprimen las características del coche
        print("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.__anchoChasis, " y un largo de ", self.__largoChasis)
               
    def __chequeo_interno(self):  #método encapsulado
        print("Realizando Chequeo Interno...")
        
        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"
        
        if self.gasolina == "ok" and self.aceite == "ok" and self.puertas=="cerradas":
            return True
        else:
            return False
        
miCoche=Coche() #primera instancia de clase

#print(f"El largo del coche es {miCoche.largoChasis}")
#print(f"Las ruedas del coche son {miCoche.ruedas}")
print(miCoche.arrancar(True))
miCoche.estado()

print("\nA continuación creamos el segundo objeto\n")

miCoche2=Coche() #segunda instancia de clase
#miCoche2.__ruedas = 2 --- esto no se debería permitir, para ello se utiliza la encapsulación, que se basa en proteger una variable para que no se pueda modificar desde fuera de la clase
                        #con la variable encapsulada no se puede cambiar hardcodeando

#print(f"El largo del coche es {miCoche2.largoChasis}")
#print(f"Las ruedas del coche son {miCoche2.ruedas}")
print(miCoche2.arrancar(False))
miCoche2.estado()

# también se pueden encapsular métodos
# POO Parte 5


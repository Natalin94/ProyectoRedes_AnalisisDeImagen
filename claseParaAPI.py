import math
import psycopg2, psycopg2.extras

conn = psycopg2.connect(database='Proyecto_Redes',user='postgres',password='123456', host='localhost')

cur = conn.cursor()

cur.execute("SELECT * FROM estudiante")
rows=cur.fetchall()
conn.close

class Figura:
    def __init__(self, nombre, largo, ancho):
        self.nombre= nombre
        self.largo=largo
        self.ancho=ancho

        # perimetro, area y radio

    # La altura es para cuando es un triangulo.
    # El radio es para cuando es un círculo.

    # Determinar según la figura lo siguiente:
    # TODAS:
    # Perimetro
    # Área
    # Circulo:
    # radio
    # Rectangulo:
    # largo y ancho
    # Triangulo
    # Altura
    # Cuadrado:
    # lados y diagonal
    #perimetro, area, circunferencia y radio
    def circleProperties(self):
        # perimetro
        pi = math.pi
        perimetro = int(pi * self.largo)
        print("El perimetro es: ", perimetro)
        # radio
        radio = int(self.largo / 2)
        print("El radio es: ",radio)
        # area
        area = int(pi * radio ** 2)
        # enviar los valores que se acaban de obtener a la base de datos no sé en que formato se define, supongo que json.
    # perimetro, area, lados y diagonal
    def squareProperties(self):
        print("Llega a la funcion del cuadrado")
        # area
        raiz = math.sqrt(2)
        area = int(self.largo ** 2)
        perimetro = int(self.largo * 4)
        diagonal = int(raiz * self.largo)
        print("El aread del cuadrado es: ",area)

        # enviar los valores que se acaban de obtener a la base de datos no sé en que formato se define, supongo que json.

    # perimetro, area, ancho y largo y diagonal
    def rectangleProperties(self):
        print("Llega a la funcion del rectangulo")
        # largo y ancho
        largo = self.largo
        ancho = self.ancho
        # diagonal
        paraDiagonal = int((largo ** 2) + (ancho ** 2))
        diagonal = math.sqrt(paraDiagonal)
        # area
        area = int(largo * ancho)
        perimetro = int(2 * (largo + ancho))
        print("El perimetro del rectangulo es: ",perimetro)

        # enviar los valores que se acaban de obtener a la base de datos no sé en que formato se define, supongo que json.

    # Existen 3 diferentes tipos de triangulos, lo que equivale a 3 diferentes formas de calcular el area
    # seremos humildes y solo calcularemos una (el equilatero)
    # perimetro, area, altura y base
    def trianguleProperties(self):
        print("Llega a la funcion del triangulo")
        raizTres = math.sqrt(3)
        area = int((raizTres / 4) * self.ancho)  # el ancho es la linea de abajo (la base)
        perimetro = int(self.ancho * 3)
        altura = int((raizTres * self.ancho) / 2)
        base = int(self.ancho)
        print("La altura del triangulo es: ", altura)

        # enviar los valores que se acaban de obtener a la base de datos no sé en que formato se define, supongo que json.

    def pentagonProperties(self):
        print("Figura fuera del conocimiento. Pronto lo lograremos.")

#Defino a donde mandarlo
    def determinarFigura(self):
        if(self.nombre=="circle"):
            print("Es circulo")
            self.circleProperties()
        elif(self.nombre=="square"):
            print("Es cuadrado")
            self.squareProperties()
        elif(self.nombre=="rectangle"):
            print("Es rectangulo")
            self.rectangleProperties()
        elif(self.nombre=="triangule"):
            print("Es triangulo")
            self.trianguleProperties()
        elif(self.nombre=="pentagon"):
            print("Es complicado amigo...")
            self.pentagonProperties()


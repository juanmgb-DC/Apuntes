x= 10

match x:
    case 10:
        print("X é 10")
    case 20:
        print("X é 20")
    case 30:
        print("X é 30")
    case 40:
        print("X é 40")
    case _:
        print("X non é 10,20,30,40")

match x:
    case 10|20|30:
        print(f"X é {x}")
    case _:
        print("X non é 10,20 ou 30")

y=20

match x:
    case 10 if y % 2 == 0:
        print("X é 10 e Y divisible entre 2")
    case 10:
        print("X é 10 e Y non divisible entre 2")
    case _:
        print("Opción descoñecida")


l = (2,3,5)

match l:
    case (x,y):
        print(f"Colección con dous elementos,{x},{y}")
    case (x, y, z):
        print(f"Colección con tres elementos,{x},{y},{z}")
    case _:
        print ("Formato descoñecido")


l = (2,3,5)

match l:
    case (2,3):
        print("Colección con dous elementos,2, 2")
    case (2, 3, 5):
        print("Colección con tres elementos,2,3,5")
    case _:
        print ("Formato descoñecido")

persoa = {"nome" : "Manuel","curso" : "Dam"}

match persoa:
    case {"nome" : nome, "curso": curso}:
        print(f"Nome: {nome}, curso: {curso}.")
    case {"nome": nome}:
        print(f"Nome: {nome}")
    case _:
        print("Formato descoñecido")



persoa = {"nome" : "Manuel","curso" : "Dam", "edade" : 19}

match persoa:
    case {"nome" : nome, "curso": curso}:
        print(f"Nome: {nome}, curso: {curso}.")
    case {"nome": nome}:
        print(f"Nome: {nome}")
    case _:
        print("Formato descoñecido")


class Figura:
    pass

class Circulo (Figura):
    def __init__(self,radio):
        self.radio = radio

class Rectangle (Figura):
    def __init__(self,ancho,alto):
        self.ancho = ancho
        self.alto = alto

f = Circulo(15)
f = Rectangle (10,12)
match f:
    case Circulo (radio = r):
        print (f"A figura é un circulo con radio {r}")
    case Rectangle (ancho = anc ,alto = alt):
        print(f"A figura é un rectangulo con ancho {anc} e alto {alt}")
    case _:
        print ("Figura descoñecida")



obxecto= "XXXX"

match obxecto:
    case int (x):
        print("É un enteiro")
    case str(cad):
        print(f"É unha cadea {cad}")
    case float(x) :
        print(f"É un float {x}")
    case _:
        print ("Clase descoñecida")





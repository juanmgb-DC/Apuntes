class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __eq__(self, other):
        # Compara nombre y edad
        if isinstance(other, Persona):
            return self.nombre == other.nombre and self.edad == other.edad
        return False

p1 = Persona("Juan", 30)
p2 = Persona("Juan", 30)
print(p1 == p2)  # Devuelve True
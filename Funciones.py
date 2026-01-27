def saudo():
    print("Ola")

benvida = saudo
print (benvida)
benvida()

def suma(a,b):
    return a + b

adicion = suma
print(adicion(1,2))

def executa(f,v1,v2):
    return f(v1, v2)

resultado = executa(suma, 2 , 2)
print(resultado)

def multiplica(y):
    def producto (x):
        return x * y
    return producto

dobre = multiplica(2)
print(dobre)
print(dobre(5))

def decorador(func):
    def envoltorio():
        print("Executa antes da funcion",func.__name__)
        func()
        print("Se executa despois da funcion",func.__name__)
    return envoltorio

funcionDecorada = decorador(saudo())
print (funcionDecorada)
decorador(saudo())

def saudo2():
    print("Ola2")
    saudo2()


def decorador2(func):
    def envoltorio (*args, **kwargs):
        print("Antes da execucion")
        resultado = func (*args, **kwargs)
        print("Despois da execucion")
        return resultado
    return envoltorio

decorador2(suma(3,3))
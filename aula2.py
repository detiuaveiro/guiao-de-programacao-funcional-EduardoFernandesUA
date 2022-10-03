from functools import reduce

#Exercicio 4.1
impar = lambda x: x % 2 != 0 

#Exercicio 4.2
positivo = lambda x: x > 0 and x != 0 

#Exercicio 4.3
comparar_modulo = lambda a, b: abs(a) < abs(b) 

#Exercicio 4.4
from math import atan, sqrt, pi
cart2pol = lambda x,y: (sqrt(x**2 + y**2), atan(y/x) if x!=0 else pi/2)

#Exercicio 4.5
ex5 = lambda f,g,h: lambda x,y,z: h(f(x,y), g(y,z))

#Exercicio 4.6
def quantificador_universal(lista, f):
    if lista == []:
        return True

    return f(lista[0]) and quantificador_universal(lista[1:], f)

def subconjunto(lista1, lista2):
    if lista1 == []:
        return True

    return lista1[0] in lista2 and subconjunto(lista1[1:], lista2)

#Exercicio 4.9
def ordem(lista, f):
    if not lista: return None
    return reduce(lambda ret,elem: elem if f(elem,ret) else ret, lista)

#Exercicio 4.10
def filtrar_ordem(lista, f):
    if not lista: return None
    n = ordem(lista,f)
    return (n, list(filter(lambda elem: elem!=n, lista)))

#Exercicio 5.2
def ordenar_seleccao(lista, ordem):
    if not lista: return None
    return sorted(lista, reverse=ordem(1,0)==1)

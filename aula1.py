#Exercicio 1.1
def comprimento(lista):
	if not lista: return 0
	return 1 + comprimento(lista[1:])

#Exercicio 1.2
def soma(lista):
	if not lista: return 0
	return lista[0] + soma(lista[1:])

#Exercicio 1.3
def existe(lista, elem):
	if not lista: return False
	if lista[0]==elem: return True
	return existe(lista[1:], elem)

#Exercicio 1.4
def concat(l1, l2):
	if not l2: return l1
	return concat(l1+l2[:1], l2[1:])

#Exercicio 1.5
def inverte(lista):
	if not lista: return lista
	return inverte(lista[1:]) + lista[:1]

#Exercicio 1.6
def capicua(lista):
	if not lista: return True
	if lista[0] != lista[-1]: return False
	return capicua(lista[1:-1])

#Exercicio 1.7
def explode(lista):
	if not lista: return lista
	return lista[:1][0] + explode(lista[1:])

#Exercicio 1.8
def substitui(lista, original, novo):
	if not lista: return lista
	if lista[0]==original:
		return [novo] + substitui(lista[1:], original, novo)
	else:
		return lista[:1] + substitui(lista[1:], original, novo)

#Exercicio 1.9
def junta_ordenado(lista1, lista2):
	if not lista1: return lista2
	if not lista2: return lista1
	if lista1[0] < lista2[0]:
		return lista1[:1] + junta_ordenado(lista1[1:], lista2)
	else:
		return lista2[:1] + junta_ordenado(lista1, lista2[1:])
	

#Exercicio 2.1
def separar(lista):
	if not lista: return [],[]
	a, b = lista[0]
	c, d = separar(lista[1:])
	return ([a]+c, [b]+d)

#Exercicio 2.2
def remove_e_conta(lista, elem):
	if not lista: return [], 0
	a, b = remove_e_conta(lista[1:], elem)
	if lista[0]==elem:
		return (a, b+1)
	else:
		return (lista[:1]+a, b+0)

#Exercicio 3.1
def cabeca(lista):
	if not lista: return None
	return lista[0]

#Exercicio 3.2
def cauda(lista):
	if not lista: return None
	return lista[1:]

#Exercicio 3.3
def juntar(l1, l2):
	if len(l1)!=len(l2): return None
	if not l1 and not l2: return []
	return [(l1[0], l2[0])] + juntar(l1[1:], l2[1:])

#Exercicio 3.4
def menor(lista):
	if not lista: return None
	a = menor(lista[1:])
	print(lista, a)
	return a if a!=None and a<lista[0] else lista[0]

#Exercicio 3.6
def max_min(lista): # -> (max, min)
	if not lista: return None
	a = max_min(lista[1:])
	return (a[0] if a[0]>lista[0] else lista[0], a[1] if a[1]<lista[0] else lista[0])

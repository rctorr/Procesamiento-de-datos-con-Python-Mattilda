lista = [1,2,3,4,5,6,7,8,9,10]

# Usando función map
def elevar_al_cuadrado(valor):
    return valor ** 2

lista_2 = list(map(elevar_al_cuadrado, lista))
print(lista_2)

elevar_al_cuadrado_l = lambda valor: valor ** 2
lista_3 = list(map(elevar_al_cuadrado_l, lista))
print(lista_3)


lista_3 = list(map(lambda valor: valor ** 2, lista))
print(lista_3)

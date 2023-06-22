lista_1 = [3.4, 0.7, 99.9, 5.41, 6.23, 7.9]
lista_2 = [3.4, 63.4, 0.7, 6.46, 99.9, 2.2, 5.41]
lista_2.pop(1)  # -> 63.4
lista_2.pop(2)  # -> 6.46
lista_2.pop(-2)  # -> 2.2
# lista_2.append(6.23)
# lista_2.append(7.9)
# lista_2 -> [3.4, 0.7, 99.9, 5.41]
lista_2 = lista_2 + [6.23, 7.9]

if lista_1 == lista_2:
    print("Tú y yo somos uno mismo")


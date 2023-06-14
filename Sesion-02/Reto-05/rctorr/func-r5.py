def numero_es_par(numero):  # numero = 3
    print("uno")
    residuo = numero % 2
    if residuo == 0:
        return True
    else:
        return False

def numero_es_par(numero):  # numero = 3
    print("dos")
    return (numero % 2) == 0


if __name__ == "__main__":
    print( numero_es_par(3) )
    print( numero_es_par(6) )
    print( numero_es_par(3) )
    print( numero_es_par(6) )



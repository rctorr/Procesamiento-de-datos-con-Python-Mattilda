import csv

proporciones = [0.45, 0.2, 0.78, 0.4, 0.77, 0.9, 0.4, 0.5, 0.67, 0.24, 0.73, 0.59]
def proporcion_a_porcentajes(x):  # proporcion <- 0.45
#    porcentaje = proporcion * 100
#    return porcentaje
    return x * 100
def imprime_propociones_y_porcentajes(datos):
    """ Imprime la lista de parejas de datos de proporciones y porcentajes
    contenidas en datos."""
    for fila in datos:  # fila -> (0.45, 45.0) <- tupla, fila[0] -> 0.45, fila[1] -> 45.0
        print(f"{fila[0]:5.2f}  {fila[1]:5.0f}%")

def exporta_a_csv(datos):
    """ Exporta la lista de parejas de datos de proporciones y porcentajes
    contenidos en datos al archivo porcentajes.csv """
    with open("porcentajes.csv", "w", newline="") as arch:
        csv_escritor = csv.writer(arch)
        csv_escritor.writerows(datos)

def mayor_a_05(valor):  # float
    return valor > 0.5

def menor_a_05_mayor_a_20p(valor):  # tupla -> (0.45, 45.0)
    return valor[0] <= 0.5 and valor[1] > 20.0

#    if valor > 0.5:
#        return True
#    else:
#        return False

def menor_05_y_mayor_20p_o_059(valor):  # tupla
#    return menor_a_05_mayor_a_20p(valor) or valor[0] == 0.59 or valor[0] == 0.73
    valores_especiales = [0.59, 0.73, 0.67]
    valores_negados = [0.4, 0.5]
    return (menor_a_05_mayor_a_20p(valor) or valor[0] in valores_especiales) and valor[0] not in valores_negados

porcentajes = list( map(proporcion_a_porcentajes, proporciones) )  # dict( map(...) )
datos = list( zip(proporciones, porcentajes) )  # Se puede hacer uso de la función zip()

print(proporciones)
print(porcentajes)
print(datos)
imprime_propociones_y_porcentajes(datos)

# Exportamos los datos a formato CSV
exporta_a_csv(datos)

# Filtrando lista
proporciones_filtradas = list( filter(mayor_a_05, proporciones) )
print(proporciones_filtradas)

# Filtrando datos por un intervalo
datos_filtrados = list( filter(menor_a_05_mayor_a_20p, datos) )
imprime_propociones_y_porcentajes(datos_filtrados)

# filtrando datos por intervalo más uno 1
datos_filtrados_1 = list( filter(menor_05_y_mayor_20p_o_059, datos) )
print(datos_filtrados_1)
imprime_propociones_y_porcentajes(datos_filtrados_1)

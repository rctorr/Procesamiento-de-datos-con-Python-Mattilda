import csv

proporciones = [0.45, 0.2, 0.78, 0.4, 0.77, 0.9, 0.4, 0.5, 0.67, 0.24, 0.73]
def proporcion_a_porcentajes(proporcion):
    porcentaje = proporcion * 100
    return porcentaje

def imprime_propociones_y_porcentajes(datos):
    """ Imprime la lista de parejas de datos de proporciones y porcentajes
    contenidas en datos."""
    for reg in datos:
        print(f"{reg[0]:5} -> {reg[1]}%")

porcentajes = list(map(proporcion_a_porcentajes, proporciones))
datos = list(zip(proporciones, porcentajes))
#print(proporciones)
#print(porcentajes)
print(datos)
imprime_propociones_y_porcentajes(datos)

with open("porcentajes.csv", "w") as arch:
    escribir_csv = csv.writer(arch)
    escribir_csv.writerows(datos)

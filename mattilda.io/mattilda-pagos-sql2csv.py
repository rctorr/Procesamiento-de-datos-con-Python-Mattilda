import sqlite3
import csv

con = sqlite3.connect("mattilda-cobranza.sqlite3")
cur = con.cursor()
cur.execute("SELECT * FROM pagos")
pagos = cur.fetchall()
cur.close()
con.close()

numreg = 0
numarch = 0
arch = None
for reg in pagos:
    if numreg % 10000 == 0:
        if arch:
            arch.close()
        numarch += 1
        archnom = f"pagos/pagos-{numarch:03d}.csv"
        arch = open(archnom, "w", newline="")
        csv_escritor = csv.writer(arch)
    csv_escritor.writerow(reg)
    numreg += 1


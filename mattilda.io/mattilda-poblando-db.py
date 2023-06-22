import random
import sqlite3
from faker import Faker

# Crear instancia de Faker
fake = Faker()

# Conexión a la base de datos SQLite3
conn = sqlite3.connect('matilda-cobranza.sqlite3')
cursor = conn.cursor()

# Generar datos aleatorios para la tabla Escuelas
def generar_escuelas(cantidad):
    for _ in range(cantidad):
        nombre_escuela = fake.company()
        direccion = fake.address().replace("\n", ", ")
        cursor.execute("INSERT INTO Escuelas (nombre_escuela, direccion) VALUES (?, ?)", (nombre_escuela, direccion))
    conn.commit()

# Generar datos aleatorios para la tabla Administradores
def generar_administradores(cantidad, num_escuelas):
    for _ in range(cantidad):
        id_escuela = random.randint(1, num_escuelas)
        nombre_administrador = fake.name()
        puesto = fake.job()
        cursor.execute("INSERT INTO Administradores (id_escuela, nombre_administrador, puesto) VALUES (?, ?, ?)",
                       (id_escuela, nombre_administrador, puesto))
    conn.commit()

# Generar datos aleatorios para la tabla Padres
def generar_padres(cantidad):
    for _ in range(cantidad):
        nombre_padre = fake.name()
        direccion = fake.address().replace("\n", ", ")
        cursor.execute("INSERT INTO Padres (nombre_padre, direccion) VALUES (?, ?)", (nombre_padre, direccion))
    conn.commit()

# Generar datos aleatorios para la tabla Hijos
def generar_hijos(cantidad, num_padres):
    for _ in range(cantidad):
        id_padre = random.randint(1, num_padres)
        nombre_hijo = fake.first_name()
        fecha_nacimiento = fake.date_of_birth().strftime("%Y-%m-%d")
        cursor.execute("INSERT INTO Hijos (id_padre, nombre_hijo, fecha_nacimiento) VALUES (?, ?, ?)",
                       (id_padre, nombre_hijo, fecha_nacimiento))
    conn.commit()

# Generar datos aleatorios para la tabla Pagos
def generar_pagos(cantidad, num_escuelas, num_padres, num_hijos):
    for _ in range(cantidad):
        id_escuela = random.randint(1, num_escuelas)
        id_padre = random.randint(1, num_padres)
        id_hijo = random.randint(1, num_hijos)
        monto = random.uniform(1000, 10000)
        fecha_pago = fake.date_between(start_date='-5y', end_date='today').strftime("%Y-%m-%d")
        cursor.execute("INSERT INTO Pagos (id_escuela, id_padre, id_hijo, monto, fecha_pago) VALUES (?, ?, ?, ?, ?)",
                       (id_escuela, id_padre, id_hijo, monto, fecha_pago))
    conn.commit()

# Generar datos de muestra
cantidad_escuelas = 30000
cantidad_administradores = 75000
cantidad_padres = 950000
cantidad_hijos = 1150000
cantidad_pagos = 5700000

generar_escuelas(cantidad_escuelas)
generar_administradores(cantidad_administradores, cantidad_escuelas)
generar_padres(cantidad_padres)
generar_hijos(cantidad_hijos, cantidad_padres)
generar_pagos(cantidad_pagos, cantidad_escuelas, cantidad_padres, cantidad_hijos)

# Cerrar conexión a la base de datos
conn.close()


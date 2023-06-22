## Descripción del proyecto mattilda.io

Esta carpeta contiene varios archivos para hacer una pequeña simulación de la base de datos SQL que tendría el proyecto Mattilda.

Acontinuación se describen la lista de archivos:
- mattilda-cobranza.sql: Archivo con las instruciones SQL para crear todas las tablas y sus relaciones utilizadas.
- mattilda-cobranza.sqlite3: Archivo de la base de datos usando el motor SQLite3
- mattilda-cobranza.zip: Archivo mattilda-cobranza.sqlite3 comprimido
- mattilda-poblando-db.py: Script en Python que genera datos aleatorios para llenar todas las tablas con aproximadamente 6 millones de registros.
- pagos/: Carpeta que contiene una lista de archivos en formato CSV y cada archivo contiene un lote de 10,000 pagos realizados.
- pagos.zip: Contenido de la carpeta pagos/ comprimido.
- mattilda-pagos-sql2csv.py: Programa en Python usada para generar todos los archivos de la carpeta pagos/ donde cada archivo cuenta con 10,000 registros.


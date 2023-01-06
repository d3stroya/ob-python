import psycopg2

# 1. Conectar con una base de datos
conn = psycopg2.connect(database='pythondb', user='postgres', password='admin', host='127.0.0.1', port='5432')
print('Connection to database estabilshed.')

# 2. Crear una tabla
# Creamos un cursos y ejecutamos una consulta sql
cur = conn.cursor()
#cur.execute('''
#    CREATE TABLE films(
#        ID INT PRIMARY KEY NOT NULL,
#        NAME VARCHAR(50) NOT NULL,
#        YEAR INT NOT NULL,
#        DIRECTOR VARCHAR(30) NOT NULL
#    );
#''')
#print('Table created.')

# Confirmamos los cambios y cerramos la conexión
#conn.commit()
#conn.close()

# 3. Insertar registros
#cur.execute('''
#    INSERT INTO films VALUES(
#        1, 'Le fabuleux destin d`Amélie Poulain', 2001, 'Jean Pierre Jeunet'
#    );
#''')
#
#cur.execute('''
#    INSERT INTO films VALUES(
#        2, 'Ikiru', 1952, 'Akira Kurosawa'
#    );
#''')
#
#cur.execute('''
#    INSERT INTO films VALUES(
#        3, 'Las niñas', 2020, 'Pilar Palomero'
#    );
#''')
#
#cur.execute('''
#    INSERT INTO films VALUES(
#        4, 'La llamada', 2018, 'Los Javis'
#    );
#''')
#print('Records created')
#conn.commit()
#conn.close()

# 4. Recuperar registros
# Seleccionamos todos los registros de la tabla
cur.execute('''
    SELECT * FROM films;
''')

# Los traemos como tuplas: 
# [columna1][columna2][columna3]
# ([datos1], [datos2], [datos3])
# ([datos1], [datos2], [datos3])
# ([datos1], [datos2], [datos3])
rows = cur.fetchall()

# Iteramos
for row in rows:
    print(row[0], '-', row[1], '(', row[2], '), directed by', row[3])

print('Operation done succefully')
#conn.close()

# 5. Actualizar registros
#cur.execute('''
#    UPDATE films SET 
#    year=2017, 
#    director='J.Ambrossi, J.Calvo'
#    WHERE id=5;
#''')
#print('Total number of rows updated:', cur.rowcount)
#
#conn.commit()
#conn.close()

# 6. Eliminar registros
cur.execute('''
    DELETE FROM films WHERE id=4;
''')
print('Total number of rows deleted:', cur.rowcount)

conn.commit()


for row in rows:
    print(row[0], '-', row[1], '(', row[2], '), directed by', row[3])

print('Operation done succefully')
conn.close()

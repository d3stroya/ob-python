# Python y PostgreSQL
Referencia: https://www.tutorialspoint.com/postgresql/postgresql_python.htm

1. Instalamos psycopg2: ```pip install psycopg2-binary```.
2. Creamos la base de datos en pgAdmin.
3. Conectamos con la base de datos: ```conn = psycopg2.connect(database='', user='', password='', host='', port='')```.
4. Creamos un cursor: ```conn.cursor()```.
5. Ejecutamos sentencias SQL: ```cur.execute([sentencia SQL])```.
6. Confirmamos las transacciones: ```conn.commit()```.
7. Cerramos la conexión: ```conn.close()```.
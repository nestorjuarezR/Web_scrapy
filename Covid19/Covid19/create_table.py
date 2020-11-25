import psycopg2


TABLE_DATA = ''' CREATE TABLE data(
    countries TEXT NOT NULL,
    cases INTEGER NOT NULL,
    deaths INTEGER NOT NULL
    )'''


try:
    connection = psycopg2.connect(
        host = 'localhost',
        user = 'nestorjr',
        password = '123456',
        dbname = 'covid19')
    print('<----- Conexion exitosa ----->')


    with connection.cursor() as cursor:
         cursor.execute(TABLE_DATA)
         connection.commit()
         connection.close()

except psycopg2.Error as error:
    print('Error con la conexion !!!', error)
import mysql.connector
try:
    connection = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='363118050maty',
        db='project',
        ssl='TLS_AES_256_GCM_SHA384'
    )

    if connection.is_connected():
        print("conexion exitosa cat")
except Exception as ex:
    print(ex)        
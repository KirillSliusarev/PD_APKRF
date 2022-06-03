import mysql.connector
import os

HOST = os.getenv('SQL_HOST')
USER = os.getenv('SQL_USER')
PASSWORD = os.getenv('SQL_PASSWORD')

# Чистит БД от изменений внесённых кодом
try:
    with mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database="apkrf",
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute("UPDATE studs SET studs.nap = NULL")
            cursor.execute('UPDATE naps SET studs = ""')
            connection.commit()

except mysql.connector.Error as e:
    print(e)

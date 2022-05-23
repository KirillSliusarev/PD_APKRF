import mysql.connector


try:
    with mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="apkrf",
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute("UPDATE studs SET studs.nap = NULL")
            cursor.execute('UPDATE naps SET studs = ""')
            connection.commit()

except mysql.connector.Error as e:
    print(e)

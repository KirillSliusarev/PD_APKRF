from classes import nap, student
import mysql.connector
import os

HOST = os.getenv('SQL_HOST')
USER = os.getenv('SQL_USER')
PASSWORD = os.getenv('SQL_PASSWORD')


#Поток льготников

try:
    with mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database="apkrf",
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT PersonID, naps, score, name, lgot, additions, golden_medal FROM studs WHERE lgot = 1")
            result = cursor.fetchall()
            for row in result:
                student(row[0], list(map(int, row[1].split(', '))), [row[2]], row[3], row[4], row[5], row[6])
        with connection.cursor() as cursor:
            cursor.execute("SELECT places, lgot_places, studs FROM naps")
            result = cursor.fetchall()
            for row in result:
                nap(int(row[0]), row[1])
except mysql.connector.Error as e:
    print(e)

for j in range(len(nap.naplist)):
    for stud in student.studslist:
        for i in stud.p:
            if stud in nap.naplist[i].studs:
                break
            elif nap.naplist[i].add_lgot(stud):
                break

try:
    with mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database="apkrf",
    ) as connection:
        with connection.cursor() as cursor:
            for stud in student.studslist:
                for napn in nap.naplist:
                    if stud in napn.studs:
                        cursor.execute(f"UPDATE studs SET studs.nap = {napn.id} WHERE studs.PersonID = {stud.id}")
            for napn in nap.naplist:
                cursor.execute(
                    f'UPDATE naps SET studs = "{nap.naplist[napn.id].get_names_string()}" WHERE NapID = {napn.id}')
            connection.commit()

except mysql.connector.Error as e:
    print(e)

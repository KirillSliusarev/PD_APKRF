from classes import nap, student
import mysql.connector

try:
    with mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="apkrf",
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM studs WHERE nap is NULL")
            result = cursor.fetchall()
            for row in result:
                student(row[0], list(map(int, row[4].split(', '))), [row[2]], row[1], row[5], row[6], row[7])
        with connection.cursor() as cursor:
            cursor.execute('SELECT places, lgot_places FROM naps')
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
            elif nap.naplist[i].add_student(stud):
                break

try:
    with mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="apkrf",
    ) as connection:
        with connection.cursor() as cursor:
            for stud in student.studslist:
                for napn in nap.naplist:
                    if stud in napn.studs:
                        cursor.execute(f"UPDATE studs SET studs.nap = {napn.id} WHERE studs.PersonID = {stud.id}")
            for napn in nap.naplist:
                cursor.execute(
                    f'UPDATE naps SET naps.studs = CONCAT(naps.studs, " {nap.naplist[napn.id].get_names_string()}") WHERE NapID = {napn.id}')
            connection.commit()

except mysql.connector.Error as e:
    print(e)

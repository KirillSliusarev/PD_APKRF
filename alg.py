import mysql.connector
from classes import nap, student

try:
    with mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="apkrf",
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM studs")
            result = cursor.fetchall()
            for row in result:
                student(list(map(int, row[4].split(', '))), [row[2]])
        with connection.cursor() as cursor:
            cursor.execute("SELECT places FROM naps")
            result = cursor.fetchall()
            for row in result:
                nap(int(row[0]))
except mysql.connector.Error as e:
    print(e)


for j in range(2):
    for stud in student.studslist:
        for i in stud.p:
            if stud in nap.naplist[i - 1].studs:
                break
            elif nap.naplist[i - 1].add_student(stud):
                break
a = []
for x in nap.naplist[0].studs:
    a.append(x.ss)
print(a)
a.clear()
for x in nap.naplist[1].studs:
    a.append(x.ss)
print(a)
print(student.studslist)

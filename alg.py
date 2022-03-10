class nap:

    naplist = []

    def __init__(self, places):
        self.p = places
        self.id = len(nap.naplist)
        self.studs = []
        nap.naplist.append(self)

    def add_student(self, student):
        if len(self.studs) < self.p:
            self.studs.append(student)
            self.minscore = min(self.studs, key=lambda x: x.ss).ss
            return True
        elif self.minscore < student.ss:
            self.studs.append(student)
            self.studs.remove(min(self.studs, key=lambda x: x.ss))
            return True
        else: return False


class student:

    studslist = []

    def __init__(self, prefer, score):
        self.p = prefer
        self.s = score
        self.ss = sum(score)
        self.id = len(student.studslist)
        student.studslist.append(self)


nap1 = nap(2)
nap2 = nap(4)
s1 = student([1,2],[99])
s2 = student([1,2],[98])
s3 = student([1,2],[97])
s4 = student([1,2],[96])
s5 = student([2,1],[95])
s6 = student([2,1],[94])
s7 = student([2,1],[93])
s8 = student([1,2],[100])

for j in range(2):
    for stud in student.studslist:
        for i in stud.p:
            if stud in nap.naplist[i-1].studs:
                break
            elif nap.naplist[i-1].add_student(stud):
                break
a = []
for x in nap1.studs:
    a.append(x.ss)
print(a)
a.clear()
for x in nap2.studs:
    a.append(x.ss)
print(a)

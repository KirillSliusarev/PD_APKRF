class student:

    studslist = []

    def __init__(self, prefer, score):
        self.p = prefer
        self.s = score
        self.ss = sum(score)
        self.id = len(student.studslist)
        student.studslist.append(self)

    def __repr__(self):
        return "{0} {1} {2} \n".format(self.id, self.ss, self.p)

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
            self.minscore = min(self.studs, key=lambda x: x.ss).ss
            return True
        else: return False

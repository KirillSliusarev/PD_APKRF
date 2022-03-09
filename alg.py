class nap:

    naplist = []

    def __init__(self, places, id):
        self.p = places
        self.id = len(nap.naplist)
        self.studs = []
        nap.naplist.append(self)

    def add_student(self, student):
        if len(self.studs) < self.p:
            self.studs.append(student.ss)
            self.studs.sort()
            self.minscore = min(self.studs)
            return True
        elif self.minscore < student.ss:
            self.studs.append(student.ss)
            self.studs.sort()
            self.studs.remove(min(self.studs))
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
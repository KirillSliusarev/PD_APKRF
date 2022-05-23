class student:
    studslist = []
    lgotlist = []

    def __init__(self,id, prefer, score, name, lgot, additions, golden_medal):
        self.p = prefer
        self.s = score
        self.ss = sum(score) + additions + golden_medal
        self.id = id
        self.name = name
        self.lgot = lgot
        if self.lgot:
            student.lgotlist.append(self)
        student.studslist.append(self)

    def __repr__(self):
        return "{0} {1} {2} {3} \n".format(self.id, self.ss, self.p, self.lgot)


class nap:
    naplist = []

    def __init__(self, places, lgotplaces):
        self.p = places
        self.id = len(nap.naplist)
        self.studs = []
        self.lgotplaces = lgotplaces
        if lgotplaces == 0:
            self.lminscore = 999999
        nap.naplist.append(self)

    def add_lgot(self, student):
        if len(self.studs) < self.lgotplaces:
            self.studs.append(student)
            self.lminscore = min(self.studs, key=lambda x: x.ss).ss
            return True
        elif self.lminscore < student.ss:
            self.studs.append(student)
            self.studs.remove(min(self.studs, key=lambda x: x.ss))
            self.lminscore = min(self.studs, key=lambda x: x.ss).ss
            return True
        else:
            return False


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
            else:
                return False

    def get_names_string(self):
        ret = ""
        for stud in self.studs:
            ret += (str(stud.name) + " ")
        return ret

class Teacher:
    def teach(self):
        print("Professor teaches students")

class Researcher:
    def research(self):
        print("Professor conducts research")

class Professor(Teacher, Researcher):
    def work(self):
        print("Professor performs teaching and research")

professor = Professor()
professor.teach()
professor.research()
professor.work()

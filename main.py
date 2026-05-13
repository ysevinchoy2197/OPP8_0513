# 9-misol
class Kurs:
    def __init__(self, nomi, student_soni):
        self.nomi = nomi
        self.student_soni = student_soni

    def qoshish(self):
        self.student_soni += 1

    def ayirish(self):
        self.student_soni -= 1

    def info(self):
        print(self.nomi, self.student_soni)

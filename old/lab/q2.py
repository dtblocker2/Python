class course():
    def __init__(self,course_name):
        self.course_name = course_name
        self.students = []
    
    def add_student(self,student_name):
        self.students.append(student_name)

    def unique_students(self):
        print(set(self.students))

ma102 = course("MA102")
for i in range(4):
    if i == 3:
        ma102.add_student("S0")
    ma102.add_student(f"S{str(i)}")

print(ma102.students)

ma102.unique_students()
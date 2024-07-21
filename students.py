class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        try:
            return sum(self.grades) / len(self.grades)
        except ZeroDivisionError:
            return 0

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __repr__(self):
        return f"Student '{self.name}', age={self.age}, grades={self.grades}"


class Group:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def best_student(self):
        return max(self.students, default=None)

    def best_student_average(self):
        best_student = self.best_student()
        return best_student.average_grade() if best_student else 0

    def __lt__(self, other):
        return self.best_student_average() < other.best_student_average()

    def __repr__(self):
        return f"{self.name} {self.students}"


def group_with_best_student(groups):
    return max(groups, default=None)


student1 = Student("Ivan", 29, [4, 5, 3, 4])
student2 = Student("Anna", 22, [5, 5, 5, 4])
student3 = Student("Alex", 25, [4, 4, 5, 4])
student4 = Student("Alla", 19, [3, 4, 5, 4])

group1 = Group("RPO 9")
group1.add_student(student1)
group1.add_student(student2)

group2 = Group("RPO 8")
group2.add_student(student3)
group2.add_student(student4)

groups = [group1, group2]

best_group = group_with_best_student(groups)
print(f"Group with best students: {best_group}")

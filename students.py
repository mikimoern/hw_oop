class Student:
    def __init__(self, name: str, age: int, grades: list):
        """
        Initializes a student with a name, age, and a list of grades.

        :param name: Name of the student.
        :param age: Age of the student.
        :param grades: List of the student's grades.
        """
        self.name = name
        self.age = age
        self.grades = grades

    def add_grade(self, grade: int) -> None:
        """
        Adds a grade to the student's list of grades.

        :param grade: Grade to add.
        """
        self.grades.append(grade)

    def average_grade(self) -> float:
        """
        Returns the student's average grade.

        :return: The student's average grade. Returns 0 if there are no grades.
        """
        try:
            return sum(self.grades) / len(self.grades)
        except ZeroDivisionError:
            return 0

    def __lt__(self, other: "Student") -> bool:
        """
        Compares the student with another student based on the average grade.

        :param other: The other student to compare with.
        :return: True if the current student's average grade is less than the other student's average grade, otherwise False.
        """
        return self.average_grade() < other.average_grade()

    def __repr__(self) -> str:
        """
        Returns a string representation of the Student object.

        :return: String representation of the student.
        """
        return f"Student '{self.name}', age={self.age}, grades={self.grades}"


class Group:
    def __init__(self, name: str):
        """
        Initializes a group with a name and a list of students.

        :param name: Name of the group.
        """
        self.name = name
        self.students: list = []

    def add_student(self, student: Student) -> None:
        """
        Adds a student to the group.

        :param student: Student to add.
        """
        self.students.append(student)

    def remove_student(self, student: Student) -> None:
        """
        Removes a student from the group.

        :param student: Student to remove.
        """
        self.students.remove(student)

    def best_student(self) -> str | None:
        """
        Returns the student with the highest average grade in the group.

        :return: The student with the highest average grade or None if the group is empty.
        """
        return max(self.students, default=None)

    def best_student_average(self) -> float:
        """
        Returns the average grade of the best student in the group.

        :return: The average grade of the best student or 0 if the group is empty.
        """
        best_student = self.best_student()
        return best_student.average_grade() if best_student else 0

    def __lt__(self, other: "Group") -> bool:
        """
        Compares the group with another group based on the average grade of the best student.

        :param other: The other group to compare with.
        :return: True if the average grade of the best student in the current group is less than that of the best student in the other group, otherwise False.
        """
        return self.best_student_average() < other.best_student_average()

    def __repr__(self) -> str:
        """
        Returns a string representation of the Group object.

        :return: String representation of the group.
        """
        return f"{self.name} {self.students}"


def group_with_best_student(groups: list) -> str | None:
    """
    Returns the group with the best student among all groups.

    :param groups: List of groups.
    :return: The group with the best student or None if the list of groups is empty.
    """
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

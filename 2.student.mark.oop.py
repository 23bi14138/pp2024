class student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob
    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, DoB: {self.dob}"

class course:
    def __init__(self, course_id, name):
        self.id = course_id
        self.name = name
    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"

class Mark:
    def __init__(self):
        self.mark = {}
    def add_mark(self, course_id, student_id, mark):
        if course_id not in self.mark:
            self.mark[course_id] = {}
        self.marks[course_id][student_id] = mark
    def course_mark(self, course_id):
        return self.marks.get(course_id, None)

class option:
    def __init__(self):
        self.student = []
        self. course = []
        self.mark = mark()
    def input_student(self):
        print("Input number of student: ")
        count = int(input())
        for _ in range(count):
            print("Enter ID: ")
            student_id = int(input())
            print("Enter st name: ")
            name = str(input())
            print("DoB: ")
            dob = str(input())
            self.student.append(student(student_id, name, dob)
    def input_course(self):
        print("")
        course_count = int(input())

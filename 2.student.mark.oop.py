class student:
    def __init__(self, person_id, name, dob):
        self.id = person_id
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

class Marks:
    def __init__(self):
        self.marks = {}

    def add_mark(self, course_id, student_id, mark):
        

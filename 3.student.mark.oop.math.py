import math
import numpy as np

def input_mark(self)
    print("Enter course ID: ")
    course_id = int(input())
    if not any(course.id == course_id for course in self.courses):
        print("Course not found")
        return
    for student in self.students:
        print(f"Enter mark for {student.id} ({student.name}): ")
        mark = float(input())
        self.mark.add_mark(course_id, student, math.floor(mark * 10)/10)
def gpa(self, student_id):
    total_credits = 0
    total_marks = 0
    for course_id, marks in self.mark.items():
        if student_id in marks:
            total_credits = total_credits + 1
            total_marks = total_marks + marks[student_id]
    if total_credits == 0:
        return 0
    return total_marks / total_credits

def sort(self):
    student_gpa = [(student.id, self.gpa(student.id)) for student in self.students]

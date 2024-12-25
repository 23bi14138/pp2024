import math
import numpy as np
import curses

class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, DoB: {self.dob}"

class Course:
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
        self.mark[course_id][student_id] = mark

    def course_mark(self, course_id):
        return self.mark.get(course_id, None)

    def calculate_gpa(self, student_id):
        total_credits = 0
        total_marks = 0
        for course_id, marks in self.mark.items():
            if student_id in marks:
                total_credits += 1
                total_marks += marks[student_id]
        if total_credits == 0:
            return 0
        return total_marks / total_credits

    def sort_students_by_gpa(self, students):
        student_gpa = [(student.id, self.calculate_gpa(student.id)) for student in students]
        student_gpa.sort(key=lambda x: x[1], reverse=True)
        return student_gpa

class Option:
    def __init__(self):
        self.students = []
        self.courses = []
        self.mark = Mark()

    def input_student(self):
        print("Input number of students: ")
        count = int(input())
        for _ in range(count):
            print("Enter ID: ")
            student_id = int(input())
            print("Enter student name: ")
            name = str(input())
            print("DoB: ")
            dob = str(input())
            self.students.append(Student(student_id, name, dob))

    def input_course(self):
        print("Input number of courses: ")
        course_count = int(input())
        for _ in range(course_count):
            print("Enter course ID: ")
            course_id = int(input())
            print("Enter course name: ")
            name = str(input())
            self.courses.append(Course(course_id, name))

    def list_students(self):
        print("Student list:")
        for student in self.students:
            print(student)

    def list_courses(self):
        print("Course list:")
        for course in self.courses:
            print(course)

    def input_mark(self):
        print("Enter course ID: ")
        course_id = int(input())
        if not any(course.id == course_id for course in self.courses):
            print("Course not found")
            return
        for student in self.students:
            print(f"Enter mark for {student.id} ({student.name}): ")
            mark = float(input())
            self.mark.add_mark(course_id, student.id, math.floor(mark * 10) / 10)

    def show_mark(self):
        print("Enter course ID: ")
        course_id = str(input())
        marks = self.mark.course_mark(course_id)
        if marks is None:
            print("Course not found")
            return
        print(f"Marks for course {course_id}:")
        for student_id, mark in marks.items():
            student_name = next((student.name for student in self.students if student.id == student_id), "Unknown")
            print(f"Student ID: {student_id}, Name: {student_name}, Mark: {mark}")

def run():
    def main(stdscr):
        option = Option()
        while True:
            stdscr.clear()
            stdscr.addstr("\nStudent Management System:\n")
            stdscr.addstr("1. Input student info\n")
            stdscr.addstr("2. Input course info\n")
            stdscr.addstr("3. Display student list\n")
            stdscr.addstr("4. Display course list\n")
            stdscr.addstr("5. Input marks\n")
            stdscr.addstr("6. Show marks\n")
            stdscr.addstr("Press any other key to exit\n")
            
            stdscr.addstr("Option: ")
            choice = stdscr.getstr().decode("utf-8")
            if choice == "1":
                option.input_student()
            elif choice == "2":
                option.input_course()
            elif choice == "3":
                option.list_students()
            elif choice == "4":
                option.list_courses()
            elif choice == "5":
                option.input_mark()
            elif choice == "6":
                option.show_mark()
            else:
                break

    curses.wrapper(main)

if __name__ == "__main__":
    run()

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
            mark = int(input())
            self.mark.add_mark(course_id, student.id, mark)

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

    def run(self):
        while True:
            print("\nStudent Management System:")
            print("1. Input student info")
            print("2. Input course info")
            print("3. Display student list")
            print("4. Display course list")
            print("5. Input marks")
            print("6. Show marks")
            print("Press any other key to exit")

            choice = input("Choose an option: ")
            if choice == "1":
                self.input_student()
            elif choice == "2":
                self.input_course()
            elif choice == "3": 
                self.list_students()
            elif choice == "4":
                self.list_courses()
            elif choice == "5":
                self.input_mark()
            elif choice == "6":
                self.show_mark()
            else:
                print("Exiting the program.")
                break

if __name__ == "__main__":
    system = Option()
    system.run()

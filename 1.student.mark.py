students = []
courses = []
mark = {}

def student_info():
    print("Enter number of students: ")
    student_number = int(input())
    for _ in range(student_number):
        print("Enter student id: ")
        id = int(input())
        print("Enter name: ")
        name = str(input())
        print("dob: ")
        dob = str(input())
        students.append({"id": id, "name": name, "dob": dob})

def student_list():
    print("Student:")
    for student in students:
        print(f"Student's ID: {student['id']}, Student's name: {student['name']}, Student's date of birth: {student['dob']}")

def course_info():
    print("Enter number of courses: ")
    course_number = int(input())
    for _ in range(course_number):
        print("Enter course ID: ")
        course_id = int(input())
        print("Enter course name: ")
        course_name = str(input())
        courses.append({"id": course_id, "name": course_name})

def course_list():
    print("Course list:")
    for course in courses:
        print(f"ID: {course['id']}, Name: {course['name']}")

def input_mark():
    print("Enter course id: ")
    marks = int(input())
    for student in students:
        print(f"Enter mark for this student {student['id']} ({student['name']}): ")
        mark = int(input())
        if course_id not in mark:
            mark[course_id] = {}
            mark[course_id][student['id']] = marks

def show_mark():
    print("enter course id: ")
    course_id = int(input())
    if course_id not in mark:
        print("Not exist")
        return
    print(f"Mark {course_id}: ")
    course_id = int(input())
    for student_id, mark in marks[course_id].items():
        student_name = next(student['name']
    for student in students if student['id'] == student_id)
    print(f"Student ID: {student_id}, Name: {student_name}, Mark: {mark}")


while True:
    print("\nStudent Management:")
    print("1. Input student info")
    print("2. Input course info")
    print("3. Student list")
    print("4. Course list")
    print("5. Input marks")
    print("6. Show mark")
    print("Press anything to exit")

    choice = input("Choose an option: ")
    if choice == "1":
        student_info()
    elif choice == "2":
        course_info()
    elif choice == "3":
        student_list()
    elif choice == "4":
        course_list()
    elif choice == "5":
        intput_mark()
    elif choice == "6":
        show_mark()
    else:
        break

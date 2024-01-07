# Functions
    # Input functions:
        # Input number of students in a class
        # Input student information: id, name, DoB
        # Input number of courses
        # Input course information: id, name
        # Select a course, input marks for student in this course
    # Listing functions:
        # List courses
        # List students
        # Show student marks for a given course
# Push your work to corresponding forked Github repository
                
def input_students():
    num_of_stu = int(input("Enter number of students: "))
    students = []
    for i in range(num_of_stu):
        student_id = input("Enter student ID: ")
        student_name = input("Enter student name: ")
        student_dob = input("Enter student DOB (DD/MM/YYYY): ")
        student = {"Student ID": student_id, "Name": student_name, "DoB": student_dob, "Courses": {}}
        students.append(student)
    return students

def input_courses():
    num_of_courses = int(input("Enter number of courses: "))
    courses = []
    for i in range(1, num_of_courses + 1):
        course_id = input(f"Enter course {i} ID: ")
        course_name = input(f"Enter course {i} name: ")
        course = {"Course ID": course_id, "Name": course_name}
        courses.append(course)
    return courses

def input_marks(students, courses):
    course_id = input("Enter course ID to input marks: ")
    for course in courses:
        if course["Course ID"] == course_id:
            for student in students:
                marks = float(input(f"Enter student {student["Student ID"]} marks: "))
                student["Courses"][course_id] = marks
                break
            else:
                print("Course not found.")

def list_courses(courses):
    print("\nList of courses: ")
    for course in courses:
        print(f"Course ID: {course["Course ID"]}, Name: {course["Name"]}")

def list_students(students):
    print("\nList of students: ")
    for student in students:
        print(f"Student ID: {student["Student ID"]}, Name: {student["Name"]}, DoB: {student["DoB"]}")

def show_student_marks(students):
    student_id = input("Enter student ID: ")
    for student in students:
        if student["Student ID"] == student_id:
            print(f"Student {student["Student ID"]}'s marks: ")
            for course_id, marks in student["Courses"].items():
                print(f"Course ID: {course_id}, Marks: {marks}")
            break

students = input_students()
courses = input_courses()

while True:
    print("Press:")
    print("1. Input marks")
    print("2. List students")
    print("3. List courses")
    print("4. Show student marks")

    choice = input("Enter your choice.\n")
    if choice == '1':
        input_marks(students, courses)
    elif choice == '2':
        list_students(students)
    elif choice == '3':
        list_courses(courses)
    elif choice == '4':
        show_student_marks(students)
        break
    else:
        print("Invalid.")
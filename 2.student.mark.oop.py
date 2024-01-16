class Student:
    def __init__(self, student_id, student_name, dob):
        self.student_id = student_id
        self.student_name = student_name
        self.dob = dob
        self.courses = {}

class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name

class Information:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def input_students(self):
        num_of_stu = int(input("Enter number of students: "))
        for i in range(num_of_stu):
            student_id = input("Enter student ID: ")
            student_name = input("Enter student full name: ")
            dob = input("Enter student DoB(DD/MM/YYYY): ")
            student = Student(student_id, student_name, dob)
            self.students[student_id] = student

    def input_courses(self):
        num_of_courses = int(input("Enter number of courses: "))
        for i in range(num_of_courses):
            course_id = input(f"Enter course ID: ")
            course_name = input(f"Enter name of course {course_id}: ")
            course = Course(course_id, course_name)
            self.courses[course_id] = course
    
    def input_marks(self):
        course_id = input("Enter course ID to input marks: ")
        if course_id not in self.courses:
            print("This course is not in the system.")
            return
        else:
            for student_id, student in self.students.items():
                marks = float(input(f"Enter student {student_id} marks: "))
                student.courses[course_id] = marks
    
    def list_courses(self):
        print("List of courses\n")
        for course_id, course in self.courses.items():
            print(f"Course ID: {course_id}, Name: {course.course_name}.")
    
    def list_students(self):
        print("List of students\n")
        for student_id, student in self.students.items():
            print(f"ID: {student_id}, Name: {student.student_name}, DoB: {student.dob}")

    def display_marks(self):
        student_id = input("Enter student ID to display marks: ")
        if student_id not in self.students:
            print("This student is not in the system.")
            return
        student = self.students[student_id]
        print(f"Student {student_id}'s marks: \n")
        for course_id, marks in student.courses.items():
            print(f"Course ID: {course_id}, Marks: {marks}")

info = Information()
info.input_students()
info.input_courses()

while True:
    print("\n1. Input marks.")
    print("2. List students.")
    print("3. List courses.")
    print("4. Display marks.")

    choice = input("Enter option\n")
    if choice == '1':
        info.input_marks()
    elif choice == '2':
        info.list_students()
    elif choice == '3':
        info.list_courses()
    elif choice == '4':
        info.display_marks()
        break
    else:
        print("Invalid.")
import random

class Student:
    def __init__(self, name):
        self.name = name
        self.ID = random.randint(1000, 9999)
        print(f"Student {self.name} admitted with ID: {self.ID}")

    def enroll_in_class(self, class_name):
        self.class_allocated = self.name
        return(f"{self.name} has been enrolled in {self.class_allocated}")
    
class Teacher:
    def __init__(self, name, department):
        self.name = name
        self.ID = random.randint(1000, 9999)
        self.department = department
        self.class_assigned = None
        print(f"Teacher {self.name} hired with ID: {self.ID} for department {self.department}")

class AdminSystem:
    def __init__(self):
        self.students = {}
        self.teachers = {}
        self.classroom = []
        self.department = {}
    
    def admit_student(self, student_name):
        student = Student(student_name)
        self.students[student.ID] = student
        return student
    
    def allocate_classroom(self, student_ID, classroom):
        if student_ID in self.students:
            self.students[student_ID].class_allocated = classroom
            print(f"student: {self.students[student_ID].name} allocated to cassroom: {classroom}")
        else:
            print(f"Error: Student with ID {student_ID} not found.")

    def assign_teacher_to_class(self, teacher_ID, classroom):
        if teacher_ID in self.teachers:
            self.teachers[teacher_ID].assigned_class = classroom
            print(f"Teacher {self.teachers[teacher_ID].name} assigned to class {classroom}")
        else:
            print(f"Error: Teacher with ID {teacher_ID} not found.")

    def assign_to_department(self, member_ID, department_name):
        if member_ID in self.students:
            self.students[member_ID].department = department_name
            print(f"Student {self.students[member_ID].name} allocated to department {department_name}")
        elif member_ID in self.teachers:
            self.teachers[member_ID].department = department_name
            print(f"Teacher {self.teachers[member_ID].name} allocated to department {department_name}")
        else:
            print(f"Error: Member with ID {member_ID} not found.")

    def view_details(self, member_ID):
        if member_ID in self.students:
            student = self.students[member_ID]
            print(f"Student: {student.name}, ID: {student.ID}, Class: {student.class_allocated}, Department: {student.department}")
        elif member_ID in self.teachers:
            teacher = self.teachers[member_ID]
            print(f"Student: {teacher.name}, ID: {teacher.ID}, Asssigned Class: {teacher.assigned_class}, De6partment: {teacher.department}")
        else:
            print(f"Error: Member with ID {member_ID} not found.")


school_admin = AdminSystem()
student1 = school_admin.admit_student("Alex Johnson")

teacher1 = Teacher("Mr. Davis", "Mathematics")
# school_admin.teachers(teacher1.ID) = teacher1

school_admin.allocate_classroom(student1.ID, "Grade 101")

school_admin.assign_teacher_to_class(teacher1.ID, "Grade 101")

school_admin.assign_to_department(student1.ID, "Science")

print("\n--- Viewing Details ---")
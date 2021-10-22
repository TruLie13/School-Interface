from classes.staff import Staff
from classes.student import Student
import csv
import os

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.objects()
        self.students = Student.objects()

    def list_students(self):
        print('\n')
        for i, student in enumerate(self.students):
            print(f'{i + 1}. {student.name} {student.school_id}')

    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.school_id == student_id:
                return student

    def find_staff_by_id(self, employee_id):
        for staff in self.staff:
            if staff.employee_id == employee_id:
                return staff

    #adds to list but doesn't save
    def add_student(self, student_name, student_age, student_password, role, student_id):
        self.students.append(Student(student_name, student_age, student_password, role, student_id))
        #saves
        self.save()

    def delete_student(self, student_id):
        student = self.find_student_by_id(student_id)
        self.students.remove(student)
        self.save()
        

    #saves data
    def save(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/students.csv")

        with open(path, 'w') as csvfile:
            student_csv = csv.writer(csvfile, delimiter = ",")
            student_csv.writerow(['name', 'age', 'role', 'school_id', 'password'])
            for student in self.students:
                student_csv.writerow([student.name, student.age, student.role, student.school_id, student.password])
from classes.school import School 

class Interface():

    def __init__(self, school_name):
        self.school = School(school_name) 

    

    @property
    def menu(self):
        return ("\nWhat would you like to do?\nOptions:\n1. List All Students\n2. View Individual Student <student_id>\n3. Add a Student\n4. Remove a Student <student_id>\n5. Quit\n"
        )

    def authenticate_user(self):

        while True:

            entered_id = input("Enter Employee Id: ")
            found_staff = self.school.find_staff_by_id(entered_id)

            if found_staff:
                break
            print("No User found: reenter ID")

        for _ in range(found_staff.p_attempts):

            entered_password = input("Enter password: ")

            if entered_password == found_staff.password:
                return True
        
        print("Too many password attempts")
        
    def run(self):
        if self.authenticate_user():

            while True:
                mode = input(self.menu)

                if mode == '1':
                    self.school.list_students()
                elif mode == '2':
                    student_id = input('Enter student id:')
                    student_string = str(self.school.find_student_by_id(student_id))
                    print(student_string)
                elif mode == '3':
                    student_name = input('Enter student name: ')
                    student_age = input('Enter student age: ')
                    student_password = input('Enter student password: ')
                    role = "student"
                    student_id = input('Enter student ID: ')
                    self.school.add_student(student_name, student_age, student_password, role, student_id)
                elif mode == '4':
                    student_id = input('Enter student ID: ')
                    self.school.delete_student(student_id)
                elif mode == '5':
                    break


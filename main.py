from department import Department
from person import Student
from person import Teacher
from db_con import DbCon
from account import Account
from attandance import Attandance
from course import Course
from university import University
from registration import Registration

print("""
        ********************************************************
        ********************************************************
        *****                                              *****
        *****           MADE BY : SADAIN AHMAD             *****
        *****                                              *****
        ********************************************************
        ********************************************************

""")

class Main:

    def __init__(self):
        self.__db = DbCon()

    # Add university
    def add_uni(self):

        id = int(input("Enter University Unique ID : "))
        name = input("Enter University name : ")
        address = input("Enter University address : ")
        self.__db.add_uni(University(id, name, address))

    # Add department
    def add_dep(self):

        dep_id = int(input("Enter Department Unique ID : "))
        name = input("Enter Department name : ")
        uni_id = int(input("Enter University ID : "))
        self.__db.add_dep(Department(dep_id, name, uni_id))

    # Add student
    def add_student(self):

        email = input("Enter Student email : ")
        password = input("Enter Student account password : ")
        id = int(input("Enter Student unique ID : "))
        cnic = input("Enter Student unique CNIC : ")
        name = input("Enter Student name : ")
        father_name = input("Enter Student father name : ")
        contact = input("Enter Student contact : ")
        address = input("Enter Student address : ")
        gender = input("Enter Student Gender(M/F) : ")
        dob = input("Enter Student date of birth(YY-MM-DD) : ")
        dep_id = input("Enter Student department ID : ")

        self.__db.add_student(Student(id, cnic, name, father_name, contact, address, email, gender, dob, dep_id), Account(id, password, email))

    # Add Teacher
    def add_teacher(self):

        email = input("Enter Teacher email : ")
        password = input("Enter Teacher account password : ")
        id = int(input("Enter Teacher unique ID : "))
        cnic = input("Enter Teacher unique CNIC : ")
        name = input("Enter Teacher name : ")
        father_name = input("Enter Teacher father name : ")
        contact = input("Enter Teacher contact : ")
        address = input("Enter Teacher address : ")
        gender = input("Enter Teacher Gender(M/F) : ")
        dob = input("Enter Teacher date of birth(YY-MM-DD) : ")
        speciality = input("Enter Teacher specialization : ")
        post = input("Enter Teacher post : ")
        dep_id = input("Enter Teacher department ID : ")

        self.__db.add_teacher(Teacher(id, cnic, name, father_name, contact, address, email, gender, dob, speciality, post, dep_id), Account(id, password, email))

    # Add course
    def add_course(self):

        course_code = input("Enter course code : ")
        course_name = input("Enter course name : ")
        credit = int(input("Enter course credit hours : "))
        dep_id = int(input("Enter department ID of that course : "))

        self.__db.add_course(Course(course_code, course_name, credit, dep_id))

    # Register Course
    def register_course(self):
        student_id = int(input("Enter Student ID : "))
        teacher_id = int(input("Enter Teacher ID : "))
        course_code = input("Enter Course code : ")
        course_name = input("Enter Course name : ")
        semester = int(input("Enter Semester : "))
        grade = int(input("Enter Credit hours : "))
        status = input("Enter Status : ")

        self.__db.register_course(Registration(student_id, course_code, teacher_id, course_name, semester, grade, status))

    # Mark Attandance
    def mark_attandance(self):

        student_id = int(input("Enter Student ID : "))
        course_code = input("Enter Course code : ")
        status = input("Enter status(P/A) : ")

        self.__db.mark_attandance(Attandance(student_id, course_code, status))

    # delete university 
    def delete_uni(self):

        id = int(input("Enter University ID that you wanna delete : "))

        self.__db.delete_uni(id)

    # delete department
    def delete_dep(self):

        id = int(input("Enter Department ID that you wanna delete : "))

        self.__db.delete_dep(id)

    # delete student
    def delete_student(self):

        id = int(input("Enter Student ID that you wanna delete : "))
        self.__db.delete_student(id)

    # delete teacher
    def delete_teacher(self):

        id = int(input("Enter Teacher ID that you wanna delete : "))

        self.__db.delete_teacher(id)

    # delete courses
    def delete_course(self):

        course_code = input("Enter course code that you wanna delete : ")
        self.__db.delete_course(course_code)

    # drop registered course
    def drop_course(self):

        sid = input("Enter Student ID to delete it's register course : ")
        course_code = input("Enter particular course code that you wanna delete : ")

        self.__db.drop_course(sid, course_code)

    # update University record
    def update_uni(self):
        
        id = int(input("Enter University ID to update it's record : "))
        name = input("Enter University updated name : ")
        address = input("Enter University updated address : ")

        self.__db.update_uni(University(id, name, address))

    # Update department record
    def update_dep(self):
        
        dep_id = int(input("Enter Department ID to update it's record : "))
        name = input("Enter Department updated name : ")
        uni_id = int(input("Enter University updated ID : "))

        self.__db.update_dep(Department(dep_id, name, uni_id))

    # update courses
    def update_course(self):

        course_code = input("Enter course code that you wanna update : ")
        course_name = input("Enter course updated name : ")
        credit = int(input("Enter course credit hours : "))
        dep_id = int(input("Enter department ID of that course : "))

        self.__db.update_course(Course(course_code,course_name, credit, dep_id))

    # update student
    def update_student(self):
        
        id = int(input("Enter Student ID to update his/her record : "))
        old_pass = input("Enter Student account password : ")
        email = input("Enter Student email : ")
        password = input("Enter Student account new password : ")
        cnic = input("Enter Student updated CNIC : ")
        name = input("Enter Student updated name : ")
        father_name = input("Enter Student updated father name : ")
        contact = input("Enter Student updated contact : ")
        address = input("Enter Student updated address : ")
        gender = input("Enter Student Gender(M/F) : ")
        dob = input("Enter Student date of birth(YY-MM-DD) : ")
        dep_id = input("Enter Student updated department ID : ")

        self.__db.update_student(Student(id, cnic, name, father_name, contact, address, email, gender, dob, dep_id), Account(id, password, email), old_pass)

    # update teacher
    def update_teacher(self):

        id = int(input("Enter Teacher ID to update his/her record : "))
        old_pass = input("Enter Teacher account old password : ")
        email = input("Enter Teacher email : ")
        password = input("Enter Teacher account new password : ")
        cnic = input("Enter Teacher unique CNIC : ")
        name = input("Enter Teacher name : ")
        father_name = input("Enter Teacher father name : ")
        contact = input("Enter Teacher contact : ")
        address = input("Enter Teacher address : ")
        gender = input("Enter Teacher Gender(M/F) : ")
        dob = input("Enter Teacher date of birth(YY-MM-DD) : ")
        dep_id = input("Enter Teacher department ID : ")
        speciality = input("Enter Teacher specialization : ")
        post = input("Enter Teacher post : ")

        self.__db.update_teacher(Teacher(id, cnic, name, father_name, contact, address, email, gender, dob, speciality, post, dep_id), Account(id, password, email), old_pass)

    # update registration record
    # def update_reg(self):
        
    #     student_id = int(input("Enter Student ID : "))
    #     course_code = input("Enter Course code : ")
    #     teacher_id = int(input("Enter Teacher ID : "))
    #     course_name = input("Enter Course name : ")
    #     semester = int(input("Enter Semester : "))
    #     grade = input("Enter Grade : ")
    #     status = input("Enter Status : ")

    #     self.__db.update_reg(Registration(student_id, course_code, teacher_id, course_name, semester, grade, status))

    # update attandance
    def update_attandance(self):
        
        student_id = int(input("Enter Student ID : "))
        course_code = input("Enter Course code : ")
        status = input("Enter status(P/A) : ")

        self.__db.update_attandance(Attandance(student_id, course_code, status))

    # Display all universities records
    def display_universities(self):

        self.__db.display_universities()

    # Display all departments records
    def display_departments(self):

        self.__db.display_depatments()

    # display all courses records
    def display_courses(self):

        self.__db.display_courses()

    # display all students records
    def display_students(self):
        self.__db.display_students()

    # Display all teacher records
    def display_teachers(self):
        self.__db.display_teachers()

    # display attandance of a student in a particular course
    def display_attandance(self):
        sid = int(input("Enter student ID to check his/her attandance : "))
        course_code = input("Enter course code to check attandance : ")
        self.__db.display_attandance(sid, course_code)

    # display courses registered by a particular student
    def display_reg_courses(self):
        id = int(input("Enter Student ID to see his/her registered courses : "))
        self.__db.display_reg_courses(id)



m = Main()
while (True):
    print("""1: Press 1 for Student\n2: Press 2 for Teacher\n3: Press 3 for University\n4: Press 4 for Department\n5: Press 5 for Courses\n6: Press 6 for Registration\n7: Press 7 for Attandance\n0: Press 0 to Cancel""")
    select = int(input("Choice : "))
    if select==0:
        exit()
    # student
    elif select==1:
        while(True):
            print("""\t1: Press 1 to add student\n\t2: Press 2 to update student\n\t3: Press 3 to delete student\n\t4: Press 4 to display all students\n\t0: Press 0 to get back""")
            choice = int(input("Select : "))
            if choice==0:
                break
            # add
            elif choice==1:
                m.add_student()
            # update
            elif choice==2:
                m.update_student()
            # delete
            elif choice==3:
                m.delete_student()
            # display
            elif choice==4:
                m.display_students()
            else:
                print("choose between 1-4")

    # Teacher
    elif select==2:
        while True:
            print("""\t1: Press 1 to add Teacher\n\t2: Press 2 to update Teacher\n\t3: Press 3 to delete Teacher\n\t4: Press 4 to display all Teachers\n\t0: Press 0 to get back""")
            choice = int(input("Select : "))
            if choice==0:
                break
            # add
            elif choice==1:
                m.add_teacher()
            # update
            elif choice==2:
                m.update_teacher()
            # delete
            elif choice==3:
                m.delete_teacher()
            # display
            elif choice==4:
                m.display_teachers()
            else:
                print("choose between 1-4")

    # Universities
    elif select==3:
        while True:
            print("""\t1: Press 1 to add University\n\t2: Press 2 to update University\n\t3: Press 3 to delete University\n\t4: Press 4 to display all Universities\n\t0: Press 0 to get back""")
            choice = int(input("Select : "))
            if choice==0:
                break
            # add
            elif choice==1:
                m.add_uni()
            # update
            elif choice==2:
                m.update_uni()
            # delete
            elif choice==3:
                m.delete_uni()
            # display
            elif choice==4:
                m.display_universities()
            else:
                print("choose between 1-4")
    # Department
    elif select==4:
        while True:
            print("""\t1: Press 1 to add Department\n\t2: Press 2 to update Department\n\t3: Press 3 to delete Department\n\t4: Press 4 to display all Departments\n\t0: Press 0 to get back""")
            choice = int(input("Select : "))
            if choice==0:
                break
            # add
            elif choice==1:
                m.add_dep()
            # update
            elif choice==2:
                m.update_dep()
            # delete
            elif choice==3:
                m.delete_dep()
            # display
            elif choice==4:
                m.display_departments()
            else:
                print("choose between 1-4")
    # courses
    elif select==5:
        while True:
            print("""\t1: Press 1 to add course\n\t2: Press 2 to update course\n\t3: Press 3 to delete course\n\t4: Press 4 to display all courses\n\t0: Press 0 to get back""")
            choice = int(input("Select : "))
            if choice==0:
                break
            # add
            elif choice==1:
                m.add_course()
            # update
            elif choice==2:
                m.update_course()
            # delete
            elif choice==3:
                m.delete_course()
            # display
            elif choice==4:
                m.display_courses()
            else:
                print("choose between 1-4")
    # Registration
    elif select==6:
        while True:
            print("""\t1: Press 1 to register course to student\n\t2: Press 2 to delete course of a student\n\t3: Press 3 to display all registered courses of particular student\n\t0: Press 0 to get back""")
            choice = int(input("Select : "))
            if choice==0:
                break
            # add
            elif choice==1:
                m.register_course()
            # delete
            elif choice==2:
                m.drop_course()
            # display
            elif choice==3:
                m.display_reg_courses()
            else:
                print("choose between 1-3")
    # attandance
    elif select==7:
        while True:
            print("""\t1: Press 1 to mark attandance of particular student at a particular course\n\t2: Press 2 to update attandance\n\t3: Press 3 to display all attandance record of a student in a particular course\n\t0: Press 0 to get back""")
            choice = int(input("Select : "))
            if choice==0:
                break
            # add
            elif choice==1:
                m.mark_attandance()
            # update
            elif choice==2:
                m.update_attandance()
            # display
            elif choice==3:
                m.display_attandance()
            else:
                print("choose between 1-3")
    else:
        print("Select between 1-7")
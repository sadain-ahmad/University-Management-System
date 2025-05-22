import mysql.connector as con


class DbCon:

    def __init__(self):
        try:
            self.__db = con.connect(host="localhost", port=3306, user="root", password="sadainahmad12345", database="department_management")
            print("connected to database")
        except Exception as e:
            print(e)


    # Add University
    def add_uni(self, uni):
        try:
            cur = self.__db.cursor()
            cur.execute("SELECT * FROM university WHERE id=%s", (uni.id,))
            if not cur.fetchall():
                insertion = "INSERT INTO university(id, name, address) VALUES(%s, %s, %s)"
                data = (uni.id, uni.name, uni.address)
                cur.execute(insertion, data)
                self.__db.commit()
                print("Uni added")
            else:
                print("Wrong ID! Univesity already exist")
        except Exception as e:
            self.__db.rollback()
            print(e)
        finally:
            cur.close()

    # Add Department
    def add_dep(self, department):
        try:
            cur = self.__db.cursor()
            cur.execute("SELECT * FROM department WHERE dep_id=%s", (department.dep_id,))
            if not cur.fetchall():
                insertion = "INSERT INTO department(dep_id, name, uni_id) VALUES(%s, %s, %s)"
                data = (department.dep_id, department.name, department.uni_id)
                cur.execute(insertion, data)
                self.__db.commit()
                print("Department added")
            else:
                print("Wrong ID! Department already exist")
        except Exception as e:
            self.__db.rollback()
            print(e)
        finally:
            cur.close()

    
    # ADD student
    def add_student(self, student, account):
        try:
            cur = self.__db.cursor()
            cur.execute("SELECT * FROM student WHERE student_id=%s", (student.id,))
            if not cur.fetchall():
                insertion = "insert into student(student_id, cnic, name, father_name, email, contact, address, gender, date_of_birth, dep_id) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                data = (student.id, student.cnic, student.name, student.father_name, student.email, student.contact, student.address, student.gender, student.date_of_birth, student.dep_id)
                # insert student data
                cur.execute(insertion, data)
                # insert student account data
                acc_data = (account.id, account.email, account.password)
                cur.execute("INSERT INTO student_account(id, email, pass) VALUES(%s, %s, %s)", acc_data)
                self.__db.commit()
                print("Student added")
            else:
                print("Wrong ID! Student already exist")
        except Exception as e:
            self.__db.rollback()
            print(e)
        finally:
            cur.close()

    # Add teacher
    def add_teacher(self, teacher, account):
        try:
            cur = self.__db.cursor()
            cur.execute("SELECT * FROM teacher WHERE teacher_id=%s", (teacher.id,))
            if not cur.fetchall():
                insertion = "insert into teacher(teacher_id, cnic, name, father_name, email, contact, address, speciality, post, gender, date_of_birth, dep_id) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                data = (teacher.id, teacher.cnic, teacher.name, teacher.father_name, teacher.email, teacher.contact, teacher.address, teacher.speciality, teacher.post, teacher.gender, teacher.date_of_birth, teacher.dep_id)
                # insert teacher data
                cur.execute(insertion, data)
                
                # insert teacher account data
                acc_data = (account.id, account.email, account.password)
                cur.execute("INSERT INTO teacher_account(id, email, pass) VALUES(%s, %s, %s)", acc_data)
                self.__db.commit()
                print("Teacher added")
            else:
                print("Wrong ID! Teacher already exist")
        except Exception as e:
            self.__db.rollback()
            print(e)
        finally:
            cur.close()

    # add courses
    def add_course(self, course):
        try:
            cur = self.__db.cursor()
            cur.execute("SELECT * FROM courses WHERE course_code=%s", (course.course_code,))
            if not cur.fetchall():
                insertion ="insert into courses(course_code, course_name, credits, dep_id) VALUES(%s, %s, %s, %s)"
                data = (course.course_code, course.course_name, course.credit, course.dep_id)
                # insert course data
                cur.execute(insertion, data)
                self.__db.commit()
                print("course added")
            else:
                print("Wrong Course Code! Course already exist")
        except Exception as e:
            self.__db.rollback()
            print(e)
        finally:
            cur.close()
        
    # register courses
    def register_course(self, reg):
        try:
            cur = self.__db.cursor()
            cur.execute("SELECT * FROM student WHERE student_id=%s", (reg.student_id,))

            if cur.fetchall():
                cur.execute("SELECT * FROM registration WHERE student_id=%s AND course_code=%s", (reg.student_id, reg.course_code))

                if not cur.fetchall():
                    insertion = "insert into registration(student_id, course_code, course_name, teacher_id, semester, credit, status) VALUES(%s, %s, %s, %s, %s, %s, %s)"
                    data = (reg.student_id, reg.course_code, reg.course_name, reg.teacher_id, reg.semester, reg.grade, reg.status)
                    # register Course
                    cur.execute(insertion, data)
                    self.__db.commit()
                    print("course registered")
                else:
                    print("Course already registered by that student")
            else:
                print("Wrong ID! Student not found")
        except Exception  as e:
            self.__db.rollback()
            print(e)
        finally:
            cur.close()

    # Mark attendance
    def mark_attandance(self, attandance):
        try:
            cur = self.__db.cursor()
            cur.execute("SELECT * FROM student WHERE student_id=%s", (attandance.student_id,))

            if cur.fetchall():
                cur.execute("SELECT * FROM registration WHERE student_id=%s AND course_code=%s", (attandance.student_id, attandance.course_code))

                if cur.fetchall():
                    insertion = "insert into attandance(student_id, course_code, date, status) VALUES(%s, %s, %s, %s)"
                    data = (attandance.student_id, attandance.course_code, attandance.date, attandance.status)
                    # mark attandance
                    cur.execute(insertion, data)
                    self.__db.commit()
                    print("attandance marked")
                else:
                    print("Student doesn't registered that course")
            else:
                print("Wrong ID! Student record not found")
        except Exception  as e:
            self.__db.rollback()
            print(e)
        finally:
            cur.close()
    
    # delete university
    def delete_uni(self, id):
        try:
            cur = self.__db.cursor()
            cur.execute("SELECT name FROM university WHERE id=%s", (id,))
            if cur.fetchone():
                deletion = "DELETE FROM university WHERE id=%s"
                data = (id,)

                # delete data
                cur.execute(deletion, data)
                self.__db.commit()
                print("University Record Deleted")
            else:
                print("Wrong ID! University record not found")
        except Exception as e:
            self.__db.rollback()
            print(e)
        finally:
            cur.close()

    # delete department
    def delete_dep(self, id):
        try:
            cur = self.__db.cursor()
            cur.execute("SELECT name FROM department WHERE dep_id=%s", (id,))
            if cur.fetchone():
                deletion = "DELETE FROM department WHERE dep_id=%s"
                data = (id,)

                # delete data
                cur.execute(deletion, data)
                self.__db.commit()
                print("Department Record Deleted")
            else:
                print("Wrong ID! Department record not found")
        except Exception as e:
            self.__db.rollback()
            print(e)
        finally:
            cur.close()

    # delete student
    def delete_student(self, id):
        try:
            cur = self.__db.cursor()
            cur.execute("SELECT name FROM student WHERE student_id=%s", (id,))

            if cur.fetchone():
                deletion = "DELETE FROM student WHERE student_id=%s"
                data = (id,)
                # delete student account
                cur.execute("DELETE FROM student_account WHERE id=%s", data)
                
                # delete data
                cur.execute(deletion, data)
                self.__db.commit()
                print("Student Record Deleted")
            else:
                print("Wrong ID! Student record not found")
        except Exception as e:
            self.__db.rollback()
            print(e)
        finally:
            cur.close()

    # delete teacher
    def delete_teacher(self, id):
        try:
            cur = self.__db.cursor()
            cur.execute("SELECT name FROM teacher WHERE teacher_id=%s", (id,))
            if cur.fetchone():
                deletion = "DELETE FROM teacher WHERE teacher_id=%s"
                data = (id,)
                # delete teacher account
                cur.execute("DELETE FROM teacher_account WHERE id=%s", data)
                
                # delete data
                cur.execute(deletion, data)
                self.__db.commit()
                print("Teacher Record Deleted")
            else:
                print("Wrong ID! Teacher record not found")
        except Exception as e:
            self.__db.rollback()
            print(e)
        finally:
            cur.close()
    
    # drop the registered course
    def drop_course(self, sid, course_code):
        try:
            cur = self.__db.cursor()
            cur.execute("SELECT * FROM student WHERE student_id=%s", (sid,))

            if cur.fetchall():
                cur.execute("SELECT * FROM registration WHERE student_id=%s AND course_code=%s", (sid, course_code))

                if cur.fetchone():
                    deletion = "DELETE FROM registration WHERE student_id=%s AND course_code=%s"
                    data = (sid, course_code)
                    # delete data
                    cur.execute(deletion, data)
                    self.__db.commit()
                    print("course droped")
                else:
                    print("That Course doesn't registered by that student")
            else:
                print("Wrong ID! Student record not found")
        except Exception as e:
            self.__db.rollback()
            print(e)
        finally:
            cur.close()

    # delete courses
    def delete_course(self, course_code):
        try:
            cur = self.__db.cursor()
            cur.execute("SELECT * FROM courses WHERE course_code=%s", (course_code,))

            if cur.fetchone():
                deletion = "DELETE FROM courses WHERE course_code=%s"
                data = (course_code,)

                # delete data
                cur.execute(deletion, data)
                self.__db.commit()
                print("course Deleted")
            else:
                print("Wrong Course Code! Course record not found")

        except Exception as e:
            self.__db.rollback()
            print(e)
        finally:
            cur.close()

    # Update university
    def update_uni(self, uni):
        try:
            cur = self.__db.cursor()
            cur.execute("SELECT id FROM university WHERE id=%s",(uni.id,))
            if cur.fetchone():
                updation = "UPDATE university SET name=%s, address=%s WHERE id=%s"
                data = (uni.name, uni.address, uni.id)
                # update data
                cur.execute(updation, data)
                self.__db.commit()
                print("university Record updated")
            else:
                print("Wrong ID! University record not found")
        except Exception as e:
            self.__db.rollback()
            print(e)
        finally:
            cur.close()

    # Update Department
    def update_dep(self, dep):
        try:
            cur = self.__db.cursor()
            cur.execute("SELECT * FROM department WHERE dep_id=%s",(dep.dep_id,))
            if cur.fetchone():
                updation = "UPDATE department SET name=%s, uni_id=%s WHERE dep_id=%s"
                data = (dep.name, dep.uni_id, dep.dep_id)
                # update data
                cur.execute(updation, data)
                self.__db.commit()
                print("department Record updated")
            else:
                print("Wrong ID! Department record not found")
        except Exception as e:
            self.__db.rollback()
            print(e)
        finally:
            cur.close()
 
    # update courses
    def update_course(self, course):
        try:
            cur = self.__db.cursor()
            cur.execute("SELECT * FROM courses WHERE course_code=%s", (course.course_code,))
            if cur.fetchone():
                updation = "UPDATE courses SET course_code=%s, course_name=%s, credits=%s, dep_id=%s WHERE course_code=%s"
                data = (course.course_code, course.course_name, course.credit, course.dep_id, course.course_code)
                # update data
                cur.execute(updation, data)
                self.__db.commit()
                print("course updated")
            else:
                print("Wrong Course Code! Course not Found")
        except Exception as e:
            self.__db.rollback()
            print(e)
        finally:
            cur.close()

    # update student
    def update_student(self, student, account, old_pass):
        try:
            cur = self.__db.cursor()
            cur.execute("SELECT pass FROM student_account WHERE id=%s", (account.id,))
            result = cur.fetchone()
            # check student account exist
            if result:
                if old_pass == result[0]: # if pass is correct
                    updation = "UPDATE student SET cnic=%s, name=%s, father_name=%s, email=%s, contact=%s, address=%s, gender=%s, date_of_birth=%s, dep_id=%s WHERE student_id=%s"
                    data = (student.cnic, student.name, student.father_name, student.email, student.contact, student.address, student.gender, student.date_of_birth, student.dep_id, student.id)
                    
                    # update Student account
                    acc_data = (account.email, account.password, account.id)
                    cur.execute("UPDATE student_account SET email=%s, pass=%s WHERE id=%s", acc_data)
                    
                    # update Student profile
                    cur.execute(updation, data)
                    self.__db.commit()
                    print("student record updated")
                else:
                    print("wrong password")
            else:
                print("Wrong ID! Student record not found")

        except Exception as e:
            self.__db.rollback()
            print(e)
        finally:
            cur.close()

    # update teacher record
    def update_teacher(self, teacher, account, old_pass):
        try:
            cur = self.__db.cursor()
            cur.execute("SELECT pass FROM teacher_account WHERE id=%s", (account.id,))
            result = cur.fetchone()
            if result:
                # if pass is correct
                if old_pass == result[0]:
                    updation = "UPDATE teacher SET cnic=%s, name=%s, father_name=%s, email=%s, contact=%s, address=%s, speciality=%s, post=%s, gender=%s, date_of_birth=%s, dep_id=%s WHERE teacher_id=%s"
                    data = (teacher.cnic, teacher.name, teacher.father_name, teacher.email, teacher.contact, teacher.address, teacher.speciality, teacher.post, teacher.gender, teacher.date_of_birth, teacher.dep_id, teacher.id)

                    # update teacher account
                    acc_data = (account.email, account.password, account.id)
                    cur.execute("UPDATE teacher_account SET email=%s, pass=%s WHERE id=%s", acc_data)

                    # update teacher profile
                    cur.execute(updation, data)
                    self.__db.commit()
                    print("teacher Record updated")
                else:
                    print("Wrong Password")
            else:
                print("Wrong ID! Teacher record not found")

        except Exception as e:
            self.__db.rollback()
            print(e)
        finally:
            cur.close()

    # Update Registration
    # def update_reg(self, reg):
    #     try:
    #         cur = db.cursor()
    #         cur.execute("SELECT student_id FROM registration WHERE student_id=%s AND course_code=%s", (reg.student_id, reg.course_code))

    #         if cur.fetchone():
    #             updation = "UPDATE attandance SET course_code=%s, course_name=%s, teacher_id=%s, semester=%s, grade=%s, status=%s WHERE student_id=%s AND course_code=%s"
    #             data = (reg.course_code, reg.course_name, reg.teacher_id, reg.semester, reg.grade, reg.status, reg.student_id, reg.course_code)

    #             # update Student registration record
    #             cur.execute(updation, data)
    #             db.commit()
    #             print("registration updated")
    #         else:
    #             print("Record Not Found")
    #     except Exception as e:
    #         db.rollback()
    #         print(e)
    #     finally:
    #         cur.close()
            
    # update attandance record
    def update_attandance(self, attandance):
        try:
            cur = self.__db.cursor()
            cur.execute("SELECT student_id FROM attandance WHERE student_id=%s", (attandance.student_id,))

            if cur.fetchone():
                cur.execute("SELECT * FROM attandance WHERE student_id=%s AND course_code=%s", (attandance.student_id, attandance.course_code))

                if cur.fetchall():
                    updation = "UPDATE attandance SET status=%s WHERE student_id=%s AND course_code=%s"
                    data = (attandance.status, attandance.student_id, attandance.course_code)
                    # update Student Attandance
                    cur.execute(updation, data)
                    self.__db.commit()
                    print("Attandance updated")
                else:
                    print("Student doesn't have any record of that course")
            else:
                print("Wrong ID! Student attandance record Not Found")
        except Exception as e:
            self.__db.rollback()
            print(e)
        finally:
            cur.close()

    # display all uni records
    def display_universities(self):
        try:
            cur = self.__db.cursor()
            cur.execute("SELECT * FROM university")
            result = cur.fetchall()

            if result:
                for uni in result:
                    print(uni)
            else:
                print("University Table is Empty")

        except Exception as e:
            self.__db.rollback()
            print(e)
        finally:
            cur.close()

    # display all dep records 
    def display_depatments(self):
        try:
            cur = self.__db.cursor()
            cur.execute("SELECT * FROM department")
            result = cur.fetchall()

            if result:
                for dep in result:
                    print(dep)
            else:
                print("Department Table is Empty")

        except Exception as e:
            self.__db.rollback()
            print(e)
        finally:
            cur.close()

    # display all courses
    def display_courses(self):
        try:
            cur = self.__db.cursor()
            cur.execute("SELECT * FROM courses")
            result = cur.fetchall()

            if result:
                for course in result:
                    print(course)
            else:
                print("Course Table is Empty")

        except Exception as e:
            self.__db.rollback()
            print(e)
        finally:
            cur.close()

    # display all students
    def display_students(self):
        try:
            cur = self.__db.cursor()
            cur.execute("SELECT * FROM student")
            result = cur.fetchall()

            if result:
                for student in result:
                    print(student)
            else:
                print("Students Table is Empty")

        except Exception as e:
            self.__db.rollback()
            print(e)
        finally:
            cur.close()

    # Display all teachers records
    def display_teachers(self):
        try:
            cur = self.__db.cursor()
            cur.execute("SELECT * FROM teacher")
            result = cur.fetchall()

            if result:
                for teacher in result:
                    print(teacher)
            else:
                print("Teacher table is empty")

        except Exception as e:
            self.__db.rollback()
            print(e)
        finally:
            cur.close()

    # display attandance of a particular course of a student
    def display_attandance(self, sid, course_code):
        try:
            cur = self.__db.cursor()
            cur.execute("SELECT * FROM student WHERE student_id=%s", (sid,))
            # check if student exist
            if cur.fetchall():
                cur.execute("SELECT * FROM attandance WHERE student_id=%s AND course_code=%s", (sid, course_code))
                result = cur.fetchall()

                if result:
                    for record in result:
                        print(record)
                else:
                    print("Student doesn't have any record of that course")
            else:
                print("Wrong ID! Student record not found")

        except Exception as e:
            self.__db.rollback()
            print(e)
        finally:
            cur.close()

    # Display courses registered by a particular student
    def display_reg_courses(self, id):
        try:
            cur = self.__db.cursor()
            cur.execute("SELECT * FROM student WHERE student_id=%s", (id,))
            
            if cur.fetchall():
                cur.execute("SELECT * FROM registration WHERE student_id=%s", (id,))
                result = cur.fetchall()

                if result:
                    for course in result:
                        print(course)
                else:
                    print("Student doesn't registered any course")
            else:
                print("Wrong ID! Student record not found")

        except Exception as e:
            self.__db.rollback()
            print(e)
        finally:
            cur.close()
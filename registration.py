class Registration:
    def __init__(self, student_id, course_code, teacher_id, course_name, semester, grade, status):
        self.__student_id = student_id
        self.__course_code = course_code
        self.__teacher_id = teacher_id
        self.__semester = semester
        self.__grade = grade
        self.__status = status
        self.__course_name = course_name

    @property
    def student_id(self):
        return self.__student_id
    @student_id.setter
    def student_id(self, student_id):
        self.__student_id = student_id

    @property
    def course_code(self):
        return self.__course_code
    @course_code.setter
    def course_id(self, course_code):
        self.__course_code = course_code

    @property
    def course_name(self):
        return self.__course_name
    @course_name.setter
    def course_name(self, course_name):
        self.__course_name = course_name

    @property
    def teacher_id(self):
        return self.__teacher_id
    @teacher_id.setter
    def teacher_id(self, teacher_id):
        self.__teacher_id = teacher_id

    @property
    def semester(self):
        return self.__semester
    @semester.setter
    def semester(self, semester):
        self.__semester = semester

    @property
    def grade(self):
        return self.__grade
    @grade.setter
    def grade(self, grade):
        self.__grade = grade

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status):
        self.__status = status

    def __str__(self):
        return f"Student ID : {self.__student_id}\nCourse Code : {self.__course_code}\nCourse Name : {self.__course_name}\nTeacher ID : {self.__teacher_id}\nSemester : {self.__semester}\nGrade : {self.__grade}\nStatus : {self.__status}"

from datetime import datetime
class Attandance:
    def __init__(self, student_id, course_code, status, date = datetime.now()):
        self.__student_id = student_id
        self.__course_code = course_code
        self.__status = status
        self.__date = date

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
    def course_code(self, course_code):
        self.__course_code = course_code

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status):
        self.__status = status

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date):
        self.__date = date

    def __str__(self):
        return f"Student ID : {self.__student_id}\nCourse Code : {self.__course_code}\nDate : {self.__date}\nStatus : {self.__status}"
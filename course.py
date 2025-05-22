class Course:
    def __init__(self, course_code, course_name, credit, dep_id):
        self.__course_code = course_code
        self.__course_name =course_name
        self.__credit = credit
        self.__dep_id = dep_id

    @property
    def course_code(self):
        return self.__course_code
    @course_code.setter
    def course_code(self, course_code):
        self.__course_code = course_code

    @property
    def course_name(self):
        return self.__course_name
    @course_name.setter
    def course_name(self, course_name):
        self.__course_name = course_name

    @property
    def credit(self):
        return self.__credit
    @credit.setter
    def credit(self, credit):
        self.__credit = credit

    @property
    def dep_id(self):
        return self.__dep_id
    @dep_id.setter
    def dep_id(self, dep_id):
        self.__dep_id = dep_id
    
    def __str__(self):
        return f"Course Code : {self.__course_code}\nCourse Name : {self.__course_name}\nCredit : {self.__credit}\nDepartment ID : {self.__dep_id}"
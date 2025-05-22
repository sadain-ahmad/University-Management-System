class Person:
    def __init__(self, cnic, name, father_name, contact, address, email, gender, dob):
        self.__name = name
        self.__cnic = cnic
        self.__father_name = father_name
        self.__contact = contact
        self.__address = address
        self.__email = email
        self.__gender= gender
        self.__date_of_birth = dob

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def cnic(self):
        return self.__cnic
    @cnic.setter
    def cnic(self, cnic):
        self.__cnic = cnic

    @property
    def father_name(self):
        return self.__father_name
    @father_name.setter
    def father_name(self, father_name):
        self.__father_name = father_name

    @property
    def contact(self):
        return self.__contact
    @contact.setter
    def contact(self, contact):
        self.__contact = contact
    
    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address):
        self.__address = address

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def gender(self):
        return self.__gender
    @gender.setter
    def gender(self, gender):
        self.__gender = gender

    @property
    def date_of_birth(self):
        return self.__date_of_birth
    @date_of_birth.setter
    def date_of_birth(self, dob):
        self.__date_of_birth = dob

    def __str__(self):
        return f"CNIC : {self.__cnic}\nName : {self.__name}\nFather Name : {self.__father_name}\nContact : {self.__contact}\nAddress : {self.__address}\nEmail : {self.__email}\nGender : {self.__gender}\nDate Of Birth : {self.__date_of_birth}"


class Student(Person):
    def __init__(self, id, cnic, name, father_name, contact, address, email, gender, dob, dep_id):
        super().__init__(cnic, name, father_name, contact, address, email, gender, dob)
        self.__dep_id = dep_id
        self.__id = id

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def dep_id(self):
        return self.__dep_id
    @dep_id.setter
    def dep_id(self, dep_id):
        self.__dep_id = dep_id

    def __str__(self):
        return super().__str__() + f"\nStudent ID :{self.__id}\nDepartment ID : {self.__dep_id}"

class Teacher(Person):
    def __init__(self, id, cnic, name, father_name, contact, address, email, gender, dob, speciality, post, dep_id):
        super().__init__(cnic, name, father_name, contact, address, email, gender, dob)
        self.__post = post
        self.__dep_id = dep_id
        self.__speciality = speciality
        self.__id = id

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def dep_id(self):
        return self.__dep_id
    @dep_id.setter
    def dep_id(self, dep_id):
        self.__dep_id = dep_id

    @property
    def post(self):
        return self.__post
    @post.setter
    def post(self, post):
        self.__post = post

    @property
    def speciality(self):
        return self.__speciality
    @speciality.setter
    def speciality(self, speciality):
        self.__speciality = speciality

    def __str__(self):
        return super().__str__() + f"\nTeacher ID : {self.__id}\nDepartment ID : {self.__dep_id}\nSpeciality : {self.__speciality}\nGrade : {self.__post}"

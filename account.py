class Account:
    def __init__(self, id, password, email):
        self.__id = id
        self.__password = password
        self.__email = email

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email):
        self.__email = email
    
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password):
        self.__password = password
    
    def __str__(self):
        return f"ID : {self.__id}\nEmail : {self.__email}\nPassword : {self.__password}"
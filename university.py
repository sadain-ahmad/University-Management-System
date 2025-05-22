class University:
    def __init__(self, id, name, address):
        self.__id = id
        self.__name = name
        self.__address = address

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address):
        self.__address = address

    def __str__(self):
        return f"University ID : {self.__id}\nName : {self.__name}\nAdress : {self.__address}"
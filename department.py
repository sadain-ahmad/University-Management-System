class Department:
    def __init__(self, dep_id, name, uni_id):
        self.__dep_id = dep_id
        self.__name = name
        self.__uni_id = uni_id

    @property 
    def uni_id(self):
        return self.__uni_id
    @uni_id.setter
    def uni_id(self, uni_id):
        self.__uni_id = uni_id

    @property
    def dep_id(self):
        return self.__dep_id
    @dep_id.setter
    def dep_id(self, dep_id):
        self.__dep_id = dep_id
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

    def __str__(self):
        return f"Department ID : {self.__dep_id}\nName : {self.__name}\nUniversity ID : {self.__uni_id}"
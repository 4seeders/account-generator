class User:
    __password = '1qaz2wsx!@'
    def __init__(self, id, name, email):
        self._id = id
        self._name = name
        self._email = email
    
    def get_password(self):
        return self.__password
    
    def get_id(self):
        return self._id
    
    def get_full_name(self):
        return self._name
    
    def get_first_name(self):
        return self._name[1:]
    
    def get_last_name(self):
        return self._name[:1]

    def get_email(self):
        return self._email
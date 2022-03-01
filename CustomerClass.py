#Class Name: Customer

#Data Attributes:
#__name
#__address
#__phone

#Methods:
#__init__(name, address, phone)
#set_name(name)
#set_address(address)
#set_phone(phone)
#get_name()
#get_address()
#get_phone()


class Customer:

    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone
    
    #def set_name(name):
    #def set_address(address):
    #def set_phone(phone):
    
    def get_name(self):
        return self.__name
    def get_address(self):
        return self.__address
    def get_phone(self):
        return self.__phone
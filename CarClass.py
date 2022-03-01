#Class Name: Car

#Data Attributes:
#__make
#__model
#__year

#Methods:
#__init__(make, model, year)
#set_make(make)
#set_model(model)
#set_year(y)
#get_make()
#get_model()
#get_year()


class Car:

    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year
    
    #def set_make(make):
    #def set_model(model):
    #def set_year(year):
    
    def get_make(self):
        return self.__make
    def get_model(self):
        return self.__model
    def get_year(self):
        return self.__year
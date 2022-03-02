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
    
    def set_make(self, make):
        self.__make = make
    def set_model(self, model):
        self.__model = model
    def set_year(self, year):
        self.__year = year

    def get_make(self):
        return self.__make
    def get_model(self):
        return self.__model
    def get_year(self):
        return self.__year

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
    
    def set_name(self, name):
        self.__name = name
    def set_address(self, address):
        self.__address = address
    def set_phone(self, phone):
        self.__phone = phone

    def get_name(self):
        return self.__name
    def get_address(self):
        return self.__address
    def get_phone(self):
        return self.__phone


#Class Name: ServiceQuote

#Data Attributes:
#__parts_charges
#__labor_charges

#Methods:
#__init__(pcharge, lcharge)
#set_parts_charges(pcharge)
#set_labor_charges(lcharge)

#get_parts_charges()
#get_labor_charges()
#get_sales_tax()
#get_total_charges()


class ServiceQuote:

    def __init__(self, pcharge, lcharge):
        self.__parts_charges = pcharge
        self.__labor_charges = lcharge
        self.__sales_tax = 1.0825
    
    def set_parts_charges(self, pcharge):
        self.__parts_charges = pcharge
    def set_labor_charges(self, lcharge):
        self.__labor_charges = lcharge

    def get_parts_charges(self):
        return self.__parts_charges
    def get_labor_charges(self):
        return self.__labor_charges


    def get_sales_tax(self):
        return self.__sales_tax

    def get_total_charges(self):
        total_charges = (self.__parts_charges + self.__labor_charges)
        taxed = total_charges * self.__sales_tax
        return taxed


import CarClass as carc
import CustomerClass as cusc
import ServiceQuoteClass as serc

def main():
    print("Enter the following data for a Customer.")
    
    cust_instance = cusc.Customer("NULL", "NULL", "NULL")

    name = input('Customer Name: ')
    address = input('Customer Address: ')
    phone = input('Customer Phone: ')

    cust_instance.set_name(name)
    cust_instance.set_address(address)
    cust_instance.set_phone(phone)

    print()
    print("Customer Name:", cust_instance.get_name())
    print("Customer Address:", cust_instance.get_address())
    print("Customer Phone:", cust_instance.get_phone())
    print()

    print("Enter the following data for a customer.")
    car_instance = carc.Car("NULL", "NULL", "NULL")

    make = input("Car Make: ")
    model = input("Care Model: ")
    year = input("Car Year:" )

    car_instance.set_make(make)
    car_instance.set_model(model)
    car_instance.set_year(year)

    print()
    print("Car Make:", car_instance.get_make())
    print("Car Model:", car_instance.get_model())
    print("Car Year:", car_instance.get_year())
    print()

    print("Enter the following data for the service quote.")

    service_instance = serc.ServiceQuote(0,0)
    pcharge = float(input("Enter Parts Charge: "))
    lcharge = float(input("Enter Labor Charge: "))
    service_instance.set_parts_charges(pcharge)
    service_instance.set_labor_charges(lcharge)

    print()
    print("Total Charge:", service_instance.get_total_charges())

main()
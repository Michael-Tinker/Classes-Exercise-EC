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
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
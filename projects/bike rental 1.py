from bike_rental  import BikeRental, Customer
from helpers import generate_order_id

def bike_rent(): 
    with open("projects/database.txt", "r") as file:
        data = eval(file.read())
    
    # data = {"store":100}
    shop = BikeRental(data["store"])

    while True:
        customer = Customer()
        
        print("""
        ====== Bike Rental Shop =======
        1. Display available bikes
        2. Request a bike on hourly basis $5
        3. Request a bike on daily basis $20
        4. Request a bike on weekly basis $60
        5. Return a bike
        6. Exit
        """)
        
        choice = input("Enter choice: ")
        
        try:
            choice = int(choice)
        except ValueError:
            print("That's not an int!")
            continue
        
        if choice == 1:
            shop.display_stock()
        
        elif (choice == 2) or (choice == 3) or (choice == 4) :
            customer.order_id = generate_order_id()
            if choice == 2:
                customer.rentalTime = shop.rent_on_hourly_basis(customer.requestBike())
                customer.rentalBasis = "hourly"


            elif choice == 3:
                customer.rentalTime = shop.rent_on_daily_basis(customer.requestBike())
                customer.rentalBasis = "daily"

            elif choice == 4:
                customer.rentalTime = shop.rent_on_weekly_basis(customer.requestBike())
                customer.rentalBasis = "weekly"
            
            print(f"Order ID: {customer.order_id}")
            data["store"] = shop.stock
            data[customer.__dict__.pop('order_id')] = customer.__dict__
        

        elif choice == 5:
            print("\nEnter your order id:")
            code = input(">")
            order = data.get(code)
            if order:
                if order["returned_bike"]:
                    print("This code has already been used!")
                else:
                    customer.rentalBasis, customer.rentalTime, customer.bikes = order['rentalBasis'], order["rentalTime"], order['bikes']
                    # print(customer.__dict__)
                    bill = shop.returnBike(customer.returnBike())
                    order['bill'] = bill
                    order["returned_bike"] = True
                    data[code] = order
                    data["store"] = shop.stock
                    customer.rentalBasis, customer.rentalTime, customer.bikes, customer.returned_bike = 0,0,0,False

            else:
                print("Invalid code")

        elif choice == 6:
            with open("projects/database.txt", "w") as file:
                file.write(str(data))
            break
        else:
            print("Invalid input. Please enter number between 1-6 ")        
    print("Thank you for using the bike rental system.")


if __name__=="__main__":
    bike_rent()
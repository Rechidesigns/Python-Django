import datetime

class BikeRental:
    """This class represents a bike rental shop"""
    
    HOURLY_PRICE = 5
    DAILY_PRICE = 20
    WEEKLY_PRICE = 60
    FAMILY_DISCOUNT = 0.75
    
    def __init__(self, stock:int = 0):
        """This constructor is used to create a new instance of the bike rental shop with a default stock of 0."""
        
        self.stock = stock
        
    
    def display_stock(self):
        """
        Displays the bikes currently available for rent in the shop.
        """
        print("We currently have {} bikes available to rent.".format(self.stock))
        return self.stock
    
    
    def rent_on_hourly_basis(self, num_of_bikes):
        """
        Rents a bike on hourly basis to a customer.
        """
        # reject invalid input 
        if num_of_bikes<= 0:
            print("Number of bikes should be positive!")
            return None
        
        if not isinstance(num_of_bikes, int):
            print("Number of bikes should be a valid integer!")
            return None
        
        # do not rent bike is stock is less than requested bikes
        
        if num_of_bikes > self.stock:
            print("Sorry! We have currently {} bikes available to rent.".format(self.stock))
            return None
        
        # rent the bikes        
        else:
            now = datetime.datetime.now()                      
            print("You have rented a {} bike(s) on hourly basis today at {}:{} hours.".format(num_of_bikes,now.hour, now.minute))
            print("You will be charged $5 for each hour per bike.")
            print("We hope that you enjoy our service.")
            self.stock -= num_of_bikes
            return now.isoformat()    
          
    def rent_on_daily_basis(self, num_of_bikes):
        """
        Rents a bike on daily basis to a customer.
        """
        # reject invalid input 
        if num_of_bikes<= 0:
            print("Number of bikes should be positive!")
            return None
        
        if not isinstance(num_of_bikes, int):
            print("Number of bikes should be a valid integer!")
            return None
        
        # do not rent bike is stock is less than requested bikes
        
        if num_of_bikes > self.stock:
            print("Sorry! We have currently {} bikes available to rent.".format(self.stock))
            return None
        
        # rent the bikes        
        else:
            now = datetime.datetime.now()                      
            print("You have rented a {} bike(s) on hourly basis today at {}:{} hours.".format(num_of_bikes,now.hour, now.minute))
            print("You will be charged $20 for each hour per bike.")
            print("We hope that you enjoy our service.")
            self.stock -= num_of_bikes
            return now.isoformat()   
            
    def rent_on_weekly_basis(self, num_of_bikes):
        """
        Rents a bike on hourly basis to a customer.
        """
        # reject invalid input 
        if num_of_bikes<= 0:
            print("Number of bikes should be positive!")
            return None
        
        if not isinstance(num_of_bikes, int):
            print("Number of bikes should be a valid integer!")
            return None
        
        # do not rent bike is stock is less than requested bikes
        
        if num_of_bikes > self.stock:
            print("Sorry! We have currently {} bikes available to rent.".format(self.stock))
            return None
        
        # rent the bikes        
        else:
            now = datetime.datetime.now()                      
            print("You have rented a {} bike(s) on hourly basis today at {}:{} hours.".format(num_of_bikes,now.hour, now.minute))
            print("You will be charged $60 for each hour per bike.")
            print("We hope that you enjoy our service.")
            self.stock -= num_of_bikes
            return now.isoformat()       
    
    def returnBike(self, request):
        """
        1. Accept a rented bike from a customer
        2. Replensihes the inventory
        3. Return a bill
        """
        
        rentalTime, rentalBasis, numOfBikes = request
        bill = 0

        if rentalTime and rentalBasis and numOfBikes:
            self.stock += numOfBikes
            now = datetime.datetime.now()
            rentalPeriod = now - datetime.datetime.fromisoformat(rentalTime)
        
            # hourly bill calculation
            if rentalBasis == "hourly":
                bill = round(rentalPeriod.seconds / 3600) * BikeRental.HOURLY_PRICE * numOfBikes
                
            # daily bill calculation
            elif rentalBasis == "daily":
                bill = round(rentalPeriod.days) * BikeRental.DAILY_PRICE * numOfBikes
                
            # weekly bill calculation
            elif rentalBasis == "weekly":
                bill = round(rentalPeriod.days / 7) * BikeRental.WEEKLY_PRICE * numOfBikes
            
               
            if (3 <= numOfBikes <= 5):
                print("You are eligible for Family rental promotion of 25% discount")
                bill *= BikeRental.FAMILY_DISCOUNT

            print("Thanks for returning your bike. Hope you enjoyed our service!")
            print("That would be ${}".format(bill))
            return bill
        else:
            print("Are you sure you rented a bike with us?")
            return None
        
class Customer:
    """This class represents a customer"""
    
    def __init__(self):
        """
        Our constructor method which instantiates various customer objects.
        """
        
        self.bikes = 0
        self.rentalBasis = 0
        self.rentalTime = 0
        self.bill = 0
        self.order_id = ""
        self.returned_bike = False

    
    def requestBike(self):
        """
        Takes a request from the customer for the number of bikes.
        """
                      
        try:
            bikes = int(input("How many bikes would you like to rent?"))
            
        except ValueError:
            print("That's not a positive integer!")
            return -1

        if bikes < 1:
            print("Invalid input. Number of bikes should be greater than zero!")
            return -1
        
        else:
            self.bikes = bikes
        return self.bikes
     
    def returnBike(self):
        """
        Allows customers to return their bikes to the rental shop.
        """
        
        if self.rentalBasis and self.rentalTime and self.bikes:
            return self.rentalTime, self.rentalBasis, self.bikes  
        else:
            return 0,0,0
        
### banking application

account_no = 0
cus_name = " "
B_code = " "
Mobile = " "
bal = 0

with open("bankapp.txt", "w") as file:
    file.write(str(cus_name))
    file.write(str(account_no))
    file.write(str(B_code))
    file.write(str(Mobile))

def create_account():
    global account_no
    global cus_name
    global B_code 
    global Mobile
    global bal
    account_no = int(input("Enter account number: "))
    cus_name = input("Enter your name: ")
    B_code = input("Enter your band sort code: ")
    Mobile = int(input("Entger your mobile No: "))
    global bal
    bal = int(input("Enter current balcance: "))


def show_acct_details():
    print("account_no:", account_no)
    print("Customers Name:",cus_name) 
    print("Bank sort Code:",B_code)
    print("Mobile",Mobile)

def deposit(amount):
    global bal
    bal = bal + amount
    check_bal()

def withdraw(amount):
    global bal 
    bal = bal - amount
    check_bal()

def check_bal():
    print("Current balance:", bal)

######### main opereations
choice_1 = "y"
while (choice_1 == "y"):
    print("1.Create account\n 2.withdraw \n 3.deposit \n 4.check balance")
    choice = int(input("select any option: "))
    if (choice == 1):
        create_account()
    elif (choice == 2):
        amount = int(input("enter amount to withraw: "))
        withdraw(amount)
    elif choice == 3:
        amount = int(input("Enter amount to withdrae: "))
        deposit(amount)
    elif choice == 4:
        check_bal()
    else:
        print("please select any 4 options available above: ")
    print("do you want to continue.. press y")

    choice_1 = input()


    
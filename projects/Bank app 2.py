import random
from re import L

data = {
    '0123445677' : {
        "first_name":"John",
        "last_name" : "Doe ",
        "login_pin" : "8424",
        "transaction_pin": "0934",
        "balance" : 0
    }
}


def signup(details : dict):
    """ This function takes in a dictionary, asks the user for input details then generates a random account number for the user. It then adds the user data to the original dictionary and returns the updated dictionary. """


    first_name = input("First Name:\n>")
    last_name = input("Last Name:\n>")
    trans_pin = input("Transaction Pin:\n>")
    login_pin = input("Login Code:\n>")


    var = "0"
    for i in range(9):
        var += str(random.choice(range(10)))



    details[var] = {"first_name":first_name,
                    "last_name" : last_name,
                    "login_pin" : login_pin,
                    "transaction_pin": trans_pin,
                    "balance" : 0}

    print(f"You have successfully created an account. Your account number is {var}. You can login to your account using your login code: {login_pin}")

    return details


def login( data: dict):
    acc_num =  input("Account number:\n>")
    login_pin = input("Login Code:\n>")
    user_detail = data.get(acc_num)

    if user_detail and user_detail["login_pin"] == login_pin:
        return user_detail

    else:
        return False


def deposit(user_detail:dict):

    amount = float(input("How much to deposit\n>"))
    user_detail["balance"] += amount
    print(f"\nYour wallet has been credited with #{amount}")
    return user_detail


def withdraw(user_detail:dict):

    trans_pin = input("Enter your pin\n>")

    if trans_pin == user_detail["transaction_pin"]:
        amount = float(input("How much to withdraw\n>"))

        if user_detail["balance"] > amount:
            user_detail["balance"] -= amount
            print(f"\nWithdraw of #{amount} was successful")
            return user_detail
        else:
            print("\nInsufficient funds to withdraw")

    else:
        print("\nIncorrect pin")
        return

def transfer(user_detail:dict, data:dict):
    beneficiary = input("Enter beneficiary account\n>")
    amount = float(input("How much to transfer\n>"))

    beneficiary_detail = data.get(beneficiary)
    if beneficiary_detail:
        if user_detail["balance"] > amount:
            user_detail["balance"] -= amount
            beneficiary_detail["balance"] += amount
            print(f"Transfer of #{amount} was successful")
            return user_detail, data

        else:
            print("\nInsufficient funds to transfer")
            return user_detail, data
    else:
        print("\nUnable to transfer to unknown account.")
        return user_detail, data


print("Welcome to ClassikAlat")

while True:
    print("\nEnter L to login or S to signup or Q to quit.")
    choice = input(">").lower()

    if choice == "s":
        data = signup(data)
    elif choice == "l":
        user_detail = login(data)
        print("Welcome", user_detail["first_name"])
        if user_detail:
            while True:
                print("""\nEnter the corresponding number for the action you wish to perform.
                1. Check Balance
                2. Deposit
                3. Withdraw
                4. Transfer
                5. Logout
                    """)
                action  = input(">")
                if action == "1":
                    print(f"\nYour account balance is #{user_detail['balance']}")
                elif action == "2":
                    user_detail = deposit(user_detail)
                elif action == "3":
                    user_detail = withdraw(user_detail)
                elif action == "4":
                    user_detail, data = transfer(user_detail, data)
                elif action == "5":
                    print("\nLog out complete!")
                    break
                else:
                    print("\nInvalid input")
        else:
            print("Invalid account number or pin")

    elif choice == "q":
        print("\nBye!")
        break
    else:
        print("\nInvalid input")

print(data) 

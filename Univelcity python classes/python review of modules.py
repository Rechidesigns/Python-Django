#### OOP

class Details:
    def __init__(self, name, age, number):
        self.name = name
        self.age = age
        self.number = number

personal_details = Details("King Rechi", "22years", "08160251019")

print(personal_details.name, personal_details.age, personal_details.number)

name = "King"
phone_no = "08160251019"
statement = f"Your name is {name} and your phone number is {phone_no}, congratulations."

print(statement)




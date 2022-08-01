# ###   class


# class Dog():

#     def __init__(self, bread, color, weight):   #self is the instance of the parameter. talks about instance
#         self.bread = bread
#         self.color = color
#         self.weight = weight

#     def __str__(self):
#         return self.bread ### magic method

#     def run(self):
#         return f"this dog with {self.weight} is running"

# dog1 = Dog("German shepherd", "Black", "20kg")
# dog2 = Dog("Bull dog", "white", "28kg")

# print(dog1)
# print(dog1.bread, dog1.color, dog1.weight)
# print(dog2.bread, dog2.weight, dog2.color)

# print(dog1.run())
# print(dog2.run())


class Dog():
    
    num_of_limbs = 4
    
    def __init__(self, breed : str, color : str, weight : int):
        self.breed = breed
        self.color = color
        self.weight = weight
        
    
    
    def __str__(self):
        return self.breed
        
    def __add__(self, other):
        
        if isinstance(other, Dog):
            
            return self.weight + other.weight
        
        raise TypeError("Expected type of Dog but got %s" % type(other))
    
    
    def run(self):
        return f"This dog with {self.weight}kg is running"
        
        
    
dog1 = Dog("German shepherd", "black", 20)
dog2 = Dog("Bull dog", "black", 14)


# print(dog1 + dog2)
# print(dog1.breed, dog1.weight, dog1.color)

# print(Dog.num_of_limbs)


print(dog1.run())
print(dog2.run())



class Data():
    def __init__(self, name, hight, age, code):
        self.name = name
        self.hight = hight
        self.age = age
        self.code = code

    def mine(self):
        return f"Your name is {self.name} and your hight is {self.hight}, you are {self.age} years and your unique number is {self.code}."
        
    def zulu(self):
        return f"Hi, my name is {self.name}, am {self.age} years old and am {self.hight} tall, my unique code is {self.code}."

personal_data = Data('King', "6.2kg", "26", "001")
rechis_data = Data("Rechi", "7 ft", 28, "005")

# print(personal_data.name, personal_data.hight,personal_data.age, personal_data.code)
        
print(personal_data.mine()) 
print(rechis_data.zulu())
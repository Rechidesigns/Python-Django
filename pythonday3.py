# string = "this is my string"
# search_for = "is"
# total = string.count (search_for)

# print(f"{total} result(s) found")
# print(string.replace(search_for, search_for.upper()))

# "string = this is a string"
# print(string.replace(" ", "_"))

# string = "this is a string"
# print(string.replace(" ", ","))

# str_list = ["this", "is", "a", "string"]
# joined= " ".join(str_list)

# print(joined)

####### FUNCTIONS    ####
from ast import Return
from email.charset import add_alias
import string


def add_numbers():
    print(4+5)

add_numbers()

def add_numbers(a, b):
    print(a+b)

add_numbers(50,50)


# docs string

def add_numbers(a:int, b:int):
    """This function adds numbers.

    Args:
        a (int): This is the first number to be added
        b (int): This is the second number to be added

    Returns:
        a+b (int): This is the addition of a and b
        """
    
    return a+b

b = add_numbers(53,35)
print(b)

#####################################

def add_numbers(p:int, r:int, t:int):
    """This function calculates and returns simple interest.

    Args:
        p (int): This is the principal
        r (int): This is the rate
        t (int): This is the time

    Returns:
        p*r*t (int): This is the addition of p, r and t
        """
    return p*(r/100)*t

b = add_numbers(6,78,9)

print(b)

 
 #### class work 2

def poc(r:int):
    """  
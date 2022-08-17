# for x in range(10):
#     print(x)

# a = [3,4,5,6,7,4]
# b = []
# for i in a:
#     b.append(i**2)
# print(b)

# a = [3,4,5,6,7,4]
# b = [x**2 for x in a] ### EXAMPLE OF LIST COMPREHENSION
# print(b)


# a = [3,4,5,6,7,4]
# c = [x for x in a if x%2==0]
# print(c)


#### classwork
## write a function that takes a number and returns true or fals,
#  that tells us if that number is a prime number or not


##############    google answer############

# # Program to check if a number is prime or not

# # To take input from the user
# num = int(input("Enter a number: "))

# # define a flag variable
# number_to_check = False

# # prime numbers are greater than 1
# if num > 1:
#     # check for factors
#     for i in range(2, num):
#         if (num % i) == 0:
#             # if factor is found, set flag to True
#             number_to_check = True
#             # break out of loop
#             break

# # check if flag is True
# if number_to_check:
#     print(num, "True")
# else:
#     print(num, "False")


# ### correction
# from math import sqrt
# from operator import truediv
# def is_prime(n:int):
#     if n == 1:
#         return False
#     if n == 2:
#         return True
    
#     for factor in range(2, int(sqrt(n))+1):
#         if n % factor == 0:
#             return False

#     return True

# print(is_prime(12))


#####   class work 2
### given two strings s1 and s2, check if both the strings are anagrams of each other.

def anagrams(str1, str2):
    if sorted(str1) == sorted(str2):
        return True
    return False
    
print(anagrams("teach", "cheat"))







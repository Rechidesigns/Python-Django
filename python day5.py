######## #conditioners

# person = input("Nationality? ").lower()

# if person == "french" or person == "francis":
#     name = input("comment tu t 'appelle? ").title()
#     going_to_school = input("Allez-vous a l' ecole? ")

#     if going_to_school == "yes":
#         print(f"Bienvenue chez au Univelcity, {name}.")
#     else:
#         print(f"Au revoir, {name}. Bonne journee.")

# elif person == "Italian":
#     print("Preferisci parlare italiano?. ")

# else:
#     print("you are neither french nor italian.")
#     print("so, let us speak english.")


######### Recursion
# def factorial(n):
#     if n == 1:
#         return 1

#     return n * factorial(n-1)

# print(factorial(5))

#### inbuilt module 

# import random 
# name = ["Alerechi", 4, 5, 23, 6]
# random.shuffle(name)
# print(name)

# import random
# from unicodedata import name
# name = "Alerechi"

# print(random.choice(name))


##### LIST

# my_list = [3,38,4,5,9,8]
# print(my_list)
# print(my_list[2:5])


# my_list = [4,5,7,8,2,1]
# print(my_list)
# my_list[3]=90

# print(my_list)

# import random as rd

# num = list(range(50,53805))
# rd.shuffle(num)

# print(sorted(num, reverse=True))
# print(sorted(num, reverse=True)[:5])


##### Guess game

import random as rd

num = list(range(60,80))
rd.shuffle(num)
print("Welcome to my Game")
print(num)
gamer_choice = int(input("Select from the numbers given > "))
comp_choice = rd.choice(num)

if gamer_choice in num:
    if gamer_choice == comp_choice:
        print("You Won")

    else:
        if gamer_choice > comp_choice:
            print("Too High")
            print(comp_choice)

        else:
            print("Too Low")
            print(comp_choice)

else:
    print("Invalid Input")

##### list 2

list1 = [4,3,5,6,7,8]
list2 = [9,4,2,5,7,9]

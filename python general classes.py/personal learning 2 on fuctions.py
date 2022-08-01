# name = input("Hello user, kindly inpute your name: ")
# my_name = name.split()
# my_name[0] = my_name[0].upper()
# print(" ".join(my_name))

# a = "i are learning python"
# print(a.replace('i', 'you'))

# statement = "i hope you had fun in class today"
# print(statement.count("a"))


# def check_fermat(a,b,c,n):
#     if n > 2 and (a**n + b**n == c**n):
#         print("holly fermat is coreect")
#     else:
#         print("that doesnt work")



# def check_fermat(a,b,c,n):
#     if n > 2 and (a**n + b**n == c**n):
#         print("Holy smokes, Fermat was wrong!")
#     else:
#         print("No, that doesn't work.")

# def get_data():
#     a = int(input())
#     b = int(input())
#     c = int(input())
#     n = int(input())

#     check_fermat(a,b,c,n)

# get_data()


# def check_fermat(a,b,c,n):
#     if n > 2 and (a**n + b**n == c**n):
#         print("Holy smokes, Fermat was wrong!")
#     else:
#         print("No, that doesn't work.")



# def get_data():
#     a = input()
#     b = input()
#     c = input()
#     n = input()

#     check_fermat(a,b,c,n)


# get_data()


# user_name = input("Hello user, kindly enter your name: ")
# name = user_name.split()
# name[0] = name[0].upper()
# print(''.join(name))

# list_1 = [2,3,5,6,7,8,9,0]
# list_2 = [8,9,6,0,4,3,2,5]

# total_list = zip(list_1, list_2)
# print(dict(total_list))

# def bd_wish(name):
#     print("Hello!", name)
#     print("Happy birthday to you")
#     print("Today you are {d_o_b} years old")

# bd_wish('Clara')
# d_o_b = [29]
 

# def bd_wish(name):
#     print("Hello!", name)
#     print("Happy birthday to you")
#     print("Today you are 29 years old")

# bd_wish('Clara')

# def add_numbers(n1, n2, n3, n4):
#     results = n1 + n2 +n3 +n4
#     print('this is your total:', results)

# number1 = 5.5
# number2 = 6.5
# number3 = 2.8
# number4 = 3.6

# add_numbers(number1, number2, number3, number4)

# def day(today):
#     print("Hello everyone!")
#     print("Its a new week and today is", today)

# today = monday   
# day()


# def birthday(a):

#     print("Hi", a)
#     print("Happy birthday to you!")

# birthday("clara")

# def numbers(n1, n2):
#     total_numbers = n1 + n2
#     print("Your total number is:", total_numbers)

# number1 = 54
# number2 = 29

# numbers(number1, number2)

# def command(name1, name2):
#     print("Hello", name1 and name2)
#     print("Every tuesday is a staff meeting")

# command("Vina", "James")

# def numbers(n1, n2):
#     total_num = n1 +n2
#     return total_num

# number1 =20
# number2 = 30
# total_num = numbers(number1, number2)

# print("The sum total is:",total_num )


# def school_marks(marks):
#     total_mark = sum(marks)
#     total_subjects = len(marks)
#     average_score = total_mark/total_subjects
#     return average_score

# def grading_score(average_score):
#     if average_score >= 80:
#         grade = "A"
#     elif average_score >= 60:
#         grade = "B"
#     elif average_score >= 50:
#         grade = "C"
#     else:
#         grade = "F"
#     return grade

# marks = [55,64,75,80,65]
# average_score = school_marks(marks)
# print("Your average score is:", average_score)
# grade = grading_score(average_score)
# print("Your grade is", grade)



# def add_numbers(a, b, c):
#     add_total = a + b + c
#     return add_total

# def multiply_numbers(a, b, c):
#     multiply_all = a * b * c
#     return multiply_all


# a = 2
# b = 4
# c = 6

# add_total = add_numbers(a, b, c)
# print("Your total is:", add_total)
# multiply_all = multiply_numbers(a, b, c)
# print("Your total multiplied sum is:", multiply_all)


# def add_numbers(numbers):
#     add_total = sum(numbers)
#     return add_total



# numbers = [2, 4, 6]
# add_total = add_numbers(numbers)
# 
# print("Your total is:", add_total)


# def total_marks(marks):
#     add_total_marks = sum(marks)
#     number_of_courses = len(marks)
#     average_mark = add_total_marks/number_of_courses
#     return average_mark

# def grading(average_mark):
#     if average_mark >= 80:
#         grade = "A"
#     elif average_mark >= 60:
#         grade = "B"
#     elif average_mark >= 50:
#         grade = "C"
#     else:
#         grade = "F"
#     return grade

# marks = [ 80, 90, 75, 98]
# average_mark = total_marks(marks)
# print("Your average score is:", average_mark)
# grade = grading(average_mark)
# print("Your grade is:", grade)



# def add_numbers(two_numbers):
#     numbers_added = sum(two_numbers)
#     return numbers_added

# def multiply_numbers(a, b):
#     numbers_multiplied = 55 * 70
#     return numbers_multiplied

# a = 55
# b = 70
# two_numbers = [55, 70]
# numbers_added = add_numbers(two_numbers)
# print('Total when adden is:', numbers_added)
# numbers_multiplied = multiply_numbers(a, b)
# print("Total when multiplied:", numbers_multiplied)

from email import message


def greet(name, message):
    print("Hello", name)
    print(message)

greet("jack", "whats going on?")
greet(message = "How are you?", name = "King")






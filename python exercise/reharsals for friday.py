#### note: a list is are statement in squar bracket []

# ####### functions

# def do_twice(f):
#     f()
#     f()

# print(do_twice)


# ###### four loop
# even_num = [2,4,6,8,]
# for num in even_num:
#     print(num)


# week_days = ["mon", "tues", "wed", "thurs", "fri", "sat", "sun"]
# for day in week_days:
#     print(day)

# sentence = "its been a long time learning python. i am revisng the basics!!"
# for letter in sentence:
#     print(letter)

# ### add split method
# sentence = "its been a long time learning python. i am revisng the basics!!"
# for letter in sentence.split():
#     print(letter)

# #for loop in dictionary

# countries_code = {"united states: 1,
# india: "}


# for i in range(1,13):
#     print("2 x", i, "=", 2 * i, "\n" )

# for i in range(1,12):
#     print("5 x", i, "=", 5 * i, "\n")

# letters = []
# for letters in "machinelearning":
#     letters.append(letters)
# letters

#### another form of index

# import struct


# name = "Richie"
# if len(name) > 5:
#     print('length of the string is greater than 5')
# else:
#     print("length of string is less tah 5")


# ######while loop
#  # while loop executes the statement(s) as long as the condition is true.
#  ###struct of a while loop


# a = 10
# while a < 20:
#     print("a is: {}".format(a))
#     #a = a+1
#     a += 1

# a = 10
# while a < 20:
#     print("a is: {}".format(a))
#     # a = a+1
#     # a += 1


# i = 1
# while i < 6:
#     print(i)
#     if i == 4:
#         break
#     i+=1


############ functions

# from sqlite3.dbapi2 import _Statement
# from this import d


# def function_name(Parameters):
#     """
#     THI IS A DOC STRING
#     YOU CAN USE IT TO WRITE NOTES ABOUT THE FUNCTIONS
#     """
#     Statements

#     return results

## function to add two numbers and return a sum

# def add_nums(a,b):
#     """"
#     function to add two numbers given as inputs
#     it will return a sum of sum of these two numbers
#     """
#     return print(a+b)
#     # return sum

# add_nums(2,4)
# add_nums(4,9)

# def activity(name_1, name_2):
#     print("{} and {} are playing basketball!".format(name_1, name_2))



######### lambda

# #####docs.python.org/3/library/functools.html
# sum_of_two_nums = lambda c,d: c + d
# sum_of_two_nums(4,5)

######built in functions
#using len() to count length of the string

# message = "do not give up"
# print(len(message))

#### map fuction
#### longer route to solve it
# num_list = [0,1,2,3,4]
# new_list = []

# def my_cubic_function(number):
#     for i in range(len(number)):
#         result = number[i] ** 3
#         new_list.append(result)
#     print(new_list)

# my_cubic_function(new_list)


### shoter form to solve it
# def cubic(number):
#     return number ** 3
# num_list = [1,2,3,4]
# print(list(map(cubic,num_list)))

# def times2(var):
#     return var * 2
# times2(5)
# ### ouput or ans 10

# seq = [1,2,3,4,5]
# list(map(times2,seq))
### ouput or ans 12345

############# filter function

# def odd_check(number):
#     return number % 2 != 0
#     #!= is not equal to operation

# num_list = [1,2,3,4,5,6,7,8,9,10]
# list(filter(odd_check, num_list))

#### using lambda and filter function

# my_list = [12,65,54,39,102,339,221,50,70]
# result = list(filter(lambda x:(x % 13 == 0), my_list))
# print(result)

# my_list = ["geeg", "peep", "geeks", "keek","madam"]
# result = list(filter(lambda x:(x == "".join(reversed(x))), my_list))
# print(result)

# seqel = [1,2,3,4]
# print(list(filter(lambda num: num % 2 == 0,seqel)))

# ###### class work
# my_list = ["soup", "cat", "sneakers", "dog", "heavy", "salad"]
# print(list(filter(lambda x: x.startswith('s'), my_list)))

### given a list of number,can you make a new list of even numbers from the list nums? 
### even numbers are numbers divisible by 2, and they give the remainder of 0
# nums = range(1,20)
# even_nums = []
# #a traditional way to do this is:

# for num in nums:
#     if num % 2 == 0:
#         even_nums.append(num)

# print(even_nums) 

# even_nums = [num for num in nums if num % 2 ==0]
# print(even_nums)




# days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",]
# day_T = []
# #make a list of days that start with T
# for day in days:

#     if day[0] =="T":
#         day_T.append(day)
# print(day_T)

#A more concise way to do it would be:

# day_T = [day for day in days if day [0] =="T"]
# print(day_T)

######### list comprehension in place of nested forloop
# pairs_1 = []
# for num1 in range(0,2):
#     for num2 in range (6,8):
#         pairs_1.append((num1, num2))
# print(pairs_1)

# seasons = [ 'spring', "summer", "fall", "winter"]
# print(list(enumerate(seasons)))

# class_names = ["rock", "paper", "scissor"]
# for index, class_names in enumerate(class_names, start=0):
#     print(index, '-', class_names)
#####list(enumerate(class_names))

# ####### zip function
# name = ["jessy", "joe", "jeannete"]
# role = ["ml engineer", "web developer", "data engineer"]

# zipped_name_role = zip(name, role)
# zipped_name_role
# list(zipped_name_role)

######3 reduce function
# def gibberish(*args):
#     """"
#     concentrate strings in args together
#     """
#     hodgepodge = ""
#     for word in args:
#         hodgepodge += word
#     return hodgepodge

# print(gibberish("hello ", "dear ", "goodluck!"))



# from functools import reduce
# stark = ["rob", "sansa", "arya", "brandon", "rickon"]
# result = reduce(lambda item1, item2: item1 + item2, stark)
# print(result)

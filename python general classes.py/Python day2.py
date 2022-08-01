# string = "50"
# number ="10"

# my_new_int = int(string)

# print(my_new_int+number)
# print(type(my_new_int))

# a = 10
# b = 5
 
# print(a==b)

##### QUESTION 1

# radius = 5
# pi = 3.142
# volume = (4/3)*pi*(radius**3)
# print (volume)

# ##### QUESTION 2
# price = 24.95
# discounted_price = price*0.6
# shipping_price = 3
# addittional_shipping_price = 0.75
# num_of_copies = 60

# total_book_price = discounted_price*num_of_copies
# total_shipping = shipping_price + (addittional_shipping_price*(num_of_copies-1))

# total_wholesale_cost = total_book_price + total_shipping
# print(total_wholesale_cost)

# ###### QUESTION 3
# start_time = (6*60 + 52) *60
# easy_pace = (8*60 + 15) *2
# tempo_pace = (7*60 + 12) *3

# run_time =  easy_pace+tempo_pace

# home_time = start_time+run_time

# break_fast_hour = home_time//3600
# break_fast_min = (home_time%3600) // 60
# break_fast_sec = (home_time%3600) % 60

# print(f"{break_fast_hour}:{break_fast_min}:{break_fast_sec}am")


###### STRINGS
# a = "Banana"
# b = "fruit"
# c = "orange"

# print(a + b)


# #### INDEX
# first_name = "Alerechi"
# last_name = "Ordu"

# username = first_name[-3:] + last_name[0:3]

# print(username)

### STRINGS 2

# b = "Alerechi Ordu"
# print(b.lower())
# print(b.upper())
# print(b.title())
# print(b.capitalize())
# print(b)

# a = b.replace("Alerechi", "KingRechi")
# print(a)
# print(b.find("r"))
# print(b.index("c"))
# print(b.count("e"))

# new_str = "545cdsd"
# print(new_str.isalnum())



from ast import keyword


name = "Alerechi"
a = 45
b = 38
print(f"welcome, {name}. the sum of {a} and {b} is {a+b}")

help()
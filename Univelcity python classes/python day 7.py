# data = {"name":"Grace",
#         "course":"Backend",
#         "scores":[10,7,9,5,8],
#         "address":{"str_num":40,
#                     "str_name":"montgomery road",
#                     "city":"yaba"},
#         (1,"john"):"this is the tuple"
#     }


# print(data[(1,'JOHN')])


# print(data["name"])
# data["name"] = "Chidi"  #changing the value of the name
# print(data["name"])
# print(data["address"]["city"])
# print(max(data["scores"]))
# print(sum(data["scores"])) 
# print(sum(data["scores"])/len(data["scores"]))

# print(subject[("girl", "young")])
# print(data["boy"]) #### this key gives key error cos the key (boy) doesn't exist

# ## GET METHOD
# print(data.get("boy"))   ###key doesn't exist
# print(data.get("name"))
# print(data.get("boy", "Key doesn't exist"))
# print(data.get("name", "Key doesn't exist"))

# print(data.keys())
# print(data.values())
# print(data.items())
# print(data.pop("name"))
# print(data.pop())  ###if you dont put a key it gives error

# print(data.keys())
# data["first_name"] = data.pop("name") #when you pop data it gives the name which u assign to a new key
# print(data)


# ### class work   / Interview friendly questions.???
# #      xxxxxxxxxxxxx

# #given this dictionary 
# #write a program to sort this dictionaryusing the value.
# data = {"5":8,
#     "3":10,
#     "4":2,
#     "9":3,
#     "2":7,
#     "0":5}

# sorted_x = sorted(data.items(), key=lambda x: x[1], reverse=True)

# print(dict(sorted_x))

# # ###class work no:2
# # #write a python program to map two lists into a dictionary.

# my_list_1 = [2,5,7,9,5]
# my_list_2 = [4,7,9,2,7]
# print(dict(zip(my_list_1, my_list_2)))

##### calss work 3
### write a python program to print all unique values in a dictionary

# data = {"V":"S001", "VI":"SOO2", "VII":"SOO1", "VIII":"SOO5", "VIV":"SOO5", "VV":"S009", "VVI":"S007"}

# print(set(data.values()))

#######  loops

# while True:
#     print(10) #it keeps printing 10 forever;

# while True:
#     data = int(input("> "))
#     print(data)
#     if data == 5:
#         break


# a = 10
# while a > 0:
#     print(a)
#     a-=1


# a = 100
# count = 0
# while a > 0:
#     print(a)
#     a-=1
#     count += 1
#     if count == 3:
#         break
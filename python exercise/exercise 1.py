# num1 = 20
# num2 = 30

# multiply = num1 * num2
# print(multiply)

# add = num1 + num2
# print(add)

# sum = range(0,10)
# print(list(sum))

# for i in range(6):
#     print(i)

# previous_num = 0

# for i in range(1, 11):
#     x_sum = previous_num + i
#     print("current number", i, "previouse number" ,previous_num, "sum in the", previous_num + i)
#     previous_num = i

# previous_num = 0
# for i in range(1,21):
#     range_sum = previous_num + i
#     print("current number", i ,"previous number", previous_num , "addition of both numbers", previous_num + i)
#     previous_num =  i




# print("Printing current and previous number and their sum in a range(10)")
# previous_num = 0

# # loop from 1 to 10
# for i in range(1, 11):
#     x_sum = previous_num + i
#     print("Current Number", i, "Previous Number ", previous_num, " Sum: ", previous_num + i)
#     # modify previous number
#     # set it to the current number
#     previous_num = i



# str = input("Type the world pynative: ")
# sum1 = len(str)
# # sum = filter(lambda x : x % 2 == 0, str)
# # print(list(sum))
# for i in range(0, sum1 -1, 2):
#     print("index[", i, "]", str[i])

# accept input string from a user
# word = input('Enter word ')
# print("Original String:", word)

# # using list slicing
# # convert string to list
# # pick only even index chars
# x = list(word)
# for i in x[0::2]:
#     print(i)

# word = input("Enter a word here: ")
# print("original word entered:", word)

# x = list(word)
# for i in x[0: :2]:
#     print(i)


# listed = range(1,11)
# all_list = list(listed)
# print(all_list)

# number = 0

# for i in range(1, 11):
#     all_num = number + i
#     print("current num", i , "previous number", all_num, "addition of both numbers", all_num + i )
#     all_num = i


# b = "pynative"
# print(b[4:8])

# def remove_chars(word, n):
#     print('Original string:', word)
#     x = word[n:]
#     return x

# print("Removing characters from a string")
# print(remove_chars("pynative", 4))
# print(remove_chars("pynative", 2))



# numbers_x = [10, 20, 30, 40, 10]
# numbers_y = [75, 65, 35, 75, 30]

# def first_last_num(numbers):
#     first_num = numbers[0]
#     last_num = numbers[-1]
#     if first_num == last_num:
#         return True
#     else:
#         return False

# print(first_last_num(numbers_x))
# print(first_last_num(numbers_y))

# num_list = [10, 20, 33, 46, 55]
# print("Given list:", num_list)
# print('Divisible by 5:')
# for i in num_list:
#     if i % 3 == 0:
#         print(i)



# str_x = "Emma is good developer. Emma is a writer"
# # use count method of a str class
# cnt = str_x.count("Emma")
# print(cnt)

# for i in range(1,6):
#     print(i)

# for num in range(10):
#     for i in range(num):
#         print (num, end=" ") #print number
#     # new line after each row to display pattern correctly
#     print("\n")


num_1 = 121
num_2 = 121
def result():
    if num_1 == num_2:
        return True
    else:
        return False

print(result)

def palindrome(number):
    print("original number", number)
    original_num = number
    
    # reverse the given number
    reverse_num = 0
    while number > 0:
        reminder = number % 10
        reverse_num = (reverse_num * 10) + reminder
        number = number // 10

    # check numbers
    if original_num == reverse_num:
        print("Given number palindrome")
    else:
        print("Given number is not palindrome")

palindrome(121)
palindrome(125)

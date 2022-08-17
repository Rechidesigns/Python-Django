# # with open("C:/Users/BudgIT Guest/Desktop/README.txt", "a") as file:
# #     # a = file.read()
    
# #     # print(a)
    
# #     file.write("\nI just append.")


# import random
# import statistics


# arr = [random.choice(range(17, 30)) for i in range(20)]

# mean = round(statistics.mean(arr), 3)
# median = round(statistics.median(arr), 3)

# try:
#     mode = round(statistics.mode(arr), 3)
# except statistics.StatisticsError:
#     mode = None

# std = round(statistics.stdev(arr), 3)
# var = round(statistics.variance(arr), 3)


# with open("stats.txt", "w") as file:
#     file.write("================\n")
#     file.write(f"The mean is {mean}.\nThe median is {median}. \nThe mode is {mode}.\nThe standard deviation is {std}.\nThe variance is {var}.")
#     file.write("\n================")



arr = [10, 11, 11, 13, 12, 140, 15, 12, 13, 13, 15, 15, 15, 15, 140, 140, 140, 140]

# element_count = {}

# for element in arr:
#     if element in element_count:

#      element_count[element] += 1
#     else:
#         element_count[element] = 1
# for key, value in element_count.items():
#     print(f'{key}: {value}') 
    
    
# from collections import Counter


# def most_freq(arr: list, k:int):
#     counter = Counter(arr)
#     ans = dict(counter.most_common()[:k])
#     return ans
    
# print(most_freq(arr, 1))



########### persistent storage with files


import random



def guess_game(trial:int, score:int):
    """This function allows users to guess what the computer has selected.j
    
    
    Args:
        trial (int): This is the total number of trials selected
        score (int): This is the score of the user at the time of function call.
        
    Returns:
        trial (int): This is the total trials left after the function call
        score (int): This is the total score left after the function call."""  
    
    
    num = list(range(53, 60))
    random.shuffle(num)

    print("You can select from the list below.")
    print(num)
    com_choice = random.choice(num)
    user_choice = int(input(">"))

    if user_choice in num:
        if user_choice == com_choice:
            print("You win!")
            print("You just got an extra trial!")
            score+=3
        else:
            trial -=1
            if user_choice > com_choice:
                print("Too High")
            else:
                print("Too low")
                
        print(f"Computer choice: {com_choice}")
    else:
        trial -=1 
        print("Invalid input")
    return score, trial 


def login(data:dict, score:int):
    
    """This function takes a dictionary, asks the user for the name and adds their name to the dictionary.
    
    Args:
        data(dict) : This is the dictionary that stores the user data
    
    Returns:
        name (str): This is the name of the user
    """
    
    name = input("Name: ").lower()

    data[name] = score
    return name

trials = 3
score = 0
with open("newfile.txt", "r") as file:
    data = eval(file.read())
    # print(type(data))
    
    
# print(eval("3") + eval("3"))

name = login(data, score)

while trials > 0:
    

    score, trials = guess_game(trials, score)
    
    if trials == 0:
        
        if score > data[name]:
            print(f"Your new high score is {score}")
            data[name] = score
        else:
            print(f"You scored {score} points.")
        
        
        print("Do you want to play again? Y/n?")
        rematch = input("> ").lower() 
        
        if rematch == "y":
            "Print welcome back"
            trials = 3
            score = 0

            name = login(data, score)
        else:
            print("Game over!")


with open("newfile.txt", "r") as file:
    file.write(str(data))
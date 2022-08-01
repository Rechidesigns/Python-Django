# #buid a game
# ########    class work

# from optparse import Option
# import random as rd
# print("welcome to Game, chose from the names below")

# gamer_choice = input("rock, scissor, paper,   ").lower
# computer_choice = rd.random

# if computer_choice == gamer_choice:
#     print("draw, no win")

# if computer_choice == "rock" and gamer_choice == "scissor":
#     print("print computer win")

# if gamer_choice == "scissor" and computer_choice == 'paper':
#     print("you win")

# if computer_choice == "paper" and gamer_choice == "rock":
#     print("compuiter win")

# if gamer_choice == "rock" and computer_choice == "scissor":
#     print("you win")

# if gamer_choice == "scissor" and computer_choice 





############# class work correction

import random 


def play_game(user:str, computer:str):
    """this function plays the rock paper and scissors game with rules that:
    scissors wins paper
    rock wins scissors
    paper wins rock.
Rock is represented as R
Paper is representged as P
Scissors is represented as S.

Args:
    user (str): this is the user's choice.
    computer (str): This is the computer's choice
Returns:
    ()
"""

    if user == "s" and computer == "p":
        return "you win"
    elif user == "p" and computer == "r":
        return "you win"
    elif user == "r" and computer == "s":
        return "you win"
    elif user == computer:
        return "its a tie"



print("welcome to the rock paper scissors game")
print("Enter R for Rockm, S for Scissors, and P for Paper")

user = input(">  ").lower()
Options = "rps"
computer = random.choice(Options)

if user in Options:
    print(play_game(user, computer))
else:
    print("Invalid input")

print(computer)





############### inbult model 

# arr = [50000, 43546, 675758, 4353, 5636]

# pay_raise = list(map(lambda x: x + (x*0.1), arr)) 

# print(pay_raise)



##############class work @50

# input_amount = input("Enter the amount to be calculated:>   ")

# entered_amount = list(map(input_amount*0.1))

# print(entered_amount)

##### class work correction

# print("Enter numbers seperate them by cooma")
# str_num = input(">").split(",")
# mapped = list(map(int, str_num))
# print(sum(mapped)/len(mapped))
 

########### filter ()

# a =  range(1, 10)

# odd = list(filter(lambda x: x % 2 == 0, a))
# print(odd) 

###### sets remove

# my_set = {2,4,5,7,8,9,}
# my_set.remove(5)
# print(my_set)

# ##### sets add

# my_set = {2,4,5,7,8,9,}
# my_set.add(5)
# print(my_set)
 
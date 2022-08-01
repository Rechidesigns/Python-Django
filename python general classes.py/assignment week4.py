###  Work on the guessing game we did in class and allow the user to keep playing until they decide to stop. To do this,
# you need to ask the user to select if they want to play again after a number of trials. Also, if the user gets the correct guess at a trial,
# give the user a score point and an extra trial. However, if the user fails to get the correct guess, reduce the trial.

import random

choices = ['p', 'r', 's']

computer_choice = random.choice(choices)

number_of_trail = 5

guess = 0

point = 5

condition = 'stop'

while guess < number_of_trail:
    print("welcome to King-Rechi gues game, you can use the key words P, R, S, to play with computer.")
    print("Note: you have 5 chances to try, and each winning carries 5 marks as score.")
    user_input = input('enter gues choices to play: ')
    guess += 1

    if user_input == 's' and computer_choice == 'p':
        print('you won')
        print(f'your score is {point}')
        break

    elif user_input == condition:
        print('game stoped')
        break

    elif user_input == 'p' and computer_choice == 'r':
        print('you win')
        print(f'your score is {point}')
        break

    elif user_input == 'r' and computer_choice == 's':
        print('you win')
        print(f'your score is {point}')
        break

    elif user_input == computer_choice:
        print('its a tie')

    elif user_input == 'r' and computer_choice == 'p':
        print('you lose')

    elif user_input == 's' and computer_choice == 'r':
        print('you lose')

    elif user_input == 'p' and computer_choice == 's':
        print('ýou lose')

    else:
        print('you entered incorect input')

    print(computer_choice)

else:
    print('you are out of choices')
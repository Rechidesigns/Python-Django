sentence = input('word: ')

print(sentence.capitalize())

write = 'i am learning python'

print(write.replace('i', 'you', 1))

joy = 'i hope you had fun today in class'

print(joy.count('a'))

def check_fermat(a, b, c, n):
    if n > 2 and (a**n + b**n == c**n):
        print('fja;lsdfjld,fdaofu;')
    else:
        print('euroe, rtrt')

check_fermat(a, b, c, n)

def check_fermatt(a, b, c, n):
#     # a = 48639
#     # b = 87864
#     # c = 74
#     n = 900563
    if n > 2 and a**n + b ** n == c ** n:
        print('holy smoke, fermat was wrong')
    else:
        print('No that "dosent work"')


#         final = (a**n + b**n == c**n)
#         return final

# check_fermatt(45, 23, 2, 900563)




def check_numbers():
    a = int(input('enter ur 1st value:   '))
    b = int(input('enter ur 2nd value:   '))
    c = int(input('enter ur 3rd value:    '))
    n = int(input('enter ur value:        '))
    

    if n > 2 and a**n + b ** n == c ** n:
        print('holy smoke, fermat was wrong')
    else:
        print('No that "dosent work"')

        final = int(a**n + b**n == c**n)
        return final

check_numbers()


def check_format(a, b, c, n):
    n = 4

    new_value = (a**n + b**n)
    cee = c**n

    if n > 4:
        print('holy smokes format was wrong')

    else:
        print('no, that does not work')

check_format(40, 56, 6, 5)


def user ():
    user_one = input('enter your number: ')
    user_two = input('enter your second number: ')
    user_three = input('enter your third number: ')    

user(use)
import random


# user = int(input("Select 1 for 'Rock', 2 for 'Paper', 3 for 'Ciger:  "))
# com = random.randint(1,3)
#
# def chack(useras,com):
#     if user == com:
#         return 0
#     if com == 1 and useras == 3:
#         return -1
#     elif com == 2 and useras == 1:
#         return -1
#     elif com == 3 and useras == 2:
#         return -1
#     return 1
# scor = chack(user,com)
# if scor == 0:
#     print("Darw")
# elif scor == -1:
#     print("You Loss")
# else:
#     print("You Win")
#
# print("Computer:  ",com)
# print("You:  ",user)

# if com == user:
#     print("Draw")
# elif com == 1 and user == 3:
#     print("You Loss")
# elif com == 2 and user == 1:
#     print("You Loss")
# elif com ==3 and user == 2:
#     print("You Loss")
#  # else:
# print("You Win")
# print("hello world")
#
def play():
    user = input("'r' for Rock, 'p' Paper, 's' for Scissors :  ")
    com = random.choice(['r', 'p', 's'])

    if user == com:
        return "It's a tie"
    # r<s, s<p, p<r can deaf
    elif (user == 'r' and com == 's') or (user == 's' and com == 'p') or (user == 'p' and com == 'r'):
        return "You Won!"
    return "you Lost!"

print(play())
# print(details())
# 
#
# name = "Arif"
# print("my name is {}.".format(name))
# print(f"my name is {name}")
# print("my name is " + name)

# a = int(input("Enter the number that be multiple: "))
# print(f"Multiplication of {a} is: ")
#
# for i in range(1,11):
#     print(f"{a}*{i}= {a*i}")


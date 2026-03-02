import random


print("welcome to my new game")
print("In this game you are to guess a number from 1 to 100")
print("you have five attempts only to guess a correct number")

number = random.randrange(1, 100)
secret_number = 6
attempts = 5
#key point
for attempt in range(1, 6):
    guess = int(input("enter any number from 1 to 100"))
    if guess == secret_number:
        print("congratulations you have won")
        break
    else:
        print("sorry,try again")
        print("exit")


def goal():
    print("You have scored")
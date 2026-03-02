import random

      

# greet = 1
# while greet <= 6:
#     print("How are you")


# market = ("banana", "mango", "apple")
# for s in market:
#     if(s == "mango"):
#         break
#     print(s)

user_Choice = input("what do you choose? Type 0 for Rock, 1 for paper or two for scissors.")

computer_Choice = random.randint(0, 2)
print(f"computer chose {computer_Choice}")

if computer_Choice > user_Choice:
    print("computer wins!")
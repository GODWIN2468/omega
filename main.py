import random
user_Choice = int(
    input("what do you choose? Type 0 for Rock, 1 for paper or 2 for scissors: "))

computer_Choice = random.randint(0, 2)
print(f"computer chose {computer_Choice}")

if user_Choice >= 3 or user_Choice < 0:
    print("You typed an invalid number , you lose!")
elif computer_Choice > user_Choice:
    print("You lose")
elif user_Choice > computer_Choice:
    print("You win")
elif computer_Choice == user_Choice:
    print("It's a draw")

import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard'").lower()

attempts = 10
if level == "hard":
    attempts = 5

correct_num = random.randint(1,100)

game_end = False

while not game_end and attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a Guess :"))
    attempts -= 1
    if guess == correct_num:
        print(f"Congrats! you guessed it correct Number is {correct_num}")
        game_end = True
    elif guess > correct_num:
        print("Too High")
    else:
        print("Too low")


if attempts < 0:
    print("No attempts left , You lose")
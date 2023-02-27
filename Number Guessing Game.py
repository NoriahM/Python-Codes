import random

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100...")
secret_number = random.randint(1, 100)

num_guesses = 0
while True:
    guess = int(input("Guess the number: "))
    num_guesses += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number in {num_guesses} guesses.")
        break

import random
secret = random.randint(1, 100)
guess = None
tries = 0

while guess != secret:
    guess = int(input("Guess the number (1-100): "))
    tries += 1
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")

print(f"Correct! You guessed it in {tries} tries.")

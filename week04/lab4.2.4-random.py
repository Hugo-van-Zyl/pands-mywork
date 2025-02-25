import random

input_nr = random.randint(1,10)
guess = 5

while input_nr != guess:

    if input_nr < guess:
        print("Guess higher")
        input_nr = random.randint(1,10)
    elif input_nr > guess:
        print("Guess lower")
        input_nr = random.randint(1,10)

print(input_nr)
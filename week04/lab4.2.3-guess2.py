input_nr = int(input("Input your guess between 1 and 10 -"))
guess = 5

while input_nr != guess:

    if input_nr < guess:
        print("Guess higher")
        input_nr = int(input("Input your guess between 1 and 10 -"))
    elif input_nr > guess:
        print("Guess lower")
        input_nr = int(input("Input your guess between 1 and 10 -"))

print(input_nr)
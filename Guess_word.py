import random

name = input("What is your name? ")

print(f"Good luck {name}!!")

words = ["rugby",
"penny",
"constituency",
"kitchen",
"community",
"assault",
"slump",
"lock",
"context",
"marble",
"yard",
"prejudice",
"climate",
"feather",
"criminal",
"show",
"valley",
"established",
"diplomat",
"extend"]

# Random choice desde el modulo random
word = random.choice(words)

print("Guess the characters ")

guesses = ''

turns = 12

while turns > 0:
    # Cuenta el numero de veces que el usuario falla
    failed = 0

    # Navegar por todas las letras que hay en la palabra (word)
    # una letra a la vez
    for char in word:
        # Si la letra esta en la palabra
        if char in guesses:
            print(char, end='')

        else:
            print("_")
            failed += 1

    if failed == 0:
        print("\nYou win!")
        print(f"The word is {word}")
        break

    print()
    guess = input("guess a character ")

    guesses += guess

    if guess not in word:
        turns -= 1

        #If the character doesn't match
        # "wrong" will be given as output
        print("Wrong")

        print(f"You have {turns} more guesses")

        if turns == 0:
            print("You loose")
            print(f"The word is {word}")
import random
import sys


repeat_again = True

numbers = [1, 2, 3, 4, 5, 6]

dice_number = random.choice(numbers)

print(dice_number)

while repeat_again:


    repeat = input("\nDo you want to play again? (y/n): ")

    if repeat == "y" or repeat == "Y":

        print(random.choice(numbers))

    elif repeat == "n" or repeat == "N":
        sys.exit()

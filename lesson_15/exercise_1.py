# Dice Rolling Simulator:
#  Develop a simple dice rolling simulator. Generate random numbers between 1
# and 6 to simulate the roll of a six-sided die using the random module.
import random as r


def dice_rolling_function():
    dice_1 = r.randint(1, 6)
    dice_2 = r.randint(1, 6)
    return f"dice_1 = {dice_1}\ndice_2 = {dice_2}"


print(dice_rolling_function())

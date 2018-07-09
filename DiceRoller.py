# --- DICE ROLLER in PYTHON 3.6 --- #
# --- r/DailyProgrammer Challenge #364 --- #
# --- Ashton Christensen --- #
import random


def main():
    dice = []
    dice_file = open("RolledDice.txt", "r")
    for line in dice_file:
        dice.append(line.rstrip())
    for roll in dice:
        throws, sides, results = get_data(roll)
        roll_dice(throws, sides, results)
    again = input("Would you like to roll another set? Y/N?\n")
    if again.upper() == "Y":
        new_roll = input("Okay, please enter in format xdy, where x is amount of throws and y is sides on dice.\n")
        throws, sides, results = get_data(new_roll)
        roll_dice(throws, sides, results)
    if again.upper() == "N":
        pass


def get_data(data):
    throws, sides = data.rpartition('d')[0:3:2]
    throws = int(throws)
    sides = int(sides)
    results = []
    return throws, sides, results


def roll_dice(throws, sides, results):
    for i in range(throws):
        results.append(random.randint(1, sides))
    print("The results of rolling {} d{} are:{} , with each roll being:{}".format(throws, sides, sum(results), results))


if __name__ == '__main__':
    main()

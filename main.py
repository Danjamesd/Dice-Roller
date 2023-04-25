import random
import time


def roll_dice() -> None:
    """
    Simulates the rolling of a dice.
    Prompts the user to roll the dice or quit, and continues to roll the dice
    until the user quits.
    """
    DICE_SIDES = 6
    while True:
        roll_again = input("[r]oll or [q]uit: ").lower()

        if roll_again == "r":
            print("\nRolling the dice...")
            time.sleep(1)

            dice = random.randint(1, DICE_SIDES)

            print(f"You rolled a {dice}\n")

        elif roll_again == "q":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please enter 'r' to roll again or 'q' to quit.")


roll_dice()

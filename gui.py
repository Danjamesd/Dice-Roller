import tkinter as tk
import random
import time


class DiceRoller:
    def __init__(self, master):
        self.master = master
        self.master.title("Dice Roller")

        # Create a label for the title
        self.title_label = tk.Label(self.master, text="Dice Roller", font=("Arial", 18, "bold"))
        self.title_label.pack(pady=10)

        # Create a label for the dice roll
        self.roll_label = tk.Label(self.master, text="", font=("Arial", 14))
        self.roll_label.pack(pady=20)

        # Create a button to roll the dice
        self.roll_button = tk.Button(self.master, text="Roll Dice", font=("Arial", 14), command=self.roll_dice)
        self.roll_button.pack(pady=10)

        # Create a button to quit the program
        self.quit_button = tk.Button(self.master, text="Quit", font=("Arial", 14), command=self.master.destroy)
        self.quit_button.pack(pady=10)

    def roll_dice(self):
        # Simulate rolling the dice
        dice = random.randint(1, 6)
        self.roll_label.configure(text=f"You rolled a {dice}")


root = tk.Tk()
app = DiceRoller(root)
root.mainloop()

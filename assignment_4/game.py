import random
from enum import Enum

JAJANKEN = ["paper", "rock", "scissors"]
WIN_CONDITIONS = {"paper": "rock", "rock": "scissors", "scissors": "paper"}

class Outcome(Enum):
    WIN = 1
    LOSS = 2
    TIE = 3

def jajanken(user_choice):
    # Randomly select an object for the computer's choice
    computer_choice = random.choice(JAJANKEN)
    if user_choice == computer_choice:
        return (Outcome.TIE, computer_choice)
    if WIN_CONDITIONS[user_choice] == computer_choice:
        return (Outcome.WIN, computer_choice)
    return (Outcome.LOSS, computer_choice)
"""Refactor you rock, paper scissors game!

All the logic has already been worked out, but now it's time
to go back and refactor it using best practices in module design.
Your goal should be to separate the main game loop code from the
game play code.

Anything related to actually playing the game should be in a module
named game. The code running the main while-loop, taking user input,
printing to the console should be part of the __main__ module.

Keep in mind best practices for documentation, variable names, and code reuse."""
import game
from game import Outcome

FORCE_PLAY_AGAIN = "y"


def main():
    user_choice = input("Choose paper, rock or scissors: ").lower()
    if user_choice not in game.JAJANKEN:
        print("You must choose paper, rock or scissors.")
        play_again(FORCE_PLAY_AGAIN)
        return
    # Tuple with game outcome then computer choice
    outcome_and_choice = game.jajanken(user_choice)
    game_outcome = outcome_and_choice[0]
    computer_choice = outcome_and_choice[1]
    if game_outcome == Outcome.WIN:
        print(f"The computer choose {computer_choice}, you win!")
    if game_outcome == Outcome.LOSS:
        print(f"The computer choose {computer_choice}, computer wins :(")
    if game_outcome == Outcome.TIE:
        print("Tie game!")
        play_again(FORCE_PLAY_AGAIN)
        return
    play_again()
    return

def play_again(force="n"):
    force_play = force == FORCE_PLAY_AGAIN
    if not force_play:
        play_again = input("Would you like to play again? (Y/N) ")
    else:
        play_again = input("Playing again... press c to confim: ")
    if play_again.lower() == "y" or force_play:
        return main()


if __name__ == "__main__":
    main()
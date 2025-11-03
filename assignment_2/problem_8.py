import random   
"""Write a Rock-Papers-Scissors game where a user plays against the computer.

The program should ask the user to choose an object and then compare to a randomly generated object from the computer.
 If the objects are the same, then play again. If the objects are different the winner is chosen from the following rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
The program should always ask if the player would like to play again. Use the following games as an example:

> Choose: rock   
Computer choose paper, the computer wins :(   
Would you like to play again? n
> Choose: rock   
Computer choose paper, the computer wins :(   
Would you like to play again? y  
  
> Choose: paper Computer choose rock, you win!.   
Would you like to play again? n  
> Choose: paper 
The computer choose paper. Let's settle this.   

> Choose: rock  
The computer choose scissors, you win!   
  
Would you like to play again? n  
You should ensure that the user makes valid object selection.

> Choose: ball   
You must choose paper, rock or scissors.   
Would you like to play again? n

Use the Python random module to randomly select an object from a list of objects. 
We will discuss the details of random in more detail later, but for now use following code snippet to make the selection.

Put the import random statement at the very top of your file.
"""
# Problem 7 
# Makunde
JAJANKEN = ["paper", "rock", "scissors"]
WIN_CONDITIONS = {"paper": "rock", "rock": "scissors", "scissors": "paper"}

def jajanken():
    # Randomly select an object for the computer's choice
    computer_object = random.choice(JAJANKEN)
    user_choice = input("Choose: ").lower()
    if user_choice not in JAJANKEN:
        print("You must choose paper, rock or scissors.")
        play_again()
        return
    if user_choice == computer_object:
        play_again()
        return
    if WIN_CONDITIONS[user_choice] == computer_object:
        print(f"The computer choose {computer_object}, you win!")
    else:
        print(f"The computer choose {computer_object}, computer wins :(")
    play_again()

def play_again():
    play_again = input("Would you like to play again? (Y/N) ")
    if play_again.lower() == "y":
        jajanken()

jajanken()

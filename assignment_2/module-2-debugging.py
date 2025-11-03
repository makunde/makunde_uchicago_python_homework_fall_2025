
# Find all the errors in this program and correct them. The program should be error free and run without any issues.

def is_on_menu(choice):
    """Determine if user choice is on the menu. Returns `True` if it is else return `False`"""
    if choice == "burger" or \
        choice == "fries" or \
        choice == "chheeseburger" or \
        choice == "nuggets" or \
        choice == "ice_cream": 
        return "Your choice is on the menu"
    else:
        return "Your choice is not on the menu."

def cost (choice):
    """Return the cost for a given menu item."""
    if choice == "burger": 
        money = 5.00
    elif choice == "fries":
        money = 2.00
    elif choice == "cheeseburger":
        money = 6.00
    elif choice == "nuggets":
        money == 4.00
    elif choice == "ice_cream":
        money = 3.00 
    else:
        mone = "n/a"
    
    return money


# Ask the user what they would like to eat
choice = input("What would you like to order?")

# Print the choice and the cost
print ("Your choice is: ", choice)
if is_on_menu(choice):
    print(f"That will be: ${cost(choice):.2f}")
else: 
    print("We don't serve that. Please try again.")


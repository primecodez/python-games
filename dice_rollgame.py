import random

def roll(sides=6):
    """Simulate rolling a single die with a given number of sides."""
    return random.randint(1, sides)

def interactive_roll():
    """Allow the user to roll dice interactively."""
    while True:
        user_input = input("Do you want to roll a die type y or n : ").lower()
        if user_input == 'y':
            
            result = roll()
            print(f"You rolled a {result}")
        elif user_input == 'n':
            print("Thanks for playing!")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
            

interactive_roll()
                
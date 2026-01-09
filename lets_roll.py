import random

print("Welcome to Roll a dice game")

def roll(side=6):
    return random.randint(1,side)

def users_choice():
    user_roll = roll(6) 
    while True:
        choice = input("To start enter y else to exit press n: ").strip().lower()
        if choice == "y":
            print(f"You roll {user_roll}")
            return user_roll
        elif choice == "n":
            print("Thanks for playing")
            return None
        else:
            print("Invalid input")

def computers_choice():
    comp_roll = roll(6)
    print(f"Computer roll {comp_roll}")
    return comp_roll     

def who_won(user_roll, comp_roll):
    if user_roll > comp_roll:
        print("You won")
    elif user_roll < comp_roll:
        print("Computer won")
    else:
        print("It's a draw")

def main():
    user_roll = users_choice()
    if user_roll is None:
        return
    comp_roll = computers_choice()
    who_won(user_roll, comp_roll)

main()
                

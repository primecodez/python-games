import random

print("🎲 Welcome to Roll a Dice Game 🎲")

def roll(side=6):
    return random.randint(1, side)

def play_round(round_no):
    print(f"\n--- Round {round_no} ---")
    user_choice = input("Press 'y' to roll the dice or 'n' to exit: ").strip().lower()
    if user_choice == 'n':
        print("Thanks for playing!")
        exit()  
    user_roll = roll()
    comp_roll = roll()
    print(f"You rolled: {user_roll}")
    print(f"Computer rolled: {comp_roll}")

    if user_roll > comp_roll:
        print("You win this round!")
        return "user"
    elif user_roll < comp_roll:
        print("Computer wins this round!")
        return "computer"
    else:
        print("This round is a draw!")
        return "draw"

def main():
    score = {
        "user": 0,
        "computer": 0,
        "draw": 0
    }

    for i in range(1, 4):   # 3 rounds
        winner = play_round(i)
        score[winner] += 1

    print("\n🎯 Final Result 🎯")
    print("Your score:", score["user"])
    print("Computer score:", score["computer"])
    print("Draws:", score["draw"])

    if score["user"] > score["computer"]:
        print("🏆 You won the game!")
    elif score["user"] < score["computer"]:
        print("💻 Computer won the game!")
    else:
        print("🤝 The game is a draw!")


main()

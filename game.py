"""Rock-Paper-Scissors game with overall winner"""

import random

def get_user_input():
    """Gets user's input"""
    choice = input("Choose your move (rock, paper, scissor): ").lower()
    if choice in ["rock", "paper", "scissor"]:
        return choice
    else:
        print("Invalid input. Please choose (rock, paper, scissor).")
        return get_user_input()

def get_computer_input():
    """Randomly select computer's input"""
    options = ["rock", "paper", "scissor"]
    return random.choice(options)

def decide_winner(player, computer):
    """Decides who's the winner of a round"""
    if player == computer:
        return "draw"
    elif (
        (player == "rock" and computer == "scissor") or
        (player == "paper" and computer == "rock") or
        (player == "scissor" and computer == "paper")
    ):
        return "user"
    else:
        return "computer"

def main():
    """Main function to play the game"""
    user_score = 0
    computer_score = 0

    for i in range(1, 4):   # play 3 rounds
        print(f"Round -> {i}\n")
        user_choice = get_user_input()
        computer_choice = get_computer_input()
        print(f"Computer chose: {computer_choice}")

        result = decide_winner(user_choice, computer_choice)

        if result == "user":
            print("You won this round!")
            user_score += 1
        elif result == "computer":
            print("Computer won this round!")
            computer_score += 1
        else:
            print("This round is a draw!")

        print("-" * 20)

    # Final overall result
    print("\nFinal Results:")
    print(f"Your score: {user_score}")
    print(f"Computer score: {computer_score}")

    if user_score > computer_score:
        print("🎉 You are the overall winner!")
    elif computer_score > user_score:
        print("💻 Computer is the overall winner!")
    else:
        print("🤝 It's an overall tie!")

if __name__ == "__main__":
    main()

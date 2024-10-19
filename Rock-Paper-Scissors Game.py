import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

# Function to display the choices
def display_choices(user_choice, computer_choice):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

# Main game function
def rock_paper_scissors_game():
    options = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0

    while True:
        # Prompt user for input
        user_choice = input("Choose rock, paper, or scissors (or type 'exit' to quit): ").lower()
        
        if user_choice == "exit":
            print("Thanks for playing!")
            break
        
        if user_choice not in options:
            print("Invalid choice! Please try again.")
            continue

        # Computer's random choice
        computer_choice = random.choice(options)

        # Display choices
        display_choices(user_choice, computer_choice)

        # Determine and display the result
        result = determine_winner(user_choice, computer_choice)
        print(result)

        # Update scores
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        print(f"Score - You: {user_score}, Computer: {computer_score}")

        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

# Run the game
rock_paper_scissors_game()

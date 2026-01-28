import random

def get_computer_choice():
    """Randomly select rock, paper, or scissors for the computer."""
    return random.choice(['rock', 'paper', 'scissors'])

def get_player_choice():
    """Get player's choice and validate it."""
    valid_choices = ['rock', 'paper', 'scissors']
    while True:
        player_input = input("\nEnter your choice (rock, paper, or scissors): ").lower()
        if player_input in valid_choices:
            return player_input
        else:
            print(f"Invalid option '{player_input}'. Please enter rock, paper, or scissors.")

def determine_winner(player_choice, computer_choice):
    """Determine the winner of the round."""
    if player_choice == computer_choice:
        return 'tie'
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return 'win'
    else:
        return 'lose'

def play_round(player_score, computer_score):
    """Play a single round of rock, paper, scissors."""
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    
    print(f"\nYou chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")
    
    result = determine_winner(player_choice, computer_choice)
    
    if result == 'win':
        print("You won this round!")
        player_score += 1
    elif result == 'lose':
        print("You lost this round!")
        computer_score += 1
    else:
        print("It's a tie!")
    
    return player_score, computer_score

def play_game():
    """Main game loop."""
    player_score = 0
    computer_score = 0
    
    print("=" * 50)
    print("Welcome to Rock, Paper, Scissors!")
    print("=" * 50)
    
    while True:
        player_score, computer_score = play_round(player_score, computer_score)
        print(f"\nScore - You: {player_score} | Computer: {computer_score}")
        
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again in ['no', 'n']:
            break
    
    print("\n" + "=" * 50)
    print("Game Over!")
    print(f"Final Score - You: {player_score} | Computer: {computer_score}")
    if player_score > computer_score:
        print("Congratulations! You won the game!")
    elif player_score < computer_score:
        print("The computer won the game!")
    else:
        print("The game was a tie!")
    print("=" * 50)

if __name__ == "__main__":
    play_game()
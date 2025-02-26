import random

def get_computer_move():
    return random.choice(["rock", "paper", "scissors"])

def check_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def play():
    player_score = 0
    computer_score = 0
    
    while True:
        player_move = input("Choose rock, paper, or scissors (or 'quit' to stop): ").lower()
        if player_move == "quit":
            print("Game Over. Thanks for playing!")
            break
        
        if player_move not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Try again.")
            continue
        
        computer_move = get_computer_move()
        print("Computer chose:", computer_move)
        
        result = check_winner(player_move, computer_move)
        print(result)
        
        if "You win!" in result:
            player_score += 1
        elif "Computer wins!" in result:
            computer_score += 1
        
        print("Score - You:", player_score, "Computer:", computer_score, "\n")

if __name__ == "__main__":
    play()
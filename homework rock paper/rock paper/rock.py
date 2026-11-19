import random
from colorama import init, Fore, Style
init(autoreset=True)

def player_move():
    move = ""
    while move not in ["rock", "paper", "scissors"]:
        move = input("Enter rock, paper, or scissors: ").lower()

        if move not in ["rock", "paper", "scissors"]:
            print("INVALID MOVE! TRY AGAIN.")

    return move

def ai_move():
    moves = ["rock", "paper", "scissors"]
    return random.choice(moves)

def check_winner(player, ai):
    if player == ai:
        return "tie"

    elif (player == "rock" and ai == "scissors") or \
         (player == "scissors" and ai == "paper") or \
         (player == "paper" and ai == "rock"):
        return "player"

    else:
        return "ai"


def rock_paper_scissors():
    print("WELCOME TO ROCK PAPER SCISSORS!")

    player_name = input("What is your name? ")

    player_score = 0
    ai_score = 0

    while True:
        player = player_move()
        ai = ai_move()

        print("You chose:", player)
        print("AI chose:", ai)

        result = check_winner(player, ai)

        if result == "player":
            print("YOU WIN!")
            player_score += 1

        elif result == "ai":
            print("AI WINS!")
            ai_score += 1

        else:
            print("IT'S A TIE!")

        print("Score:", player_name, player_score, "| AI:", ai_score)

        play_again = input("Do you want to play again? yes/no: ").lower()

        if play_again != "yes":
            print("=== THANK YOU FOR PLAYING ===")
            break

if __name__ == "__main__":
    rock_paper_scissors()
import random
from colorama import init, Fore, Style
init(autoreset=True)

def display_board(board):
    print()
    def colored(cell):
        if cell == 'X':
            return Fore.RED + cell + Style.RESET_ALL
        elif cell == 'O':
            return Fore.BLUE + cell + Style.RESET_ALL
        else:
            return Fore.YELLOW + cell + Style.RESET_ALL
    print(' ' + colored(board[0]) + ' | ' + colored(board[1]) + ' | ' + colored(board[2]))
    print(Fore.CYAN + '-----------' + Style.RESET_ALL)
    print(' ' + colored(board[3]) + ' | ' + colored(board[4]) + ' | ' + colored(board[5]))
    print(Fore.CYAN + '-----------' + Style.RESET_ALL)
    print(' ' + colored(board[6]) + ' | ' + colored(board[7]) + ' | ' + colored(board[8]))
    print()

def player_choice():
    symbol = ''
    while symbol not in ['X', 'O']:
        symbol = input(Fore.GREEN + "Do you want to be X or O? " + Style.RESET_ALL).upper()
    if symbol == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def player_move (board,symbol):
    move=-1
    while move not in range (1,10) or not board [move -1].isdigit():
        try:
            move = init (input("ENTER YOUR MOVE:" ))
            if move not in range(1,10) or not board [move -1].isdigit():
                print("INVALID MOVE! TRY AGAIN.")
        except ValueError:
            print("PLEASE ENTER A NUMBER BETWEEN 1-9")
    board[move-1]=symbol 


def ai_move (board,ai_symbol,player_symbol):
    for i in range (9):
        if board [i].isdigit():
            board_copy=board.copy()
            board_copy[i]=ai_symbol
            if check_win(board_copy,ai_symbol):
                board[i]=ai_symbol
                return
    for i in range (9):
         if board [i].isdigit():
             board_copy=board.copy()
             board_copy[i]=player_symbol
             if check_win(board_copy,player_symbol):
                 board[i]=ai_symbol
                 return
    possible_moves=[i for i in range(9)if board[i].isdigit()]
    move=random.choice(possible_moves)
    board[move]=ai_symbol
    
def check_win(board,symbol):
    win_conditions=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for cond in win_conditions:
        if board[cond[0]]==board[cond[1]]==board[cond[2]]==symbol:
            return True 
    return False 
 
def check_full(board):
    return all (not spot.isdigit() for spot in board)

def tic_tac_toe():
    print("Welcome to Tic-Tac-Toe!")
    player_name=input("What is your name?")
    while True:
        board=["1","2","3","4","5","6","8","9"]
       




board = None # replace this line

# TODO (MAIN-3): Get symbols using player_choice()

player_symbol, ai_symbol = None, None # replace this line

# TODO (MAIN-4): Decide who starts ("Player" or "AI")

# Simple option: always start with Player

turn = None # replace this line

while True:

display_board(board)

if turn == "Player":

# TODO (MAIN-5): Call player_move() to place player's symbol

# player_move(board, player_symbol)

# TODO (MAIN-6): If player wins, print win message with name and break

# if check_win(...):

# TODO (MAIN-7): If tie (board full), print tie message and break

# if check_full(...):

# TODO (MAIN-8): Switch turn to "AI"

pass

else:

# TODO (MAIN-9): Call ai_move() to place AI symbol

# ai_move(board, ai_symbol, player_symbol)

# TODO (MAIN-10): If AI wins, print AI win message and break

# if check_win(...):

# TODO (MAIN-11): If tie (board full), print tie message and break

# if check_full(...):

# TODO (MAIN-12): Switch turn to "Player"

pass

# TODO (MAIN-13): Ask "Play again? (yes/no): "

# If answer is NOT "yes", print thank you and return

again = None # replace this line

if __name__ == "__main__":

tic_tac_toe()


# 
#   - Return True if no cell contains a digit (i.e., all spots are taken).

# Function: tic_tac_toe()
#   - Purpose: Main game loop for Tic-Tac-Toe.
#   - Welcome the player and prompt for the player's name (display prompt in green).
#   - Loop to play games until the player chooses not to continue:
#         * Initialize the board with cell numbers.
#         * Get player's and AI's symbols via player_choice().
#         * Set the starting turn to 'Player'.
#         * While the game is on:
#               - Display the board.
#               - If it's the player's turn:
#                     > Call player_move() to get and execute the player's move.
#                     > Check if the player wins using check_win(); if so, display a win message and end the game.
#                     > Else, if the board is full, display a tie message and break.
#                     > Otherwise, set turn to 'AI'.
#               - If it's the AI's turn:
#                     > Call ai_move() to decide and execute the AI's move.
#                     > Check if the AI wins; if so, display a win message and end the game.
#                     > Else, if the board is full, display a tie message and break.
#                     > Otherwise, set turn to 'Player'.
#         * After the game ends, prompt the player if they want to play again.
#         * If the player does not type 'yes', exit the loop and thank the player.
#
# If the script is executed as the main module, call tic_tac_toe() to start the game.






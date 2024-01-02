import random

board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-', ]


def print_board(board):
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])


def print_menu():
    print("Welcome to TICTACTOE")
    print("Board moves are as follows\n"
          "1|2|3\n"
          "4|5|6\n"
          "7|8|9\n")


def player_choice():
    while True:
        pl_move = input("Select a space on the board (1-9) ")
        if 1 <= int(pl_move) <= 9:
            pl_move = int(pl_move) - 1
            if board[pl_move] == '-':
                board[int(pl_move)] = "X"
                break
            else:
                print("Invalid move")
        else:
            print("Invalid move")



def pc_choice():
    while True:
        pc_move = random.randint(0, 8)
        pc_move = int(pc_move)
        if board[pc_move] == '-':
            board[pc_move] = 'O'
            break
        else:
            continue


def check_win_player(board):
    if (board[0] == board[1] == board[2] and board[0] == "X") or (board[3] == board[4] == board[5] and board[3] == "X")\
            or (board[6] == board[7] == board[8] and board[6] == "X"):
        return True
    elif (board[0] == board[3] == board[6] and board[0] == "X") or (board[1] == board[4] == board[7] and board[1] == "X")\
            or (board[2] == board[5] == board[8] and board[2] == "X"):
        return True
    elif (board[0] == board[4] == board[8] and board[0] == 'X') or (board[2] == board[4] == board[6] and board[2] == 'X'):
        return True
    else:
        return False


def check_win_pc(board):
    if (board[0] == board[1] == board[2] and board[0] == "O") or (board[3] == board[4] == board[5] and board[3] == "O")\
            or (board[6] == board[7] == board[8] and board[6] == "O"):
        return True
    elif (board[0] == board[3] == board[6] and board[0] == "O") or (board[1] == board[4] == board[7] and board[1] == "O")\
            or (board[2] == board[5] == board[8] and board[2] == "O"):
        return True
    elif (board[0] == board[4] == board[8] and board[0] == 'O') or (board[2] == board[4] == board[6] and board[2] == 'O'):
        return True
    else:
        return False


def main():
        turns = 0
        print_menu()
        pl_turn = True
        round_loop = True
        while round_loop:
            if pl_turn:
                print_board(board)
                player_choice()
                print_board(board)
                pl_turn = False
                turns += 1
            else:
                print("Now it is the computers turn:\n")
                pc_choice()
                pl_turn = True
                turns += 1
            result = check_win_player(board)
            if result:
                print("You won!")
                break
            pc_win = check_win_pc(board)
            if pc_win:
                print("You suck, you lost to a random bot")
                break
            elif turns == 9:
                print("GAME IS A DRAW!")
                break
while True:
    ans = input("Do you want to play again (Y/N)? ")
    if ans.upper() == "Y":
        board = ['-', '-', '-',
                 '-', '-', '-',
                 '-', '-', '-', ]
        print("======================")
        main()
    else:
        break
#CODE DONE




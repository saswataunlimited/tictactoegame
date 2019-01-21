from IPython.display import clear_output
clear_output()
def display_board(board):
    print(" | | ")
    print(board[7]+"|"+board[8]+"|"+board[9])
    print("_|_|_ ")
    print(" | | ")
    print(board[4]+"|"+board[5]+"|"+board[6])
    print("_|_|_ ")
    print(" | | ")
    print(board[1]+"|"+board[2]+"|"+board[3])

import sys
def player_input():

    # Quick introduction 
    player =choose_first()
    print(f"Welcome to the tic tac toe game. Hey {player}...")

    # While loop to force the users to give correct input
    marker = ""
    while marker!="X" and marker!="O":
        marker = input("Please pick a marker 'X' or 'O'")

    # Assigning first marker to player
    if player == "Player1":
        player1 = marker
        print("player1 will go first")

        # Checking if other player want to play or not
        styn = input("Hey player2...\nAre you ready to go?(Enter 'Yes' for entering or 'no if you want to exit')")
        if not (styn=="Yes" or styn=="yes"):
            sys.exit()
        # Assigning the opposite marker to player2
        if player1=="X":
            player2 = "O"
        else:
            player2 = "X"

        return (player1, player2)

    elif player == "Player2":
        player2 = marker
        print("player2 will go first")
        # Checking if other player want to play or not
        styn = input("Hey player1...\nAre you ready to go?(Enter 'Yes' for entering or 'no if you want to exit')")
        if not (styn=="Yes" or styn=="yes"):
            sys.exit()
        # Assigning the opposite marker to player1
        if player2 == "X":
            player1 = "O"
        else:
            player1 = "X"
        return (player1, player2)

def place_marker(board, marker, position):
    
    board[position]=marker


def win_check(board, mark):
    if board[7]==board[8]==board[9]==mark:
        return True
    elif board[4]==board[5]==board[6]==mark:
        return True
    elif board[1]==board[2]==board[3]==mark:
        return True
    elif board[7]==board[4]==board[1]==mark:
        return True
    elif board[2]==board[8]==board[5]==mark:
        return True
    elif board[3]==board[6]==board[9]==mark:
        return True
    elif board[7]==board[5]==board[3]==mark:
        return True
    elif board[1]==board[5]==board[9]==mark:
        return True
    return False

from random import randint

def choose_first():
    player = randint(0,1)
    if player==1:
        return "Player1"
    else:
        return "Player2"

    #return "Player2"

def space_check(board, position):
    if board[position]==" ":
        return True
    return False

def full_board_check(board):
    for item in board:
        if item==" ":
            return False
    return True

def player_choice(board):
    position = int(input("Enter a position ot insert a marker"))
    if space_check(board, position)==True:
        return position

def replay():
    r = int(input("Hey, do you want to play it again?(1 for yes, 0 for no)"))
    if r==1:
        return True
    return False



print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    display_board(board)
    player1, player2 = player_input()
    print(player1,player2)
    #pass


    #while game_on:
    while win_check(board,"X")!=True or win_check(board,"O")!=True or full_board_check(board)==False:
        #Player 1 Turn
        position = 0
        while not position>=1 and position<=9:
            position = int(input(f"Hey Player1, Choose a poisition to put {player1}"))
            #Check the position is empty or not
            if space_check(board, position)==False:
                position=0
                print("Soory that position has been occupied already")

        place_marker(board,player1,position)
        display_board(board)
        if win_check(board,player1)==True or full_board_check(board)==True:
            break
        # Player2's turn.
        position = 0
        while not position>=1 and position<=9:
            position = int(input(f"Hey Player2, Choose a poisition to put {player2}"))
            #Check the position is empty or not
            if space_check(board, position)==False:
                position=0
                print("Soory that position has been occupied already")
        place_marker(board,player2,position)
        display_board(board)
        if win_check(board,player2)==True or full_board_check(board)==True:
            break
        #pass
    #Who wins or match drawn:
    if win_check(board,"X")==True:
        if player1=="X":
            print("player1 won the game")
        else:
            print("player2 won the game")
    elif win_check(board,"O")==True:
        if player1=="O":
            print("player1 won the game")
        else:
            print("player2 won the game")
    elif full_board_check(board)==True:
        print("Game draw!!!")
    if not replay():
        break

#Complete

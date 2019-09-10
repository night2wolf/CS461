import random
import copy
def create_game_board(size):
    # Create game board as 2 dimensional array sizexsize based on user input
    board = [[0 for x in range(size)] for y in range(size)]
    for i in range(size):
        for j in range(size):
            board[i][j] = 1
    return board


class Solution:
    def __init__(self, Gameboard, x_flip, y_flip, solution_flips):
        self.Gameboard = copy.deepcopy(Gameboard)
        self.x_flip = copy.copy(x_flip)
        self.y_flip = copy.copy(y_flip)
        self.solution_flips = copy.copy(solution_flips)

def create_game_board0(size):
    # Create game board as 2 dimensional array sizexsize based on user input
    board = [[0 for x in range(size)] for y in range(size)]
    for i in range(size):
        for j in range(size):
            board[i][j] = 0
    return board


def create_random_board(size):
     # Create a random game board as 2 dimensional array sizexsize based on user input
    board = [[0 for x in range(size)] for y in range(size)]
    for i in range(size):
        for j in range(size):
            board[i][j] = random.randint(0, 1)
    return board

# Being Lazy.


def check_win1(gameboard,size):
    if gameboard == create_game_board(size):
        return True
    else:
        return False


def check_win0(gameboard,size):
    if gameboard == create_game_board0(size):
        return True
    else:
        return False
# Flip all tiles in row X and column Y


def flip_board(ix, iy, gameboard,size):
    
    for i in range(size):
        row = gameboard[i-1][iy]
        row = flip(row)
        gameboard[i-1][iy] = row
    for i in range(size):
        column = gameboard[ix][i-1]
        column = flip(column)
        gameboard[ix][i-1] = column
    a = gameboard[ix][iy]
    a = flip(a)
    gameboard[ix][iy] = a
    return gameboard

# Flips the token to the opposite


def flip(a):
    if a == 1:
        a = 0
    else:
        a = 1
    return a

def get_user_input(size):
    valid = False
    print("Which spot would you like to flip?")
    x = input("X coordinate: ")
    y = input("Y coordinate: ")
    try:
        x = int(x)
        y = int(y)
        if x-1 >= size or x <= 0:
            print("X must be less then the size of the board and greater then 0") 
        else:
            if y-1 >= size or y <= 0:
                print("Y must be less then the size of the board and greater then 0")
            else:
                valid = True
    except ValueError:
        print("That is not a valid number please try again.")
        return -1,-1,valid        
    return x-1,y-1,valid




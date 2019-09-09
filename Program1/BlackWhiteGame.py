import random
import boardhelpers

# import generatesolutions
size = input("Please enter the board size : ")
size = int(size)


# TODO fix this so it doesn't overflow into a loop.. Probably need logic to remove duplicates
def compsearch(gameboard, solution_array):
    desired_solution = boardhelpers.Solution(gameboard,-1,-1,-1)
    search_sol = boardhelpers.Solution
    len_solarr = len(solution_array)
    print("Searching for this Board:" + '\n')
    print(str(gameboard))
    for i in range(len_solarr):
        search_sol = solution_array[i]
        if list(search_sol.Gameboard) == list(desired_solution.Gameboard):
            print("found board")
            desired_solution = search_sol
               
    return desired_solution

#game program
def game():
    moves = 0
    win = False
    print("Game Time!" + '\n' + "Here is your Board:")
    ranboard = boardhelpers.create_random_board(size)
    for row in ranboard:
        print("{0}".format(row))
    while win == False:
        x,y,valid = boardhelpers.get_user_input(size)
        while valid == False:
            x, y, valid = boardhelpers.get_user_input(size)
        ranboard = boardhelpers.flip_board(x, y, ranboard, size)
        moves = moves + 1
        print("Current Board : " + '\n')
        for row in ranboard:
            print("{0}".format(row))
        # Check win condition
        win = boardhelpers.check_win0(ranboard,size)
        if win == True:
            break
        win = boardhelpers.check_win1(ranboard, size)
        if win ==True:
            break
        # a  have program ask if it would like to solve for the player
        response = input("Would you like me to solve?" + " (Y/N): ")
        if response == "Y":
           compwin = False
           while compwin == False:
              compsolution = compsearch(ranboard, solutionset)
              ranboard = boardhelpers.flip_board(compsolution.x_flip, compsolution.y_flip, compsolution.Gameboard,size)
              if compsolution.solution_flips == -1:
                  print("Board missing from Solution Set")
                  break
              moves = moves +1
              print("My Current Board : " + '\n')
              for row in ranboard:
                  print("{0}".format(row))
              print('\n' + "I need to flip " + str(compsolution.solution_flips) + " More times.")
              compwin = boardhelpers.check_win0(ranboard,size)
              if compwin == True:
                  break
              compwin = boardhelpers.check_win1(ranboard,size)
              if win ==True:
                  break
    print("Congrats you win! You / I finished in " + str(moves) + " Moves." )


# Main Program
with open("solutions.txt", "r") as solutionfile:
    data = solutionfile.readlines()
solutionset = []
for line in data:
    gameboard,x,y,flips = line.split(":")
    state = boardhelpers.Solution
    state.Gameboard = gameboard
    state.x_flip = x
    state.y_flip = y
    state.solution_flips = flips
    solutionset.append(state)
game()




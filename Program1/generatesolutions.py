import boardhelpers
import copy
solutionfile = open('solutions.txt','w')
#solutionfile.write('Beginning of solutions' + '\n')
size = 5
class Solution:
    def __init__(self, Gameboard, x_flip, y_flip, solution_flips):
        self.Gameboard = copy.deepcopy(Gameboard)
        self.x_flip = copy.copy(x_flip)
        self.y_flip = copy.copy(y_flip)
        self.solution_flips = copy.copy(solution_flips)

def generate_solutions(iteration, size):
    d = []
    arraycount = 0
    for i in range(size):
        for j in range(size):
            arraycount + 1
            gameboard = boardhelpers.create_game_board(size)
            # Create an object of the Solution sets and put them in the list
            #print(str(gameboard))   
            gameboard = boardhelpers.flip_board(i, j, gameboard, size)
            sol = Solution(gameboard, i, j, iteration)
            d.append(sol)
            solutionfile.write(str(sol.Gameboard) + ":" + str(sol.x_flip) +
                               ":" + str(sol.y_flip) + ":" + str(sol.solution_flips) + '\n')
            
    return d

firstsol = generate_solutions(1, size)
def generate_big(firstsol,itr):
# create all next order flip permutations
    secondarr = []
    length = len(firstsol)
    for k in range(length):
        second_flip = firstsol[k]
        for i in range(size):
            for j in range(size):
                second = second_flip.Gameboard
                sol = Solution(second,i,j,itr)
                second = boardhelpers.flip_board(i, j, sol.Gameboard, size)
                # Check if the gameboard is present. Only append if it isn't
                """
                with open("solutions.txt", "r+") as solutionfile:
                    data = solutionfile.read()
                    for line in data:
                        board, x, y, flip = line.split(":")                            
                        if second == list(board):
                            break
                        else:
                            print("Writing to file" + str(second))                             

                                    """
                solutionfile.write(str(sol.Gameboard) + ":" + str(sol.x_flip) +
                                    ":" + str(sol.y_flip) + ":" + str(sol.solution_flips) + '\n')                    
                secondarr.append(sol) 
    return secondarr

# comment out so that new solution file does not get created    
"""
big = generate_big(firstsol,2)
print(str(len(big)))
for i in range(int(size*size-2)):
    big = generate_big(big,i+2)
    print(str(len(big)))
"""

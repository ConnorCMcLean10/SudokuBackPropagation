import numpy as np
from framework import *

nums = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

Sudoku = np.array([[0, 0, 0, 2, 7, 3, 9, 0, 5],
                   [5, 0, 0, 0, 0, 9, 0, 3, 7],
                   [7, 9, 0, 4, 0, 0, 0, 0, 2],
                   [0, 8, 0, 5, 2, 6, 4, 0, 0],
                   [1, 6, 5, 8, 0, 0, 0, 0, 0],
                   [0, 0, 2, 0, 9, 0, 5, 0, 6],
                   [0, 0, 1, 0, 0, 5, 3, 6, 0],
                   [9, 3, 8, 0, 6, 2, 0, 0, 0],
                   [0, 0, 0, 9, 3, 0, 0, 2, 8]])

test = np.array([[1, 0, 0, 0, 0, 7, 0, 9, 0],
                   [0, 3, 0, 0, 2, 0, 0, 0, 8],
                   [0, 0, 9, 6, 0, 0, 5, 0, 0],
                   [0, 0, 5, 3, 0, 0, 9, 0, 0],
                   [0, 1, 0, 0, 8, 0, 0, 0, 2],
                   [6, 0, 0, 0, 0, 4, 0, 0, 0],
                   [3, 0, 0, 0, 0, 0, 0, 1, 0],
                   [0, 4, 0, 0, 0, 0, 0, 0, 7],
                   [0, 0, 7, 0, 0, 0, 3, 0, 0]])




current = Sudoku.copy()
backpropPossibilities = possibilityList(current)
choices = createChoices()
path = np.empty((0, 2), int)                          # Order of blank spaces that the program has iterated through


def backprop(x, y, current):
    global path
    global backpropPossibilities
    # by current is passed by reference so the only thing returned will be x and y to reset the program backwards
    x = path[len(path)-1, 0]
    y = path[len(path)-1, 1]
    while True:
        path = np.delete(path, -1, 0)
        # Determining possible replacements
        poss1 = choices[y, x]
        poss2 = possible(current, x, y)
        poss = (list(list(set(poss1) - set(poss2)) + list(set(poss2) - set(poss1))))
        poss.remove(0)

        if (len(poss) != 0):
            choices[y, x] = np.append(choices[y, x], poss[0])
            current[y, x] = poss[0]
            return np.array([x, y])
        else:
            current[y, x] = 0
        if (len(path) == 0):
            return("bruh")

        choices[y, x] = [0]
        x = path[len(path) - 1, 0]
        y = path[len(path) - 1, 1]



def solve(current):
    global path

    x = 0
    y = 0
    while True:
        # if it has iterated past the last square it is unsolvable
        if y == 9 and x == 1:
            return("Cannot Solve")

        # If there are no blank cells left it validates the sudoku
        noBlanks = True
        for i in range(len(current)):
            for j in range(len(current[0])):
                if current[i, j] == 0:
                    noBlanks = False

        if (noBlanks and checkSolved(current)):
            return current

        possibilities = possible(current, x, y)
        # If there are blanks left then this chooses the next cell
        if (current[y, x] == 0):
            if (len(possibilities) == 0):
                xy = backprop(x, y, current)
                if type(xy) == str:
                    return "Cannot Solve"
                x = xy[0]
                y = xy[1]
            else:
                current[y, x] = possibilities[0]
                path = np.append(path, [[x, y]], axis=0)



        x+=1
        if x == 9:
            y+=1
            x=0

print(solve(Sudoku))

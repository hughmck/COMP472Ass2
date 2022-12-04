# Take in input file to format grid
import numpy as np
from textwrap import wrap


# Returns a list of lists of lists

# First list contains every single grid,
# Second list contains one grid
# Third list (inside) are the rows in the grid

def function(str, k):
    for i in range(len(str)):
        if i % k == 0:
            sub = str[i:i + k]
            lst = []
            for j in sub:
                lst.append(j)
            print(' '.join(lst))


def readFile():
    path = 'Sample/sample-input.txt'
    grids = []
    with open(path) as f:
        lines = f.readlines()  # reads in as list
        for i in lines:
            if not (i.startswith('#') or (i.startswith('\n'))):
                i.strip()  # each i is a string that looks like this "IJBBCCIJDDL.IJAAL.EEK.L...KFF..GGHH. F0 G6"
                grids.append(i)

    return grids  # list of puzzle but return only the first to work on for now


if __name__ == "__main__":
    # To access one grid, index at the position or loop through, board[i]
    grids, fuel = readfile()  # grids and fuel have corresponding index.

    for i in grids:
        print(np.matrix(i))

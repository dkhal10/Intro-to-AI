'''
The state is a list of 2 items: the board, the path
The target for 8-puzzle is: (zero is the hole)
012
345
678
'''
import random
import math

#returns a random board nXn
def create(n):
    s=list(range(n*n))      # s is the board itself. a vector that represent a matrix. s=[0,1,2....n^2-1]
    m="<>v^"                # m is "<>v^" - for every possible move (left, right, down, up)
    for i in range(n**3):  # makes n^3 random moves to mix the tiles
        if_legal(s,m[random.randrange(4)])
    return [s,""]           # at the beginning "" is an empty path, later on path
                            # contains the path that leads from the initial state to the state

def get_next(x):            # returns a list of the children states of x
    ns=[]                   # the next state list
    for i in "<>v^":
        s=x[0][:]           # [:] - copies the board in x[0]
        if_legal(s,i)       # try to move in direction i
        # checks if the move was legal and...
        if s.index(0)!=x[0].index(0) and \
           (x[1]=="" or x[1][-1]!="><^v"["<>v^".index(i)]): # check if it's the first move or it's a reverse move
            ns.append([s,x[1]+i])   # appends the new state to ns
    return ns


def path_len(x):
    return len(x[1])

def is_target(x):
    n=len(x[0])                     # the size of the board
    return x[0]==list(range(n))     # list(range(n)) is the target state

#############################
def if_legal(x,m):                  # gets a board and a move and makes the move if it's legal
    n=int(math.sqrt(len(x)))        # the size of the board is nXn
    z=x.index(0)                    # z is the place of the empty tile (0)
    if z%n>0 and m=="<":            # checks if the empty tile is not in the first col and the move is to the left
        x[z]=x[z-1]                 # swap x[z] and x[z-1]...
        x[z-1]=0                    # ...and move the empty tile to the left
    elif z%n<n-1 and m==">":        # check if the empty tile is not in the n's col and the move is to the right
        x[z]=x[z+1]
        x[z+1]=0
    elif z>=n and m=="^":           # check if the empty tile is not in the first row and the move is up
        x[z]=x[z-n]
        x[z-n]=0
    elif z<n*n-n and m=="v":        # check if the empty tile is not in the n's row and the move is down
        x[z]=x[z+n]
        x[z+n]=0

# This is your HW
def hdistance0(s):                   # the heuristic value of s -- uniform cost
    return 0
def hdistance1(s):
    # count = 0
    # for each in int(math.sqrt(len(x))):
    #     if each != x[each]:
    #         count+=1
    # return count
    count = 0
    for each in range(len(s[0])):
        if each != s[0][each]:
            count += 1
    return count
def hdistance2(s):
    length = int(math.sqrt(len(s[0])))
    distance = 0
    for each in range(len(s[0])):
        number = s[0][each]
        currentRow = each // length
        currentCol = each % length

        targetRow = number // length
        targetCol = number % length

        distance += abs(currentRow - targetRow) + abs(currentCol - targetCol)
        
    return distance
def hdistance3(s):
    length = int(math.sqrt(len(s[0])))
    distance = hdistance2(s)
    conflicts = 0

    for row in range(length):
        for col1 in range(length):
            number1 = s[0][row * length + col1]

            if number1 != 0 and number1 // length == row:
                for col2 in range(col1 + 1, length):
                    number2 = s[0][row * length + col2]

                    if number2 != 0 and number2 // length == row:
                        if number1 % length > number2 % length:
                            conflicts += 1

    for col in range(length):
        for row1 in range(length):
            number1 = s[0][row1 * length + col]

            if number1 != 0 and number1 % length == col:
                for row2 in range(row1 + 1, length):
                    number2 = s[0][row2 * length + col]

                    if number2 != 0 and number2 % length == col:
                        if number1 // length > number2 // length:
                            conflicts += 1

    return distance + 2 * conflicts
    

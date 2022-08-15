from random import randrange
board=[[1, 2, 3], [4, 'X', 6], [7, 8, 9]]
#board=[['X', 2, 3], [4, 'X', 6], [7, 8, 'X']]
used=[5]
finish=[1, 2, 3, 4, 5, 6, 7, 8, 9]
#print(board)

def DisplayBoard(board):
#the function accepts one parameter containing the board's current status
#and prints it out to the console
    print("+-------+-------+-------+", end="\n") 
    print("|       |       |       |", end="\n")
    print("|  ",board[0][0],"  |  ",board[0][1],"  |  ", board[0][2],"  |", end="\n")
    print("|       |       |       |", end="\n")
    print("+-------+-------+-------+", end="\n") 
    print("|       |       |       |", end="\n")
    print("|  ",board[1][0],"  |  ",board[1][1],"  |  ", board[1][2],"  |", end="\n")
    print("|       |       |       |", end="\n")
    print("+-------+-------+-------+", end="\n") 
    print("|       |       |       |", end="\n")
    print("|  ",board[2][0],"  |  ",board[2][1],"  |  ", board[2][2],"  |", end="\n")
    print("|       |       |       |", end="\n")
    print("+-------+-------+-------+", end="\n")

def EnterMove(board):
# the function accepts the board current status, asks the user about their move, 
# checks the input and updates the board according to the user's decision
    move=int(input("Enter your move: "))
    while move > 9 or move < 1:
        move=int(input("Enter your move: "))
    while move in used:
        move=int(input("Enter your move: "))
        
    for row in range(3):
        for i in range (3):
            if board[row][i] == move: 
                board[row][i]= 'O'
    used.append(move)
    DisplayBoard(board)
    MakeListOfFreeFields(board)
    VictoryFor(board, 'O')

def MakeListOfFreeFields(board):
# the function browses the board and builds a list of all the free squares; 
# the list consists of tuples, while each tuple is a pair of row and column numbers
    freefields=[]
    ff=()
    for row in range(3):
        for i in range (3):
            if not board[row][i] == 'O' and not board[row][i] == 'X': 
                ff=row, i
                freefields.append(ff)
    #print(type(freefields[1]))
    if len(freefields)==9:
        return print('Game over')
    
                
def VictoryFor(board, sign):

    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return print(sign, "has won!")
    
    if board[0][2] == sign and board[1][2] == sign and board[2][0] == sign:
        return print(sign, "has won!")
    
    for row in range(3):
        if board[row][0] == sign and board[row][1] == sign and board[row][2] == sign:
            return print(sign, "has won!")
    
    for i in range(3):
        if board[0][i] == sign and board[1][i] == sign and board[2][i] == sign:
           return print(sign, "has won!")
    if sign == 'X':
        EnterMove(board)
    if sign == 'O':
        DrawMove(board)
    
    
    

def DrawMove(board):
# the function draws the computer's move and updates the board
    move = randrange(1,10)
    while move in used:
        move = randrange(1,10)
    
    for row in range(3):
        for i in range (3):
            if board[row][i] == move: 
                board[row][i]= 'X'
    used.append(move)
    DisplayBoard(board)
    MakeListOfFreeFields(board)
    VictoryFor(board, 'X')
       
DisplayBoard(board)
EnterMove(board)

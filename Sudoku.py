#Program checks if Sudoku is correct or not

##sudoku = ['295743861', '431865927', '876192543', '387459216',\
##          '612387495', '549216738', '763524189', '928671354', '154938672'] #yes
##sudoku = ['195743862', '431865927', '876192543', '387459216',\
##          '612387495', '549216738', '763524189', '928671354', '254938671'] #no
##
##for i in range(9):
##    row=sudoku[i]
##    for elem in row:
##        rows[i].append(int(elem))

columns=[[], [], [], [], [], [], [], [], []]
squares=[[], [], [], [], [], [], [], [], []]
rows = [[], [], [], [], [], [], [], [], []]
control=0

print('This program checks if your Sudoku is correct')

for i in range(9):
    row=str(input("Enter row here: "))
    for elem in row:
        rows[i].append(int(elem))

for i in range(9):
    row=sudoku[i]
    for elem in row:
        rows[i].append(int(elem))
    

for row in range(9):
    for i in range(9):
        columns[i].append(rows[row][i])

for row in range(3):
    for i in range(3):
        squares[0].append(rows[row][i])
    for i in range(3,6):
        squares[1].append(rows[row][i])
    for i in range(6,9):
        squares[2].append(rows[row][i])

for row in range(3,6):
    for i in range(3):
        squares[3].append(int(sudoku[row][i]))
    for i in range(3,6):
        squares[4].append(int(sudoku[row][i]))
    for i in range(6,9):
        squares[5].append(int(sudoku[row][i]))

for row in range(6,9):
    for i in range(3):
        squares[6].append(rows[row][i])
    for i in range(3,6):
        squares[7].append(rows[row][i])
    for i in range(6,9):
        squares[8].append(rows[row][i])


for i in range(9):
    if sum(squares[i]) == 45:
        control += 1
    if sum(columns[i]) == 45:
        control += 1
    if sum(rows[i]) == 45:
        control += 1

if control == 27:
    print('Yes')
else: print('No')


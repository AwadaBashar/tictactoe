# TIC TAC TOE game
import random
# function to print a tic-tao-toe grid stored as a list of 3 lists
def print_grid(grid):
    for row in grid:
        for e in row:
            print(e, end = ' ')
        print()

# test the function print_grid
#g = [ ['_', 'o', 'x'], ['_', 'x', '_'], ['o', '_', '_'] ]
lst=[]

def grid1(lst):#gives the grid
    for i in range(3):
        p=[]
        for j in range(3):
            p.append("_")
        lst.append(p)
    return lst
grid1(lst)
#print_grid(lst)

empty_cells=[]
def ep(lst):#gives empty_cells that countains list of tuples
    for i in range (0,3):
        for j in range (0,3):
            if lst[i][j]=="_":
                empty_cells.append((i,j))
    return(empty_cells)
(ep(lst))
def check_win(grid, player):
    '''your code goes here'''
    if (grid[0][0]=="x" and grid[0][1]=="x" and grid[0][2]=="x") or (grid[0][0]=="x" and grid[1][0]=="x" and grid[2][0]=="x") or (grid[1][0]=="x" and grid[1][1]=="x" and grid[1][2]=="x") or (grid[2][0]=="x" and grid[2][1]=="x" and grid[2][2]=="x") or (grid[1][1]=="x" and grid[0][1]=="x" and grid[2][1]=="x") or (grid[0][2]=="x" and grid[1][2]=="x" and grid[2][2]=="x") or (grid[0][0]=="x" and grid[1][1]=="x" and grid[2][2]=="x") or (grid[0][2]=="x" and grid[1][1]=="x" and grid[2][0]=="x"):
        return True
    if (grid[0][0]=="o" and grid[0][1]=="o" and grid[0][2]=="o") or (grid[0][0]=="o" and grid[1][0]=="o" and grid[2][0]=="o") or (grid[1][0]=="o" and grid[1][1]=="o" and grid[1][2]=="o") or (grid[2][0]=="o" and grid[2][1]=="o" and grid[2][2]=="o") or (grid[1][1]=="o" and grid[0][1]=="o" and grid[2][1]=="o") or (grid[0][2]=="o" and grid[1][2]=="o" and grid[2][2]=="o") or (grid[0][0]=="o" and grid[1][1]=="o" and grid[2][2]=="o") or (grid[0][2]=="o" and grid[1][1]=="o" and grid[2][0]=="o"):
        return False
        

def get_user_pick(empty_cells, grid):
    ''' your code goes here'''
    i=int(input("choose a row:"))
    j=int(input("choose a cell in the row:"))
    t=(i,j)
    if t in empty_cells:
        grid[i][j]='x'
        empty_cells.remove(t)
    else:
        print("please choose an empty cell")
        get_user_pick(empty_cells,grid)
def computer_pick(empty_cells, grid):
    '''your code goes here'''
    t=random.choice(empty_cells)
    i=t[0]
    j=t[1]
    b=(i,j)
    if b in empty_cells:
        grid[i][j]="o"
        empty_cells.remove(b)

def tictactoe():
    ''' Your code goes here
    '''
    turn=random.choice([True,False])
    while len(empty_cells)>0 and not check_win(lst,"o") and not check_win(lst,"x"):
        print_grid(lst)
        print("----------------")
        if turn==True:
            get_user_pick(empty_cells,lst)
        else:
            computer_pick(empty_cells,lst)
        turn=not turn
        if check_win(lst,"x")==True:
            print_grid(lst)
            print("user has won")    
            break
        if check_win(lst,"o")==False:
            print_grid(lst)
            print("computer has won")
            break 
    if len(empty_cells)==0 and not check_win(lst,"o") and not check_win(lst,"x"):
        print_grid(lst)
        print("Tie")
# start the game
tictactoe()

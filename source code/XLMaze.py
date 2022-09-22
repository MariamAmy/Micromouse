#this part is just simulation for multiple mazes on excel to try to figure out the behavior of the algorithm and code
# the same for this is the distance values got from the TOF module 
# just an ease access for me  
import numpy as np
import random
import win32com.client as win

excel = win.gencache.EnsureDispatch('Excel.Application')
wb = excel.Workbooks.Open(r'D:\Work\micromouse\Maze.xlsx') #put the full file path there

excel.Visible = True

maze = wb.Worksheets("Sheet5") #each sheet of the 5 represents a diffrent maze 
write = wb.Worksheets("Maze")


def pos(y,x, i):
    y = (y+1)*2
    x = (x+1)*2
    maze.Cells(y,x).Value = i
    return y,x

def turn(set, x, y,i):
    y,x = pos(y,x, i)
    up = [y-1,x]
    down = [y+1,x]
    right = [y,x+1]
    left = [y,x-1]
    sets = [down, right, up , left]
    if set == 1:
        forwardcell = sets[0]
        rightcell = sets[-1]
        leftcell = sets[1]
    elif set == 2:
        forwardcell = sets[-1]
        rightcell = sets[2]
        leftcell = sets[0]
    elif set == 3:
        forwardcell = sets[2]
        rightcell = sets[1]
        leftcell = sets[-1]
    elif set == 4:
        forwardcell = sets[1]
        rightcell = sets[0]
        leftcell = sets[2]
    return rightcell, forwardcell ,leftcell


def check_avl(set, y , x, i): #return the avalaible paths or the walls (1 is a wall , None is a clear path)
    right, forward, left = turn(set, x , y, i)
    r = maze.Cells(right[0],right[1]).Value
    f = maze.Cells(forward[0],forward[1]).Value
    l = maze.Cells(left[0],left[1]).Value
    if r == 1.0:
        r = None
    else:
        r = "1"
    if f == 1.0:
        f = None
    else:
        f = "1"
    if l == 1.0:
        l = None
    else:
        l = "1"
    return r, f , l

def show(Maze):
    for i in range(len(Maze)):
        for j in range(len(Maze[i])):
            write.Cells[j+1][i+1].Value = Maze[i][j]
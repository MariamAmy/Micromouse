from XLMaze import check_avl, show
from MAZEfinal import MazeSolving, MazeBack, MazeRun

Explore = MazeSolving()

i = 0
pos_x = 0
pos_y = 0
set = 1
count = 1
path = []

solved = False
back = False
run = False

while solved == False:
    Explore.turn(set,pos_x,pos_y)
    r_avlb, f_avlb, l_avlb = check_avl(set,pos_y,pos_x, 2)
    r_avlb,f_avlb,l_avlb = Explore.check(r_avlb, f_avlb, l_avlb)
    Next, Nextcell = Explore.nextmove(r_avlb,f_avlb,l_avlb, pos_y, pos_x)
    Explore.countindex(Nextcell, pos_x, pos_y)
    pos_x, pos_y, set = Explore.move(Next,set, pos_x, pos_y)
    print(f"y: {pos_y} x: {pos_x} set: {set}")
    solved = Explore.end(pos_y,pos_x)
    

# show(Explore.Maze)
print(Explore.Maze)
Back = MazeBack(Explore.Maze, pos_y, pos_x)

if set == 5:
    set = 1
elif set == 6:
    set = 2
elif set == 0:
    set = 4

while back == False:
    Back.turn(set, pos_x, pos_y)
    r_avlb, f_avlb, l_avlb = check_avl(set,pos_y,pos_x, 3)
    r_avlb,f_avlb,l_avlb = Back.check(r_avlb, f_avlb, l_avlb)
    Next, Nextcell = Back.nextmove(r_avlb,f_avlb,l_avlb, pos_y, pos_x)
    Back.countindex(Nextcell, pos_x, pos_y)
    pos_x, pos_y, set = Back.move(Next,set, pos_x, pos_y)
    print(f"y: {pos_y} x: {pos_x} set: {set}")
    back = Back.end(pos_y, pos_x)

Back.countindex(Nextcell, pos_x, pos_y)
print(Back.Maze)

RuN = MazeRun(Back.Maze, 25)

print(RuN.Maze2)
print(RuN.path)

set = set + 2
if set == 5:
    set = 1
elif set == 6:
    set = 2
elif set == 0:
    set = 4

while run == False:
    RuN.turn(set, pos_x, pos_y)
    r_avlb, f_avlb, l_avlb = check_avl(set,pos_y,pos_x, 4)
    r_avlb,f_avlb,l_avlb = RuN.check(r_avlb, f_avlb, l_avlb)
    Next, Nextcell = RuN.nextmove(r_avlb,f_avlb,l_avlb, pos_y, pos_x)
    pos_x, pos_y, set = RuN.move(Next,set, pos_x, pos_y)
    print(f"y: {pos_y} x: {pos_x} set: {set}")
    run = RuN.end(pos_y, pos_x)
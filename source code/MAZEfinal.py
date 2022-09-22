import numpy as np
import random
from scipy.spatial.distance import cityblock #manhattan distance between two vectors

# The Maze with all cells unidentified except for the 4 middle cells 
Maze= np.array([
    [-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ],
    [-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ],
    [-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ],
    [-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ],
    [-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ],
    [-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ],
    [-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ],
    [-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,0  ,0  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ],
    [-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,0  ,0  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ],
    [-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ],
    [-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ],
    [-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ],
    [-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ],
    [-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ],
    [-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ],
    [-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ,-1  ],
    ])


#how many times each cell been visited to avoid loops 
visit= np.array([
    [0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ],
    [0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ],
    [0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ],
    [0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ],
    [0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ],
    [0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ],
    [0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ],
    [0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ],
    [0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ],
    [0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ],
    [0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ],
    [0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ],
    [0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ],
    [0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ],
    [0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ],
    [0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ],
    ])

path = np.copy(visit)
visit2 = np.copy(visit)

class MazeSolving: # exploring the maze 
    def __init__(self):
        self.Maze = Maze
        self.visit = visit
        self.count = 1

    def turn(self, set, x, y): # how the robot is facing
        up = [y-1,x]
        down = [y+1,x]
        right = [y,x+1]
        left = [y,x-1]
        sets = [down, right, up , left]
        if set == 1: #facing down
            self.forwardcell = sets[0]
            self.rightcell = sets[-1]
            self.leftcell = sets[1]
        elif set == 2: #facing right
            self.forwardcell = sets[-1]
            self.rightcell = sets[2]
            self.leftcell = sets[0]
        elif set == 3: #facing up
            self.forwardcell = sets[2]
            self.rightcell = sets[1]
            self.leftcell = sets[-1]
        elif set == 4: #facing left
            self.forwardcell = sets[1]
            self.rightcell = sets[0]
            self.leftcell = sets[2]

    def check(self, r,f,l): #checking available cells next to current cells
        if r == "1":
            rightcell = self.Maze[self.rightcell[0]][self.rightcell[1]]
        else: 
            rightcell = None
        if f == "1":
            forwardcell = self.Maze[self.forwardcell[0]][self.forwardcell[1]]
        else: 
            forwardcell = None
        if l == "1":
            leftcell = self.Maze[self.leftcell[0]][self.leftcell[1]]
        else: 
            leftcell = None
        return rightcell, forwardcell, leftcell

    def shortest(self, where,right, forward, left): #return the cell that is nearest to the distination in case 2 cells has equal values
        distances = []
        movement = []
        right_dist = None
        forward_dist = None
        left_dist = None
        for poss in where[0]:
            if poss == 0:
                right_dist = min(cityblock(right,[7,7]),cityblock(right,[7,8]),cityblock(right,[8,7]),cityblock(right,[8,8]))
                distances.append(right_dist)
            if poss == 1:
                forward_dist = min(cityblock(forward,[7,7]),cityblock(forward,[7,8]),cityblock(forward,[8,7]),cityblock(forward,[8,8]))
                distances.append(forward_dist)
            if poss == 2:
                left_dist = min(cityblock(left,[7,7]),cityblock(left,[7,8]),cityblock(left,[8,7]),cityblock(left,[8,8]))
                distances.append(left_dist)

        mindist = min(distances)
        if mindist == right_dist:
            movement.append(0)
        if mindist == forward_dist:
            movement.append(1)
        if mindist == left_dist:
            movement.append(2)
        if len(movement) == 1:
            return movement[0]
        else:
            rand = random.randint(0,len(movement)-1)
            return movement[rand]    

    def nextmove(self,rightcell, forwardcell, leftcell, y , x): #decide the next move and return the move and the cell value
        surround = [rightcell, forwardcell, leftcell]
        surrdic = {0: 'r', 1: 'f', 2: 'l'}
        possibles = []
        move = "d"
        minimum = -5
        for cell in surround:
            if cell != None and cell != -5: #kickout the dead ends and unavailable cells
                possibles.append(int(cell))
            if cell == 0:
                minimum = cell
                where = np.where(np.array(surround) == minimum)
                move = surrdic[where[0][0]]
                return move , minimum
        try:
            minimum = min(possibles) #selects the minimum cell value
            if minimum == -1: #-1 cell is a new cell that needs to be detected
                where = np.where(np.array(surround) == minimum)
                if where[0].size == 1: 
                    move = surrdic[where[0][0]] #if its the only -1 cell it returns the move
                else:
                    move = surrdic[self.shortest(where,self.rightcell,self.forwardcell,self.leftcell)] # numerous -1 cells it select the nearest to the middle
            else:    
                if self.visit[y][x] <= 4: #no -1 cells available select the one with most value to reach the end of the trace to continue searching
                    minimum = max(possibles)
                else:
                    minimum = min(possibles) #for cells visited multiple times more than 4 it increase its value and search for the minimum ones 
                where = np.where(np.array(surround) == minimum)
                if where[0].size == 1:
                    move = surrdic[where[0][0]]
                else:
                    move = surrdic[self.shortest(where,self.rightcell,self.forwardcell,self.leftcell)]
            return move , minimum
        except ValueError: #if possibles has no items in the list it return and error "dead end"
            move = "d"
            minimum = -5
            return move , minimum

    def end(self,y,x): #end the search if the value = 0
        if self.Maze[y][x] == 0:
            self.Maze[y][x] = self.count
            return True
        else:
            return False
    
    def countindex(self, Nextindex, x , y): #counting the trace the robot leaves behind
        if self.Maze[y][x] == -1 or Nextindex == -1: #new cells is givne a new value more than the last cell value + 1 
            self.Maze[y][x] = self.count
            self.count +=1
        elif Nextindex == -5: #dead end
            self.Maze[y][x] = -5
        elif self.count >= Nextindex and Nextindex != -5: #counter is larger than the next value so it should be decreased to mach the next cell
            self.count = Nextindex
        elif self.Maze[y][x] >= self.count: # cell value is larger than counter so the cell value is decreased to counter 
            self.Maze[y][x] = self.count
            self.count +=1
        if self.Maze[0][0] == -5: #the start cell never to be a dead end
            self.Maze[0][0] = 1
        
    
    def move(self,Next, set, x , y): #change the location of the robot after given the next move argument from nextmove function
        if Next == "r": 
            y = self.rightcell[0] 
            x = self.rightcell[1]
            set+=1
        elif Next == "f":
            y = self.forwardcell[0]
            x = self.forwardcell[1]
        elif Next == "l":
            y = self.leftcell[0]
            x = self.leftcell[1]
            set-=1
        else:
            y = y
            x = x
            set += 2
        if set == 5: #set value cannot exceed 4 or be less than 1 
            set = 1
        elif set == 6:
            set = 2
        elif set == 0:
            set = 4
        self.visit[y][x] +=1 #increas the visit array to see how many times the cell is visited
        self.Score()
        return x, y , set

    def Score(self): #increase the cells that is visited to much to kick it out and define it as a bad cells
        for i in range(len(Maze)):
            for j in range(len(Maze[i])):
                if self.visit[i][j] > 4:
                    self.Maze[i][j] = abs(self.Maze[i][j] * self.visit[i][j])
                if self.Maze[i][j] > 300:
                    self.Maze[i][j] = 300
                else:
                    pass



class MazeBack: #back to start cell journey begins :)
    def __init__(self, Maze, y, x): #initializing the class by giving it the current position and Maze created from the last class
        self.Maze = Maze
        self.visit2 = visit2
        self.count = self.Maze[y][x]

    def turn(self, set, x, y):
        up = [y-1,x]
        down = [y+1,x]
        right = [y,x+1]
        left = [y,x-1]
        sets = [down, right, up , left]
        if set == 1:
            self.forwardcell = sets[0]
            self.rightcell = sets[-1]
            self.leftcell = sets[1]
        elif set == 2:
            self.forwardcell = sets[-1]
            self.rightcell = sets[2]
            self.leftcell = sets[0]
        elif set == 3:
            self.forwardcell = sets[2]
            self.rightcell = sets[1]
            self.leftcell = sets[-1]
        elif set == 4:
            self.forwardcell = sets[1]
            self.rightcell = sets[0]
            self.leftcell = sets[2]

    def check(self, r,f,l):
        if r == "1":
            rightcell = self.Maze[self.rightcell[0]][self.rightcell[1]]
            self.rdist = cityblock([0,0],self.rightcell) #distance between the rightcell and the strat cell
        else: 
            rightcell = None
            self.rdist = None
        if f == "1":
            forwardcell = self.Maze[self.forwardcell[0]][self.forwardcell[1]]
            self.fdist = cityblock([0,0],self.forwardcell)
        else: 
            forwardcell = None
            self.fdist = None
        if l == "1":
            leftcell = self.Maze[self.leftcell[0]][self.leftcell[1]]
            self.ldist = cityblock([0,0],self.leftcell)
        else: 
            leftcell = None
            self.ldist = None
        return rightcell, forwardcell, leftcell
    
    def end(self,y,x): #ending the phase when the y and x = 0
        if y == 0:
            if x == 0:
                return True
            else:
                return False
        else:
            return False
    
    def shortest(self, where,right, forward, left): #the shortest of 2 or more to the start cell 
        distances = []
        movement = []
        right_dist = None
        forward_dist = None
        left_dist = None
        for poss in where[0]:
            if poss == 0:
                right_dist = cityblock([0,0],right)
                distances.append(right_dist)
            if poss == 1:
                forward_dist = cityblock([0,0],forward)
                distances.append(forward_dist)
            if poss == 2:
                left_dist = cityblock([0,0],left)
                distances.append(left_dist)
        mindist = min(distances)
        if mindist == right_dist:
            movement.append(0)
        if mindist == forward_dist:
            movement.append(1)
        if mindist == left_dist:
            movement.append(2)
        if len(movement) == 1:
            return movement[0]
        else:
            rand = random.randint(0,len(movement)-1)
            return movement[rand]

    def shortmove(self): #if the distance is less than 10 it takes that path no matter other cell values
        try:
            distances = []
            movement = []
            if self.rdist != None:
                distances.append(self.rdist)
            if self.fdist != None:
                distances.append(self.fdist)
            if self.ldist != None:
                distances.append(self.ldist)
            mindist = min(distances)
            if mindist <= 10:
                if mindist == self.rdist:
                    movement.append(0)
                if mindist == self.fdist:
                    movement.append(1)
                if mindist == self.ldist:
                    movement.append(2)
                if len(movement) == 1:
                    return movement[0]
                else:
                    rand = random.randint(0,len(movement)-1)
                    return movement[rand]
            else:
                return False
        except:
            return False
        

    def nextmove(self,rightcell, forwardcell, leftcell, y , x): #decides next move and return the move and cell value
        surround = [rightcell, forwardcell, leftcell]
        surrdic = {0: 'r', 1: 'f', 2: 'l'}
        possibles = []
        move = "d"
        minimum = -5
        short = self.shortmove()
        try:
            if short != False:
                move = surrdic[short]
                minimum = surround[short]
                return move , minimum 
            else:
                for cell in surround:
                    if cell != None and cell != -5:
                        possibles.append(int(cell))
                minimum = min(possibles)    
                if minimum == -1:
                    where = np.where(np.array(surround) == minimum)
                    if where[0].size == 1:
                        move = surrdic[where[0][0]]
                    else:
                        move = surrdic[self.shortest(where,self.rightcell,self.forwardcell,self.leftcell)]
                else:    
                    if self.visit2[y][x] <= 7:
                        minimum = min(possibles)
                    else:
                        minimum = max(possibles)
                        if minimum == 300:
                            minimum = min(possibles)
                    where = np.where(np.array(surround) == minimum)
                    if where[0].size == 1:
                        move = surrdic[where[0][0]]
                    else:
                        move = surrdic[self.shortest(where,self.rightcell,self.forwardcell,self.leftcell)]
                return move , minimum
        except ValueError:
            move = "d"
            minimum = -5
            return move , minimum    

    def countindex(self, Nextindex, x , y):
        if self.count < 0: #if the counting reached 0 and the it's not the start cell then its a longer way than the other
            pass
        else:
            if self.Maze[y][x] == 0 or Nextindex == 0: #4 midlle cells are givin same value
                self.Maze[y][x] = self.count
            else:
                if Nextindex == -5: #dead ends 
                    self.Maze[y][x] = -5
                elif self.Maze[y][x] >= self.count: #decreasing counter to cell values
                    self.count = self.Maze[y][x]
                elif self.Maze[y][x] < self.count:#new cells are given a value less than the last one by 1 
                    self.count -=1
                    self.Maze[y][x] = self.count
                elif self.Maze[y][x] == -1 or Nextindex == -1:    
                    self.count -=1
                    self.Maze[y][x] = self.count
                elif self.count >= Nextindex:
                    self.count -=1
                if self.Maze[0][0] == -5:
                    self.Maze[0][0] = 1


    def move(self,Next, set, x , y):
        if Next == "r":
            y = self.rightcell[0] 
            x = self.rightcell[1]
            set+=1
        elif Next == "f":
            y = self.forwardcell[0]
            x = self.forwardcell[1]
        elif Next == "l":
            y = self.leftcell[0]
            x = self.leftcell[1]
            set-=1
        else:
            y = y
            x = x
            set += 2
        if set == 5:
            set = 1
        elif set == 6:
            set = 2
        elif set == 0:
            set = 4
        self.visit2[y][x] +=1
        self.Score()
        return x, y , set

    def Score(self):
        for i in range(len(Maze)):
            for j in range(len(Maze[i])):
                if self.visit2[i][j] > 8:
                    self.Maze[i][j] = abs(self.Maze[i][j] * self.visit2[i][j])
                if self.Maze[i][j] > 300:
                    self.Maze[i][j] = 300
                else:
                    pass

class MazeRun: #let's Run
    def __init__(self, Maze2, replay): #intializing by giving the class the maze created to find the best path
        self.Maze2 = Maze2
        self.Maze = Maze2
        self.path = Maze2
        self.inverse()
        i =0
        while i < replay: #how many times it repeat the pathmaking
            self.pathmake()
            self.Maze = self.path
            i += 1

    def inverse(self): # making a floodfill for the maze by the cell values 
        critc = self.Maze[7][7]
        for i in range(len(self.Maze)):
            for j in range(len(self.Maze[i])):
                if self.Maze[i][j] != -1 and self.Maze[i][j] != 300 and self.Maze[i][j] != -5:
                    self.Maze[i][j] = critc - self.Maze[i][j] #the midlle cell minus all other cells
                else:
                    self.Maze[i][j] = -10 #except deadends and loop cells
    
    def pathmake(self): #elemnitaing the cells that leads to a dead end
        for i in range(len(self.Maze)):
            for j in range(len(self.Maze[i])):
                if i == 0:
                    if j == 0:
                        self.path[i][j] = self.Maze[i][j]
                        continue
                    else:
                        pass
                else:
                    pass
                if i == 7 or i == 8:
                    if j == 7 or j == 8:
                        self.path[i][j] = self.Maze[i][j] # middle cells and start are excepted
                        continue
                    else:
                        pass
                else:
                    pass
                val = self.Maze[i][j] #perfect cell that has an enterance (less than its value by one) and an exit (more than its value by one)
                try:
                    if i-1 >= 0: #cell above
                        val_u = self.Maze[i-1][j]
                    else:
                        val_u = -10
                except IndexError:
                    val_u = -10
                try:
                    if i+1 >= 0: #cell under
                        val_d = self.Maze[i+1][j]
                    else:
                        val_d = -10
                except IndexError:
                    val_d = -10
                try:
                    if j+1 >= 0: #cell right
                        val_r = self.Maze[i][j+1]
                    else:
                        val_r = -10
                except IndexError:
                    val_r = -10
                try:
                    if j-1 >= 0: #cell left
                        val_l = self.Maze[i][j-1]
                    else:
                        val_l = -10
                except IndexError:
                    val_l = -10
                check1 = False
                check2 = False
                if val_u == val+1 or val_u == val:
                    check1 = True
                elif val_r == val+1 or val_r == val:
                    check1 = True
                elif val_l == val+1 or val_l == val:
                    check1 = True
                elif val_d == val+1 or val_d == val:
                    check1 = True
                if val_u == val-1 or val_u == val:
                    check2 = True
                elif val_r == val-1 or val_r == val:
                    check2 = True
                elif val_l == val-1 or val_l == val:
                    check2 = True
                elif val_d == val-1 or val_d == val:
                    check2 = True
                if check1 == True and check2 == True:
                    continue
                else:
                    self.path[i][j] = -10 # elemenating cells that have no exit or no enterance to avoid dead ends in the run
    #repeating the last method too much will eleminate important cells and repeating it once will make no effect so it had to be callibrated
    
    def turn(self, set, x, y):
        up = [y-1,x]
        down = [y+1,x]
        right = [y,x+1]
        left = [y,x-1]
        sets = [down, right, up , left]
        if set == 1:
            self.forwardcell = sets[0]
            self.rightcell = sets[-1]
            self.leftcell = sets[1]
        elif set == 2:
            self.forwardcell = sets[-1]
            self.rightcell = sets[2]
            self.leftcell = sets[0]
        elif set == 3:
            self.forwardcell = sets[2]
            self.rightcell = sets[1]
            self.leftcell = sets[-1]
        elif set == 4:
            self.forwardcell = sets[1]
            self.rightcell = sets[0]
            self.leftcell = sets[2]

    def check(self, r,f,l):
        if r == "1":
            rightcell = self.path[self.rightcell[0]][self.rightcell[1]]
        else: 
            rightcell = None
        if f == "1":
            forwardcell = self.path[self.forwardcell[0]][self.forwardcell[1]]
        else: 
            forwardcell = None
        if l == "1":
            leftcell = self.path[self.leftcell[0]][self.leftcell[1]]
        else: 
            leftcell = None
        return rightcell, forwardcell, leftcell

    def move(self,Next, set, x , y):
        if Next == "r":
            y = self.rightcell[0] 
            x = self.rightcell[1]
            set+=1
        elif Next == "f":
            y = self.forwardcell[0]
            x = self.forwardcell[1]
        elif Next == "l":
            y = self.leftcell[0]
            x = self.leftcell[1]
            set-=1
        else:
            y = y
            x = x
            set += 2
        if set == 5:
            set = 1
        elif set == 6:
            set = 2
        elif set == 0:
            set = 4
        return x, y , set

    def nextmove(self,rightcell, forwardcell, leftcell, y , x): #decides next move
        surround = [rightcell, forwardcell, leftcell]
        surrdic = {0: 'r', 1: 'f', 2: 'l'}
        possibles = []
        for cell in surround:
            if cell != None and cell != -10: #eleminate the bad cells and walls 
                possibles.append(int(cell))
        try:
            minimum = min(possibles)
            if minimum < self.Maze[y][x]-50: #selects the minimum but with limit if the cell is less by 50 it selects the max
                minimum = max(possibles)
            else:
                pass 
            where = np.where(np.array(surround) == minimum)
            if where[0].size == 1:
                move = surrdic[where[0][0]]
            else:
                move = surrdic[random.randint(0,where[0].size-1)]
            return move, minimum
        except:
            for cell in surround:
                if cell != None:
                    possibles.append(int(cell))
            minimum = min(possibles)
            where = np.where(np.array(surround) == minimum)
            if where[0].size == 1:
                move = surrdic[where[0][0]]
            else:
                move = surrdic[random.randint(0,where[0].size-1)]
            return move, minimum
            

    def end(self,y,x): #ending the run ISA 
        if self.Maze[y][x] == 0:
            return True
        else:
            return False

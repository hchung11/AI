import Queue

try:
    bfsDfs = int(raw_input("Choose shearch \n 1) BFS \n 2) DFS \n >>>>>>"))
    print "Row\Colmn 0 1 2 3 4 5 6 7"
    with open("textFile.txt") as f:
            for value, l in enumerate(f) :
                        
                 print "   ",value,"   ", l
    start = int(raw_input("Choose Start, row first and colmn(ex: 11): "))
     
    
    goal = int(raw_input("Choose Goal, row first and colmn (ex: 51)"))
    
except ValueError:
    print("Oops!  That was no valid number.  Try again...")

class Node:


    def readGrid (filename):
        grid = []
        with open(filename) as f:
            for l in f :
                grid.append([int(x) for x in l.split()])
            return grid
    grid = readGrid("textFile.txt")
    

    def findAllFreeLocs(grid):
        countOne = []
        for row_index, row in enumerate(grid):
            for col_index, item in enumerate(row):
                if grid[row_index][col_index] == 0:
                    count = [row_index,col_index]

                    #coutOne[put coutn[] ]
                    countOne.append(count)
                    #print "[row",row_index ,"]", "[column", col_index, "]"
                    #print count
        return countOne
    def modifyGrid (grid, location, value):
        grid[location[0]][location[1]] = value
    #----------------------------------------
    s = list((int(digit) for digit in str(start)))
    g = list((int(digit) for digit in str(goal)))
    modifyGrid(grid,s,"S")
    modifyGrid(grid,g,"G")

    #-----------------------------------------

    
    def getChildren(grid, start):
        startLeft = [start[0], start[1]-1]
        startRight = [start[0], start[1]+1]
        startUp = [start[0]-1, start[1]]
        startDown = [start[0]+1, start[1]]
        ch = []
        if grid[startLeft[0]][startLeft[1]] == 0 or grid[startLeft[0]][startLeft[1]] == "G" :
            ch.append(startLeft)
        if grid[startRight[0]][startRight[1]] == 0 or grid[startRight[0]][startRight[1]] == "G":
            ch.append(startRight)
        if grid[startUp[0]][startUp[1]] == 0 or grid[startUp[0]][startUp[1]] =="G" :
            ch.append(startUp)
        if grid[startDown[0]][startDown[1]] == 0 or grid[startDown[0]][startDown[1]] == "G":
            ch.append(startDown)
        
        return ch

    #----------------------------------------

    def getParent(par, goal):
        sol = []
        for s in par:
            goalLeft = [goal[0], goal[1]-1]
            goalRight = [goal[0], goal[1]+1]
            goalUp = [goal[0]-1, goal[1]]
            goalDown = [goal[0]+1, goal[1]]
            if s == goalLeft or s == goalRight or s == goalUp or s == goalDown:
                goal = s
                sol.append(s)
        sol.remove(s)        
        return sol
    def writeGrid(filename, grid):
        #Change twoD to oneD array
        with open(filename, 'w') as f:
            for x in grid:
                d = ' '.join(str(y) for y in x)
                f.write("\n {0}".format(d))
                

    #----------------------------------------
    find = True
    parant= []
    openList = []
    closedList =[]
    openList.append(s)
    #----------------------------------------

    if bfsDfs == 1:
        s = 0
    if bfsDfs !=1:
        s = len(openList)-1
    #----------------------------------------
    nodeCount = 0
    while find:
    
        
        node = openList.pop(s)
        nodeCount += 1
        if grid[node[0]][node[1]] == grid[g[0]][g[1]]:
            find = not find
            print "Success"
        
        closedList.append(node)
        children = getChildren(grid, node)
            
        if len(children) >= 1:
                parant.append(node)

        for x in children:
            if  not x in openList  and not x in closedList:  
                openList.append(x)
            
      
        node = None
        childrean = None
    rever_parant = parant[::-1]
   

    soem = getParent(rever_parant, g)
    print nodeCount
    for s in soem:
        modifyGrid (grid, s, '*')
    writeGrid("gridAfter.txt", grid)
    print "Row\Colmn 0 1 2 3 4 5 6 7"
    with open("gridAfter.txt") as f:
            for value, l in enumerate(f) :
                
                print "   ",value,"  ", l

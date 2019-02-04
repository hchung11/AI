import Queue
import math
from heapq import heappush, heappop

try:
    print "Row\Colmn  0 1 2 3 4 5 6 7"
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
    
    grid2 = readGrid("textFile.txt")
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
    orgStart = list((int(digit) for digit in str(start)))
    orgGoal = list((int(digit) for digit in str(goal)))
    modifyGrid(grid2,orgStart,"S")
    modifyGrid(grid2,orgGoal,"G")
    modifyGrid(grid,orgStart,"S")
    modifyGrid(grid,orgGoal,"G")
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
                
     #make the function that caculate distance frome node to goal
    def distance(first_node, goal):
        return (math.sqrt((first_node[0] - goal[0])**2 + (first_node[1] - goal[1])**2))
        
    #----------------------------------------
    find = True

    some = orgStart
    parant= []
    openList = []
    chil_nodes_to_goal = []
    children = []
    sortlowq = []
    heap_caoy =[]
    count = 0
    #----------------------------------------

  
    #----------------------------------------
    heappush(openList,some)
    nodeCount = 0
    while find:
        
        #put first open list on to node
       

        print "openlist :", openList
        first_array_openList= heappop(openList)
        print "first arry pop:::::", first_array_openList
        children = getChildren(grid2,first_array_openList)
        print "childre : ",children
        for i in children:
            heappush(openList,i)
        
        print "openlist after:", openList
        #caculate distance node to goal
        for value, op in enumerate(openList):
 
            fn = count + distance(op, orgGoal)
            #change the number on grid to distance value
            modifyGrid(grid2,op,fn)
            #I just push the distance
            heappush(sortlowq, fn)
            #print "Put value on array ",sortlowq
            #low to high #
        sortlowq.sort()
        print sortlowq
        #lowest will come out of queue
        value_of_sortlest = heappop(sortlowq)
       # print "grid", grid
        #i need to find location of that value on grid
        
        for x in openList:
            
            if value_of_sortlest == distance(x, orgGoal)+count:
                z = x
                openList.insert(0,x)
                openList.insert(0,openList.pop(len(openList)-1))
                modifyGrid(grid, x, "*")
                #every time find smellest children +1
                count += 1
                print "count count count count -------------------------",count                
                break

        print "openlist after sort====== :",openList
        if grid2[z[0]][z[1]] == grid2[orgGoal[0]][orgGoal[1]]:
            modifyGrid(grid, z, "G")
            find = not find
            print "Success"
        
        nodeCount += 1
        
        
    print "grid 2222222",grid2
    print "grid 1111111",grid
        
        #how to put node distance to array postion. 
        
        
    
        
            
        #if len(children) >= 1:
            #    parant.append(node)

    writeGrid("gridAfter.txt", grid)
    print "Row\Colmn 0 1 2 3 4 5 6 7"
    with open("gridAfter.txt") as f:
        for value, l in enumerate(f) :
                
            print "   ",value,"  ", l
            
      
        

   

    print nodeCount
 

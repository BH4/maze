import sys
sys.path.insert(0, 'C:\Users\Bryce\Programming\Python\Pre-implemented algorithms')

from disjointSets import disjointSets
from random import shuffle

class maze:#creates a random maze
    #An nxm maze has n*m cells but this data structure holds the (m+1)*n+(n+1)*m
    #walls. Each could be on or off. The walls are indexed by their row and collumn
    #and are separated into vertical and horizontal
    def __init__(self,width,height):
        self.width=width
        self.height=height
        
        hWalls=[]
        for i in xrange(width):
            col=[1]*(height+1)
            hWalls.append(col)

        vWalls=[]
        for i in xrange(width+1):
            col=[1]*height
            vWalls.append(col)

        self.walls=[vWalls,hWalls]

        self.createRandom()

    def convert(self,x,y):
        return self.width*y+x
    def unconvert(self,n):
        x=n%self.width
        y=n/self.width
        return (x,y)
    
    #take in any interior wall and return numbers labeling the two cells it separates
    def wallCells(self,VorH,x,y):
        if VorH==0:
            return self.vWallCells(x,y)
        else:
            return self.hWallCells(x,y)
    def vWallCells(self,x,y):
        if x==0 or x==self.width:
            print "Not interior wall"
            return None

        xL=x-1
        xR=x
        yBoth=y
        return (self.convert(xL,yBoth),self.convert(xR,yBoth))
    def hWallCells(self,x,y):
        if y==0 or y==self.height:
            print "Not interior wall"
            return None

        yT=y-1
        yB=y
        xBoth=x
        return (self.convert(xBoth,yT),self.convert(xBoth,yB))

    #returns a list of coordinates for each interior wall
    def getWalls(self):
        wallList=[]

        for i in xrange(1,self.width):
            for j in xrange(self.height):
                wallList.append((0,i,j))

        for i in xrange(self.width):
            for j in xrange(1,self.height):
                wallList.append((1,i,j))

        return wallList

    #takes in a maze with all walls on and turns off some walls in such a
    #way that every cell has one path to any other cell
    def createRandom(self):
        #convert cell position into a single number by width*y+x
        #contains the information about if sells are disjoint
        dsets=disjointSets(self.width*self.height)
        
        #randomize interior walls
        walls=self.getWalls()
        shuffle(walls)

        i=0
        while dsets.size>1:
            curr=walls[i]
            cells=self.wallCells(curr[0],curr[1],curr[2])

            cellsWereSeparated=dsets.union(cells[0],cells[1])

            if cellsWereSeparated:#turn off the wall
                self.walls[curr[0]][curr[1]][curr[2]]=0
            
            i+=1


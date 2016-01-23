from PIL import Image

class mazePic:
    def __init__(self,maze):
        self.wallThickness=1#cant change this yet

        #desired image max(width,height)
        desired=500
        m=max(maze.width,maze.height)
        desired-=(m+1)*self.wallThickness
        
        
        self.cellSize=int(desired/m)


        
        self.im=Image.new("RGB",((maze.width+1)*self.wallThickness+maze.width*self.cellSize,(maze.height+1)*self.wallThickness+maze.height*self.cellSize),"white")

        self.pix=self.im.load()

        self.drawMaze(maze.walls)

    def savePic(self,name):
        self.im.save(name+'.jpg', "JPEG")

    def drawMaze(self,walls):
        for i in xrange(len(walls)):#vert or horiz
            lwi=len(walls[i])
            for j in xrange(lwi):#x coordinate
                lwij=len(walls[i][j])
                for k in xrange(lwij):#y coordinate
                    if walls[i][j][k]==1:
                        self.drawWall((i,j,k))

    def drawWall(self,coord):
        (x1,x2,y1,y2)=self.wallEndPoints(coord)
        if coord[0]==0:
            self.drawVertLine(x1,y1,y2)
        if coord[0]==1:
            self.drawHorLine(x1,x2,y1)

    def drawVertLine(self,x,y1,y2):
        dy=abs(y2-y1)
        y=min(y1,y2)

        for i in xrange(dy+2):#making this +2 means some lines will overlap but there wont be any white spots
            self.pix[x,y+i]=(0,0,0)
        
    def drawHorLine(self,x1,x2,y):
        dx=abs(x2-x1)
        x=min(x1,x2)

        for i in xrange(dx+2):
            self.pix[x+i,y]=(0,0,0)


    def wallEndPoints(self,coord):
        if coord[0]==0:
            x1=self.wallThickness*coord[1]+self.cellSize*coord[1]
            x2=x1
            y1=self.wallThickness*coord[2]+self.cellSize*coord[2]
            y2=y1+self.cellSize
        if coord[0]==1:
            y1=self.wallThickness*coord[2]+self.cellSize*coord[2]
            y2=y1
            x1=self.wallThickness*coord[1]+self.cellSize*coord[1]
            x2=x1+self.cellSize

        return (x1,x2,y1,y2)

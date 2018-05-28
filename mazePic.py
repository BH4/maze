from PIL import Image


class mazePic:
    def __init__(self, maze):
        # cant change this yet everything is written so that it moves correctly but the walls are still only 1 thick
        self.wallThickness = 1

        # desired image max(width,height)
        desired = 500
        m = max(maze.width,maze.height)
        desired -= (m+1)*self.wallThickness

        self.cellSize = int(desired/m)

        self.im = Image.new("RGB", ((maze.width+1)
                                    * self.wallThickness+maze.width
                                    * self.cellSize, (maze.height+1)
                                    * self.wallThickness+maze.height
                                    * self.cellSize), "white")

        self.pix = self.im.load()

        self.drawMaze(maze.walls)

    def savePic(self, name):
        self.im.save(name+'.jpg', "JPEG")

    # ----------------------------------------------------
    # drawing the maze walls
    def drawMaze(self, walls):
        for i in range(len(walls)):  # vert or horiz
            lwi = len(walls[i])
            for j in range(lwi):  # x coordinate
                lwij = len(walls[i][j])
                for k in range(lwij):  # y coordinate
                    if walls[i][j][k] == 1:
                        self.drawWall((i, j, k))

    def drawWall(self, coord):
        self.coloredWall(coord, (0, 0, 0))

    def coloredWall(self, coord, color):
        (x1, x2, y1, y2) = self.wallEndPoints(coord)
        if coord[0] == 0:
            self.drawVertLine(x1, y1, y2, color)
        if coord[0] == 1:
            self.drawHorLine(x1, x2, y1, color)

    def drawVertLine(self, x, y1, y2, color):
        dy = abs(y2-y1)
        y = min(y1, y2)

        for i in range(dy+2):  # making this +2 means some lines will overlap but there wont be any white spots
            self.pix[x, y+i] = color

    def drawHorLine(self, x1, x2, y, color):
        dx = abs(x2-x1)
        x = min(x1, x2)

        for i in range(dx+2):
            self.pix[x+i, y] = color

    def wallEndPoints(self, coord):
        if coord[0] == 0:
            x1 = self.wallThickness*coord[1]+self.cellSize*coord[1]
            x2 = x1
            y1 = self.wallThickness*coord[2]+self.cellSize*coord[2]
            y2 = y1+self.cellSize
        if coord[0] == 1:
            y1 = self.wallThickness*coord[2]+self.cellSize*coord[2]
            y2 = y1
            x1 = self.wallThickness*coord[1]+self.cellSize*coord[1]
            x2 = x1+self.cellSize

        return (x1, x2, y1, y2)
    # -------------------------------------------------------

    # given two cells find the coordinates of the wall between them
    def findWall(self, pos1, pos2):
        if pos1==pos2:
            print('same point')
            return None

        dx = pos1[0]-pos2[0]
        dy = pos1[1]-pos2[1]
        if abs(dx)+abs(dy) > 1:
            print('not connected')
            return None

        # at this point either (dx=+1 or -1 and dy=0) or (dy=+1 or -1 and dx=0)

        # wall vertical or horizontal?
        if dx == 0:  # horizonatal
            wVorH = 1

            x = pos1[0]
            y = max(pos1[1],pos2[1])
        if dy == 0:  # vertical
            wVorH = 0

            x = max(pos1[0], pos2[0])
            y = pos1[1]

        return (wVorH, x, y)

    # find top left corner of cell (corners are inside the cell not on wall)
    # cood = (x,y)
    def corner(self, coord):
        x = self.wallThickness*(coord[0]+1)+self.cellSize*coord[0]
        y = self.wallThickness*(coord[1]+1)+self.cellSize*coord[1]

        return (x, y)

    # fill squre with color
    def fill(self, coord, color):
        (x, y) = self.corner(coord)

        for i in range(self.cellSize):
            for j in range(self.cellSize):
                self.pix[x+i, y+j] = color

    # color cells in specified color given in RGB format
    def solution(self, path, color):
        # path is list of coordinates
        last = None
        for cell in path:
            # need to fill the space between the walls. Assumes path is in order
            if last is not None:
                wall = self.findWall(cell, last)
                self.coloredWall(wall, color)

            self.fill(cell, color)

            last = cell

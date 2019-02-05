
class mazeSolver:
    def __init__(self, maze):
        """
        In addition to each solution method returning a path from the beginning
        to the end I want them to keep track of all the nodes they have visited
        in the course of solving the maze. In the future I would like to create
        gifs of the solution algorithms so the visited nodes should be in order
        """
        self.reset()
        self.maze = maze

    def reset(self):
        self.visited_path = []
        self.visited = set()
        self.solution = []

    def cellsConnected(self, pos1, pos2):
        if pos1 == pos2:
            print('same point')
            return False

        dx = pos1[0]-pos2[0]
        dy = pos1[1]-pos2[1]
        if abs(dx)+abs(dy) > 1:
            return False

        # at this point either (dx=+1 or -1 and dy=0) or (dy=+1 or -1 and dx=0)

        # wall vertical or horizontal?
        if dx == 0:  # horizonatal
            wVorH = 1

            x = pos1[0]
            y = max(pos1[1], pos2[1])
        if dy == 0:  # vertical
            wVorH = 0

            x = max(pos1[0], pos2[0])
            y = pos1[1]

        return self.maze.walls[wVorH][x][y] == 0

    def cellNeighbors(self, cell):  # neighbors must be inside maze and not separated by a wall from cell
        change = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        N = []
        for c in change:
            curr = (cell[0]+c[0], cell[1]+c[1])

            if curr[0] >= 0 and curr[1] >= 0 and curr[0] < self.maze.width and curr[1] < self.maze.height:
                if self.cellsConnected(cell, curr):
                    N.append(curr)

        return N

    def depthFirstSearch(self, start, end):
        self.visited_path.append(start)
        self.visited.add(start)

        if start == end:
            self.solution = [end]
            return True

        neighbors = self.cellNeighbors(start)
        for n in neighbors:
            if n not in self.visited:
                solved = self.depthFirstSearch(n, end)
                if solved:
                    self.solution = [start]+self.solution
                    return True

        return False

    def breadthFirstSearch(self, start, end):
        queue = []
        self.visited_path = []
        self.visited = set()

        # push first path
        queue.append([start])
        while len(queue) > 0:
            path = queue.pop(0)
            curr = path[-1]
            self.visited_path.append(curr)
            self.visited.add(curr)

            if curr == end:
                self.solution = path
                return None

            neighbors = self.cellNeighbors(curr)
            for n in neighbors:
                if n not in self.visited:
                    new_path = list(path)
                    new_path.append(n)
                    queue.append(new_path)

        return None

    def aStar(self, start, end):
        return None

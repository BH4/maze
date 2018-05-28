from maze import maze
from mazePic import mazePic
from mazeSolver import mazeSolver

size = 20

# create random maze
a = maze(size, size)

# draw the walls of the maze
aPic = mazePic(a)

# solve the maze
solver = mazeSolver(a)
solver.breadthFirstSearch((0, 0), (size-1, size-1))

# color visited spots and solution
# aPic.listFill(solver.visited,(0,0,255))
aPic.solution(solver.solution, (255, 0, 0))


aPic.savePic('test')

from maze import maze
from mazePic import mazePic
from mazeSolver import mazeSolver

if __name__ == '__main__':
    size = 20

    # create random maze
    small_maze = maze(size, size)
    solver = mazeSolver(small_maze)

    names = ['Breadth First Search', 'Depth First Search']
    methods = [solver.breadthFirstSearch, solver.depthFirstSearch]

    for i, search in enumerate(methods):
        # draw the walls of the maze
        pic = mazePic(small_maze)

        # solve the maze
        search((0, 0), (size-1, size-1))

        # color visited spots and solution
        pic.listFill(solver.visited_path, (0, 0, 255))
        pic.listFill(solver.solution, (255, 0, 0))

        # Solution lengths will always be the same. There is only one solution.
        print('{}: Visited {} squares. Solution length = {} squares.'.format(names[i], len(solver.visited_path), len(solver.solution)))

        pic.savePic(names[i])

        # Reset visited and solution arrays
        solver.reset()

__author__ = 'leon'
import random

class MazeGen:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.maze = [['O' for j in xrange(col)] for i in xrange(row)]
        self.mazeinit()

    def mazegen(self):
        visited = [(random.randint(0, 20)/2*2 + 1, random.randint(0, 20)/2*2 + 1)]
        while len(visited) < 100:
            curr_coord = visited[random.randint(0, len(visited) - 1)]
            availabedirections = self.getavailable(curr_coord[0], curr_coord[1], visited)
            if len(availabedirections) == 0:
                continue
            else:
                next_coord = random.choice(availabedirections)
                self.maze[(curr_coord[0] + next_coord[0])/2][(curr_coord[1] + next_coord[1])/2] = '#'
                visited.append(next_coord)


    def mazeinit(self):
        for i in xrange(1, self.row, 2):
            for j in xrange(1, self.col, 2):
                self.maze[i][j] = '#'

    def getavailable(self, row, col, visited):
        res = []
        if row > 1 and (row - 2, col) not in visited:
            res.append((row - 2, col))
        if col > 1 and (row, col - 2) not in visited:
            res.append((row, col - 2))
        if row < self.row - 2 and (row + 2, col) not in visited:
            res.append((row + 2, col))
        if col < self.col - 2 and (row, col + 2) not in visited:
            res.append((row, col + 2))

        return res

mazeGen = MazeGen(20, 20)
mazeGen.mazegen()
for row in mazeGen.maze:
    print ' '.join(row)
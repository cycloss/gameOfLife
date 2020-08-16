import random, copy, sys
from vector2 import Vector2


class GameOfLife:

    grid = []
    directions = Vector2.getAllDirections()

    def startGameWithGrid(self, grid):
        self.grid = grid
   
    def startGameWithRandomGrid(self, width, height):

        arr: list[str]

        tempGrid = []
        choices = ['#', ' ']


        for i in range(height):
            row = []
            for j in range(width):
                row.append(random.choice(choices))
            tempGrid.append(row)
        
        self.grid = tempGrid

    def printGrid(self):

        for row in self.grid:
            for cell in row:
                print(cell, end='')
            print()
        print('*' * len(self.grid[0]))


    def iterateGrid(self):

        iteratedGrid = copy.deepcopy(self.grid)
        gridRowCount = len(iteratedGrid)
        

        for i in range(gridRowCount):
            currentRow = iteratedGrid[i]
            currentRowCount = len(currentRow)
            for j in range(currentRowCount):

                currentCoord = Vector2(j, i)
                neighbCoords = self.generateNeighbouringCoords(currentCoord)
                wrappedCoords = self.generateWrappedCoords(neighbCoords, currentRowCount, gridRowCount)
                
                aliveCount = 0

                for coord in wrappedCoords:
                    if self.getGridValAlive(coord):
                        aliveCount += 1

                currentCell = currentRow[j]

                if currentCell == '#':
                    if aliveCount != 2 and aliveCount != 3:
                        ##cell that was alive dies
                        iteratedGrid[i][j] = ' '
                else:
                    if aliveCount == 3:
                        ##cell that was dead becomes alive
                        iteratedGrid[i][j] = '#'
        self.grid = iteratedGrid


    def generateNeighbouringCoords(self, vector2: Vector2):
        points = []

        for dir in self.directions:
            point = dir + vector2
                
            points.append(point)
            
        return points


    def generateWrappedCoords(self, coords, maxX, maxY):

        for coord in coords:
            coord = self.getWrappedCoord(coord, maxX, maxY)
            
        return coords


    def getAliveCount(self) -> int:
        print('Getting alive')


    def getWrappedCoord(self, currentCoord: Vector2, maxRow, maxHeight):
    
        wrappedCoord = currentCoord

        if currentCoord.x < 0:
            wrappedCoord.x = maxRow - 1
        elif currentCoord.x >= maxRow:
            wrappedCoord.x = 0
        
        if currentCoord.y < 0:
            wrappedCoord.y = maxHeight - 1
        elif currentCoord.y >= maxHeight:
            wrappedCoord.y = 0

        return wrappedCoord


    def getGridValAlive(self, vector2: Vector2):
        
        try:
            isAlive = self.grid[vector2.y][vector2.x] == '#'
                
        except Exception as e:
            print(e)
            print(vector2.x)
            print(vector2.y)
            sys.exit()
        else:
            return isAlive
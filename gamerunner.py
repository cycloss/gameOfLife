from gameOfLife import GameOfLife
import time

def playGame(iterations):

    game = GameOfLife()
    game.startGameWithRandomGrid(50, 20)

    print('starting game')
    for i in range(iterations):
        game.printGrid()
        game.iterateGrid()
        time.sleep(0.2)
        
    print('over')


playGame(30)

oscillator
# startingGrid = [[' ', ' ', ' ', ' ', ' ', ' '],
#                 [' ', ' ', ' ', ' ', ' ', ' '],
#                 [' ', ' ', '#', '#', '#', ' '],
#                 [' ', '#', '#', '#', ' ', ' '],
#                 [' ', ' ', ' ', ' ', ' ', ' '],
#                 [' ', ' ', ' ', ' ', ' ', ' ']]

# glider
# startingGrid = [[' ', ' ', ' ', ' ', ' ', ' '],
#                 [' ', ' ', '#', ' ', ' ', ' '],
#                 [' ', ' ', ' ', '#', ' ', ' '],
#                 [' ', '#', '#', '#', ' ', ' '],
#                 [' ', ' ', ' ', ' ', ' ', ' '],
#                 [' ', ' ', ' ', ' ', ' ', ' ']]
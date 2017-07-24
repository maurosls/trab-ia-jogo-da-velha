from board import  *
from alphabeta import *
from minmax import *

board = Board()
alphabeta = AlphaBeta()
minmax = MinMax()
array = [0,0,0,0,0,0,0,0,0]
array = board.set(array)
menuLoop = True
minmaxLoop = False
alphabetaLoop = False

def checkWin():
    if(alphabeta.checkWin(array)==1):
        board.xWins()
        return True
    if(alphabeta.checkWin(array)==2):
        board.oWins()
        return True
    if(alphabeta.checkWin(array)==0):
        board.tie()
        return True
    return False

while menuLoop:

    board.drawMenu()
    input = board.menuInput()
    if (input == 'minmax'):
        minmaxLoop = True
    if (input == 'alphabeta'):
        alphabetaLoop = True
    while minmaxLoop:
        board.draw()
        array = board.press()
        board.draw()
        if (checkWin()):
            minmaxLoop=False
            board.reset()
            break
        array = minmax.choose(array)
        board.set(array)
        board.setCont(minmax.getCont())
        board.draw()
        if (checkWin()):
            minmaxLoop=False
            board.reset()
            break
    while alphabetaLoop:
        board.draw()
        array = board.press()
        board.draw()
        if (checkWin()):
            alphabetaLoop=False
            board.reset()
            break
        array = alphabeta.choose(array)
        board.set(array)
        board.setCont(alphabeta.getCont())
        board.draw()
        if (checkWin()):
            alphabetaLoop=False
            board.reset()
            break

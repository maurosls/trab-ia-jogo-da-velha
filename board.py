from PPlay.window import *
from PPlay.sprite import *
import math

class Board():

    window = None
    mouse = None
    background = None
    blankSprite = None
    xSprite = None
    oSprite = None
    startsAISprite = None
    start = None
    sprites = None
    array = None
    cont = None
    menuBackground = None
    minmaxButton = None
    alphabetaButton = None

    def __init__(self):
        self.window = Window(600, 700)
        self.mouse = Window.get_mouse()
        self.background = Sprite('background.png')
        self.sprites = []
        self.array = [[]]
        for x in  range(0,9):
            blankSprite = Sprite('blank.png')
            blankSprite.drawable=False
            self.sprites.append(blankSprite)
        for i in range(0,3):
            for j in range(0,3):
                self.sprites[i*3+j].x = 200*j + 20
                self.sprites[i*3+j].y = 200*i + 20
        self.startsAISprite = Sprite('startsAI.png')
        self.startsAISprite.y = self.background.height-self.startsAISprite.height
        self.start = True
        self.cont = 0
        self.menuBackground = Sprite('menuBackground.png')
        self.minmaxButton = Sprite('minmaxButton.png')
        self.minmaxButton.x = self.window.width/2-self.minmaxButton.width/2
        self.minmaxButton.y = 400
        self.alphabetaButton = Sprite('alphabetaButton.png')
        self.alphabetaButton.x = self.window.width/2-self.alphabetaButton.width/2
        self.alphabetaButton.y = 500

    def set(self,arr):
        self.array = arr
        self.update()
        return self.array

    def setCont(self,cont):
        self.cont = cont
        self.update()

    def press(self):
        exit = True
        while (exit):
            while (self.mouse.is_button_pressed(1)):
                for i in range(0,len(self.sprites)):
                    self.draw()
                    if (self.mouse.is_over_object(self.sprites[i]) and self.array[i] == 0):
                        self.array[i]=2
                        exit = False
                    if (self.mouse.is_over_object(self.startsAISprite) and self.start):
                        self.start = False
                        exit = False
            self.draw()
        self.update()
        return self.array


    def update(self):
        for i in range(0,len(self.sprites)):
            if(self.array[i] == 1):
                x = Sprite('x.png')
                x.x = self.sprites[i].x
                x.y = self.sprites[i].y
                self.sprites[i] = x
            if(self.array[i] == 2):
                o = Sprite('o.png')
                o.x = self.sprites[i].x
                o.y = self.sprites[i].y
                self.sprites[i] = o
            if (self.array[i] == 0):
                b = Sprite('blank.png')
                b.x = self.sprites[i].x
                b.y = self.sprites[i].y
                self.sprites[i] = b

    def delay(self):
        self.window.delay(2000)

    def draw(self):
        self.background.draw()
        for x in range(0, len(self.sprites)):
            self.sprites[x].draw()
        self.startsAISprite.draw()
        self.window.draw_text(str(self.cont),0,0)
        self.window.update()

    def xWins(self):
        self.delay()
        sprite = Sprite('xwins.png')
        sprite.draw()
        self.window.update()
        self.delay()

    def oWins(self):
        self.delay()
        sprite = Sprite('owins.png')
        sprite.draw()
        self.window.update()
        self.delay()

    def tie(self):
        self.delay()
        sprite = Sprite('tie.png')
        sprite.draw()
        self.window.update()
        self.delay()

    def drawMenu(self):
        self.menuBackground.draw()
        self.minmaxButton.draw()
        self.alphabetaButton.draw()
        self.window.update()

    def menuInput(self):
        exit = True
        while (exit):
            while (self.mouse.is_button_pressed(1)):
                self.drawMenu()
                if (self.mouse.is_over_object(self.minmaxButton)):
                        res = 'minmax'
                        exit = False
                if (self.mouse.is_over_object(self.alphabetaButton)):
                        res = 'alphabeta'
                        exit = False
            self.drawMenu()
        self.update()
        return res

    def reset(self):
        self.array = [0,0,0,0,0,0,0,0,0]
        self.start = True
        self.set(self.array)
        self.setCont(0)







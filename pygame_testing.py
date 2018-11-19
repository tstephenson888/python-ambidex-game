import pygame as pg
pg.init()
class Nameplate:
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.font = pg.font.SysFont("None", 30)
        self.text = ""
        self.center = (320,240)

screen = pg.display.set_mode((1000, 750))

tablebg = pg.image.load("PLATES/blankchartA.png")

bg = tablebg

clock = pg.time.Clock()
keepGoing = True
while keepGoing:
    clock.tick(10)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            keepGoing = False
    screen.blit(bg, (0, 0))
    pg.display.flip()

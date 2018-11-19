import pygame as pg
pg.init()
class Nameplate:
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.font = pg.font.SysFont("None", 30)
        self.text = "TEST"
screen = pg.display.set_mode((1000, 750))
layout = B
tablebg = pg.image.load("PLATES/blankchart" + layout + ".png")

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

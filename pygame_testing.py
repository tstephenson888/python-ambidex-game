import pygame as pg
pg.init()
class Label(pg.sprite.Sprite):
    """Label Class (simplest version
        Atttributes :
            font: any pygame Font or SysFont object
            text:  text to display
            center:  desired positon of label center (x,y)
    """
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.font = pg.font.SysFont("None", 30)
        self.text = ""
        self.center = (320,240)
    def update(self):
        self.image = self.font.render(self.text, 1, (0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = self.center


screen = pg.display.set_mode((1000, 750))
layout = "B"


tablebg = pg.image.load("PLATES/blankchart" + layout + ".png")
bg = tablebg
roundnum = 3
roundtitle = pg.image.load(("PLATES/r" + str(roundnum) + ".png"))
clock = pg.time.Clock()
keepGoing = True
while keepGoing:
    clock.tick(10)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            keepGoing = False
    screen.blit(bg, (0, 0))
    screen.blit(roundtitle, (360, 112))
    pg.display.flip()


# print the player names to the grid at the top

# Slowly show what each party voted for

# Stinger sound!!

# Quickly show the change in scores in a "sweeping motion"


# Hold it...

# Print a picture

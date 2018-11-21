import pygame as pg
import time
import os
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

class ABPlayer():

    def __init__(self, name="Tester", points=3, role="???", vote="A", alive=True, won=False):
        self.name = name
        self.points = points
        self.role = role
        self.vote = vote
        self.alive = alive
        self.won = won

screen = pg.display.set_mode((1000, 750))
layout = "B"

p1 = ABPlayer("Junpei")
p2 = ABPlayer("June")
p3 = ABPlayer("Ace")
p4 = ABPlayer("Snake")
p5 = ABPlayer("Santa")
p6 = ABPlayer("Clover")
p7 = ABPlayer("Seven")
p8 = ABPlayer("Lotus")
p9 = ABPlayer("Bofa")

tablebg = pg.image.load("PLATES/blankchart" + layout + ".png")
bg = tablebg
roundnum = 3
roundtitle = pg.image.load(("PLATES/r" + str(roundnum) + ".png"))
clock = pg.time.Clock()
playertable = [p1, p2, p3, p4, p5, p6, p7, p8, p9]
keepGoing = True
while keepGoing:
    clock.tick(10)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            keepGoing = False
    screen.blit(bg, (0, 0))
    screen.blit(roundtitle, (400, 120))
    initial_offset = 200
    spacebetween = 80
    for x in range (0,9):
        if os.path.isfile("PLATES/nameplates/" + playertable[x].name + ".png"):
            plate_exists = pg.image.load(("PLATES/nameplates/" + playertable[x].name + ".png"))
            screen.blit(plate_exists, (initial_offset + (spacebetween * x), 320))
        else:
            customplate = pg.image.load(("PLATES/nameplates/Custom " + str((x + 1)) + ".png"))
            screen.blit(customplate, (initial_offset + (spacebetween * x), 320))

    pg.display.flip()


# print the player names to the grid at the top

# Slowly show what each party voted for

# Stinger sound!!

# Quickly show the change in scores in a "sweeping motion"


# Hold it...

# Save the picture

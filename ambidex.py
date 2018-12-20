import os
import random
import time

import pygame as pg

pg.init()
namepool = ["Ace", "Snake", "Santa",  "Junpei",  "Seven", "9th Man",
                "Sigma", "Quark", "Dio", "K",
                "Carlos",  "Eric", "Q",

                "Clover", "June", "Lotus",
                "Alice","Phi","Luna"
                "Mira", "Diana",

                "Olivia", "Emma", "Charlotte", "Sophia", "Aria", "Ava", "Chloe", "Zoey", "Abigail", "Amilia", "Lea",
                "Florence", "Rosalin",
                "Noah", "Liam", "Jackson", "Lucas", "Logan", "Benjamin", "Jacob", "William", "Oliver", "James",
                "Thomas", "Raphael", "Nathan", "Leo", "Alexis",
                ]
deathmessage = [" is no longer with us.",
                " stopped breathing.", " perished.", " isn't coming back from that.",
                " is in a better place now.",
                " forgot to write their will.", " welcomed Death with open arms.", " expired."]
# gamelog = open("ambidex-log-" + str(datetime.datetime.now()) + ".txt", "a+")



class ABPlayer():

    def __init__(self, name="Tester", points=3, role="???", vote="A", change="", alive=True, won=False):
        self.name = name
        self.points = points
        self.role = role
        self.vote = vote
        self.change = change
        self.alive = alive
        self.won = won

    def kill(self):
        self.alive = False
        print(self.name + random.choice(deathmessage))
p1 = ABPlayer("DEBUG")
p2 = ABPlayer("DEBUG")
p3 = ABPlayer("DEBUG")
p4 = ABPlayer("DEBUG")
p5 = ABPlayer("DEBUG")
p6 = ABPlayer("DEBUG")
p7 = ABPlayer("DEBUG")
p8 = ABPlayer("DEBUG")
p9 = ABPlayer("DEBUG")
playertable = [p1, p2, p3, p4, p5, p6, p7, p8, p9]
pk = pg.font.SysFont("Pokemon Classic.ttf",40)
class Label(pg.sprite.Sprite):
    """Label Class (simplest version
        Atttributes :
            font: any pygame Font or SysFont object
            text:  text to display
            center:  desired positon of label center (x,y)
    """
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.font = pg.font.SysFont("None", 32)
        self.text = ""
        self.center = (320,240)


    def update(self):
        self.image = self.font.render(self.text, 1, (255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = self.center

class Button(pg.sprite.Sprite):
    def __init__(self, text = "", posx = 320, posy = 240, color = (255,0,0)):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((50,50))
        self.image.fill((color))
        self.rect = self.image.get_rect()
        self.font = pg.font.SysFont("None", 32)
        self.text = text
        self.center = (posx,posy)
        self.background = (0,118,163)
        self.mouse = pg.mouse.get_pos()

    def update(self):
        '''create an image based on the font and text'''
        self.image = self.font.render(self.text, 1, (0,0,0), self.background)
        self.rect = self.image.get_rect()       #set the rectangle to be the size of the image.
        self.rect.center = self.center          #position the button
        self.mouse = pg.mouse.get_pos()
        self.check_hover()            #check if mouse is hovering
        self.color()                            #change color of background of label


    def check_hover(self):
      '''adjust is_hover value based on mouse over button - to change hover color'''
      if self.rect.collidepoint(self.mouse):
         self.is_hover = True
      else:
         self.is_hover = False

    def color(self):
      '''change color when hovering'''
      if self.is_hover  == True:
         self.background = (0,84,166)
      else:
         self.background = (57,181,74)

    def click(self):
        '''return true or false based on mouse over the button '''
        if self.rect.collidepoint(self.mouse):
            return True
        else:
            return False
p1 = ABPlayer("DEBUG")
p2 = ABPlayer("DEBUG")
p3 = ABPlayer("DEBUG")
p4 = ABPlayer("DEBUG")
p5 = ABPlayer("DEBUG")
p6 = ABPlayer("DEBUG")
p7 = ABPlayer("DEBUG")
p8 = ABPlayer("DEBUG")
p9 = ABPlayer("DEBUG")
playable = False
playertable = [p1, p2, p3, p4, p5, p6, p7, p8, p9]
layout = "R"
roundnum = 1
screen = pg.display.set_mode((1280, 720))

def abroller():
    #RNG time
    for index in range(0,8):
        temp = random.randint(1, 100)
        if temp <= 50:
            playertable[index].vote = "A"
        else:
            playertable[index].vote = "B"
        # check if a player is dead, change their vote to ally if they are
        if not playertable[index].alive:
            playertable[index].vote = "A"
    if not playertable[0].alive:
        playertable[0].vote = playertable[1].vote
    if not playertable[2].alive:
        playertable[2].vote = playertable[3].vote
    if not playertable[4].alive:
        playertable[4].vote = playertable[5].vote

def setup():

    pg.display.set_caption("Python Ambidex Game")
    global screen

    bg = pg.Surface(screen.get_size())
    bg = bg.convert()
    bg.fill((0,118,163))
    titlegfx = pg.image.load(("img/UI/title.png"))
    titlegfx = titlegfx.convert_alpha()
    titlegfx2 = pg.image.load(("img/UI/subtitle.png"))
    titlegfx2 = titlegfx2.convert_alpha()
    titlegfx3 = pg.image.load(("img/UI/sub2.png"))
    titlegfx3 = titlegfx3.convert_alpha()
    start = Button('Start Game', 320, 600)
    readme = Button("Explanation/Rules", 640,600)
    quit = Button("Close Game", 960,600)
    introButtons = pg.sprite.Group(start,readme,quit)
    clock = pg.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                keepGoing = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                if start.click():
                    print('start clicked')
                    introButtons.remove()
                    keepGoing = False
                    setup2()
                if readme.click():
                    os.open("README.txt",os.O_RDONLY)
                if quit.click():
                    exit()
        screen.blit(bg, (0, 0))
        bg.blit(titlegfx, (400,113))
        bg.blit(titlegfx2, (393,250))
        bg.blit(titlegfx3, (393,400))
        introButtons.clear(screen, bg)
        introButtons.update()
        introButtons.draw(screen)
        pg.mouse.set_visible(True)
        pg.display.flip()


def setup2():
    pg.display.set_caption("Python Ambidex Game")
    global screen
    global p1
    global p2
    global p3
    global p4
    global p5
    global p6
    global p7
    global p8
    global p9
    global playertable
    bg = pg.Surface(screen.get_size())
    bg = bg.convert()
    bg.fill((0,118,163))
    textBox = pg.image.load(("img/UI/textBox.png"))
    textBox = textBox.convert_alpha()
    nvlText = Label()
    nvlText.text = "Select your participants."
    nvlText.center = (640,600)
    buttonA = Button("Cast A [999]", 180,180)
    buttonB = Button("Cast B [Virtue's Last Reward]", 720,180)
    buttonC = Button("Cast C [Zero Time Dilemma]", 640,400)
    buttonGroup = pg.sprite.Group(buttonA,buttonB,buttonC)
    labelGroup = pg.sprite.Group(nvlText)

    clock = pg.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                keepGoing = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                if buttonA.click():
                    p1 = ABPlayer("Junpei")
                    p2 = ABPlayer("June")
                    p3 = ABPlayer("Ace")
                    p4 = ABPlayer("Snake")
                    p5 = ABPlayer("Santa")
                    p6 = ABPlayer("Clover")
                    p7 = ABPlayer("Seven")
                    p8 = ABPlayer("Lotus")
                    p9 = ABPlayer("9th Man")
                    playertable = [p1, p2, p3, p4, p5, p6, p7, p8, p9]
                    keepGoing = False
                    partOverview()
                if buttonB.click():
                    p1 = ABPlayer("Sigma")
                    p2 = ABPlayer("Phi")
                    p5 = ABPlayer("Alice")
                    p4 = ABPlayer("Clover")
                    p3 = ABPlayer("K")
                    p6 = ABPlayer("Luna")
                    p7 = ABPlayer("Tenmyouji")
                    p8 = ABPlayer("Quark")
                    p9 = ABPlayer("Dio")
                    playertable = [p1, p2, p3, p4, p5, p6, p7, p8, p9]
                    keepGoing = False
                    partOverview()
                if buttonC.click():
                    p1 = ABPlayer("Carlos")
                    p2 = ABPlayer("Akane")
                    p3 = ABPlayer("Junpei")
                    p4 = ABPlayer("Sigma")
                    p5 = ABPlayer("Phi")
                    p6 = ABPlayer("Diana")
                    p7 = ABPlayer("Q")
                    p8 = ABPlayer("Mira")
                    p9 = ABPlayer("Eric")
                    playertable = [p1, p2, p3, p4, p5, p6, p7, p8, p9]
                    keepGoing = False
                    partOverview()
        screen.blit(bg, (0, 0))
        bg.blit(textBox,(100,550))
        buttonGroup.clear(screen, bg)
        buttonGroup.update()
        buttonGroup.draw(screen)
        labelGroup.update()
        labelGroup.draw(screen)
        pg.mouse.set_visible(True)
        pg.display.flip()
def partOverview():
    global screen
    global p1
    global p2
    global p3
    global p4
    global p5
    global p6
    global p7
    global p8
    global p9
    global playertable
    bg = pg.Surface(screen.get_size())
    bg = bg.convert()
    bg.fill((0,118,163))
    textlabel = Label()
    textlabel.text = "Your participants are:"
    textlabel.center = (320,270)
    part1 = Label()
    part1.text = playertable[0].name
    part1.center = (960,60)
    part2 = Label()
    part2.text = playertable[1].name
    part2.center = (960,110)
    part3 = Label()
    part3.text = playertable[2].name
    part3.center = (960,160)
    part4 = Label()
    part4.text = playertable[3].name
    part4.center = (960,210)
    part5 = Label()
    part5.text = playertable[4].name
    part5.center = (960,260)
    part6 = Label()
    part6.text = playertable[5].name
    part6.center = (960,310)
    part7 = Label()
    part7.text = playertable[6].name
    part7.center = (960,360)
    part8 = Label()
    part8.text = playertable[7].name
    part8.center = (960,410)
    part9 = Label()
    part9.text = playertable[8].name
    part9.center = (960,460)
    continueBtn = Button("Continue", 1080,640)
    buttonGroup = pg.sprite.Group(continueBtn)
    labelGroup = pg.sprite.Group(textlabel,part1,part2,part3,part4,part5, part6, part7, part7, part8, part9)
    clock = pg.time.Clock()
    keepGoing = True
    while keepGoing:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                keepGoing = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                if continueBtn.click():
                    keepGoing = False
                    teamShuffle()

        screen.blit(bg, (0, 0))
        buttonGroup.clear(screen, bg)
        buttonGroup.update()
        buttonGroup.draw(screen)
        labelGroup.update()
        labelGroup.draw(screen)
        pg.mouse.set_visible(True)
        pg.display.flip()

def teamShuffle():
    global screen
    global p1
    global p2
    global p3
    global p4
    global p5
    global p6
    global p7
    global p8
    global p9
    global playertable
    global layout
    bg = pg.image.load("img/layout/scrambled.png")
    bg = bg.convert_alpha()


    random.shuffle(playertable)
    playertable[0].role = "Red Pair"
    playertable[1].role = "Red Pair"

    playertable[2].role = "Blue Pair"
    playertable[3].role = "Blue Pair"

    playertable[4].role = "Green Pair"
    playertable[5].role = "Green Pair"

    playertable[6].role = "Red Solo"
    playertable[7].role = "Blue Solo"
    playertable[8].role = "Green Solo"

    textBox = pg.image.load(("img/UI/textBox.png"))
    textBox = textBox.convert_alpha()
    nvlText = Label()
    nvlText.text = "The teams have been scrambled!"
    nvlText.center = (640,600)

    PredText = Label()
    PredText.text = playertable[0].name + " & " + playertable[1].name
    PredText.center = (550,220)

    PbluText = Label()
    PbluText.text = playertable[2].name + " & " + playertable[3].name
    PbluText.center = (550,340)

    PgrnText = Label()
    PgrnText.text = playertable[4].name + " & " + playertable[5].name
    PgrnText.center = (550,460)

    SredText = Label()
    SredText.text = playertable[6].name
    SredText.center = (890,220)

    SbluText = Label()
    SbluText.text = playertable[7].name
    SbluText.center = (890,340)

    SgrnText = Label()
    SgrnText.text = playertable[8].name
    SgrnText.center = (890,460)
    labelGroup = pg.sprite.Group(PredText,PbluText,PgrnText,SredText,SbluText,SgrnText,nvlText)

    continueBtn = Button("Continue", 1080,640)
    buttonGroup = pg.sprite.Group(continueBtn)
    keepGoing = True
    while keepGoing:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                keepGoing = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                if continueBtn.click():
                    layoutChooser()
                    keepGoing = False
        screen.blit(bg, (0, 0))
        buttonGroup.clear(screen, bg)
        buttonGroup.update()
        buttonGroup.draw(screen)
        labelGroup.update()
        labelGroup.draw(screen)
        pg.mouse.set_visible(True)
        pg.display.flip()

def layoutChooser():
    global screen
    global p1
    global p2
    global p3
    global p4
    global p5
    global p6
    global p7
    global p8
    global p9
    global playertable
    global layout
    bg = pg.Surface(screen.get_size())
    bg = bg.convert()
    bg.fill((0,118,163))
    textBox = pg.image.load(("img/UI/textBox.png"))
    textBox = textBox.convert_alpha()
    nvlText = Label()
    nvlText.text = "Select your team layout."
    nvlText.center = (640,600)

    buttonA = Button()
    buttonA.text = "Layout A: Red Pair vs. Blue Solo, Blue Pair vs. Green Solo, Green Pair vs. Red Solo"
    buttonA.center = 640,160
    buttonB = Button()
    buttonB.text = "Layout B: Red Pair vs. Green Solo, Blue Pair vs. Red Solo, Green Pair vs. Blue Solo"
    buttonB.center = 640,320
    buttonC = Button()
    buttonC.text = "Layout C: The same-colored Pairs and Solos vote against each other. (RvR, BvB, GvG)"
    buttonC.center = 640,480
    buttonGroup = pg.sprite.Group(buttonA,buttonB,buttonC)
    labelGroup = pg.sprite.Group(nvlText)
    keepGoing = True

    while keepGoing:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                keepGoing = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                if buttonA.click:
                    layout = "A"
                    imgChart()
                    keepGoing = False
                elif buttonB.click:
                    layout = "B"
                    imgChart()
                    keepGoing = False
                elif buttonC.click:
                    layout = "C"
                    imgChart()
                    keepGoing = False
        screen.blit(bg, (0, 0))
        bg.blit(textBox,(100,550))
        buttonGroup.clear(screen, bg)
        buttonGroup.update()
        buttonGroup.draw(screen)
        labelGroup.update()
        labelGroup.draw(screen)
        pg.mouse.set_visible(True)
        pg.display.flip()
        abroller()

def pointAssignment():
    global playertable
    global layout
    if layout.upper() == "A":
        a = 0
        b = 1
        c = 7
        d = 2
        e = 3
        f = 8
        g = 4
        h = 5
        i = 6
    elif layout.upper() == "B":
        a = 0
        b = 1
        c = 8
        d = 2
        e = 3
        f = 6
        g = 4
        h = 5
        i = 7
    elif layout.upper() == "C":
        a = 0
        b = 1
        c = 6
        d = 2
        e = 3
        f = 7
        g = 4
        h = 5
        i = 8
    if playertable[a].vote == "A" and playertable[c].vote == "A":
        playertable[a].points = playertable[a].points + 2
        playertable[a].change = "+2"
        playertable[b].points = playertable[b].points + 2
        playertable[b].change = "+2"
        playertable[c].points = playertable[c].points + 2
        playertable[a].change = "+2"
        print(playertable[a].role + " and " + playertable[c].role + " both allied. Both parties gain 2 points.")
    elif playertable[a].vote == "A" and playertable[c].vote == "B":
        playertable[a].points = playertable[a].points - 2
        playertable[a].change = "-2"
        playertable[b].points = playertable[b].points - 2
        playertable[b].change = "-2"
        playertable[c].points = playertable[c].points + 3
        playertable[c].change = "+3"
        print(playertable[a].role + " allied while " + playertable[c].role + " betrayed. " + playertable[a].role + " loses 2 points while " + playertable[c].role + " gains 3.")
    elif playertable[a].vote == "B" and playertable[c].vote == "A":
        playertable[a].points = playertable[a].points + 3
        playertable[a].change = "+3"
        playertable[b].points = playertable[b].points + 3
        playertable[b].change = "+3"
        playertable[c].points = playertable[c].points - 2
        playertable[c].change = "-2"
        print(playertable[c].role + " allied while " + playertable[a].role + " betrayed. " + playertable[c].role + " loses 2 points while " + playertable[a].role + " gains 3.")
    else:
        print(playertable[a].role + " and " + playertable[c].role + " both betrayed each other. Nothing happened with their scores.")

        playertable[a].change = "0"
        playertable[b].change = "0"
        playertable[c].change = "0"
    if playertable[d].vote == "A" and playertable[f].vote == "A":
        playertable[d].points = playertable[d].points + 2
        playertable[d].change = "+2"
        playertable[e].points = playertable[e].points + 2
        playertable[e].change = "+2"
        playertable[f].points = playertable[f].points + 2

        playertable[f].change = "+2"
        print(playertable[d].role + " and " + playertable[f].role + " both allied. Both parties gain 2 points.")
    elif playertable[d].vote == "A" and playertable[f].vote == "B":
        playertable[d].points = playertable[d].points - 2

        playertable[d].change = "-2"
        playertable[e].points = playertable[e].points - 2

        playertable[e].change = "-2"
        playertable[f].points = playertable[f].points + 3

        playertable[f].change = "+3"
        print(playertable[d].role + " allied while " + playertable[f].role + " betrayed. " + playertable[
            a].role + " loses 2 points while " + playertable[f].role + " gains 3.")
    elif playertable[d].vote == "B" and playertable[f].vote == "A":
        playertable[d].points = playertable[d].points + 3
        playertable[d].change = "+3"
        playertable[e].points = playertable[e].points + 3
        playertable[e].change = "+3"
        playertable[f].points = playertable[f].points - 2
        playertable[f].change = "-2"
        print(playertable[f].role + " allied while " + playertable[d].role + " betrayed. " + playertable[
            c].role + " loses 2 points while " + playertable[d].role + " gains 3.")
    else:
        print(playertable[d].role + " and " + playertable[f].role + " both betrayed each other. Nothing happened with their scores.")
        playertable[d].change = "0"
        playertable[e].change = "0"
        playertable[f].change = "0"
    if playertable[g].vote == "A" and playertable[i].vote == "A":
        playertable[g].points = playertable[g].points + 2
        playertable[g].change = "+2"
        playertable[h].points = playertable[h].points + 2
        playertable[h].change = "+2"
        playertable[i].points = playertable[i].points + 2
        playertable[i].change = "+2"
        print(playertable[g].role + " and " + playertable[i].role + " both allied. Both parties gain 2 points.")
    elif playertable[g].vote == "A" and playertable[i].vote == "B":
        playertable[g].points = playertable[g].points - 2
        playertable[g].change = "-2"
        playertable[h].points = playertable[h].points - 2
        playertable[h].change = "-2"
        playertable[i].points = playertable[i].points + 3
        playertable[i].change = "+3"
        print(playertable[g].role + " allied while " + playertable[i].role + " betrayed. " + playertable[g].role + " loses 2 points while " + playertable[i].role + " gains 3.")
    elif playertable[g].vote == "B" and playertable[i].vote == "A":
        playertable[g].points = playertable[g].points + 3
        playertable[g].change = "+3"
        playertable[h].points = playertable[h].points + 3
        playertable[h].change = "+3"
        playertable[i].points = playertable[i].points - 2
        playertable[i].change = "-2"
        print(playertable[i].role + " allied while " + playertable[g].role + " betrayed. " + playertable[i].role + " loses 2 points while " + playertable[g].role + " gains 3.")
    else:
        print(playertable[g].role + " and " + playertable[i].role + " both betrayed each other. Nothing happened with their scores.")
        playertable[g].change = "0"
        playertable[h].change = "0"
        playertable[i].change = "0"
def imgChart():
    global p1
    global p2
    global p3
    global p4
    global p5
    global p6
    global p7
    global p8
    global p9
    global playertable
    global layout
    pg.display.set_caption("Python Ambidex Game")
    global screen
    bg = pg.image.load(("img/chartstuff/blankchart" + layout.upper() + ".png"))
    roundtitle = pg.image.load(("img/chartstuff/r" + str(roundnum) + ".png"))

    # pairs
    namea = Label()
    namea.text = playertable[0].name
    namea.center = (250,260)
    nameb = Label()
    nameb.text = playertable[1].name
    nameb.center = (370,260)
    namec = Label()
    namec.text = playertable[2].name
    namec.center = (600,260)
    named = Label()
    named.text = playertable[3].name
    named.center = (720,260)
    namee = Label()
    namee.text = playertable[4].name
    namee.center = (940,260)
    namef = Label()
    namef.text = playertable[5].name
    namef.center = (1050,260)

    #solos
    nameg = Label()
    nameg.text = playertable[6].name
    nameh = Label()
    nameh.text = playertable[7].name
    namei = Label()
    namei.text = playertable[8].name
    #logic
    if layout == "A":
        nameh.center = (480,260)
        namei.center = (820,260)
        nameg.center = (1180,260)
    if layout == "B":
        namei.center = (480,260)
        nameg.center = (820,260)
        nameh.center = (1180,260)
    if layout == "C":
        nameh.center = (480,260)
        namei.center = (820,260)
        nameg.center = (1180,260)

    # points, pairs
    pointsa = Label()
    pointsa.text = str(playertable[0].points)
    pointsa.center = (250,350)
    pointsb = Label()
    pointsb.text = str(playertable[1].points)
    pointsb.center = (370,350)
    pointsc = Label()
    pointsc.text = str(playertable[2].points)
    pointsc.center = (600,350)
    pointsd = Label()
    pointsd.text = str(playertable[3].points)
    pointsd.center = (720,350)
    pointse = Label()
    pointse.text = str(playertable[4].points)
    pointse.center = (940,350)
    pointsf = Label()
    pointsf.text = str(playertable[5].points)
    pointsf.center = (1050,350)

    # solos
    pointsg = Label()
    pointsg.text = str(playertable[6].points)
    pointsh = Label()
    pointsh.text = str(playertable[7].points)
    pointsi = Label()
    pointsi.text = str(playertable[8].points)
    #logic
    if layout == "A":
        pointsh.center = (480,350)
        pointsi.center = (820,350)
        pointsg.center = (1180,350)
    if layout == "B":
        pointsi.center = (480,350)
        pointsg.center = (820,350)
        pointsh.center = (1180,350)
    if layout == "C":
        pointsg.center = (480,350)
        pointsh.center = (820,350)
        pointsi.center = (1180,350)
    #A/B, pairs
    AB1 = Label()
    AB1.center = (320,420)
    AB2 = Label()
    AB2.center = (650,420)
    AB3 = Label()
    AB3.center = (1000,420)
    AB4 = Label()
    AB5 = Label()
    AB6 = Label()
    if playertable[0].vote == "A":
        AB1.text = "Ally"
    else:
        AB1.text = "Betray"
    if playertable[2].vote == "A":
        AB2.text = "Ally"
    else:
        AB2.text = "Betray"
    if playertable[4].vote == "A":
        AB3.text = "Ally"
    else:
        AB3.text = "Betray"
    #solos
    if playertable[6].vote == "A":
        AB4.text = "Ally"
    else:
        AB4.text = "Betray"
    if playertable[7].vote == "A":
        AB5.text = "Ally"
    else:
        AB5.text = "Betray"
    if playertable[8].vote == "A":
        AB6.text = "Ally"
    else:
        AB6.text = "Betray"
    #solos-logic
    if layout == "A":
        AB5.center = (480,420)
        AB6.center = (820,420)
        AB4.center = (1180,420)
    if layout == "B":
        AB6.center = (480,420)
        AB4.center = (820,420)
        AB5.center = (1180,420)
    if layout == "C":
        AB4.center = (480,420)
        AB5.center = (820,420)
        AB6.center = (1180,420)

    pointAssignment()
    #points changes, pairs
    changea = Label()
    changeb = Label()
    changec = Label()
    changed = Label()
    changee = Label()
    changef = Label()
    changeg = Label()
    changeh = Label()
    changei = Label()
    changea.text = playertable[0].change
    changeb.text = playertable[1].change
    changec.text = playertable[2].change
    changed.text = playertable[3].change
    changee.text = playertable[4].change
    changef.text = playertable[5].change
    changeg.text = playertable[6].change
    changeh.text = playertable[7].change
    changei.text = playertable[8].change
    changea.center = (250,490)
    changeb.center = (370,490)
    changec.center = (600,490)
    changed.center = (710,490)
    changee.center = (930,490)
    changef.center = (1050,490)
    if layout == "A":
        changeh.center = (480,490)
        changei.center = (820,490)
        changeg.center = (1180,490)
    if layout == "B":
        changei.center = (480,490)
        changeg.center = (820,490)
        changeh.center = (1180,490)
    if layout == "C":
        changeg.center = (480,490)
        changeh.center = (820,490)
        changei.center = (1180,490)
    npointsa = Label()
    npointsa.text = str(playertable[0].points)
    npointsa.center = (250,570)
    npointsb = Label()
    npointsb.text = str(playertable[1].points)
    npointsb.center = (370,570)
    npointsc = Label()
    npointsc.text = str(playertable[2].points)
    npointsc.center = (600,570)
    npointsd = Label()
    npointsd.text = str(playertable[3].points)
    npointsd.center = (720,570)
    npointse = Label()
    npointse.text = str(playertable[4].points)
    npointse.center = (940,570)
    npointsf = Label()
    npointsf.text = str(playertable[5].points)
    npointsf.center = (1050,570)

    # solos
    npointsg = Label()
    npointsg.text = str(playertable[6].points)
    npointsh = Label()
    npointsh.text = str(playertable[7].points)
    npointsi = Label()
    npointsi.text = str(playertable[8].points)
    #logic
    if layout == "A":
        npointsh.center = (480,570)
        npointsi.center = (820,570)
        npointsg.center = (1180,570)
    if layout == "B":
        npointsi.center = (480,570)
        npointsg.center = (820,570)
        npointsh.center = (1180,570)
    if layout == "C":
        npointsg.center = (480,570)
        npointsh.center = (820,570)
        npointsi.center = (1180,570)
    nameGroup = pg.sprite.Group(namea,nameb,namec,named,namee,namef,nameg,nameh,namei)
    sPointsGroup = pg.sprite.Group(pointsa,pointsb,pointsc,pointsd,pointse,pointsf,pointsg,pointsh,pointsi)
    voteGroup = pg.sprite.Group(AB1,AB2,AB3,AB4,AB5,AB6)
    changeGroup = pg.sprite.Group(changea,changeb,changec,changed,changee,changef,changeg,changeh,changeh,changei)
    nPointsGroup = pg.sprite.Group(npointsa,npointsb,npointsc,npointsd,npointse,npointsf,npointsg,npointsh,npointsi)
    continueBtn = Button("Continue", 1080,640)
    buttonGroup = pg.sprite.Group(continueBtn)
    clock = pg.time.Clock()
    keepGoing = True
    sPointsGroup.update()
    while keepGoing:
        clock.tick(30)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                keepGoing = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                if continueBtn.click():
                    keepGoing = False
                    StatusScreen()
        screen.blit(bg, (0, 0))

        # bg.blit(nvlText,nvlText.get_rect())
        pg.mouse.set_visible(True)
        screen.blit(bg, (0, 0))
        screen.blit(roundtitle, (640, 40))
        nameGroup.update()
        nameGroup.draw(screen)

        sPointsGroup.draw(screen)
        voteGroup.update()
        voteGroup.draw(screen)
        changeGroup.update()
        changeGroup.draw(screen)
        nPointsGroup.update()
        nPointsGroup.draw(screen)
        buttonGroup.update()
        buttonGroup.draw(screen)
        pg.mouse.set_visible(True)
        pg.display.flip()

def StatusScreen():
    global screen
    global p1
    global p2
    global p3
    global p4
    global p5
    global p6
    global p7
    global p8
    global p9
    global playertable
    global layout
    bg = pg.Surface(screen.get_size())
    bg = bg.convert()
    bg.fill((0,118,163))
    textBox = pg.image.load(("img/UI/textBox.png"))
    textBox = textBox.convert_alpha()
    nvlText = Label()
    nvlText.center = (640,580)
    nvlText2 = Label()
    nvlText2.center = (640,610)
    nvlText3 = Label()
    nvlText3.center = (640,640)
    nvlText4 = Label()
    nvlText4.center = (640,640)
    for x in range(0,9):
        if playertable[x].points <= 0:
            if playertable[x].alive:
                playertable[x].kill()
                if not nvlText.text:
                    nvlText.text = playertable[x].name + random.choice(deathmessage)
                    pass
                elif not nvlText2.text:
                    nvlText2.text = playertable[x].name + random.choice(deathmessage)
                    pass
                elif not nvlText3.text:
                    nvlText3.text = playertable[x].name + random.choice(deathmessage)
                    pass
                elif not nvlText4.text:
                    nvlText4.text = playertable[x].name + random.choice(deathmessage)
                    pass
    for x in range(0,9):
        if playertable[x].points >= 9:
            playertable[x].won = True
            temp = (playertable[x].name + " has " + str(playertable[x].points) + " points, and leaves the facility.")
            if not nvlText.text:
                nvlText.text = temp
            elif not nvlText2.text:
                nvlText2.text = temp
            elif not nvlText3.text:
                nvlText3.text = temp
            elif not nvlText4.text:
                nvlText4.text = temp
            winflag = True
        else:
            winflag = False
    labelGroup = pg.sprite.Group(nvlText,nvlText2,nvlText3)
    continueBtn = Button("Continue", 1080,400)
    buttonGroup = pg.sprite.Group(continueBtn)
    keepGoing = True
    while keepGoing:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                keepGoing = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                if continueBtn.click():
                    if winflag:
                        quit()
                    teamShuffle()
                    keepGoing = False
        screen.blit(bg, (0, 0))
        buttonGroup.clear(screen, bg)
        buttonGroup.update()
        buttonGroup.draw(screen)
        bg.blit(textBox,(100,550))
        labelGroup.update()
        labelGroup.draw(screen)
        pg.mouse.set_visible(True)
        pg.display.flip()
def main():
    setup()
    setup2()
    partOverview()
    teamShuffle()
    layoutChooser()
    imgChart()
    StatusScreen()

main()

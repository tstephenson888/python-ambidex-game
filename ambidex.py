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

    def __init__(self, name="Tester", points=3, role="???", vote="A", alive=True, won=False):
        self.name = name
        self.points = points
        self.role = role
        self.vote = vote
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

    #buttonA = pg.image.load(("img/layout/layoutA.png"))
    #buttonA = buttonA.convert_alpha()
    #buttonB = pg.image.load(("img/layout/layoutB.png"))
    #buttonB = buttonB.convert_alpha()
    #buttonC = pg.image.load(("img/layout/layoutC.png"))
    #buttonC = buttonC.convert_alpha()

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
    abroller()
    while keepGoing:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                keepGoing = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                if buttonA.click:
                    layout = "A"
                    imgChart()
                if buttonB.click:
                    layout = "B"
                    imgChart()
                if buttonC.click:
                    layout = "C"
                    imgChart()
        screen.blit(bg, (0, 0))
        bg.blit(textBox,(100,550))
        buttonGroup.clear(screen, bg)
        buttonGroup.update()
        buttonGroup.draw(screen)
        labelGroup.update()
        labelGroup.draw(screen)
        pg.mouse.set_visible(True)
        pg.display.flip()

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
        playertable[b].points = playertable[b].points + 2
        playertable[c].points = playertable[c].points + 2
        print(playertable[a].role + " and " + playertable[c].role + " both allied. Both parties gain 2 points.")
    elif playertable[a].vote == "A" and playertable[c].vote == "B":
        playertable[a].points = playertable[a].points - 2
        playertable[b].points = playertable[b].points - 2
        playertable[c].points = playertable[c].points + 3
        print(playertable[a].role + " allied while " + playertable[c].role + " betrayed. " + playertable[a].role + " loses 2 points while " + playertable[c].role + " gains 3.")
    elif playertable[a].vote == "B" and playertable[c].vote == "A":
        playertable[a].points = playertable[a].points + 3
        playertable[b].points = playertable[b].points + 3
        playertable[c].points = playertable[c].points - 2
        print(playertable[c].role + " allied while " + playertable[a].role + " betrayed. " + playertable[c].role + " loses 2 points while " + playertable[a].role + " gains 3.")
    else:
        print(playertable[a].role + " and " + playertable[c].role + " both betrayed each other. Nothing happened with their scores.")
    time.sleep(2)
    if playertable[d].vote == "A" and playertable[f].vote == "A":
        playertable[d].points = playertable[d].points + 2
        playertable[e].points = playertable[e].points + 2
        playertable[f].points = playertable[f].points + 2
        print(playertable[d].role + " and " + playertable[f].role + " both allied. Both parties gain 2 points.")
    elif playertable[d].vote == "A" and playertable[f].vote == "B":
        playertable[d].points = playertable[d].points - 2
        playertable[e].points = playertable[e].points - 2
        playertable[f].points = playertable[f].points + 3
        print(playertable[d].role + " allied while " + playertable[f].role + " betrayed. " + playertable[
            a].role + " loses 2 points while " + playertable[f].role + " gains 3.")
    elif playertable[d].vote == "B" and playertable[f].vote == "A":
        playertable[d].points = playertable[d].points + 3
        playertable[e].points = playertable[e].points + 3
        playertable[f].points = playertable[f].points - 2
        print(playertable[f].role + " allied while " + playertable[d].role + " betrayed. " + playertable[
            c].role + " loses 2 points while " + playertable[d].role + " gains 3.")
    else:
        print(playertable[d].role + " and " + playertable[f].role + " both betrayed each other. Nothing happened with their scores.")
    time.sleep(2)
    if playertable[g].vote == "A" and playertable[i].vote == "A":
        playertable[g].points = playertable[g].points + 2
        playertable[h].points = playertable[h].points + 2
        playertable[i].points = playertable[i].points + 2
        print(playertable[g].role + " and " + playertable[i].role + " both allied. Both parties gain 2 points.")
    elif playertable[g].vote == "A" and playertable[i].vote == "B":
        playertable[g].points = playertable[g].points - 2
        playertable[h].points = playertable[h].points - 2
        playertable[i].points = playertable[i].points + 3
        print(playertable[g].role + " allied while " + playertable[i].role + " betrayed. " + playertable[g].role + " loses 2 points while " + playertable[i].role + " gains 3.")
    elif playertable[g].vote == "B" and playertable[i].vote == "A":
        playertable[g].points = playertable[g].points + 3
        playertable[h].points = playertable[h].points + 3
        playertable[i].points = playertable[i].points - 2
        print(playertable[i].role + " allied while " + playertable[g].role + " betrayed. " + playertable[i].role + " loses 2 points while " + playertable[g].role + " gains 3.")
    else:
        print(playertable[g].role + " and " + playertable[i].role + " both betrayed each other. Nothing happened with their scores.")
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
    pg.display.set_caption("Python Ambidex Game")
    global screen
    roundnum = 3
    custom_count = 0
    bg = pg.image.load(("img/chartstuff/blankchart" + layout.upper() + ".png"))
    roundtitle = pg.image.load(("img/chartstuff/r" + str(roundnum) + ".png"))
    #assigning temp variables due to layout
    namea = Label
    namea.text = playertable[0].name
    namea.center = (250,260)
    nameb = Label
    nameb.text = playertable[1].name
    nameb.center = (370,260)
    namec = Label
    namec.text = playertable[2].name
    namec.center = (480,260)
    named = Label
    named.text = playertable[3].name
    named.center = (600,260)
    namee = Label
    namee.text = playertable[4].name
    namee.center = (710,260)
    namef = Label
    namef.text = playertable[5].name
    namef.center = (830,260)
    nameg = Label
    nameg.text = playertable[6].name
    nameg.center = (950,260)
    nameh = Label
    nameh.text = playertable[7].name
    nameh.center = (1050,260)
    namei = Label
    namei.text = playertable[8].name
    namei.center = (1160,260)
    for p in playertable:
        pass
    nameGroup = pg.sprite.Group(namea,nameb,namec,named,namee,namef,nameg,nameh,namei)
    sPointsGroup = pg.sprite.Group()
    voteGroup = pg.sprite.Group()
    changeGroup = pg.sprite.Group()
    nPointsGroup = pg.sprite.Group()
    pointAssignment()
    clock = pg.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                keepGoing = False
        screen.blit(bg, (0, 0))

        # bg.blit(nvlText,nvlText.get_rect())
        pg.mouse.set_visible(True)
        screen.blit(bg, (0, 0))
        screen.blit(roundtitle, (640, 40))
        pg.display.flip()


def main():
    setup()
    setup2()
    partOverview()
    teamShuffle()
    layoutChooser()
    imgChart()

main()

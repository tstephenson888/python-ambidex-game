import random
import time
import sys
import datetime
import os
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
f1 = pg.font.Font("Pokemon Classic.ttf", 32)
class Label(pg.sprite.Sprite):
    """Label Class (simplest version
        Atttributes :
            font: any pygame Font or SysFont object
            text:  text to display
            center:  desired positon of label center (x,y)
    """
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.font = pg.font.Font(f1, 32)
        self.text = ""
        self.center = (640,600)


    def update(self):
        self.image = self.font.render(self.text, 1, (0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = self.center

def wait():
    input("Press any key to continue.")

def linebreak():
    print("-----------------")

playable = False

def setup():

    pg.display.set_caption("Python Ambidex Game")
    screen = pg.display.set_mode((1280, 720))

    bg = pg.Surface(screen.get_size())
    bg = bg.convert()
    bg.fill((255,255,0))
    textbox = Label
    textbox.font = (f1, 48)
    textbox.center = 640,600
    textbox.text = "TEST STRING"
    clock = pg.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                keepGoing = False
        screen.blit(bg, (0, 0))

        pg.display.flip()

def intro():
    #Init players because Python likes to complain
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

        print("Hello! This is a simulation for the Ambidex Game found in Zero Escape: Virtue's Last Reward.")
        print("Please read the README file in this .py file's directory for a rundown of how the game works.")
        nameprompt = input("What cast would you like as your participants? (Enter [9]99, [V]LR, [Z]TD, "
                           "or press enter for custom names.) ")


        if nameprompt.upper() == "999" or nameprompt.upper() == "9":
            p1 = ABPlayer("Junpei")
            p2 = ABPlayer("June")
            p3 = ABPlayer("Ace")
            p4 = ABPlayer("Snake")
            p5 = ABPlayer("Santa")
            p6 = ABPlayer("Clover")
            p7 = ABPlayer("Seven")
            p8 = ABPlayer("Lotus")
            p9 = ABPlayer("Kutoba")

        elif nameprompt.upper() == "VLR" or nameprompt.upper() == "V":
            p1 = ABPlayer("Sigma")
            p2 = ABPlayer("Phi")
            p5 = ABPlayer("Alice")
            p4 = ABPlayer("Clover")
            p3 = ABPlayer("K")
            p6 = ABPlayer("Luna")
            p7 = ABPlayer("Tenmyouji")
            p8 = ABPlayer("Quark")
            p9 = ABPlayer("Dio")

        elif nameprompt.upper() == "ZTD" or nameprompt.upper() == "Z":
            p1 = ABPlayer("Carlos")
            p2 = ABPlayer("Akane")
            p3 = ABPlayer("Junpei")
            p4 = ABPlayer("Sigma")
            p5 = ABPlayer("Phi")
            p6 = ABPlayer("Diana")
            p7 = ABPlayer("Q")
            p8 = ABPlayer("Mira")
            p9 = ABPlayer("Eric")
        else:
            p1 = ABPlayer(input("Enter the name of the first player. "))
            p2 = ABPlayer(input("Enter the name of the second player. "))
            p3 = ABPlayer(input("Enter the name of the third player. "))
            p4 = ABPlayer(input("Enter the name of the fourth player. "))
            p5 = ABPlayer(input("Enter the name of the fifth player. "))
            p6 = ABPlayer(input("Enter the name of the sixth player. "))
            p7 = ABPlayer(input("Enter the name of the seventh player. "))
            p8 = ABPlayer(input("Enter the name of the eighth player. "))
            p9 = ABPlayer(input("Enter the name of the ninth player. "))
        print("Your players are: ")
        linebreak()
        print(p1.name)
        print(p2.name)
        print(p3.name)
        print(p4.name)
        print(p5.name)
        print(p6.name)
        print(p7.name)
        print(p8.name)
        print(p9.name)
        playertable = [p1, p2, p3, p4, p5, p6, p7, p8, p9]
        linebreak()
        print("Finally, would you like to have a part in the game? You can take control of your first player (" + p1.name.upper() + ") and influence their decisions in the game.")
        print("This is entirely optional. If you decline, they will make choices randomly.")
        charoverride = input("(Press [Y]ES to override " + p1.name + ".)")
        if charoverride.upper() == "Y" or charoverride.upper() == "YES":
            global playable
            playable = True
            print(p1.name.upper() + " has been overridden.")
        print("Lettuce start the game!")




playertable = [p1, p2, p3, p4, p5, p6, p7, p8, p9]
layout = "R"
roundnum = 1

def shuffleteams():
    # create a table from the players, randomize role
    print("The teams are being scrambled!")
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
    linebreak()
    # Print the new pair/solo arrangements
    print(playertable[0].name + " and " + playertable[1].name + " are together as the Red Pair.")
    print(playertable[2].name + " and " + playertable[3].name + " are together as the Blue Pair.")
    print(playertable[4].name + " and " + playertable[5].name + " are together as the Green Pair.")

    print(playertable[6].name + " is the Red Solo.")
    print(playertable[7].name + " is the Blue Solo.")
    print(playertable[8].name + " is the Green Solo.")
    wait()


def layoutselect():
    global layout
    print("You can choose a layout for the voting.")
    print("Layout A: Red Pair vs. Blue Solo, Blue Pair vs. Green Solo, Green Pair vs. Red Solo")
    print("Layout B: Red Pair vs. Green Solo, Blue Pair vs. Red Solo, Green Pair vs. Blue Solo")
    print("Layout C: The same-colored Pairs and Solos vote against each other.")
    layout = input("Or you can have the game randomly decide. What will you do? (enter [A], [B], [C], [R]ANDOM) ")


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


def voting():
    global layout
    global playertable
    if layout != "A" or layout != "B" or layout != "C" or layout != "R":
        layout = input("That is not a valid input. Please try again. (enter [A], [B], [C], [R]ANDOM) ")
        voting()
    if layout.upper() == "R":
        temp = random.randint(1, 3)
        if temp == 1:
            layout = "A"
        elif temp == 2:
            layout = "B"
        else:
            layout = "C"
    print("The match-ups are:")

    if layout.upper() == "A":
        print(playertable[0].name + " and " + playertable[1].name + " vs. " + playertable[7].name)
        print(playertable[2].name + " and " + playertable[3].name + " vs. " + playertable[8].name)
        print(playertable[4].name + " and " + playertable[5].name + " vs. " + playertable[6].name)
    if layout.upper() == "B":
        print(playertable[0].name + " and " + playertable[1].name + " vs. " + playertable[8].name)
        print(playertable[2].name + " and " + playertable[3].name + " vs. " + playertable[6].name)
        print(playertable[4].name + " and " + playertable[5].name + " vs. " + playertable[7].name)
    if layout.upper() == "C":
        print(playertable[0].name + " and " + playertable[1].name + " vs. " + playertable[6].name)
        print(playertable[2].name + " and " + playertable[3].name + " vs. " + playertable[7].name)
        print(playertable[4].name + " and " + playertable[5].name + " vs. " + playertable[8].name)
    abroller()
    if playable:
        ABVote = input("Here's the big question: Will you Ally or Betray? (Enter [A] or [B]. Invalid inputs will return as Ally.) ")
        if ABVote.upper() == "B":
            print("You have selected BETRAY.")
            p1.vote = "B"
        else:
            print("You have selected ALLY.")
            p1.vote = "A"

        if p1.role == "Red Pair":
            playertable[0].vote = p1.vote
        if p1.role == "Blue Pair":
            playertable[2].vote = p1.vote
        if p1.role == "Green Pair":
            playertable[2].vote = p1.vote
    time.sleep(2)
    print("The results are in! Let's see what happens...")
    wait()
    global roundnum
    time.sleep(1)
    print("AMBIDEX GAAAAAAME!")
    time.sleep(1)
    print("ROUND " + str(roundnum) + "!")
    roundnum = roundnum + 1
    time.sleep(1)
    print("The resultssssss!")
    time.sleep(2)

    #chart time



    # assigning proper players to temp. variables depending on layout choice
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
    # recreating the AB chart from Zero 3
    linebreak()
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
    linebreak()
    if playertable[d].vote == "A" and playertable[f].vote == "A":
        playertable[d].points = playertable[d].points + 2
        playertable[e].points = playertable[e].points + 2
        playertable[f].points = playertable[f].points + 2
        print(playertable[d].role + " and " + playertable[f].role + " both allied. Both parties gain 2 points.")
    elif playertable[d].vote == "A" and playertable[f].vote == "B":
        playertable[d].points = playertable[d].points - 2
        playertable[e].points = playertable[e].points - 2
        playertable[f].points = playertable[f].points+ 3
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
    linebreak()
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
    linebreak()
    wait()
    # quickly display new scores



    print("")
    print(playertable[a].name + ": " + str(playertable[a].points))
    time.sleep(0.15)
    print(playertable[b].name + ": " + str(playertable[b].points))
    time.sleep(0.15)
    print(playertable[c].name + ": " + str(playertable[c].points))
    time.sleep(0.15)
    print(playertable[d].name + ": " + str(playertable[d].points))
    time.sleep(0.15)
    print(playertable[e].name + ": " + str(playertable[e].points))
    time.sleep(0.15)
    print(playertable[f].name + ": " + str(playertable[f].points))
    time.sleep(0.15)
    print(playertable[g].name + ": " + str(playertable[g].points))
    time.sleep(0.15)
    print(playertable[h].name + ": " + str(playertable[h].points))
    time.sleep(0.15)
    print(playertable[i].name + ": " + str(playertable[i].points))
    time.sleep(0.15)
    wait()

def winCheck():
        for x in range(0,9):
            if playertable[x].points <= 0:
                if playertable[x].alive:
                    playertable[x].kill()
                if playable:
                    if not p1.alive:
                        print("You died! Better luck next time.")
        for x in range(0, 9):
            if playertable[x].points >= 9:
                playertable[x].won = True
                print(playertable[x].name + " has " + str(playertable[x].points) + " points, and leaves the facility.")


        for x in range (0,9):
            if playertable[x].won:
                # gamelog.close()
                exit()

                # TODO: Write the whole simulation to the log when the game is won



def main():
        shuffleteams()
        linebreak()
        layoutselect()
        linebreak()
        voting()
        linebreak()
        if not winCheck():
            main()



setup()

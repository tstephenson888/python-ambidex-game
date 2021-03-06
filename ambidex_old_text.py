import os
import random
import time
import datetime
import sys

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
deathmessage = [" is no longer with us.",
                " stopped breathing.", " perished.", " isn't coming back from that.",
                " is in a better place now.",
                " forgot to write their will.", " welcomed Death with open arms.", " expired."]
log = open("ambidex_log_" + str(datetime.date.today()) + "_" + str(random.randint(0,99999)) + ".txt","w+")
log.write("Ambidex Game Log: " + str(datetime.datetime.now()) + "\n\n")
playable = False

def wait():

    input("Press any key to continue.")

def linebreak():
    print("--------------------------")
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


        log.write("Participants:\n" + playertable[0].name + ", " + playertable[1].name + ", " + playertable[2].name + ", "
          + playertable[3].name + ", " + playertable[4].name + ", " + playertable[5].name + ", " + playertable[6].name
          + ", " + playertable[7].name + ", " + playertable[8].name + ".\n\n")
        linebreak()
        print("Finally, would you like to have a part in the game? You can take control of your first player (" + p1.name + ") and influence their decisions in the game.")
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
    log.write("Team Shuffle:\n\n")
    random.shuffle(playertable)
    playertable[0].role = "Red Pair"
    playertable[1].role = "Red Pair"
    log.write(playertable[0].role + ": " + playertable[0].name + " & " +  playertable[1].name + '\n')

    playertable[2].role = "Blue Pair"
    playertable[3].role = "Blue Pair"
    log.write(playertable[2].role + ": " + playertable[2].name + " & " + playertable[3].name + '\n')

    playertable[4].role = "Green Pair"
    playertable[5].role = "Green Pair"
    log.write(playertable[4].role + ": " + playertable[4].name + " & " + playertable[5].name + '\n')

    playertable[6].role = "Red Solo"
    log.write(playertable[6].role + ": " + playertable[6].name + '\n')
    playertable[7].role = "Blue Solo"
    log.write(playertable[7].role + ": " + playertable[7].name + '\n')
    playertable[8].role = "Green Solo"
    log.write(playertable[8].role + ": " + playertable[8].name + '\n')
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
    log.write("=== Round " + str(roundnum) + " ===\n\n")
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
    global playable
    if layout != "A" and layout != "B" and layout != "C" and layout != "R":
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
            playertable[4].vote = p1.vote
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
        log.write(
            playertable[a].role + "'s team and " + playertable[c].role + " both allied. Both parties gain 2 points.\n")
    elif playertable[a].vote == "A" and playertable[c].vote == "B":
        playertable[a].points = playertable[a].points - 2
        playertable[b].points = playertable[b].points - 2
        playertable[c].points = playertable[c].points + 3
        print(playertable[a].role + " allied while " + playertable[c].role + " betrayed. " + playertable[a].role + " loses 2 points while " + playertable[c].role + " gains 3.")
        log.write(playertable[a].role + "'s team allied while " + playertable[c].role + " betrayed. " + playertable[
            a].role + "'s team loses 2 points while " + playertable[c].role + " gains 3.\n")
    elif playertable[a].vote == "B" and playertable[c].vote == "A":
        playertable[a].points = playertable[a].points + 3
        playertable[b].points = playertable[b].points + 3
        playertable[c].points = playertable[c].points - 2
        print(playertable[c].role + " allied while " + playertable[a].role + " betrayed. " + playertable[c].role + " loses 2 points while " + playertable[a].role + " gains 3.")
        log.write(playertable[c].role + " allied while " + playertable[a].role + "'s team betrayed. " + playertable[
            c].role + " loses 2 points while " + playertable[a].role + "'s team gains 3.\n")
    else:
        print(playertable[a].role + " and " + playertable[c].role + " both betrayed each other. Nothing happened with their scores.")
        log.write(playertable[a].role + " and " + playertable[
            c].role + " both betrayed each other. Nothing happened with their scores.\n")
    time.sleep(2)
    linebreak()
    if playertable[d].vote == "A" and playertable[f].vote == "A":
        playertable[d].points = playertable[d].points + 2
        playertable[e].points = playertable[e].points + 2
        playertable[f].points = playertable[f].points + 2
        print(playertable[d].role + " and " + playertable[f].role + " both allied. Both parties gain 2 points.")
        log.write(
            playertable[d].role + "'s team and " + playertable[f].role + " both allied. Both parties gain 2 points.\n")
    elif playertable[d].vote == "A" and playertable[f].vote == "B":
        playertable[d].points = playertable[d].points - 2
        playertable[e].points = playertable[e].points - 2
        playertable[f].points = playertable[f].points + 3
        print(playertable[d].role + " allied while " + playertable[f].role + " betrayed. " + playertable[
            a].role + " loses 2 points while " + playertable[f].role + " gains 3.")
        log.write(playertable[d].role + "'s team allied while " + playertable[f].role + " betrayed. " + playertable[
            d].role + "'s team loses 2 points while " + playertable[f].role + " gains 3.\n")
    elif playertable[d].vote == "B" and playertable[f].vote == "A":
        playertable[d].points = playertable[d].points + 3
        playertable[e].points = playertable[e].points + 3
        playertable[f].points = playertable[f].points - 2
        print(playertable[f].role + " allied while " + playertable[d].role + " betrayed. " + playertable[
            c].role + " loses 2 points while " + playertable[d].role + " gains 3.")
        log.write(playertable[f].role + " allied while " + playertable[d].role + "'s team betrayed. " + playertable[
            c].role + " loses 2 points while " + playertable[d].role + "'s team gains 3.\n")
    else:
        print(playertable[d].role + " and " + playertable[f].role + " both betrayed each other. Nothing happened with their scores.")
        log.write(playertable[d].role + "'s team and " + playertable[
            f].role + " both betrayed each other. Nothing happened with their scores.\n")
    time.sleep(2)
    linebreak()
    if playertable[g].vote == "A" and playertable[i].vote == "A":
        playertable[g].points = playertable[g].points + 2
        playertable[h].points = playertable[h].points + 2
        playertable[i].points = playertable[i].points + 2
        print(playertable[g].role + " and " + playertable[i].role + " both allied. Both parties gain 2 points.")
        log.write(
            playertable[g].role + "'s team and " + playertable[i].role + " both allied. Both parties gain 2 points.\n")
    elif playertable[g].vote == "A" and playertable[i].vote == "B":
        playertable[g].points = playertable[g].points - 2
        playertable[h].points = playertable[h].points - 2
        playertable[i].points = playertable[i].points + 3
        print(playertable[g].role + " allied while " + playertable[i].role + " betrayed. " + playertable[g].role + " loses 2 points while " + playertable[i].role + " gains 3.")
        log.write(playertable[g].role + "'s team allied while " + playertable[i].role + " betrayed. " + playertable[
            g].role + " loses 2 points while " + playertable[i].role + " gains 3.\n")
    elif playertable[g].vote == "B" and playertable[i].vote == "A":
        playertable[g].points = playertable[g].points + 3
        playertable[h].points = playertable[h].points + 3
        playertable[i].points = playertable[i].points - 2
        print(playertable[i].role + " allied while " + playertable[g].role + " betrayed. " + playertable[i].role + " loses 2 points while " + playertable[g].role + " gains 3.")
        log.write(playertable[i].role + " allied while " + playertable[g].role + "'s team betrayed. " + playertable[
            i].role + " loses 2 points while " + playertable[g].role + "'s team gains 3.\n")
    else:
        print(playertable[g].role + " and " + playertable[i].role + " both betrayed each other. Nothing happened with their scores.")
        log.write(playertable[g].role + "'s team and " + playertable[
            i].role + " both betrayed each other. Nothing happened with their scores.\n")
    linebreak()
    wait()
    # quickly display new scores



    print("")
    log.write("Points Update:\n\n")
    for x in range(9):
        log.write(playertable[x].name + ": " + str(playertable[x].points) + "\n")
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
                    log.write(playertable[x].name + random.choice(deathmessage) + "\n")
                    playertable[x].kill()
                if playable:
                    if not p1.alive:
                        print("You died! Better luck next time...")
                        wait()
                        quit()
        for x in range(0, 9):
            if playertable[x].points >= 9:
                playertable[x].won = True
                print(playertable[x].name + " has " + str(playertable[x].points) + " points, and leaves the facility.")
                log.write(playertable[x].name + " won the game!\n")


        for x in range (0,9):
            if playertable[x].won:

                log.close()
                exit()

                # TODO: Write the whole simulation to the log when the game is won



def main():
    shuffleteams()
    linebreak()
    layoutselect()
    linebreak()
    voting()
    linebreak()
    winCheck()

intro()
while not winCheck():
    main()


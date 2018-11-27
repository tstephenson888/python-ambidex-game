screen = pg.display.set_mode((1000, 750))
    tablebg = pg.image.load("PLATES/blankchart" + layout + ".png")
    bg = tablebg
    roundtitle = pg.image.load(("PLATES/r" + str(roundnum) + ".png"))
    keepGoing = True
    clock = pg.time.Clock()
    while keepGoing:
        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                keepGoing = False
        screen.blit(bg, (0, 0))
        screen.blit(roundtitle, (400, 120))
        initial_offset = 150
        for x in range (0,9):
            if os.path.isfile("PLATES/nameplates/" + playertable[x].name + ".png"):
                plate_exists = pg.image.load(("PLATES/nameplates/" + playertable[x].name + ".png"))
                screen.blit(plate_exists, (initial_offset + (100 * x) + 75, 345))
                plate_exists = pg.image.load(("PLATES/nameplates/" + playertable[x].name + ".png"))
            else:
                customplate = pg.image.load(("PLATES/nameplates/Custom " + str((x + 1)) + ".png"))
                screen.blit(customplate, (initial_offset + (100 * x) + 25, 345))
            pointplate = pg.image.load(("PLATES/numbers/" + str(playertable[x].points) + ".png"))
            if not playertable[x].alive:
                pointplate = pg.image.load(("PLATES/numbers/dead.png"))
            screen.blit(pointplate, (100 + (80 * x) + 100, 400))
    #end chart init
            time.sleep(2)








    # Slowly show what each party voted for w/ sound
    #These are for Ally/Betray
    voteplate1 = pg.image.load("PLATES/numbers/" + playertable[0].vote + ".png", (200,465))
    voteplate2 = pg.image.load("PLATES/numbers/" + playertable[2].vote + ".png", (500,465))
    voteplate3 = pg.image.load("PLATES/numbers/" + playertable[4].vote + ".png", (800,465))
    voteplate4 = pg.image.load("PLATES/numbers/" + playertable[6].vote + ".png")
    voteplate5 = pg.image.load("PLATES/numbers/" + playertable[7].vote + ".png")
    voteplate6 = pg.image.load("PLATES/numbers/" + playertable[8].vote + ".png")
    vplategroup =  pg.sprite.Group[voteplate1, voteplate2, voteplate3,voteplate4,voteplate5,voteplate6]
    screen.blit(vplategroup)


    # Stinger sound!!

    # Quickly show the change in scores in a "sweeping motion"
    #These are for the change in scores
    cplate1 = pg.image.load("PLATES/numbers/" + playertable[4].vote + ".png", (200,465))

    # Hold it...

    pg.display.flip()
    # Save the picture
    pg.image.save(bg, "ABGAME_TABLE_" + datetime.now + ".png")
    time.sleep(5)

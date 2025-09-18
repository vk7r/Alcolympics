import random
import time
import turtle

# STÄNG EJ AV TURTLE GRAPHICS FÖNSTRET NÄR DET ÄR VÄL SKAPAT. KRASHAR ISF.


# Vad har jag gjort
# Vad är denna skapelse
# Mer tecken än i Bibeln

# Spaghetti Carbonara

# Bara inte röra och köra

#----------------------------------------------------------------------------

# Funktioner
def print_centre(str):
    print(str.center(118))

def menu():
    print_centre("╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩ MENU ╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩ \n")
    print_centre("Spel:\n")
    print_centre("1: RNG-Turtles (BUGGED)\n")
    print_centre("2: Över eller Under\n")
    print_centre("3: TärningsProfeten\n")
    print_centre("4: Röd eller Svart\n")
    print_centre("5: Sköldpaddornas Race\n")
    print_centre("6: Wheel of Bärka\n")
    print_centre("7: Bärka Bussen\n")
    print_centre("╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩\n")
    print_centre("Annat:\n")
    print_centre("s: Stats (Klunk-Listor)\n")
    print_centre("i: info om spel (straff / reward)\n")
    print_centre("q: EXIT\n")
    decision = input(" Vad vill du göra?: ")
    while decision not in ["1","2","3","4","5","6","7","i","s","q"]:
        print(" Fel input, försök igen: ")
        decision = input(" Vad vill du göra?: ")

   
    return decision

def show_stats(drink_give, drink_take):
    print(" KLUNKAR ATT GE UT:")
    for player in drink_give:
        print(f' {player}: {drink_give[player]} st')
    print("\n KLUNKAR ATT SKA DRICKA: ")
    for player in drink_take:
        print(f' {player}: {drink_take[player]} st')
        #print('{0:1}:{1:>8}'.format(player, drink_take[player])) # inte ideal, fixa bättre lineup
    print()

def standby_turtle_screen():
    #turtles
    standby_turtle = turtle.Turtle()
    legend_turtle = turtle.Turtle()

    #standby turtle movement
    standby_turtle.speed("fastest")
    standby_turtle.hideturtle()
    standby_turtle.penup()
    standby_turtle.goto(-175,-25)
    standby_turtle.pensize(10)
    standby_turtle.pendown()

    #legend turtle movement
    legend_turtle.speed("fastest")
    legend_turtle.hideturtle()
    legend_turtle.fillcolor("red")
    legend_turtle.color("red")
    legend_turtle.penup()
    legend_turtle.goto(-465,-390)
    legend_turtle.pendown()
    
    #text
    standby_turtle.write("STANDBY", font=("Arial",50 , "normal"))

    legend_turtle.write('Om man heter Viktor får man ge ut 50 klunkar', font=("Arial",10 , "normal"))

def enter_to_continue():
    x = input(' press "ENTER" to Continue ')
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    return x

def games_info():
    print("\n\n\n\n")
    print_centre("RNG-Turtles:\nFörsta Plats = Ge ut 3 Klunkar\nAndra Plats = Ge ut 2 Klunkar\nTredje Plats = Ge ut 1 Klunk\n\
            \nÖver eller Under:\nRätt = Ge ut 1 Klunk\nFel = Drik 1 Klunk\n\nTärningsprofeten:\nGissa Rätt = Ge ut 5 Klunkar!\
            \n\nRöd eller Svart:\nGissa rätt = Ge ut 1 Klunk\nGissa Fel = Drick 1 Klunk\n\
            \nSköldpaddornas Race:\nGissa Rätt = Ge ut 5 Klunkar\n\nWheel of bärka:\nRöd = ?\nGrön = ?\nBlå = ?\nGul = ?\nRosa = ?\n\
            ")
    print()


# GAMES:


def RNGturtles(spelar_lista, drink_give):
    """ hur många gånger kommer sköldpaddorna korsa varandra? Betta närmast och slipp straff """
    # #1 = ge ut 3 klunkar
    # #2 = ge ut 2 klunkar
    # #3 = ge ut 1 klunk


    # Fixa lika många poäng om lika stort steg ifrån siffra

    #import turtle

    print("------------------------------RNG-Turtles------------------------------\n")

    print("Max antal krockar är 1000")

    bet_dict = {}
    
    for player in spelar_lista:
        ask = True
        while ask:
            try:
                print(player,",", end="")
                bet = int(input(" Hur många gånger krockar sköldpaddorna?: "))
                
                unique = False
                if bet in bet_dict.values():
                    unique = True
                while unique:
                    print("\nfel input, du måste välja ett unikt nummer")
                    print(player,",", end="")
                    bet = int(input(" Hur många gånger krockar sköldpaddorna?: "))
                    if bet not in bet_dict.values():
                        unique = False
                        
                bet_dict[player] = bet
                ask = False
            except:
                print("felaktig input, försök igen: ")
            
    print("\n", bet_dict)

    def rectangle(x, y, w, h, c):
        t = make_turtle(x, y, c)
        t.speed(0)
        t.hideturtle()
        t.color('black')
        t.fillcolor(c)
        t.begin_fill()
        for x in [w, h, w, h]:
            t.forward(x)
            t.left(90)
        t.end_fill()

    def jump(t, x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()

    def make_turtle(x, y, c):
        t = turtle.Turtle()
        turtle.delay(0)
        t.color(c)
        jump(t, x, y)
        return t

    def move_random(t):
        t.left(random.randint(-45, 45))
        t.forward(random.randint(0, 25))
        if abs(t.xcor()) > 250 or abs(t.ycor()) > 250:
            t.setheading(t.towards(0,0))

    rectangle(-500,-500,1000,1000,"White")
    rectangle(-250, -250, 500, 500, 'turquoise')

    t = make_turtle((random.randint(-250, 250)), (random.randint(-250, 250)),
                    'red')
    t2 = make_turtle((random.randint(-250, 250)), (random.randint(-250, 250)),
                    'blue')

    t.shape("turtle")
    t2.shape("turtle")


    L = []
    for x in range(1000):
        #print(x)
        move_random(t)
        move_random(t2)
        if t.distance(t2) < 50:
            t.write('x')
            L.append(1)
    print()

    print(f'{len(L)} Gånger var sköldpaddorna nära varandra!')

    p = make_turtle(-250, -350, 'black')
    p.hideturtle()
    p.speed(0)

    p.write(f' Crashed {len(L)} Times! ', font=("Arial", 50, "normal"))

    crash_count = len(L)
    
    step_lst = []
    for player in bet_dict:
        player_val = bet_dict[player]
        steps_from_crash_count = abs(crash_count - player_val)
        step_lst.append([steps_from_crash_count, player])

    step_lst = sorted(step_lst)


    ranking = {}
    for x in range(len(step_lst)):
        if step_lst[x][0] in ranking:
            ranking[step_lst[x][0]] += [step_lst[x][1]]
        else:
            ranking[step_lst[x][0]] = [step_lst[x][1]]

    rank = 1
    for key in ranking:
        if len(ranking[key]) > 1: 
            print(f' #{rank}, {ranking[key][0]} och {ranking[key][1]} med {key} steg ifrån!')
            if rank == 1:
                drink_give[ranking[key][0]] += 3
                drink_give[ranking[key][1]] += 3
            if rank == 2:
                drink_give[ranking[key][0]] += 2
                drink_give[ranking[key][1]] += 2
            if rank == 3:
                drink_give[ranking[key][0]] += 1
                drink_give[ranking[key][1]] += 1
        else:
            print(f' #{rank}, {ranking[key][0]} med {key} steg ifrån!')
            if rank == 1:
                drink_give[ranking[key][0]] += 3
            if rank == 2:
                drink_give[ranking[key][0]] += 2
            if rank == 3:
                drink_give[ranking[key][0]] += 1
        
        rank += 1

    # Printa Ranking sidan om kvadraten
    rt = make_turtle(-450, 100, 'black')
    rt.hideturtle()
    rt.speed(0)

    placement2 = 1
    c = 50
    for key in ranking:
        if len(ranking[key]) > 1:
            rt.write(f'#{placement2}: {ranking[key][0]} och {ranking[key][1]}', font=("Arial", 25, "normal"))
            rt.penup()
            rt.goto(-450, 100 - c)
            rt.pendown()
            c += 50
            placement2 += 1
        else:
            rt.write(f'#{placement2}: {ranking[key][0]}', font=("Arial", 25, "normal"))
            rt.penup()
            rt.goto(-450, 100 - c)
            rt.pendown()
            c += 50
            placement2 += 1
    print()

    return drink_give

def ÖverUnder(spelar_lista, drink_give, drink_take):
    """ Få ett nummer, gissa om nästa kommer bli högre eller lägre """
    # gissa rätt (u/ö) = ge ut 1 klunk
    # Gissa fel (u/ö/s) = drink 1 klunk
    # Gissa rätt med "samma" = ge ut 4 klunkar

    print_centre("------------------------------Över eller Under------------------------------\n")
    print_centre("SPELET SLUTAR NÄR 5 KLUNAR ÄR UTDELADE\n\n")

    klunkar = 0
    current_value = random.choice(["2","3","4","5","6","7","8","9","10","11","12","13","14"])
    while klunkar < 5:
        for player in spelar_lista:
            next_value = random.choice(["1","2","3","4","5","6","7","8","9","10","11","12","13"])
            if current_value in ["11","12","13","1"]:
                if current_value == "11":
                    print(f'Nuvarande Nummer: {"Knekt"}\n')
                elif current_value == "12":
                    print(f'Nuvarande Nummer: {"Dam"}\n')
                elif current_value == "13":
                    print(f'Nuvarande Nummer: {"Kung"}\n')
                elif current_value == "1":
                    print(f'Nuvarande Nummer: {"Ess"}\n')
            else:
                print(f'Nuvarande Nummer: {current_value}\n')
            print(f'{player}, ',end="")
            ans = input("Över under eller samma?:(ö/u/s) ")
            print()
            ans = ans.lower()
            while ans not in ["ö","u","s"]:
                print_centre("fel input, försök igen: ")
                ans = input("Över, Under eller Samma?:(ö/u/s) ")
            print_centre("Nästa kort är...\n")
            time.sleep(0.5)
            if next_value in ["11","12","13","1"]:
                if next_value == "11":
                    print_centre(f'{"Knekt"}\n')
                elif next_value == "12":
                    print_centre(f'{"Dam"}\n')
                elif next_value == "13":
                    print_centre(f'{"Kung"}\n')
                elif next_value == "1":
                    print_centre(f'{"Ess"}\n')
            else:
                print_centre(next_value)
            time.sleep(0.5)
            print()

            if current_value == next_value:
                result = "s"
            elif int(next_value) > int(current_value):
                result = "ö"
            elif int(next_value) < int(current_value):
                result = "u"

            if ans == result:
                print_centre("Rätt!")
                print("\n\n")
                if ans == "s":
                    drink_give[player] += 4
                elif ans == "ö":
                    drink_give[player] += 1
                elif ans == "u":
                    drink_give[player] += 1

                time.sleep(0.5)
            elif ans != result:
                print_centre("Fel!")
                print("\n\n")
                drink_take[player] += 1
                klunkar += 1
                time.sleep(0.5)
                

            if klunkar == 5:
                print_centre(f"Nu har {klunkar} klunkar Utdelats. Game Over") 
                break

            current_value = next_value
    
    print()
    return drink_give, drink_take

def TärningsProfeten(spelar_lista, drink_give):
    """ gissa rätt på tärningsnumret från 1-10, om du gör ge ut x klunk """

    # gissa rätt och ge ut 5 klunkar

    print_centre("------------------------------TärningsProfeten------------------------------\n")

    print_centre("Gissa rätt nummer mellan 1-10 och ge ut 5 Klunkar!!!\n")

    for player in spelar_lista:
        r_val = random.randint(1,10)
        ask = True
        while ask:
            try:
                print(player,",", end="")
                ans = int(input("Gissa på ett tal inom intervallet 1-10: "))
                print()
                ask = False
            except:
                print("felaktig input, försök igen: ")


        time.sleep(0.5)

        if ans == r_val:
            print_centre(f'Rätt, tärningen slog en {r_val}:a!\n')
            drink_give[player] += 5
        elif ans != r_val:
            print_centre(f'Fel! Tärningen slog en {r_val}:a  :(\n')

    return drink_give

def RedBlack(spelar_lista, drink_give, drink_take):
    """ är nästa kort rött eller svart?? """

    # gissa rätt och ge ut 1 klunk
    # gissa fel och drink 1 klunk


    print("\n\n\n\n\n\n\n\n")
    print_centre("------------------------------Röd eller Svart------------------------------\n")
    print("\n\n\n\n")

    colors = ["RÖD", "SVART"]

    current_color = random.choice(colors)

    for player in spelar_lista:
        print_centre("Nuvarande Färg:")
        print()
        print_centre(current_color)
        next_color = random.choice(colors)
        print(player,", ", end="")
        ans = input("Är nästa kort Röd eller Svart? (r/s): ")
        while ans not in ["r", "s"]:
            print("fel input, försök igen:")
            ans = input("Är nästa kort Röd eller Svart?: (r/s)")
        ans = ans.lower()
        print_centre(".  ")
        time.sleep(0.5)    
        print_centre(".. ")
        time.sleep(0.5)        
        print_centre("...")
        time.sleep(0.5)
        print()
        print_centre(next_color)
        time.sleep(0.7)
        print()

        if next_color == "RÖD":
            res = "r"
        elif next_color == "SVART":
            res = "s"

        if ans == res:
            print_centre("Rätt Färg!")
            print("\n\n\n")
            drink_give[player] += 1
        elif ans != res:
            print_centre("Fel Färg!")
            print("\n\n\n")
            drink_take[player] += 1

        current_color = next_color
        input("-->")
        time.sleep(0.1)
 
    print()

    return drink_give, drink_take

# Kanske fixa så att sköldpaddorna går i en uppåtgående sinuskurva med random frekvens och slumpmässig "t.forward(x)"
def SnailRace(spelar_lista, drink_give):

    print_centre("------------------------------SKÖLDPADDORNAS RACE------------------------------\n")

    print_centre("GISSA RÄTT PÅ VINNANDE SKÖLDPADDA OCH GE UT 5 KLUNKAR")
    
    #import turtle

    
    # Betting Phase:
    bet_dict = {}
    
    
    # Man skulle kunna lägga till att den kontrollerar i loopen att samma siffra ej uppstår (för della ger ett fel)
    for player in spelar_lista:
        ask = True
        while ask:
            try:
                print()
                print(" Sköldpaddor:\n Röd (r)\n Blå (b)\n Grön (g)\n Lila (l)\n Gul (gu)\n Brun (br)")
                print(player,",", end="")
                bet = input(" Vilken Sköldpadda vinner racet?: ")
                bet = bet.lower()
                
                while bet not in ["r","b","g","l","gu","br"]:
                    print("felaktig input, försök igen:")
                    bet = input(" Vilken Sköldpadda vinner racet?: ")
                    bet = bet.lower()
                
                if bet == "r":
                    bet = "Röd"
                elif bet == "b":
                    bet = "Blå"
                elif bet == "g":
                    bet = "Grön"
                elif bet == "l":
                    bet = "Lila"
                elif bet == "gu":
                    bet = "Gul"
                elif bet == "br":
                    bet = "Brun"

                bet_dict[player] = bet
                ask = False
            except:
                print("felaktig input, försök igen: ")
            
    print(bet_dict)
    print()

    def jump(t, x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()

    def make_turtle(x, y, c):
        t = turtle.Turtle()
        turtle.delay(0)
        t.color(c)
        jump(t, x, y)
        return t

    def rectangle(x, y, w, h, c):
        t = make_turtle(x, y, c)
        t.speed(0)
        t.hideturtle()
        t.color('black')
        t.fillcolor(c)
        t.begin_fill()
        for x in [w, h, w, h]:
            t.forward(x)
            t.left(90)
        t.end_fill()

    rectangle(-500,-500,1000,1000,"lightgreen" )

    # Finish Line:
    Fin_line = make_turtle(300,250,"red")
    Fin_line.pensize(5)
    Fin_line.hideturtle()
    Fin_line.left(180)
    Fin_line.forward(600)
    # Text
    Fin_line.penup()
    Fin_line.left(180)
    Fin_line.forward(228)
    Fin_line.left(90)
    Fin_line.forward(25)
    Fin_line.pendown()
    Fin_line.color("Black")
    Fin_line.write("MÅL", font=("Arial", 50, "normal"))

    # Start Line:
    Start_line = make_turtle(-300, -250, "Black")
    Start_line.hideturtle()
    Start_line.pensize(5)
    Start_line.forward(600)
    # Text
    Start_line.penup()
    Start_line.left(180)
    Start_line.forward(420)
    Start_line.left(90)
    Start_line.forward(100)
    Start_line.pendown()
    Start_line.color("Black")
    Start_line.write("START", font=("Arial", 50, "normal"))

    #Snails
    s1 = make_turtle(-250,-250, "Red")
    s2 = make_turtle(-150,-250, "Blue")
    s3 = make_turtle(-50,-250, "Green")
    s4 = make_turtle(50,-250, "VioletRed")
    s5 = make_turtle(150,-250, "yellow1")
    s6 = make_turtle(250,-250, "SaddleBrown")

    snail_lst = [s1,s2,s3,s4,s5,s6]
    original_xpos = {s1:-250, s2:-150, s3:-50, s4:50, s5:150, s6:250}

    for snail in snail_lst:
        snail.shape("turtle")
        snail.speed(0.1)
        snail.left(90)


    rank_dict = {}
    time_lst = []
    step_round = 0
    race_live = True
    while race_live:
        for snail2 in snail_lst:
            if snail2 in rank_dict.values():
                continue
            elif snail2.ycor() >= 250:
                if step_round not in rank_dict:
                    rank_dict[step_round] = snail2
                    snail2.write(f'GG',font=("Arial", 10, "normal"))
                    time_lst.append(step_round) 
                elif step_round in rank_dict:
                    rank_dict[step_round+1] = snail2
                    snail2.write(f'GG',font=("Arial", 10, "normal"))
                    time_lst.append(step_round+1)  
            elif snail2.ycor() < 250:
                snail2.forward(random.randint(0,15))

                if snail2.xcor() < (original_xpos[snail2] - 15): #Om snigeln är för långt till L gå R
                        snail2.right(10)
                        snail2.forward(1)
                if snail2.xcor() > (original_xpos[snail2] + 15): #Om snigeln är för långt till R gå L
                        snail2.left(10)
                        snail2.forward(1)

                random_dir = random.choice(["L","R"])
                random_dir_val = random.randint(0,3)
                if random_dir == "L":
                    snail2.left(random_dir_val)
                elif random_dir == "R":
                    snail2.right(random_dir_val)

                

        step_round += 1
        if len(rank_dict) == 6:
            race_live = False
        time.sleep(0.23)


    object_repr = {s1 : "Röd", s2 : "Blå", s3 : "Grön",
    s4 : "Lila", s5 : "Gul", s6 : "Brun"}

    winner = []
    final_rank_lst = []
    rank_turtle = make_turtle(-450,50,"black")
    rank_turtle.left(270)
    rank_turtle.hideturtle()
    nplacement = 1
    for time1 in rank_dict:
        print(f'#{nplacement}, {object_repr[rank_dict[time1]]}')
        rank_turtle.write(f'#{nplacement}, {object_repr[rank_dict[time1]]}',font=("Arial", 20, "normal"))
        final_rank_lst.append([object_repr[rank_dict[time1]], nplacement])
        rank_turtle.penup()
        rank_turtle.forward(30)
        rank_turtle.pendown
        if nplacement == 1:
            winner.append(object_repr[rank_dict[time1]])
        nplacement += 1

    rank_turtle.color("Orange")
    for player in playerlist:
        if bet_dict[player] == winner[0]:
            drink_give[player] += 5
            rank_turtle.write(f'Grattis {player}!',font=("Arial", 20, "normal"))
            rank_turtle.penup()
            rank_turtle.forward(30)
            rank_turtle.pendown

    print()

    return drink_give



    print_centre("------------------------------WHEEL OF BÄRKA------------------------------\n")

    def jump(t,x,y):
        t.penup()
        t.goto(x,y)
        t.pendown()
    
    def make_turtle(x, y, c):
        t = turtle.Turtle()
        turtle.delay(0)
        t.color(c)
        jump(t, x, y)
        return t

    def rectangle(x, y, w, h, c):
        t = make_turtle(x, y, c)
        t.speed(0)
        t.hideturtle()
        t.color('black')
        t.fillcolor(c)
        t.begin_fill()
        for x in [w, h, w, h]:
            t.forward(x)
            t.left(90)
        t.end_fill()
    
    def pizza_slice(t, r, v, color_lst):
        color_lst_copy = color_lst

        t.setheading(90)
        recent_heading = 180
        recent_position = (0,300)
        for x in range(5):
            t.fillcolor(color_lst_copy[x])
            t.begin_fill()
            t.goto(recent_position)
            t.setheading(recent_heading)
            t.circle(r,v)
            recent_heading = t.heading() # Snapshot of angle
            recent_position = t.pos() # Snapshot of pos
            t.goto(0,0)
            t.end_fill()

    #--------------------------------------------------------------------------

    # Vem vill snurra hjulet och riskera få eller ge ut klunkar?

    player_number = 1
    print(" Vem ska snurra The Wheel of Bärka? ")
    for player in spelar_lista:
        print(f'{player_number}: {player}')
        player_number += 1

    ask = True
    while ask:
        try:
            chosen_player = int(input("skriv numret på den valda spelaren: "))
            while chosen_player not in range(1,len(spelar_lista)+1):
                print("invalid input. try again")
                chosen_player = int(input("skriv numret på den valda spelaren: "))
            for index in range(len(spelar_lista)+1):
                if index == chosen_player:
                    confirmed_player = spelar_lista[index-1] # Detta är spelaren som kommer snurra hjulet
                
                ask = False
        except:
            print("felaktig input, försök igen: ")    
    
        rectangle(-500,-500,1000,1000,"White")

    print()
    print(f'{confirmed_player} Snurrar och får...')


    # Text på den som snurrar hjulet
    player_name_turtle = turtle.Turtle()
    player_name_turtle.hideturtle()
    player_name_turtle.pensize(10)

    # loop som ser till att texten med namnet centreras
    char_widht = 0
    for j in range(len(confirmed_player)):
        jump(player_name_turtle, -25 + char_widht, 315)
        char_widht = char_widht - 15
    player_name_turtle.write(f'{confirmed_player}', font=("Comic Sans MS",50,"normal"))

    # Hjul
    wheel_turtle = turtle.Turtle() # Skapa sköldpadda som skapar hjulet
    wheel_turtle.hideturtle()
    wheel_turtle.speed("fastest")
    wheel_turtle.pensize(10) # Storlek på penna

    color_lst = ["SteelBlue1","Yellow","SpringGreen","Red","VioletRed1"]
    pizza_slice(wheel_turtle,300,72, color_lst)

    # Rörande Boll
    decision_ball = turtle.Turtle()
    decision_ball.hideturtle()
    decision_ball.speed("fastest")
    decision_ball.color("black", "azure4")
    decision_ball.shape("circle")

    decision_ball.setheading(180)
    jump(decision_ball, 0, 150)

    decision_ball.showturtle()
    decision_ball.penup()

    # Iterationer
    random_range = random.randint(100,200)
    for x in range(random_range):
        decision_ball.circle(150, random.uniform(0.1, 360))

    
    speed = 30
    friction = 0
    while friction <= 30:
        decision_ball.circle(150, (speed - friction))
        friction += 0.1
    for y in range(100):
        decision_ball.circle(150, 0.1)

    # kolla om decision ball är nära given pos
    blå_pos = (-176.34,242.71)
    gul_pos = (-285.32,-92.71)
    grön_pos = (0.00,-300.00)
    röd_pos = (285.32,-92.71)
    rosa_pos = (176.34,242.71)

    pos_lst = [blå_pos, gul_pos, grön_pos, röd_pos, rosa_pos]

    final_clr_str = ["Blå", "Gul", "Grön", "Röd", "Rosa"]

    chosen_pos = decision_ball.pos()

    shortest_distance = 1000000
    for color_pos in pos_lst:
        if decision_ball.distance(color_pos) < shortest_distance:
            shortest_distance = decision_ball.distance(color_pos)
            winner_color = color_pos
    

    FINAL_DECISION = "" # Detta är variabeln innehållandes färgen som beslutar straffet
    iterations = 0
    for rep in pos_lst:
        if winner_color == rep:
            print(f'{final_clr_str[iterations]}!')
            FINAL_DECISION = final_clr_str[iterations]
        iterations += 1

    
    if FINAL_DECISION == "Blå":
        drink_give[confirmed_player] += 2
    if FINAL_DECISION == "Gul":
        drink_take[confirmed_player] += 2
    if FINAL_DECISION == "Grön":
        drink_give[confirmed_player] += 1
    if FINAL_DECISION == "Röd":
        drink_take[confirmed_player] += 1
    if FINAL_DECISION == "Rosa":
        drink_take[confirmed_player] += 1

    print()
    return drink_give, drink_take


    # fixa i fallet att den är lika nära 2 färger

    # fixa text på hjulet som visar straffet/rewardet

    # Fixa bättre straff

    # Skriv namnet på spelaren som snurrar i rutan :)

# Istället för klunkar kan man ge ett direktiv som straff. kanske att man måste spela ngt straff spel
def Wheel_of_Bärka(spelar_lista, drink_give, drink_take):

    print_centre("------------------------------WHEEL OF BÄRKA------------------------------\n")

    def jump(t,x,y):
        t.penup()
        t.goto(x,y)
        t.pendown()
    
    def make_turtle(x, y, c):
        t = turtle.Turtle()
        turtle.delay(0)
        t.color(c)
        jump(t, x, y)
        return t

    def rectangle(x, y, w, h, c):
        t = make_turtle(x, y, c)
        t.speed(0)
        t.hideturtle()
        t.color('black')
        t.fillcolor(c)
        t.begin_fill()
        for x in [w, h, w, h]:
            t.forward(x)
            t.left(90)
        t.end_fill()
    
    def pizza_slice(t, r, v, color_lst):
        color_lst_copy = color_lst

        t.setheading(90)
        recent_heading = 180
        recent_position = (0,300)
        for x in range(5):
            t.fillcolor(color_lst_copy[x])
            t.begin_fill()
            t.goto(recent_position)
            t.setheading(recent_heading)
            t.circle(r,v)
            recent_heading = t.heading() # Snapshot of angle
            recent_position = t.pos() # Snapshot of pos
            t.goto(0,0)
            t.end_fill()

    #--------------------------------------------------------------------------

    # Vem vill snurra hjulet och riskera få eller ge ut klunkar?

    player_number = 1
    print(" Vem ska snurra The Wheel of Bärka? ")
    for player in spelar_lista:
        print(f'{player_number}: {player}')
        player_number += 1

    ask = True
    while ask:
        try:
            chosen_player = int(input("skriv numret på den valda spelaren: "))
            while chosen_player not in range(1,len(spelar_lista)+1):
                print("invalid input. try again")
                chosen_player = int(input("skriv numret på den valda spelaren: "))
            for index in range(len(spelar_lista)+1):
                if index == chosen_player:
                    confirmed_player = spelar_lista[index-1] # Detta är spelaren som kommer snurra hjulet
                
                ask = False
        except:
            print("felaktig input, försök igen: ")    
    
        rectangle(-500,-500,1000,1000,"White")

    print()
    print(f'{confirmed_player} Snurrar och får...')


    # Text på den som snurrar hjulet
    player_name_turtle = turtle.Turtle()
    player_name_turtle.hideturtle()
    player_name_turtle.pensize(10)

    # loop som ser till att texten med namnet centreras
    char_widht = 0
    for j in range(len(confirmed_player)):
        jump(player_name_turtle, -25 + char_widht, 315)
        char_widht = char_widht - 15
    player_name_turtle.write(f'{confirmed_player}', font=("Comic Sans MS",50,"normal"))

    # Hjul
    wheel_turtle = turtle.Turtle() # Skapa sköldpadda som skapar hjulet
    wheel_turtle.hideturtle()
    wheel_turtle.speed("fastest")
    wheel_turtle.pensize(10) # Storlek på penna

    color_lst = ["SteelBlue1","Yellow","SpringGreen","Red","VioletRed1"]
    pizza_slice(wheel_turtle,300,72, color_lst)

     # Sköldpadda som ritar straffen/rewardsen på rutorna
    consequence_display_turtle = turtle.Turtle()
    consequence_display_turtle.hideturtle()
    consequence_display_turtle.penup()
    consequence_display_turtle.goto((-115.17,121.35)) # Blå
    consequence_display_turtle.write("+2", font=("comic sans MS", 30, "normal"))
    consequence_display_turtle.goto((-162.66,-66.35)) # Gul
    consequence_display_turtle.write("-1", font=("comic sans MS", 30, "normal"))
    consequence_display_turtle.goto((-25.00,-160.00)) # Grön
    consequence_display_turtle.write("+1", font=("comic sans MS", 30, "normal"))
    consequence_display_turtle.goto((120.66,-60.35)) # Röd
    consequence_display_turtle.write("Bussen", font=("comic sans MS", 30, "normal"))
    consequence_display_turtle.goto((70,121.35)) # Rosa
    consequence_display_turtle.write("+1", font=("comic sans MS", 30, "normal"))


    # Rörande Boll
    decision_ball = turtle.Turtle()
    decision_ball.hideturtle()
    decision_ball.speed("fastest")
    decision_ball.color("black", "azure4")
    decision_ball.shape("circle")

    decision_ball.setheading(180)
    jump(decision_ball, 0, 150)

    decision_ball.showturtle()
    decision_ball.penup()

    # Iterationer
    random_range = random.randint(100,200)
    for x in range(random_range):
        decision_ball.circle(150, random.uniform(0.1, 360))

    
    speed = 30
    friction = 0
    while friction <= 30:
        decision_ball.circle(150, (speed - friction))
        friction += 0.1
    for y in range(100):
        decision_ball.circle(150, 0.1)

    # kolla om decision ball är nära given pos
    blå_pos = (-176.34,242.71)
    gul_pos = (-285.32,-92.71)
    grön_pos = (0.00,-300.00)
    röd_pos = (285.32,-92.71)
    rosa_pos = (176.34,242.71)

    pos_lst = [blå_pos, gul_pos, grön_pos, röd_pos, rosa_pos]

    final_clr_str = ["Blå", "Gul", "Grön", "Röd", "Rosa"]

    chosen_pos = decision_ball.pos()

    shortest_distance = 1000000
    for color_pos in pos_lst:
        if decision_ball.distance(color_pos) < shortest_distance:
            shortest_distance = decision_ball.distance(color_pos)
            winner_color = color_pos
    

    FINAL_DECISION = "" # Detta är variabeln innehållandes färgen som beslutar straffet
    iterations = 0
    for rep in pos_lst:
        if winner_color == rep:
            print(f'{final_clr_str[iterations]}!')
            FINAL_DECISION = final_clr_str[iterations]
        iterations += 1

    
    if FINAL_DECISION == "Blå":
        drink_give[confirmed_player] += 2
        print(f'{confirmed_player} får ge ut 2 klunkar\n')
    if FINAL_DECISION == "Gul":
        drink_take[confirmed_player] += 1
        print(f'{confirmed_player} får ta 1 klunk\n')
    if FINAL_DECISION == "Grön":
        drink_give[confirmed_player] += 1
        print(f'{confirmed_player} får ge ut 1 klunk\n')
    if FINAL_DECISION == "Röd":
        print("\n\n")
        print(f'{confirmed_player} ska spela bussen!\n')
    if FINAL_DECISION == "Rosa":
        drink_take[confirmed_player] += 1

    print()
    return drink_give, drink_take


    # fixa i fallet att den är lika nära 2 färger

    # fixa text på hjulet som visar straffet/rewardet

    # Fixa bättre straff

    # Skriv namnet på spelaren som snurrar i rutan :)



    print_centre("------------------------------BÄRKA BUSSEN------------------------------\n")

    #FUNKTIONER----------------------
    def jump(t, x, y):
            t.penup()
            t.goto(x, y)
            t.pendown()

    def make_turtle(x, y):
        t = turtle.Turtle()
        turtle.delay(0)
        jump(t, x, y)
        return t

    #CARDS-----------------------

    def blank_card_up(x, y):
        w = 100
        h = 150

        t = make_turtle(x, y)
        t.pensize(5)
        t.speed(0)
        t.hideturtle()
        t.color('black')
        t.fillcolor("White")
        t.begin_fill()
        for x in [w, h, w, h]:
            t.forward(x)
            t.left(90)
        t.end_fill()
        end_pos = t.pos()
        end_heading = t.heading()

        t.penup()
        t.forward(33)
        t.left(90)
        t.forward(35)

        return t

    # Man skulle kunna iterera genom alla istället för att skriva alla.
    def kort_2(x,y):
        t = blank_card_up(x,y)
        t.write("2", font=("Arial",50,"normal"))

    def kort_3(x,y):
        t = blank_card_up(x,y)
        t.write("3", font=("Arial",50,"normal"))

    def kort_4(x,y):
        t = blank_card_up(x,y)
        t.write("4", font=("Arial",50,"normal"))

    def kort_5(x,y):
        t = blank_card_up(x,y)
        t.write("5", font=("Arial",50,"normal"))
        
    def kort_6(x,y):
        t = blank_card_up(x,y)
        t.write("6", font=("Arial",50,"normal"))

    def kort_7(x,y):
        t = blank_card_up(x,y)
        t.write("7", font=("Arial",50,"normal"))

    def kort_8(x,y):
        t = blank_card_up(x,y)
        t.write("8", font=("Arial",50,"normal"))

    def kort_9(x,y):
        t = blank_card_up(x,y)
        t.write("9", font=("Arial",50,"normal"))

    def kort_10(x,y):
        t = blank_card_up(x,y)
        t.left(90)
        t.forward(23)
        t.write("10", font=("Arial",50,"normal"))

    def kort_knekt(x,y):
        t = blank_card_up(x,y)
        t.color("red")
        t.left(90)
        t.forward(23)
        t.write("Kn", font=("Arial",50,"normal"))

    def kort_dam(x,y):
        t = blank_card_up(x,y)
        t.color("red")
        t.left(90)
        t.forward(5)
        t.write("D", font=("Arial",50,"normal"))

    def kort_kung(x,y):
        t = blank_card_up(x,y)
        t.color("red")
        t.left(90)
        t.forward(5)
        t.write("K", font=("Arial",50,"normal"))

    def kort_ess(x,y):
        t = blank_card_up(x,y)
        t.color("red")
        t.left(90)
        t.forward(5)
        t.write("E", font=("Arial",50,"normal"))

    #TURTLE BILDER-----------------------

    def background(x, y, w, h):
            t = make_turtle(x, y)
            t.speed(0)
            t.hideturtle()
            t.color('black')
            t.fillcolor("bisque2")
            t.begin_fill()
            for x in [w, h, w, h]:
                t.forward(x)
                t.left(90)
            t.end_fill()

    def card_face_down(x, y, w, h):
        t = make_turtle(x, y)
        t.pensize(5)
        t.speed(0)
        t.hideturtle()
        t.color('black')
        t.fillcolor("DarkRed")
        t.begin_fill()
        for x in [w, h, w, h]:
            t.forward(x)
            t.left(90)
        t.end_fill()
        end_pos = t.pos()
        end_heading = t.heading()

        t.penup()
        t.forward(33)
        t.left(90)
        t.forward(35)
        t.write("?", font=("Arial",50,"normal"))
        t.goto(end_pos)
        t.setheading(end_heading)

    def turn_card_face_up(random_card, vald_pos):
        x = vald_pos[0]
        y = vald_pos[1]
        if random_card == 1:
            kort_ess(x,y)

        if random_card == 2:
            kort_2(x,y)

        if random_card == 3:
            kort_3(x,y)

        if random_card == 4:
            kort_4(x,y)

        if random_card == 5:
            kort_5(x,y)

        if random_card == 6:
            kort_6(x,y)

        if random_card == 7:
            kort_7(x,y)

        if random_card == 8:
            kort_8(x,y)

        if random_card == 9:
            kort_9(x,y)

        if random_card == 10:
            kort_10(x,y)

        if random_card == 11:
            kort_knekt(x,y)

        if random_card == 12:
            kort_dam(x,y)

        if random_card == 13:
            kort_kung(x,y)

    def start_layout():
        background(-500,-500,1000,1000)

        w = 100
        h = 150

        layer4_start_x = -275
        layer4_start_y = -325

        layer3_start_x = -200
        layer3_start_y = -150

        layer2_start_x = -125
        layer2_start_y = 25

        layer1_start_x = -50
        layer1_start_y = 200

        for x in range(11):
            if x < 4: # layer 4
                card_face_down(layer4_start_x, layer4_start_y, w, h)
                layer4_start_x += w + w/2

            elif 3 < x < 7: # layer 3
                card_face_down(layer3_start_x,layer3_start_y, w, h)
                layer3_start_x += w + w/2

            elif 7 < x < 10: # layer 2
                card_face_down(layer2_start_x, layer2_start_y, w, h)
                layer2_start_x += w + w/2

            elif x == 10: # final layer
                card_face_down(layer1_start_x, layer1_start_y, w, h)

    def layer_pointer(layer, prev_pointer= "none", prev_numbers="none"):
        if prev_pointer != "none":
            prev_pointer.hideturtle()
        if prev_numbers != "none":
            prev_numbers.clear()
        pointer = turtle.Turtle()
        pointer.color("Black")
        pointer.fillcolor("yellow")
        pointer.shapesize(8)
        pointer.penup()

        number_turtle = turtle.Turtle()
        number_turtle.hideturtle()
        number_turtle.penup()

        if layer == 1:
            pointer.goto(-350,-250)

            jump_constant = 0
            number = 1
            for jumps in range(4):
                number_turtle.goto(-225 + jump_constant, -350)
                number_turtle.write(f'{number}',font=("arial","10","normal"))
                jump_constant += 150
                number += 1

        if layer == 2:
            pointer.goto(-250, -75)

            jump_constant = 0
            number = 1
            for jumps in range(3):
                number_turtle.goto(-150 + jump_constant, -175)
                number_turtle.write(f'{number}',font=("arial","10","normal"))
                jump_constant += 150
                number += 1

        if layer == 3:
            pointer.goto(-175, 100)

            jump_constant = 0
            number = 1
            for jumps in range(2):
                number_turtle.goto(-75 + jump_constant, 0)
                number_turtle.write(f'{number}',font=("arial","10","normal"))
                jump_constant += 150
                number += 1    


        if layer == 4:
            pointer.goto(-125, 275)

            jump_constant = 0
            number = 1
            for jumps in range(1):
                number_turtle.goto(0 + jump_constant, 175)
                number_turtle.write(f'{number}',font=("arial","10","normal"))
                jump_constant += 150
                number += 1

        return pointer, number_turtle
    
    
    #------------------------------------------------------------
    # fixa så att alla fyra kort är ngt random value. för just nu är det inte mening med flera kort
    # kanske vid varje iteration göra en dict med position = kort
    if __name__ == "__main__":

        player_number = 1
        print(" Vem ska snurra The Wheel of Bärka? ")
        for player in spelar_lista:
            print(f'{player_number}: {player}')
            player_number += 1

        ask = True
        while ask:
            try:
                chosen_player = int(input("Vem ska köra bussen?: "))
                print()
                while chosen_player not in range(1,len(spelar_lista)+1):
                    print("invalid input. try again")
                    chosen_player = int(input("skriv numret på den valda spelaren: "))
                for index in range(len(spelar_lista)+1):
                    if index == chosen_player:
                        confirmed_player = spelar_lista[index-1] # Detta är spelaren som kommer snurra hjulet
                    
                    ask = False
            except:
                print("felaktig input, försök igen: ")

        visual_klunk_dict = {"klunkar":0}

        # Position på kort, för varje lager
        card_pos_dict_L4 = {"1":(-275,-325), "2":(-125,-325), "3":(25,-325), "4":(175,-325)} # Layer 4
        card_pos_dict_L3 = {"1":(-200,-150), "2":(-50,-150), "3":(100,-150)} # Layer 3
        card_pos_dict_L2 = {"1":(-125,25), "2":(25,25)} # Layer 2
        card_pos_dict_L1 = {"1":(-50 ,200)} # Layer 1, kanske man inte behöver skriva in input för denna

        #card_pos_dict = {"1":(-275,-325), "2":(-125,-325), "3":(25,-325), "4":(175,-325), "5":(-200,-150), "6":(-50,-150), "7":(100,-150), "8":(-125,25), "9":(25,25), "10":(-50 ,200)}

        # Blanda korten på bordet:
        value_list = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        start_layout()

        #Klunk Turtle
        klunk_turtle = turtle.Turtle()
        klunk_turtle.hideturtle()
        klunk_turtle.penup()
        


        # Max 4 rounds
        layer = 1
        buss_status = True
        while buss_status:
            while layer < 5: # runda 1 - 4
                
                klunk_turtle.clear()
                klunk_turtle.goto(-400,325)
                klunk_turtle.write(f'{confirmed_player}s',font=("Arial",40, "normal"))
                klunk_turtle.goto(-400,280)
                klunk_turtle.write(f'Klunkar: {visual_klunk_dict["klunkar"]}',font=("Arial",40, "normal"))

                print("round:",layer)
                current_random_card = random.choice(value_list) # tar fram ett slumpmässigt kort

                if layer == 1: # 1 = lager 4 (yttre lagret)
                    prev_turtle, prev_pointer = layer_pointer(layer) # pekaren. returnerar sköldpaddan så man can cleara den vid ny runda
                    ask = True
                    while ask:
                        try:
                            kort_man_vill_vända = input("vilket kort vill du vända? (1,2,3,4): ")
                            pos_of_card = card_pos_dict_L4[kort_man_vill_vända]
                            turn_card_face_up(current_random_card, pos_of_card)
                            input("Press ENTER to continue")
                            if current_random_card in [11,12,13,1]:
                                print("Klätt Kort! Startar om!")
                                turtle.Screen().clear()
                                start_layout()
                                visual_klunk_dict["klunkar"] += 3 # +3 klunkar till dict som skriver ut på skärm
                                drink_take[confirmed_player] += 3 # +3 klunkar till den riktiga dict.
                                ask = False
                                layer = 1
                                break
                            elif current_random_card in [2,3,4,5,6,7,8,9,10]:
                                ask = False
                                layer += 1
                                break
                        except:
                            print("Felaktig input. Försök igen")

                elif layer == 2: # lager 3
                    prev_turtle, prev_pointer = layer_pointer(layer, prev_turtle, prev_pointer)
                    ask = True
                    while ask:
                        try:
                            kort_man_vill_vända = input("vilket kort vill du vända? (1,2,3): ")
                            pos_of_card = card_pos_dict_L3[kort_man_vill_vända]
                            turn_card_face_up(current_random_card, pos_of_card)
                            input("Press ENTER to continue")
                            if current_random_card in [11,12,13,1]:
                                print("Klätt Kort! Startar om!")
                                turtle.Screen().clear()
                                start_layout()
                                visual_klunk_dict["klunkar"] += 3 # +3 klunkar till dict som skriver ut på skärm
                                drink_take[confirmed_player] += 3
                                ask = False
                                layer = 1
                                break
                            elif current_random_card in [2,3,4,5,6,7,8,9,10]:
                                ask = False
                                layer += 1
                                break
                        except:
                            print("Felaktig input. Försök igen")

                elif layer == 3: # lager 2
                    prev_turtle, prev_pointer = layer_pointer(layer, prev_turtle, prev_pointer)
                    ask = True
                    while ask:
                        try:
                            kort_man_vill_vända = input("vilket kort vill du vända? (1,2): ")
                            #Fixa safe loop
                            pos_of_card = card_pos_dict_L2[kort_man_vill_vända]
                            turn_card_face_up(current_random_card, pos_of_card)
                            input("Press ENTER to continue")
                            if current_random_card in [11,12,13,1]:
                                print("Klätt Kort! Startar om!")
                                turtle.Screen().clear()
                                start_layout()
                                visual_klunk_dict["klunkar"] += 3 # +3 klunkar till dict som skriver ut på skärm
                                drink_take[confirmed_player] += 3
                                ask = False
                                layer = 1
                                break
                            elif current_random_card in [2,3,4,5,6,7,8,9,10]:
                                ask = False
                                layer += 1
                                break
                        except:
                            print("Felaktig input. Försök igen")
                    
                elif layer == 4: # lager 1 SISTA KORTET
                    prev_turtle, prev_pointer = layer_pointer(layer, prev_turtle, prev_pointer)
                    ask = True
                    while ask:
                        try:
                            kort_man_vill_vända = input("Vänd det sista kortet! (1): ")
                            #Fixa safe loop
                            pos_of_card = card_pos_dict_L1[kort_man_vill_vända]
                            turn_card_face_up(current_random_card, pos_of_card)
                            input("Press ENTER to continue")
                            if current_random_card in [11,12,13,1]:
                                print("Klätt Kort! Startar om!")
                                turtle.Screen().clear()
                                start_layout()
                                visual_klunk_dict["klunkar"] += 3 # +3 klunkar till dict som skriver ut på skärm
                                drink_take[confirmed_player] += 3
                                ask = False
                                layer = 1
                                break
                            elif current_random_card in [2,3,4,5,6,7,8,9,10]:
                                prev_turtle.hideturtle()
                                print("DU HAR KLARAT BUSSEN!!!")
                                ask = False
                                buss_status = False
                                layer += 1
                                break
                        except:
                            print("Felaktig input. Försök igen")


        print("GRATTIS MANNEN!!!")
        print()

        return drink_take

def Bärka_Bussen(spelar_lista, drink_take):

    print_centre("------------------------------BÄRKA BUSSEN------------------------------\n")

    #FUNKTIONER----------------------
    def jump(t, x, y):
            t.penup()
            t.goto(x, y)
            t.pendown()

    def make_turtle(x, y):
        t = turtle.Turtle()
        turtle.delay(0)
        jump(t, x, y)
        return t

    #CARDS-----------------------

    def blank_card_up(x, y):
        w = 100
        h = 150

        t = make_turtle(x, y)
        t.pensize(5)
        t.speed(0)
        t.hideturtle()
        t.color('black')
        t.fillcolor("White")
        t.begin_fill()
        for x in [w, h, w, h]:
            t.forward(x)
            t.left(90)
        t.end_fill()
        end_pos = t.pos()
        end_heading = t.heading()

        t.penup()
        t.forward(33)
        t.left(90)
        t.forward(35)

        return t

    # Man skulle kunna iterera genom alla istället för att skriva alla.
    def kort_2(x,y):
        t = blank_card_up(x,y)
        t.write("2", font=("Arial",50,"normal"))

    def kort_3(x,y):
        t = blank_card_up(x,y)
        t.write("3", font=("Arial",50,"normal"))

    def kort_4(x,y):
        t = blank_card_up(x,y)
        t.write("4", font=("Arial",50,"normal"))
        

    def kort_5(x,y):
        t = blank_card_up(x,y)
        t.write("5", font=("Arial",50,"normal"))
        
    def kort_6(x,y):
        t = blank_card_up(x,y)
        t.write("6", font=("Arial",50,"normal"))

    def kort_7(x,y):
        t = blank_card_up(x,y)
        t.write("7", font=("Arial",50,"normal"))

    def kort_8(x,y):
        t = blank_card_up(x,y)
        t.write("8", font=("Arial",50,"normal"))

    def kort_9(x,y):
        t = blank_card_up(x,y)
        t.write("9", font=("Arial",50,"normal"))

    def kort_10(x,y):
        t = blank_card_up(x,y)
        t.left(90)
        t.forward(23)
        t.write("10", font=("Arial",50,"normal"))

    def kort_knekt(x,y):
        t = blank_card_up(x,y)
        t.color("red")
        t.left(90)
        t.forward(23)
        t.write("Kn", font=("Arial",50,"normal"))

    def kort_dam(x,y):
        t = blank_card_up(x,y)
        t.color("red")
        t.left(90)
        t.forward(5)
        t.write("D", font=("Arial",50,"normal"))

    def kort_kung(x,y):
        t = blank_card_up(x,y)
        t.color("red")
        t.left(90)
        t.forward(5)
        t.write("K", font=("Arial",50,"normal"))

    def kort_ess(x,y):
        t = blank_card_up(x,y)
        t.color("red")
        t.left(90)
        t.forward(5)
        t.write("E", font=("Arial",50,"normal"))

    #TURTLE BILDER-----------------------

    def background(x, y, w, h):
            t = make_turtle(x, y)
            t.speed(0)
            t.hideturtle()
            t.color('black')
            t.fillcolor("bisque2")
            t.begin_fill()
            for x in [w, h, w, h]:
                t.forward(x)
                t.left(90)
            t.end_fill()

    def card_face_down(x, y, w, h):
        t = make_turtle(x, y)
        t.pensize(5)
        t.speed(0)
        t.hideturtle()
        t.color('black')
        t.fillcolor("DarkRed")
        t.begin_fill()
        for x in [w, h, w, h]:
            t.forward(x)
            t.left(90)
        t.end_fill()
        end_pos = t.pos()
        end_heading = t.heading()

        t.penup()
        t.forward(33)
        t.left(90)
        t.forward(35)
        t.write("?", font=("Arial",50,"normal"))
        t.goto(end_pos)
        t.setheading(end_heading)

    def turn_card_face_up(random_card, vald_pos):
        x = vald_pos[0]
        y = vald_pos[1]
        if random_card == 1:
            kort_ess(x,y)

        if random_card == 2:
            kort_2(x,y)

        if random_card == 3:
            kort_3(x,y)

        if random_card == 4:
            kort_4(x,y)

        if random_card == 5:
            kort_5(x,y)

        if random_card == 6:
            kort_6(x,y)

        if random_card == 7:
            kort_7(x,y)

        if random_card == 8:
            kort_8(x,y)

        if random_card == 9:
            kort_9(x,y)

        if random_card == 10:
            kort_10(x,y)

        if random_card == 11:
            kort_knekt(x,y)

        if random_card == 12:
            kort_dam(x,y)

        if random_card == 13:
            kort_kung(x,y)

    def start_layout():
        background(-500,-500,1000,1000)

        w = 100
        h = 150

        layer4_start_x = -275
        layer4_start_y = -325

        layer3_start_x = -200
        layer3_start_y = -150

        layer2_start_x = -125
        layer2_start_y = 25

        layer1_start_x = -50
        layer1_start_y = 200

        for x in range(11):
            if x < 4: # layer 4
                card_face_down(layer4_start_x, layer4_start_y, w, h)
                layer4_start_x += w + w/2

            elif 3 < x < 7: # layer 3
                card_face_down(layer3_start_x,layer3_start_y, w, h)
                layer3_start_x += w + w/2

            elif 7 < x < 10: # layer 2
                card_face_down(layer2_start_x, layer2_start_y, w, h)
                layer2_start_x += w + w/2

            elif x == 10: # final layer
                card_face_down(layer1_start_x, layer1_start_y, w, h)

    def layer_pointer(layer, prev_pointer= "none", prev_numbers="none"):
        if prev_pointer != "none":
            prev_pointer.hideturtle()
        if prev_numbers != "none":
            prev_numbers.clear()
        pointer = turtle.Turtle()
        pointer.color("Black")
        pointer.fillcolor("yellow")
        pointer.shapesize(8)
        pointer.penup()

        number_turtle = turtle.Turtle()
        number_turtle.hideturtle()
        number_turtle.penup()

        if layer == 1:
            pointer.goto(-350,-250)

            jump_constant = 0
            number = 1
            for jumps in range(4):
                number_turtle.goto(-225 + jump_constant, -350)
                number_turtle.write(f'{number}',font=("arial","10","normal"))
                jump_constant += 150
                number += 1

        if layer == 2:
            pointer.goto(-250, -75)

            jump_constant = 0
            number = 1
            for jumps in range(3):
                number_turtle.goto(-150 + jump_constant, -175)
                number_turtle.write(f'{number}',font=("arial","10","normal"))
                jump_constant += 150
                number += 1

        if layer == 3:
            pointer.goto(-175, 100)

            jump_constant = 0
            number = 1
            for jumps in range(2):
                number_turtle.goto(-75 + jump_constant, 0)
                number_turtle.write(f'{number}',font=("arial","10","normal"))
                jump_constant += 150
                number += 1    


        if layer == 4:
            pointer.goto(-125, 275)

            jump_constant = 0
            number = 1
            for jumps in range(1):
                number_turtle.goto(0 + jump_constant, 175)
                number_turtle.write(f'{number}',font=("arial","10","normal"))
                jump_constant += 150
                number += 1

        return pointer, number_turtle
    
    
    #------------------------------------------------------------
    # fixa så att alla fyra kort är ngt random value. för just nu är det inte mening med flera kort
    # kanske vid varje iteration göra en dict med position = kort
    if __name__ == "__main__":

        player_number = 1
        print(" Vem ska snurra The Wheel of Bärka? ")
        for player in spelar_lista:
            print(f'{player_number}: {player}')
            player_number += 1

        ask = True
        while ask:
            try:
                chosen_player = int(input("Vem ska köra bussen?: "))
                print()
                while chosen_player not in range(1,len(spelar_lista)+1):
                    print("invalid input. try again")
                    chosen_player = int(input("skriv numret på den valda spelaren: "))
                for index in range(len(spelar_lista)+1):
                    if index == chosen_player:
                        confirmed_player = spelar_lista[index-1] # Detta är spelaren som kommer snurra hjulet
                    
                    ask = False
            except:
                print("felaktig input, försök igen: ")

        visual_klunk_dict = {"klunkar":0}

        # Position på kort, för varje lager
        card_pos_dict_L4 = {"1":(-275,-325), "2":(-125,-325), "3":(25,-325), "4":(175,-325)} # Layer 4
        card_pos_dict_L3 = {"1":(-200,-150), "2":(-50,-150), "3":(100,-150)} # Layer 3
        card_pos_dict_L2 = {"1":(-125,25), "2":(25,25)} # Layer 2
        card_pos_dict_L1 = {"1":(-50 ,200)} # Layer 1, kanske man inte behöver skriva in input för denna

        #card_pos_dict = {"1":(-275,-325), "2":(-125,-325), "3":(25,-325), "4":(175,-325), "5":(-200,-150), "6":(-50,-150), "7":(100,-150), "8":(-125,25), "9":(25,25), "10":(-50 ,200)}

        # Blanda korten på bordet:
        value_list = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        start_layout()

        #Klunk Turtle
        klunk_turtle = turtle.Turtle()
        klunk_turtle.hideturtle()
        klunk_turtle.penup()
        


        # Max 4 rounds
        layer = 1
        buss_status = True
        while buss_status:
            while layer < 5: # runda 1 - 4
                
                klunk_turtle.clear()
                klunk_turtle.goto(-400,325)
                klunk_turtle.write(f'{confirmed_player}s',font=("Arial",40, "normal"))
                klunk_turtle.goto(-400,280)
                klunk_turtle.write(f'Klunkar: {visual_klunk_dict["klunkar"]}',font=("Arial",40, "normal"))


                
                print("round:",layer)

                # SKAPELSE AV dict som har pos bunden till random val. riktiiig stökig kod men fk it
                layer_4_pos_lst = [(-275,-325), (-125,-325),(25,-325),(175,-325)]
                layer_3_pos_lst = [(-200,-150),(-50,-150),(100,-150)]
                layer_2_pos_lst = [(-125,25),(25,25)]
                layer_1_pos_lst = [(-50 ,200)]

                random_card_dict_L4 = {(-275,-325):1 , (-125,-325):1 ,(25,-325):1 ,(175,-325):1 }
                random_card_dict_L3 = {(-200,-150):1 ,(-50,-150):1 ,(100,-150):1 }
                random_card_dict_L2 = {(-125,25):1 ,(25,25):1 }
                random_card_dict_L1 = {(-50 ,200):1 }

                for pos in layer_4_pos_lst: # Skapar pos och val dict för lager 4
                    randomval = random.choice(value_list)
                    random_card_dict_L4[pos] = randomval
                
                for pos in layer_3_pos_lst: # Skapar pos och val dict för lager 4
                    randomval = random.choice(value_list)
                    random_card_dict_L3[pos] = randomval

                for pos in layer_2_pos_lst: # Skapar pos och val dict för lager 4
                    randomval = random.choice(value_list)
                    random_card_dict_L2[pos] = randomval

                for pos in layer_1_pos_lst: # Skapar pos och val dict för lager 4
                    randomval = random.choice(value_list)
                    random_card_dict_L1[pos] = randomval

                #print(random_card_dict_L4)
                #print(random_card_dict_L3)
                #print(random_card_dict_L2)
                #print(random_card_dict_L1)
                
            

                if layer == 1: # 1 = lager 4 (yttre lagret)
                    prev_turtle, prev_pointer = layer_pointer(layer) # pekaren. returnerar sköldpaddan så man can cleara den vid ny runda
                    ask = True
                    while ask:
                        try:
                            kort_man_vill_vända = input("vilket kort vill du vända? (1,2,3,4): ")
                            pos_of_card = card_pos_dict_L4[kort_man_vill_vända]
                            chosen_random_card = random_card_dict_L4[pos_of_card]
                            turn_card_face_up(chosen_random_card, pos_of_card)
                            input("Press ENTER to continue")
                            if chosen_random_card in [11,12,13,1]:
                                print("Klätt Kort! Startar om!")
                                turtle.Screen().clear()
                                start_layout()
                                visual_klunk_dict["klunkar"] += 3 # +3 klunkar till dict som skriver ut på skärm
                                drink_take[confirmed_player] += 3 # +3 klunkar till den riktiga dict.
                                ask = False
                                layer = 1
                                break
                            elif chosen_random_card in [2,3,4,5,6,7,8,9,10]:
                                ask = False
                                layer += 1
                                break
                        except:
                            print("Felaktig input. Försök igen")

                elif layer == 2: # lager 3
                    prev_turtle, prev_pointer = layer_pointer(layer, prev_turtle, prev_pointer)
                    ask = True
                    while ask:
                        try:
                            kort_man_vill_vända = input("vilket kort vill du vända? (1,2,3,4): ")
                            pos_of_card = card_pos_dict_L3[kort_man_vill_vända]
                            chosen_random_card = random_card_dict_L3[pos_of_card]
                            turn_card_face_up(chosen_random_card, pos_of_card)
                            input("Press ENTER to continue")
                            if chosen_random_card in [11,12,13,1]:
                                print("Klätt Kort! Startar om!")
                                turtle.Screen().clear()
                                start_layout()
                                visual_klunk_dict["klunkar"] += 3 # +3 klunkar till dict som skriver ut på skärm
                                drink_take[confirmed_player] += 3 # +3 klunkar till den riktiga dict.
                                ask = False
                                layer = 1
                                break
                            elif chosen_random_card in [2,3,4,5,6,7,8,9,10]:
                                ask = False
                                layer += 1
                                break
                        except:
                            print("Felaktig input. Försök igen")
                            
                elif layer == 3: # lager 2
                    prev_turtle, prev_pointer = layer_pointer(layer, prev_turtle, prev_pointer)
                    ask = True
                    while ask:
                        try:
                            kort_man_vill_vända = input("vilket kort vill du vända? (1,2,3,4): ")
                            pos_of_card = card_pos_dict_L2[kort_man_vill_vända]
                            chosen_random_card = random_card_dict_L2[pos_of_card]
                            turn_card_face_up(chosen_random_card, pos_of_card)
                            input("Press ENTER to continue")
                            if chosen_random_card in [11,12,13,1]:
                                print("Klätt Kort! Startar om!")
                                turtle.Screen().clear()
                                start_layout()
                                visual_klunk_dict["klunkar"] += 3 # +3 klunkar till dict som skriver ut på skärm
                                drink_take[confirmed_player] += 3 # +3 klunkar till den riktiga dict.
                                ask = False
                                layer = 1
                                break
                            elif chosen_random_card in [2,3,4,5,6,7,8,9,10]:
                                ask = False
                                layer += 1
                                break
                        except:
                            print("Felaktig input. Försök igen")
                    
                elif layer == 4: # lager 1 SISTA KORTET
                    prev_turtle, prev_pointer = layer_pointer(layer, prev_turtle, prev_pointer)
                    ask = True
                    while ask:
                        try:
                            kort_man_vill_vända = input("vilket kort vill du vända? (1,2,3,4): ")
                            pos_of_card = card_pos_dict_L1[kort_man_vill_vända]
                            chosen_random_card = random_card_dict_L1[pos_of_card]
                            turn_card_face_up(chosen_random_card, pos_of_card)
                            input("Press ENTER to continue")
                            if chosen_random_card in [11,12,13,1]:
                                print("Klätt Kort! Startar om!")
                                turtle.Screen().clear()
                                start_layout()
                                visual_klunk_dict["klunkar"] += 3 # +3 klunkar till dict som skriver ut på skärm
                                drink_take[confirmed_player] += 3 # +3 klunkar till den riktiga dict.
                                ask = False
                                layer = 1
                                break
                            elif chosen_random_card in [2,3,4,5,6,7,8,9,10]:
                                prev_turtle.hideturtle()
                                print("DU HAR KLARAT BUSSEN!!!")
                                ask = False
                                buss_status = False
                                layer += 1
                                break
                        except:
                            print("Felaktig input. Försök igen")


        print("GRATTIS MANNEN!!!")
        print()

        return drink_take

# Roulette, siffror och färg

def main():
    standby_turtle_screen()

    # Skapar lista med Spelare och 2 "klunk-lexikon"
    drink_take = {}
    drink_give = {}
    playerlist = []
    ask2 = True
    while ask2:
        try:
            p_amount = int(input(" Antalet Spelare: "))
            ask2 = False
        except:
            print("Felaktig input, Försök igen: ")
    for _ in range(p_amount):
        player = input(" Spelare: ")
        playerlist.append(player)
        drink_take[player] = 0
        drink_give[player] = 0
    #playerlist = [i.capitalize() for i in playerlist]
    print()

    # Spel-Loop
    while True:
        game_decision = menu()
        print()
        # Games:
        if game_decision == "1":
            drink_give = RNGturtles(playerlist, drink_give)
            enter_to_continue()
            turtle.Screen().clear()
            standby_turtle_screen()
        elif game_decision == "2":
            drink_give, drink_take = ÖverUnder(playerlist, drink_give, drink_take)
            enter_to_continue()
        elif game_decision == "3":
            drink_give = TärningsProfeten(playerlist, drink_give)
            enter_to_continue()
        elif game_decision == "4":
            drink_give, drink_take, = RedBlack(playerlist, drink_give, drink_take)
            enter_to_continue()
        elif game_decision == "5":
            drink_give = SnailRace(playerlist, drink_give)
            enter_to_continue()
            turtle.Screen().clear()
            standby_turtle_screen()
        elif game_decision == "6":
            drink_give, drink_take = Wheel_of_Bärka(playerlist, drink_give, drink_take)
            enter_to_continue()
            turtle.Screen().clear()
            standby_turtle_screen()
        elif game_decision == "7":
            drink_take = Bärka_Bussen(playerlist, drink_take)
            enter_to_continue()
            turtle.Screen().clear()
            standby_turtle_screen()

        # Stats:
        elif game_decision == "s":
            show_stats(drink_give, drink_take)
            enter_to_continue()
        elif game_decision == "i":
            games_info()
            enter_to_continue()
        # Exit:
        elif game_decision == "q":
            quit_or_nah = input(" Är du säker på att du vill lämna? (y/ENTER)")
            while quit_or_nah not in ["","y"]:
                print(" invalid input")
                quit_or_nah = input(" Är du säker på att du vill lämna? (y/ENTER)")
            if quit_or_nah == "":
                print(" Går tillbaka till Menu...\n\n\n")
                time.sleep(0.5)
            elif quit_or_nah == "y":
                break

#----------------------------------------------------------------------------

if __name__ == "__main__":
    main()
    
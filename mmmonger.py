## MADE BY ~-~ KaizNike, see him on most socials. ##
## Alpha 1 - Github Release ##
#! All testing prints left in where they might be needed.
# SEED - any integer positive or negative from which we mod.
seed = input("Welcome to a world of monsters user; enter with a drop of your mind, a number, any number. Seed:")

while(type(seed) is not int):
    try:
        seed = int(seed)
        break
    except ValueError:
        seed = input("You must add a seed to germinate this world, it is a number. Enter or quit now! Seed:")

print("Very good, now for your first real choice:\n")

def spell_friend(ls,answer):
    length = 0
    for letter in answer:
        length += 1
    #print("Answer len: " + str(length))
    for word in ls:
        word_length = 0
        for letter in word:
            word_length += 1
        value = 0
        iterand = 0
        if 1.8 > word_length / length > 0.5:
            for letter in answer:
                if iterand + 1 > word_length:
                    break
                if value > 0.65 * word_length:
                    return word
                if letter == word[iterand]:
                    value += 1
                iterand += 1
        #print("word checked: " + word + " range: " + str(word_length / length) + " value: " + str(value))
    return False

choicesLS = ["decide my fate","create a character"]
choice = spell_friend(choicesLS, input("Would you like to ~decide my fate~ or ~create a character~? Type in your choice: "))
print(choice)
while(not choice):
    choice = spell_friend(choicesLS, input("Would you like to ~decide my fate~ or ~create a character~? Spell better! IT IS THE OPTION BETWEEN THE '~'."))

player = {}

def define_background(lifestyle):
    if lifestyle == 0:
        print("You are a painter, gifted to envision creatures beyond normal sight.")
    if lifestyle == 1:
        print("You are an aspiring rap artist, with grand purpose; comes great need. For monster talk.")
    if lifestyle == 2:
        print("You are a soldier, your war is ongoing; any edge would be a boon.")
    if lifestyle == 3:
        print("You are a young student, ready to explore the world.")
    if lifestyle == 4:
        print("You are an elderly teacher, you almost experienced death once and now can witness Beasts.")
    if lifestyle == 5:
        print("You are a wildsperson, ready to resume the hunt.")
    if lifestyle == 6:
        print("You have noble heritage, you might rule one day, maybe some kicking the start?")
    if lifestyle == 7:
        print("You are a rider, granted a normal beast to care for and in return are blessed with speed.")
    if lifestyle == 8:
        print("You have a connection with the gods, perhaps they tell you of Elysian Fields.")
    if lifestyle == 9:
        print("You are a layabout...")

def define_beastkin(amount):
    if amount == "full":
        print("You sport hair from ear to tail, you are shunned in daily society or maybe worshipped.")
    if amount == "most":
        print("Your blood burns from the hatred of the little of the non-Beast in you, for corralling it, for tempting it.")
    if amount == "half":
        print("Your mother or father was a beast. This union is forbidden; yet it happened all the same.")
    if amount == "some":
        print("Most everyone has some Beast blood, you fit right in that category.")            
    if amount == "none":
        print("By some bizzarre turn of fate, you are without the blood of Beasts. Your communion with them is impossible, but bonds of friendship may foster with a few.")


def create_character():
    inpLS = ["full","most","half","some","none"]
    inp = spell_friend(inpLS, input("How much have Beastkind called your card? ~full~/~most~/~half~/~some~/~none~"))
    while(not inp):
        inp = spell_friend(inpLS, input("How much have Beastkind called your card? The beasts of this world resemble those of yours, inhabiting mind rather than body. Be sure to choose one: ~full~/~most~/~half~/~some~/~none~"))
    define_beastkin(inp)
    to_quit = input("If you are happy with that description type ~y~, else we start over.")
    if to_quit != "y":
        return False
    print("Good! Let's now define your background.")
    player["beast"] = inp
    inp = -1
    #print(player) 
    #print(inp) ## BUG BAD WHILE CONDITION - FIXED
    while(not 0 <= inp <= 9):
        inp = input("CHOOSE: 0: Painter, 1: Rapper, 2: Soldier, 3: Student, 4: Teacher, 5: Wildspersonn, 6: Noble One, 7: Rider, 8: Priest, 9: Layabout. Enter a number associated with your choice.")
        try:
            inp = int(inp)
        except ValueError:
            print("Enter a choice between 0 and 9. Don't choose 9 if you care.")
    define_background(inp)
    to_quit = input("If you are happy with that description type ~y~, else we start over.")
    if to_quit != "y":
        return False
    print("Good! We won't bother with such things such as name or gender, such things can be settled later.")
    player["background"] = inp
    return True
    
    

if choice and choice == "decide my fate":
    LifeStyle = seed % 10
    player["background"] = LifeStyle
    define_background(LifeStyle)
    options = ["full","most","half","some","none"]
    BeastNature = seed % 5
    player["beast"] = options[BeastNature]
    define_beastkin(options[BeastNature])
if choice and choice == "create a character":
    check = False
    while(not check):
        check = create_character()

beastText = ""
if player["beast"] == "full" or player["beast"] == "most":
    beastText = " Your BeastBlood is howling, yes!"
input("Let us begin your adventure into the world of Mon Mon." + beastText + " At these moments you can press anything but the quit keys to continue!")
#print(spell_friend(choicesLS,choice))
## DAY 1 PROGRESS REPORT
# Background and Beast setup, now for the intro crawl!

print("At some point you lost track of where you where and when.\n\nThe world is dangerous once you leave the safe cushion you are used to...\n\n")
mainSettings = {}
choicesLS = ["full","micro","text based","none"]
choice = spell_friend(choicesLS, input(r"Enter your choice for ASCII Art: ~full~/~micro~/~text based~/~none~."))
while(not choice):
    choice = spell_friend(choicesLS, input(r"This is our manner of letting our scribes illustrate your adventure, choose: ~full~/~micro~/~text based~/~none~."))

mainSettings["ASCIIMODE"] = choice
##(!) Update this with new art :)
def display_ASCII(indx):
    if mainSettings["ASCIIMODE"] == "none":
        return False
    elif mainSettings["ASCIIMODE"] == "text based":
        return True
    elif mainSettings["ASCIIMODE"] == "micro":
        if indx == 0:
            #Study of a Smoo
            print(r'''
         \  /
          ||
          ||   ^u^
         /  \ (. .)

''')
        if indx == -1:
            #Study of a Smoo: Its Eyes Enlarged
            print(r'''
         \  /
          ||
          ||   ^u^
         /  \ (o o)

''')
        if indx == 1:
            #Wide World - Hilly Small
            print(r'''
- <x> -
  / \   ^   ^4^ ^
''')
        if indx == 2:
            #Wide World - Forests Small
            print(r'''
- <x> -  ^^^^ ^   ^^^^^^
  / \     ^^ ^^^   ^^^^^^^^^^^^
''')
        if indx == 3:
            #Wide World - P Fields Small
            print(r'''
- <x> -     PPPP    PPPP P
  / \   PPPP    PPPP   PP
''')
    
    elif mainSettings["ASCIIMODE"] == "full":
        if indx == 0:
            #Forest at Night
            print(r"""
c            H
             H (  )
          ( )H/
   vv      \ H           (i)
            \H            0
             H           /|\
    (i)      H
     L      VVVV
        VVVVVVVVVVVV
       VVVVVVVVVVVVVVV""")
        if indx == 1:
            #Wide World - Hilly
            print(r"""


                  - <x> -
                    / \

    ___/----\
---4         3--------------




""")
        if indx == 2:
            #Wide World - Forests
            print(r"""

     V
    (   )      ) (  - <x> -
      |         H     / \
     /          H
    /           H
---4--^^-^--3--VHV----^^^---
\               
 \      <(oo) (uu)    
  4                    ( )

""")
        if indx == 3:
            #Wide World - P Fields
            print(r"""


                  - <x> -
                    / \
         P
 P  ___/----\    P   P
---4         3-------------
PP
P       P      PiP
PP            PPP
              PPP
""")


happy = ""

while(happy != "y"):
    textDisplay = display_ASCII(0)
    if textDisplay:
        print("You spend a year getting to know the world better, lost as you are. Eventually something calls to you in the dark and you lose memory there...")
    happy = input("Are you happy with your choice? ~y~ or ~n~.")
    if happy != "y":
        choice = spell_friend(choicesLS, input(r"Enter your choice for ASCII Art: ~full~/~micro~/~text based~/~none~."))
        while(not choice):
            choice = spell_friend(choicesLS, input(r"This is our manner of letting our scribes illustrate your adventure, choose: ~full~/~micro~/~text based~/~none~."))

        mainSettings["ASCIIMODE"] = choice
if mainSettings["ASCIIMODE"] == "micro":
    display_ascii(-1)
input("Press enter.")
## END OF SETUP

print("/nCHAPTER 1: The Starter Mon Picks You")
n = ((seed + 77) % 3) + 1
display_ASCII(n)

##(!) Update this with encounters of all areas.
def encounter_library():
    pass


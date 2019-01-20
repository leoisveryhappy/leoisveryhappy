import os
import random
import time
import colorama
from colorama import Fore, Back, Style


#
# add monsters
#
    # monster1
    # village
    # outpost
    # abandoned (house, mine, factory, town)


#
# add animals
#


#
# add caravan
#


#
# add seasons
#


#
# add buildings
#


#
# tutorial
#


#
# add a book with locations of mysterious place
#


#
# level system!!!
#


# the list that the draw_map funcion is based off of
CELLS = []


# clear the screen when the funcion is run
def clear_screen():
    os.system('cls' if os.name == 'int' else 'clear')


# sets locations of all the tile-types
def get_locations():
    return random.sample(CELLS, 15)


# for creating the map
def set_grid(SIZE):
    x = 0
    y = 0
    # adding to SIZE below here will elongate the map
    while y <= SIZE:
        cell = x,y
        CELLS.append(cell)
        if x == SIZE:
            x = 0
            y += 1
            continue
        x += 1
def draw_map(monster1, monster2, monster3, potato_farm, mysterious1, mysterious2, shop1, casino1, chest1, chest2, chest3, berries1, berries2, berries3, player, SIZE):
    # list_of_letters = [" A", " B", " C", " D", " E", " F", " G", " H", " I", " J", " K", " L", " M", " N", " O", " P", " Q", " R", " S", " T", " U", " V" ," W", " X", " Y", " Z"]
    # print(Fore.YELLOW+" A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"+Style.RESET_ALL)
    print((Fore.YELLOW+" _"+Style.RESET_ALL)*(SIZE+1))
    tile = Fore.YELLOW+"|"+Style.RESET_ALL+"{}"
    for cell in CELLS:
        x, y = cell
        if x < SIZE:
            line_end = ""
            if cell == player:
                output = tile.format(Fore.GREEN+"X"+Style.RESET_ALL)
            elif (cell == berries1) or (cell == berries2) or (cell == berries3):
                output = tile.format(Fore.BLUE+"+"+Style.RESET_ALL)
            elif (cell == chest1) or (cell == chest2) or (cell == chest3):
                output = tile.format(Fore.CYAN+"C"+Style.RESET_ALL)
            elif (cell == shop1):
                output = tile.format(Fore.LIGHTYELLOW_EX+"S"+Style.RESET_ALL)
            elif (cell == casino1):
                output = tile.format(Fore.LIGHTYELLOW_EX+"$"+Style.RESET_ALL)
            elif (cell == potato_farm) or (cell == mysterious1) or (cell == mysterious2):
                output = tile.format(Fore.LIGHTMAGENTA_EX+"?"+Style.RESET_ALL)
            elif (cell == monster1) or (cell == monster2) or (cell == monster3):
                output = tile.format(Fore.RED+"M"+Style.RESET_ALL)
            else:
                output = tile.format(Fore.YELLOW+"_"+Style.RESET_ALL)
        else:
            line_end = "\n"
            if cell == player:
                output = tile.format(Fore.GREEN+"X"+Fore.YELLOW+"|"+Style.RESET_ALL)
            elif (cell == berries1) or (cell == berries2) or (cell == berries3):
                output = tile.format(Fore.BLUE+"+"+Fore.YELLOW+"|"+Style.RESET_ALL)
            elif (cell == chest1) or (cell == chest2) or (cell == chest3):
                output = tile.format(Fore.CYAN+"C"+Fore.YELLOW+"|"+Style.RESET_ALL)
            elif (cell == shop1):
                output = tile.format(Fore.LIGHTYELLOW_EX+"S"+Fore.YELLOW+"|"+Style.RESET_ALL)
            elif (cell == casino1):
                output = tile.format(Fore.LIGHTYELLOW_EX+"$"+Fore.YELLOW+"|"+Style.RESET_ALL)
            elif (cell == potato_farm):
                output = tile.format(Fore.LIGHTMAGENTA_EX+"?"+Fore.YELLOW+"|"+Style.RESET_ALL)
            elif (cell == monster1) or (cell == monster2) or (cell == monster3):
                output = tile.format(Fore.RED+"M"+Fore.YELLOW+"|"+Style.RESET_ALL)
            else:
                output = tile.format(Fore.YELLOW+"_|"+Style.RESET_ALL)
        print(output, end=line_end)
    print("-"*2*SIZE+"---")


# for moving the player
def move_player(default_message, health, max_health, player, move):
    x, y = player
    message = default_message
    if move == "W":
        x -= 1
    if move == "E":
        x += 1
    if move == "N":
        y -= 1
    if move == "NE":
        y -= 1
        x += 1
    if move == "NW":
        y -= 1
        x -= 1
    if move == "S":
        y += 1
    if move == "SE":
        y += 1
        x += 1
    if move == "SW":
        y += 1
        x -= 1
    if move == "WAIT":
        if health != max_health:
            health += 1
            message = Fore.BLUE + "You rest and gain 1 health." + Style.RESET_ALL
    player = x, y
    return player, message, health
def get_moves(player, SIZE):
    moves = ["W","E","N","NE","NW","S","SE","SW","WAIT"]
    x, y = player
    if x == 0 and y == 0:
        moves.remove("N")
        moves.remove("W")
        moves.remove("NW")
        moves.remove("NE")
        moves.remove("SW")
    elif x == 0 and y == SIZE:
        moves.remove("S")
        moves.remove("W")
        moves.remove("SW")
        moves.remove("SE")
        moves.remove("NW")
    elif x == SIZE and y == 0:
        moves.remove("N")
        moves.remove("E")
        moves.remove("NW")
        moves.remove("NE")
        moves.remove("SE")
    elif x == SIZE and y == SIZE:
        moves.remove("S")
        moves.remove("E")
        moves.remove("SW")
        moves.remove("SE")
        moves.remove("NE")
    else:
        if x == 0:
            moves.remove("W")
            moves.remove("NW")
            moves.remove("SW")
        elif x == SIZE:
            moves.remove("E")
            moves.remove("NE")
            moves.remove("SE")
        elif y == 0:
            moves.remove("N")
            moves.remove("NE")
            moves.remove("NW")
        elif y == SIZE:
            moves.remove("S")
            moves.remove("SE")
            moves.remove("SW")
    return moves
def escape(player, SIZE):
    escape_tile = ["W","E","N","NE","NW","S","SE","SW"]
    x, y = player
    if x == 0 and y == 0:
        escape_tile.remove("N")
        escape_tile.remove("W")
        escape_tile.remove("NW")
        escape_tile.remove("NE")
        escape_tile.remove("SW")
    elif x == 0 and y == SIZE:
        escape_tile.remove("S")
        escape_tile.remove("W")
        escape_tile.remove("SW")
        escape_tile.remove("SE")
        escape_tile.remove("NW")
    elif x == SIZE and y == 0:
        escape_tile.remove("N")
        escape_tile.remove("E")
        escape_tile.remove("NW")
        escape_tile.remove("NE")
        escape_tile.remove("SE")
    elif x == SIZE and y == SIZE:
        escape_tile.remove("S")
        escape_tile.remove("E")
        escape_tile.remove("SW")
        escape_tile.remove("SE")
        escape_tile.remove("NE")
    else:
        if x == 0:
            escape_tile.remove("W")
            escape_tile.remove("NW")
            escape_tile.remove("SW")
        elif x == SIZE:
            escape_tile.remove("E")
            escape_tile.remove("NE")
            escape_tile.remove("SE")
        elif y == 0:
            escape_tile.remove("N")
            escape_tile.remove("NE")
            escape_tile.remove("NW")
        elif y == SIZE:
            escape_tile.remove("S")
            escape_tile.remove("SE")
            escape_tile.remove("SW")
    return random.choice(escape_tile)


# print the title, death, inventory, and UI
def print_title():
    print("""
     _ _ _       _                                          _    _        
    | | | | ___ | | ___  ___  _____  ___      ____         | |_ | |_  ___ 
    | | | || -_|| ||  _|| . ||     || -_|    |__  \        |  _||   || -_|
    |_____||___||_||___||___||_|_|_||___|    __/  /        |_|  |_|_||___|
                                            /  __/                  
                                           /_____/                                                                                  
                dddddddd                                                                                                             
                d::::::d                                                                                                             
                d::::::d                                                                                                             
                d::::::d                                                                                                             
                d:::::d                                                                                                              
        ddddddddd:::::d uuuuuu    uuuuuunnnn  nnnnnnnn       ggggggggg   ggggg    eeeeeeeeeeee       ooooooooooo   nnnn  nnnnnnnn    
      dd::::::::::::::d u::::u    u::::un:::nn::::::::nn    g:::::::::ggg::::g  ee::::::::::::ee   oo:::::::::::oo n:::nn::::::::nn  
     d::::::::::::::::d u::::u    u::::un::::::::::::::nn  g:::::::::::::::::g e::::::eeeee:::::eeo:::::::::::::::on::::::::::::::nn 
    d:::::::ddddd:::::d u::::u    u::::unn:::::::::::::::ng::::::ggggg::::::gge::::::e     e:::::eo:::::ooooo:::::onn:::::::::::::::n
    d::::::d    d:::::d u::::u    u::::u  n:::::nnnn:::::ng:::::g     g:::::g e:::::::eeeee::::::eo::::o     o::::o  n:::::nnnn:::::n
    d:::::d     d:::::d u::::u    u::::u  n::::n    n::::ng:::::g     g:::::g e:::::::::::::::::e o::::o     o::::o  n::::n    n::::n
    d:::::d     d:::::d u::::u    u::::u  n::::n    n::::ng:::::g     g:::::g e::::::eeeeeeeeeee  o::::o     o::::o  n::::n    n::::n
    d:::::d     d:::::d u:::::uuuu:::::u  n::::n    n::::ng::::::g    g:::::g e:::::::e           o::::o     o::::o  n::::n    n::::n
    d::::::ddddd::::::ddu:::::::::::::::uun::::n    n::::ng:::::::ggggg:::::g e::::::::e          o:::::ooooo:::::o  n::::n    n::::n
     d:::::::::::::::::d u:::::::::::::::un::::n    n::::n g::::::::::::::::g  e::::::::eeeeeeee  o:::::::::::::::o  n::::n    n::::n
      d:::::::::ddd::::d  uu::::::::uu:::un::::n    n::::n  gg::::::::::::::g   ee:::::::::::::e   oo:::::::::::oo   n::::n    n::::n
       ddddddddd   ddddd    uuuuuuuu  uuuunnnnnn    nnnnnn    gggggggg::::::g     eeeeeeeeeeeeee     ooooooooooo     nnnnnn    nnnnnn
                                                                      g:::::g                                                        
                                                          gggggg      g:::::g                                                        
                                                          g:::::gg   gg:::::g                                                        
                                                           g::::::ggg:::::::g                                                        
                                                            gg:::::::::::::g                                                         
                                                              ggg::::::ggg                                                           
                                                                 gggggg                                                              
    """)
    input("Press return to start:")
def print_death(turn, health, hunger, gold, kills, fashion):
    print("""
                                                                
                                                                
    RRRRRRRRRRRRRRRRR        IIIIIIIIII     PPPPPPPPPPPPPPPPP   
    R::::::::::::::::R       I::::::::I     P::::::::::::::::P  
    R::::::RRRRRR:::::R      I::::::::I     P::::::PPPPPP:::::P 
    RR:::::R     R:::::R     II::::::II     PP:::::P     P:::::P
      R::::R     R:::::R       I::::I         P::::P     P:::::P
      R::::R     R:::::R       I::::I         P::::P     P:::::P
      R::::RRRRRR:::::R        I::::I         P::::PPPPPP:::::P 
      R:::::::::::::RR         I::::I         P:::::::::::::PP  
      R::::RRRRRR:::::R        I::::I         P::::PPPPPPPPP    
      R::::R     R:::::R       I::::I         P::::P            
      R::::R     R:::::R       I::::I         P::::P            
      R::::R     R:::::R       I::::I         P::::P            
    RR:::::R     R:::::R     II::::::II     PP::::::PP          
    R::::::R     R:::::R     I::::::::I     P::::::::P          
    R::::::R     R:::::R     I::::::::I     P::::::::P          
    RRRRRRRR     RRRRRRR     IIIIIIIIII     PPPPPPPPPP          
                                                            
                You have died. Game over.
        """)
    print("Turn: {} | Health: {} | Hunger: {} | Gold: {} | Kills: {} | Fashion: {} ".format(turn, health, hunger, gold, kills, fashion))
    print("-"*2*SIZE+"---")
def print_UI(turn, health, hunger, armour, gold):
    if hunger <= 10:
        hunger = Fore.RED + str(hunger) + Style.RESET_ALL
    if health <= 10:
        health = Fore.RED + str(health) + Style.RESET_ALL
    print("Turn: {} | Health: {} | Hunger: {} | Armour: {} | Gold: {} ".format(turn, health, hunger, armour, gold))
    hunger = Style.RESET_ALL + str(hunger)
    health = Style.RESET_ALL + str(health)
    print("-"*2*SIZE+"---")
def print_inventory(inventory):
    print("Your inventory:")
    if len(inventory) == 0:
        print(Fore.RED+"Empty"+Style.RESET_ALL)
    for item in inventory:
        if item.get("type") == "weapon":
            print("-", item.get("name"), "  Durability:", item.get("durability"), "  Damage:", item.get("effect"))
        elif item.get("type") == "food":
            print("-", item.get("name"), "  Durability:", item.get("durability"), "  Feeding Power:", item.get("effect"))
        elif item.get("type") == "armour":
            print("-", item.get("name"), "  Durability:", item.get("durability"), "  Armour Power:", item.get("effect"))
        elif item.get("name") == "Brown fluffy jacket":
            print("-", item.get("name"), Fore.GREEN+" SPECIAL: Heals 2 per turn."+Style.RESET_ALL)
        elif item.get("name") == "Volleyball":
            print("-", item.get("name"), Fore.GREEN+" SPECIAL: Just a volleyball."+Style.RESET_ALL)
    print("-"*2*SIZE+"---")
def print_shop_keeper(SIZE):
    print("""
                (.,------...__
             _.'"             `.
           .'  .'   `, `. `.    `
          . .'   .'/''--...__`.  \\    --  Hello! My name is Seb.
         . .--.`.  ' "-.     '.  |           What can I do for you today?
         ''  .'  _.' .())  .--":/
         ''(  \_\      '   (()(
         ''._'          (   \ '
         ' `.            `--'  '
          `.:    .   `-.___.'  '
           `.     .    _  _  .'
             )       .____.-'
           .'`.        (--..
         .' \  /\      / /  `.
       .'    \(  \    /|/     `.
     .'           \__/          `.
    /      |        o      |      \\
           |               |      |
    """)
    print("-"*2*SIZE+"---")
def print_potato_farmer(SIZE):
    print("""
                     $$$$$$$$
                    $$$$$$$$$$
                   $$$$$$$$$$$$
                   $$ 0    0 $$   --  Hello! My name is Kris.
                   $$   ()   $$         What can I do for you today?
                  $$$ \    / $$$
                  $$$  \__/  $$$
                     \______/
                  _____!  !_____
                  !            !
                  !  !      !  !
                  !  !      !  !
                  !  !      !  !
               ====================
    """)
    print("-"*2*SIZE+"---")
def print_monster(monster_health, SIZE):
    print("""
               .----.__
              /---.__  \\
             /        `\ |
            | o     o    \|   ------- GRRRR
          ./| .vvvvvvvv.  |\\           I'm gonna eat you
         / /| |        |  | \\
        //' | `^vvvvvvv'  |/\\\\
        ~   \            /   \\\\
            |   """, monster_health, """   |     ~
            7          /
           /    .     |
          -|_/\/ `---.|_
    """)
    print("-"*2*SIZE+"---")
def print_casino(SIZE):
    print("""
            .------\ /------.
            |       -       |
            |               |
            |               |
            |               |
         _______________________
         ===========.===========
           / ~~~~~     ~~~~~ \\
          /|    |         |   \\
          W   ---  / \  ---   W
          \.      |o o|      ./
           |                 |
           \    #########    /
            \  ## ----- ##  /
             \##         ##/
              \_____v_____/
    """)
    print("-"*2*SIZE+"---")

# prints a message, like a recent action
def return_message(message, SIZE):
    print(message)
    print("-"*2*SIZE+"---")


# the tutorial
def tutorial():
    print("This is a small adventure game where you, the player, move around a map collecting loot. It's not all fun and games though, if you don't keep your hunger and health up you will die and lose all your progress.")
    print("Anyway, now on to the controls and stuff.")
    print("Every time you want to complete an action you need to click return. Yes, that means you can't just click the arrow keys, you need to type 'n', 's', 'e' or 'w' AND THEN click enter to move.")
    print("Everytime you eat something or wear something, it will disappear from your inventory and there is no way to be able to get it back")
    print("Another thing you might want to note is that you should READ THE WORDS on the page. Just be patient please, this is only the first real game I've made.")
    print("Thanks for playing!")
    print("-MegaMogul and Leoisveryhappy")
    input("\nPress return to continue:")
    clear_screen()

# the game loop, very important!!
def game_loop():
    # define basic player stats
    turn = 0
    health = 100
    max_health = 100
    hunger = 100
    max_hunger = 100
    armour = 0
    max_armour = 100
    gold = 10
    fashion = 0
    kills = 0

    # define basic monster stats
    monster_max_health = 25

    # default weapon
    Fists = {
        "name":"Fists",
        "durability":None,
        "effect":3,
        "value":None,
        "type":"Fists"
        }
    equiped_weapon = Fists

    # lists of items
    misc = [{
        "name":"Knife",
        "durability":1,
        "effect":10,
        "value":15,
        "type":"weapon"
        },{
        "name":"Gold",
        "value":random.randint(10,50)
        }]
    foods = [{
        "name":"Potato",
        "durability":1,
        "effect":7,
        "value":11,
        "type":"food"
        },{
        "name":"Melon",
        "durability":3,
        "effect":4,
        "value":16,
        "type":"food"
        },{
        "name":"Pineapple",
        "durability":2,
        "effect":4,
        "value":12,
        "type":"food"
        },{
        "name":"Papaya",
        "durability":1,
        "effect":4,
        "value":8,
        "type":"food"
        },{
        "name":"Nugget",
        "durability":1,
        "effect":50,
        "value":50,
        "type":"food"
        }]
    tools = [{
        "name":"Sword",
        "durability":3,
        "effect":10,
        "value":35,
        "type":"weapon"
        },{
        "name":"Shield",
        "durability":3,
        "effect":2,
        "value":11,
        "type":"weapon"
        },{
        "name":"Axe",
        "durability":5,
        "effect":20,
        "value":105,
        "type":"weapon"
        },{
        "name":"Staff",
        "durability":7,
        "effect":7,
        "value":54,
        "type":"weapon"
        },{
        "name":"Mace",
        "durability":2,
        "effect":14,
        "value":33,
        "type":"weapon"
        },{
        "name":"Club",
        "durability":5,
        "effect":6,
        "value":35,
        "type":"weapon"
        }]
    magic = [{
        "name":"Magic potato",
        "durability":1,
        "effect":"100",
        "value":"100",
        "type":"magic"
        }]
    clothes = [{
        "name":"Baseball cap",
        "durability":1,
        "effect":5,
        "value":10,
        "type":"armour"
        },{
        "name":"Helmet",
        "durability":1,
        "effect":30,
        "value":50,
        "type":"armour"
        },{
        "name":"Shoulder guard",
        "durability":1,
        "effect":20,
        "value":30,
        "type":"armour"
        },{
        "name":"Bulletproof vest",
        "durability":1,
        "effect":80,
        "value":100,
        "type":"armour"
        }]
    # inventory starts with food, random armour, and a random weapon, the max items in the inventory is 7
    
    inventory = [{
        "name":"Energy bar",
        "durability":1,
        "effect":15,
        "value":20,
        "type":"food"
        }]
    inventory.append(random.choice(tools))
    inventory.append(random.choice(clothes))
    # shop items
    items_in_shop1 = []
    items_in_shop1.extend(random.sample(tools, 3))
    # items in the potato shop
    potato_shop1 = [{
        "name":"Potato",
        "durability":1,
        "effect":7,
        "value":10,
        "type":"food"
        },{
        "name":"Mashed potato",
        "durability":1,
        "effect":8,
        "value":13,
        "type":"food"
        },{
        "name":"Sweet potato",
        "durability":1,
        "effect":6,
        "value":20,
        "type":"food"
        },{
        "name":"Baked potato",
        "durability":1,
        "effect":9,
        "value":15,
        "type":"food"
        },{
        "name":"Magic potato",
        "durability":1,
        "effect":"100",
        "value":"300",
        "type":"magic"
        }]
    # fill chests
    items_in_chest1 = random.sample(misc, 2)
    items_in_chest1.append(random.choice(clothes))
    items_in_chest2 = random.sample(tools, 1)
    items_in_chest2.append(random.choice(clothes))
    items_in_chest3 = random.sample(foods, 2)
    items_in_chest3.append(random.choice(clothes))
    
    # generate random mysterious events for the mysterious tiles
    generate_mysterious_event = ["gold", "dead body", "ambush"]
    mysterious1_event, mysterious2_event = random.sample(generate_mysterious_event, 2)

    # booleans
    playing = True
    show_inventory = False

    # defines initial messages, but they can change later
    message = Fore.BLACK + "You have done nothing yet. Try moving somewhere." + Style.RESET_ALL
    default_message = Fore.BLACK + ("-"*2*SIZE+"---") + Style.RESET_ALL

    # spawn the things
    monster1_spawn, monster2_spawn, monster3_spawn, potato_farm, mysterious1, mysterious2, shop1, casino1, chest1, chest2, chest3, berries1, berries2, berries3, player = get_locations()
    monster1 = monster1_spawn
    monster1_respawn = -1
    monster2 = monster2_spawn
    monster2_respawn = -1
    monster3 = monster3_spawn
    monster3_respawn = -1

    while playing:
        if (monster1 == None) and monster1_respawn == turn:
            monster1 = monster1_spawn
        if (monster2 == None) and monster2_respawn == turn:
            monster2 = monster2_spawn
        if (monster3 == None) and monster3_respawn == turn:
            monster3 = monster3_spawn
        clear_screen()
        draw_map(
            monster1, monster2, monster3,
            potato_farm, 
            mysterious1, mysterious2,
            shop1,
            casino1,
            chest1, chest2, chest3,
            berries1, berries2, berries3,
            player,
            SIZE)
        valid_moves = get_moves(player, SIZE)
        print_UI(turn, health, hunger, armour, gold)
        if show_inventory == False:
            pass
        else:
            print_inventory(inventory)

        # this place needs to be fixed later when the clothing system comes in
        if {"name":"Shinguard", "durability":None, "effect":None, "value":100, "type":"clothing"} in inventory:
            max_health = 110
        if {"name":"Brown fluffy jacket", "durability":None, "effect":None, "value":125, "type":"clothing"} in inventory:
            max_health = 125

        print("'99' to quit")
        print("'??' for help")
        print("-"*2*SIZE+"---")
        return_message(message, SIZE)
        message = default_message
        move = input("> ")
        move = move.upper()

        if move == "99":
            break
        elif move == "??":
            clear_screen()
            print("Key:")
            print("X = player")
            print("+ = berry")
            print("C = chest")
            print("S = shop")
            print("M = monster")
            print("-"*2*SIZE+"---")
            print("Controls:")
            print("- 'N' or 'n' to travel north")
            print("- 'E' or 'e' to travel east")
            print("- 'S' or 's' to travel south")
            print("- 'W' or 'w' to travel west")
            print("Hint: you can also move diagonally, ie 'ne' or 'sw'.")
            print("Extra hint: you can also 'wait'")
            print("- '99' to quit")
            print("- '??' to get help")
            print("- 'II' or 'ii' to toggle inventory")
            print("- 'Eat' or 'eat' to eat something")
            print("- 'Wear' or 'wear' to wear something")
            input("\nPress return to continue:")
        elif move == "II":
            if show_inventory == True:
                show_inventory = False
            elif show_inventory == False:
                show_inventory = True
            continue
        elif move == "WEAR":
            while True:
                clear_screen()
                draw_map(
                    monster1, monster2, monster3,
                    potato_farm,
                    mysterious1, mysterious2,
                    shop1,
                    casino1,
                    chest1, chest2, chest3,
                    berries1, berries2, berries3,
                    player,
                    SIZE)

                print_UI(turn, health, hunger, armour, gold)
                print_inventory(inventory)
                return_message(message, SIZE)

                print("What would you like to wear? ('exit' to exit')")
                wear = input("> ").capitalize()
                if wear.lower() == "exit":
                    break
                for item in inventory:
                    if wear == item.get("name") and item.get("type") == "armour":
                        add_armour = item.get("effect")
                        armour += add_armour
                        if armour > max_armour:
                            armour = max_armour
                        inventory.remove(item)
                        message = (Fore.BLUE+"You wore the {}.".format(wear)+Style.RESET_ALL)
                    else:
                        message = (Fore.RED+"You can not wear '{}'.".format(wear)+Style.RESET_ALL)
        elif move == "EAT":
            while True:
                clear_screen()
                draw_map(
                    monster1, monster2, monster3,
                    potato_farm, mysterious1, mysterious2,
                    shop1,
                    casino1,
                    chest1, chest2, chest3,
                    berries1, berries2, berries3,
                    player,
                    SIZE)

                print_UI(turn, health, hunger, armour, gold)
                print_inventory(inventory)
                return_message(message, SIZE)

                print("What would you like to eat? ('exit' to exit)")
                eat = input("> ").capitalize()
                if eat == "Exit":
                    break
                for item in inventory:
                    if eat == item.get("name") and item.get("type") == "food":
                        add_hunger = item.get("effect")
                        hunger += add_hunger
                        if hunger > max_hunger:
                            hunger = max_hunger
                        inventory.remove(item)
                        durability = item.get("durability")
                        durability -= 1
                        if durability <= 0:
                            message = (Fore.BLUE+"You finished the {}. +{} hunger.".format(item.get("name"), item.get("effect"))+Style.RESET_ALL)
                            break
                        else:
                            item.update({"durability":durability})
                            message = (Fore.BLUE+"You ate a piece of the {}. +{} hunger.".format(item.get("name"), item.get("effect"))+Style.RESET_ALL)
                            inventory.append(item)
                            break
                    else:
                        message = (Fore.RED+"You can not eat '{}'.".format(eat)+Style.RESET_ALL)
                for magic in inventory:
                    if eat == item.get("name") and item.get("type") == "magic":
                        add_hunger = item.get("effect")
                        add_health = item.get("effect")
                        if hunger > max_hunger:
                            hunger = max_hunger
                        inventory.remove(item)
                        durability = item.get("durability")
                        durability -= 1
                        if durability <= 0:
                            message = (Fore.BLUE+"You finished the {}. +{} hunger. +{} health".format(item.get("name"), item.get("effect"), item.get ("effect"))+Style.RESET_ALL)
                            break

        elif move in valid_moves:
            # update where the player is
            player, message, health = move_player(default_message, health, max_health, player, move)
            # auto move player for testing hehe
            # mysterious1_event = "ambush"
            # player = mysterious1

        #
        # hunger and turn management area
        #
            # increase the turn number
            turn += 1
            # natural deterioration of hunger
            hunger -= 2
            # lose health when starving
            if hunger <= 0:
                hunger = 0
                health -= 15
                message = Fore.RED + ("You are starving! {} turns left to eat something.".format(health/10)) + Style.RESET_ALL
            # if the player is on a berry tile, they eat it
            if (player == berries1) or (player == berries2) or (player == berries3):
                hunger += 10
                if hunger > max_hunger:
                    hunger = max_hunger
                if player == berries1:
                    berries1 = None
                if player == berries2:
                    berries2 = None
                if player == berries3:
                    berries3 = None
                message = Fore.BLUE + "You ate some berries, +15 hunger." + Style.RESET_ALL


        #
        # chest and inventory management area
        #
            if (player == chest1):
                message = Fore.GREEN+"You opened chest 1."+Style.RESET_ALL
                while True:
                    clear_screen()
                    draw_map(
                        monster1, monster2, monster3,
                        potato_farm, mysterious1, mysterious2,
                        shop1,
                        casino1,
                        chest1, chest2, chest3,
                        berries1, berries2, berries3,
                        player,
                        SIZE)
                    print_UI(turn, health, hunger, armour, gold)
                    return_message(message, SIZE)

                    # show items in the chest
                    print("Chest:")
                    if len(items_in_chest1) == 0:
                        print(Fore.RED+"Empty"+Style.RESET_ALL)
                    for item in items_in_chest1:
                        print("- "+item.get("name"))

                    print("Which items would you like to take from this chest?\n('exit' to exit or 'i' to list inventory)")
                    get_item = input("> ")
                    if get_item.lower() == "exit":
                        message = default_message
                        break

                    # print current inventory
                    elif get_item.lower() == "i":
                        print_inventory(inventory)
                        input("\nPress return to continue:")
                        message = default_message
                        continue

                    if len(inventory) <= 7:
                        # gets the item the user selected from the chest, or prints an error message
                        for item in items_in_chest1:
                            if get_item.capitalize() == item.get("name"):
                                if item.get("name") != "Gold":
                                    inventory.append(item)
                                    message = Fore.MAGENTA+"Added 1 {} to your inventory.".format(item.get("name"))+Style.RESET_ALL
                                else:
                                    gold += item.get("value")
                                    message = Fore.MAGENTA+"Added {} Gold to your gold.".format(item.get("value"))+Style.RESET_ALL
                                items_in_chest1.remove(item)
                            else:
                                message = Fore.RED+"'{}' is not an item in this chest.".format(get_item)+Style.RESET_ALL
                    else:
                        message = Fore.RED+"Your inventory is full. Use an item to make room."+Style.RESET_ALL
            if (player == chest2):
                message = Fore.GREEN+"You opened chest 2."+Style.RESET_ALL
                while True:
                    clear_screen()
                    draw_map(
                        monster1, monster2, monster3,
                        potato_farm, mysterious1, mysterious2,
                        shop1,
                        casino1,
                        chest1, chest2, chest3,
                        berries1, berries2, berries3,
                        player,
                        SIZE)
                    print_UI(turn, health, hunger, armour, gold)
                    return_message(message, SIZE)

                    # show items in the chest
                    print("Chest:")
                    if len(items_in_chest2) == 0:
                        print(Fore.RED+"Empty"+Style.RESET_ALL)
                    for item in items_in_chest2:
                        print("- "+item.get("name"))

                    print("Which items would you like to take from this chest?\n('exit' to exit or 'i' to list inventory)")
                    get_item = input("> ")
                    if get_item.lower() == "exit":
                        message = default_message
                        break

                    # print current inventory
                    elif get_item.lower() == "i":
                        print_inventory(inventory)
                        input("\nPress return to continue:")
                        message = default_message
                        continue
                    
                    if len(inventory) <= 7:
                        # gets the item the user selected from the chest, or prints an error message
                        for item in items_in_chest2:
                            if get_item.capitalize() == item.get("name"):
                                if item.get("name") != "Gold":
                                    inventory.append(item)
                                    message = Fore.MAGENTA+"Added 1 {} to inventory.".format(item.get("name"))+Style.RESET_ALL
                                else:
                                    gold += item.get("value")
                                    message = Fore.MAGENTA+"Added {} Gold to your gold.".format(item.get("value"))+Style.RESET_ALL
                                items_in_chest2.remove(item)
                            else:
                                message = Fore.RED+"'{}' is not an item in this chest.".format(get_item)+Style.RESET_ALL
                    else:
                        message = Fore.RED+"Your inventory is full. Use an item to make room."+Style.RESET_ALL
            if (player == chest3):
                message = Fore.GREEN+"You opened chest 3."+Style.RESET_ALL
                while True:
                    clear_screen()
                    draw_map(
                        monster1, monster2, monster3,
                        potato_farm, mysterious1, mysterious2,
                        shop1,
                        casino1,
                        chest1, chest2, chest3,
                        berries1, berries2, berries3,
                        player,
                        SIZE)
                    print_UI(turn, health, hunger, armour, gold)
                    return_message(message, SIZE)

                    # show items in the chest
                    print("Chest:")
                    if len(items_in_chest3) == 0:
                        print(Fore.RED+"Empty"+Style.RESET_ALL)
                    for item in items_in_chest3:
                        print("- "+item.get("name"))

                    print("Which items would you like to take from this chest?\n('exit' to exit or 'i' to list inventory)")
                    get_item = input("> ")
                    if get_item.lower() == "exit":
                        message = default_message
                        break

                    # print current inventory
                    elif get_item.lower() == "i":
                        print_inventory(inventory)
                        input("\nPress return to continue:")
                        message = default_message
                        continue
                    
                    if len(inventory) <= 7:
                        # gets the item the user selected from the chest, or prints an error message
                        for item in items_in_chest3:
                            if get_item.capitalize() == item.get("name"):
                                if item.get("name") != "Gold":
                                    inventory.append(item)
                                    message = Fore.MAGENTA+"Added 1 {} to inventory.".format(item.get("name"))+Style.RESET_ALL
                                else:
                                    gold += item.get("value")
                                    message = Fore.MAGENTA+"Added {} Gold to your gold.".format(item.get("value"))+Style.RESET_ALL
                                items_in_chest3.remove(item)
                            else:
                                message = Fore.RED+"'{}' is not an item in this chest.".format(get_item)+Style.RESET_ALL
                    else:
                        message = Fore.RED+"Your inventory is full. Use an item to make room."+Style.RESET_ALL


        #
        # shop area
        #
            if (player == shop1):
                message = Fore.GREEN+"You entered the shop!"+Style.RESET_ALL
                while True:
                    clear_screen()
                    print_shop_keeper(SIZE)
                    print_UI(turn, health, hunger, armour, gold)
                    print_inventory(inventory)
                    print("Shop items:")
                    for item in items_in_shop1:
                            print("-", item.get("name"), "for {}G.".format(item.get("value")))
                    print("-"*2*SIZE+"---")
                    return_message(message, SIZE)
                    if len(inventory) == 0:
                        almost_useless_variabale = " "
                    else:
                        almost_useless_variabale = " or 's' to sell "
                    print("Welcome to the shop!")
                    print("'b' to buy"+ almost_useless_variabale +"items.\n('exit' to exit)")
                    buy_sell = input("> ")
                    if buy_sell == "exit":
                        break
                    # buy items
                    if buy_sell.lower() == "b":
                        buy_item = input("What would you like to buy?\n> ").capitalize()
                        for item in items_in_shop1:
                            if buy_item == item.get("name"):
                                if gold < item.get("value"):
                                    message = Fore.RED + "You don't have enough money to afford {}.".format(item.get("name")) + Style.RESET_ALL
                                    break
                                else:
                                    print("Are you sure you want to buy 1 {} for {}G.".format(item.get("name"), item.get("value")))
                                    confirm_purchase = input("(y/n)\n> ").lower()
                                    if confirm_purchase == "y":
                                        gold -= item.get("value")
                                        inventory.append(item)
                                        items_in_shop1.remove(item)
                                        message = Fore.MAGENTA + "You bought 1 {} for {}G.".format(item.get("name"), item.get("value")) + Style.RESET_ALL
                                        break
                                    else:
                                        message = Fore.RED + "Purchase cancelled." + Style.RESET_ALL
                                        break
                            message = Fore.RED + "Sorry, we don't have '{}' in stock.".format(buy_item) + Style.RESET_ALL

                    # sell items
                    elif len(inventory) != 0:
                        if buy_sell.lower() == "s":
                            sell_item = input("What would you like to sell?\n> ").capitalize()
                            for item in inventory:
                                if sell_item == item.get("name"):
                                    print("Are you sure you want to sell a {} for {}?".format(item.get("name"), item.get("value")))
                                    confirm_sale = input("(y/n)\n> ").lower()
                                    if confirm_sale == "y":
                                        gold += item.get("value")

                                        # fixed a bug where the equiped weapon could stay the same even if the user sold it, not tested
                                        if item == equiped_weapon:
                                            equiped_weapon = Fists

                                        inventory.remove(item)
                                        items_in_shop1.append(item)
                                        message = Fore.MAGENTA + "You sold 1 {} for {}G.".format(item.get("name"), item.get("value")) + Style.RESET_ALL
                                        break
                                    else:
                                        message = Fore.MAGENTA + "Sale cancelled." + Style.RESET_ALL
                                        break
                                message = Fore.RED + "You don't have '{}' in your inventory.".format(sell_item) + Style.RESET_ALL


        #
        # casino area
        #
            if (player == casino1):
                message = Fore.GREEN+"You entered the casino!"+Style.RESET_ALL
                while True:
                    clear_screen()
                    print_casino(SIZE)
                    print_UI(turn, health, hunger, armour, gold)
                    return_message(message, SIZE)
                    message = default_message
                    print("Which game would you like to play? ('more' for info)")
                    print("1)Coin flip  2)R.P.S.  3)Guess the number  4)Blackjack")
                    game = input("> ").capitalize()
                    if game == "Exit":
                        break
                    elif game == "More":
                        clear_screen()
                        print("Coin flip:\nYou guess heads or tails and then choose how much money you want to bet, up to 5G. If you win, you get what you bet times two.\n\nRock paper scissors:\nIt\'s rock paper scissors, bet up to 10G. If you win, you get what you bet times two.\n\nGuess the number:\nYou guess the number I am thinking of, 1 to 5. Then you bet up to 15G. If you guess right, you get what you bet times two.\n\nBlack jack:\nYour goal is to get 21 points, one card at a time. Bet up to 100G. If you win, you win the whole pot.\n\n                    --->    Type 'exit' and you exit the casino. Unless you are mid game.    <---")
                        input("\n\n\n\nreturn to continue:")
                        continue
                    elif (game.capitalize() == "Coin flip") or (game == "1"):
                        # make sure the user chooses either heads or tails
                        heads_tails = input("Heads or Tails?\n> ").capitalize()
                        if (heads_tails == "Heads") or (heads_tails == "Tails"):
                            pass
                        elif heads_tails == "Exit":
                            break
                        else:
                            message = Fore.RED + "Please type only 'Heads' or 'Tails'." + Style.RESET_ALL
                            continue
                        # make sure the user bets between 1 and 5 and only a number
                        bet = input("How much do you want to bet? (1 to 5)\n> ")
                        try:
                            bet = int(bet)
                        except ValueError:
                            message = Fore.RED + "Please only type a number (ie '3')." + Style.RESET_ALL
                            continue
                        if bet > gold:
                            message = Fore.RED + "You don't have enough gold" + Style.RESET_ALL
                        elif (bet < 1) or (bet > 5):
                            message = Fore.RED + "You must bet between 1 and 5." + Style.RESET_ALL
                            continue
                        else:
                            flip_outcome = random.choice(["Heads","Tails"])
                            if flip_outcome == heads_tails:
                                message = Fore.GREEN + "You win! +{}.".format(bet) + Style.RESET_ALL 
                                gold += bet
                            else:
                                message = Fore.RED + "You lose! -{}.".format(bet) + Style.RESET_ALL 
                                gold -= bet
                    elif (game.capitalize() == "R.p.s") or (game.capitalize() == "Rock paper scissors") or (game == "2"):
                        rps = input("Rock, Paper or Scissors?\n> ").capitalize()
                        if (rps == "Rock") or (rps == "Paper") or (rps == "Scissors"):
                            pass
                        elif rps == "Exit":
                            break
                        else:
                            message = Fore.RED + "Please type only 'Rock', 'Paper' or 'Scissors'." + Style.RESET_ALL
                            continue
                        # make sure the user bets between 1 and 5 and only a number
                        bet = input("How much do you want to bet? (1 to 10)\n> ")
                        try:
                            bet = int(bet)
                        except ValueError:
                            message = Fore.RED + "Please only type a number (ie '3')" + Style.RESET_ALL
                            continue
                        if bet > gold:
                            message = Fore.RED + "You don't have enough gold" + Style.RESET_ALL
                        elif (bet < 1) or (bet > 10):
                            message = Fore.RED + "You must bet between 1 and 10" + Style.RESET_ALL
                            continue
                        else:
                            computer_rps = random.choice(["Rock","Paper","Scissors"])
                            if computer_rps == rps:
                                message = Fore.BLUE + "It's a tie." + Style.RESET_ALL
                            elif (computer_rps == "Rock" and rps == "Paper") or (computer_rps == "Paper" and rps == "Scissors") or (computer_rps == "Scissors" and rps == "Rock"):
                                message = Fore.GREEN + "You win! +{}".format(bet) + Style.RESET_ALL 
                                gold += bet
                            else:
                                message = Fore.RED + "You lose! -{}".format(bet) + Style.RESET_ALL 
                                gold -= bet
                    elif (game.capitalize() == "Guess the number") or (game == "3"):
                        num_guess = input("Guess a number between 1 and 5\n> ").capitalize()
                        try:
                            num_guess = int(num_guess)
                        except ValueError:
                            message = Fore.RED + "Please only type a number (ie '3')" + Style.RESET_ALL
                            continue
                        if num_guess >= 1 and num_guess <= 10:
                            pass
                        elif num_guess == "Exit":
                            break
                        # make sure the user bets between 1 and 5 and only a number
                        bet = input("How much do you want to bet? (1 to 15)\n> ")
                        try:
                            bet = int(bet)
                        except ValueError:
                            message = Fore.RED + "Please only type a number (ie '3')" + Style.RESET_ALL
                            continue
                        if bet > gold:
                            message = Fore.RED + "You don't have enough gold" + Style.RESET_ALL
                        elif (bet < 1) or (bet > 15):
                            message = Fore.RED + "You must bet between 1 and 15" + Style.RESET_ALL
                            continue
                        else:
                            computer_num_guess = random.randint(1,5)
                            if computer_num_guess == num_guess:
                                message = Fore.GREEN + "You win! +{}".format(bet) + Style.RESET_ALL 
                                gold += bet
                            else:
                                message = Fore.RED + "You lose! -{}".format(bet) + Style.RESET_ALL 
                                gold -= bet
                    elif (game.capitalize() == "Blackjack") or (game == "4"):
                        clear_screen()
                        print_casino(SIZE)
                        print_UI(turn, health, hunger, armour, gold)
                        return_message(message, SIZE)
                        # the ante is how much it costs to play
                        if gold < 50:
                            message = Fore.RED + "You need at least 50G to play." + Style.RESET_ALL
                            continue
                        ante = input("To play this game you must bet " + Fore.YELLOW + "5G" + Style.RESET_ALL + " to start.\nWould you like to play?\n(y/n)\n> ")
                        # the pot starts at 5 because the computer has to ante up as well
                        pot = 5
                        if ante.lower() == "y":
                            gold -= 5
                            pot += 5
                            clear_screen()
                            print_casino(SIZE)
                            print_UI(turn, health, hunger, armour, gold)
                            return_message(message, SIZE)
                            message = Fore.YELLOW + "Pot: " + str(pot) + Style.RESET_ALL
                        else:
                            break
                        # this is the full deck of cards
                        cards = [1,2,3,4,5,6,7,8,9,10,10,10,10, 1,2,3,4,5,6,7,8,9,10,10,10,10, 1,2,3,4,5,6,7,8,9,10,10,10,10, 1,2,3,4,5,6,7,8,9,10,10,10,10]
                        # cards the player has
                        your_cards = []
                        # total of the players cards
                        total_p_cards = 0
                        # computers cards
                        computer_cards = []
                        # total of the computers cards
                        total_c_cards = 0
                        # starting cards, these will got to the computer
                        start_cards = random.sample(cards, 2)
                        # deletes used cards
                        for card in start_cards:
                            cards.remove(card)
                        computer_cards.extend(start_cards)
                        print("Computer cards:")
                        show_card1 = computer_cards[0]
                        print("Card:", show_card1)
                        computer_cards.remove(show_card1)
                        for card in computer_cards:
                            total_c_cards += card
                            print("Card: ?")
                        computer_cards.insert(0, show_card1)
                        total_c_cards += show_card1
                        print("-"*2*SIZE+"---")
                        # these will go to the player
                        start_cards = random.sample(cards, 2)
                        your_cards.extend(start_cards)
                        print("Your cards:")
                        for card in your_cards:
                            total_p_cards += card
                            print("Card:", card)
                        print(Fore.GREEN + "Total of your cards:", str(total_p_cards) + Style.RESET_ALL)
                        print("-"*2*SIZE+"---")
                        # now the betting starts
                        betting = True
                        while betting == True:
                            clear_screen()
                            print_casino(SIZE)
                            print_UI(turn, health, hunger, armour, gold)
                            return_message(message, SIZE)
                            message = Fore.YELLOW + "Pot: " + str(pot) + Style.RESET_ALL
                            print("Computer cards:")
                            show_card1 = computer_cards[0]
                            print("Card:", show_card1)
                            computer_cards.remove(show_card1)
                            total_c_cards = 0
                            for card in computer_cards:
                                total_c_cards += card
                                print("Card: ?")
                            computer_cards.insert(0, show_card1)
                            total_c_cards += show_card1
                            print("-"*2*SIZE+"---")
                            print("Your cards:")
                            total_p_cards = 0
                            for card in your_cards:
                                total_p_cards += card
                                print("Card:", card)
                            print(Fore.GREEN + "Total of your cards:", str(total_p_cards) + Style.RESET_ALL)
                            print("-"*2*SIZE+"---")
                            if gold < 5:
                                message = Fore.RED + "You ran out of money that you could spend." + Style.RESET_ALL
                                break
                            bet = input("How much would you like to bet? (5 to 100)\n> ")
                            try:
                                bet = int(bet)
                            except ValueError:
                                message = Fore.RED + "Please only type a number (ie '3')" + Style.RESET_ALL
                                continue
                            if (bet < 5) or (bet > 100):
                                message = Fore.RED + "You must bet between 5 and 100" + Style.RESET_ALL
                                continue
                            else:
                                gold -= bet
                                pot += bet *2
                                message = Fore.YELLOW + "Pot: " + str(pot) + Style.RESET_ALL
                                choosing_hit_stand_fold = True
                                while choosing_hit_stand_fold == True:
                                    clear_screen()
                                    print_casino(SIZE)
                                    print_UI(turn, health, hunger, armour, gold)
                                    return_message(message, SIZE)
                                    print("Computer cards:")
                                    show_card1 = computer_cards[0]
                                    print("Card:", show_card1)
                                    computer_cards.remove(show_card1)
                                    for card in computer_cards:
                                        print("Card: ?")
                                    computer_cards.insert(0, show_card1)
                                    print("-"*2*SIZE+"---")
                                    print("Your cards:")
                                    for card in your_cards:
                                        print("Card:", card)
                                    print(Fore.GREEN + "Total of your cards:", str(total_p_cards) + Style.RESET_ALL)
                                    print("-"*2*SIZE+"---")
                                    print(Fore.RED + "Don't go over 21!" + Style.RESET_ALL)
                                    hit_stand_fold = input("1)Hit  2)Stand  3)Fold\n> ").capitalize()
                                    if (hit_stand_fold == "Hit") or (hit_stand_fold == "1"):
                                        add_card = random.choice(cards)
                                        cards.remove(add_card)
                                        your_cards.append(add_card)
                                        total_p_cards += add_card
                                        choosing_hit_stand_fold = False
                                    elif (hit_stand_fold == "Stand") or (hit_stand_fold == "2"):
                                        hit_stand_fold ="Stand"
                                        choosing_hit_stand_fold = False
                                    else:
                                        message = Fore.RED + "Please write only 'Hit' 'Stand' or 'Fold'" + Style.RESET_ALL
                                        continue

                            # total_c_cards += add_card
                            if total_p_cards > 21:
                                message = Fore.RED + "You busted, you lose." + Style.RESET_ALL
                                break

                            c_hit_stand_fold = "Hit"
                            if (total_c_cards >= 16) and (total_c_cards <= 21):
                                c_hit_stand_fold = "Stand"
                            elif (total_c_cards < 16):
                                add_card = random.choice(cards)
                                total_p_cards += add_card
                                cards.remove(add_card)
                                computer_cards.append(add_card)
                            else:
                                message = Fore.GREEN + "Computer busts, you win! +{}".format(pot) + Style.RESET_ALL
                                gold += pot
                                break

                            if c_hit_stand_fold == "Stand" and hit_stand_fold == "Stand":
                                print(total_c_cards)
                                print(total_p_cards)
                                total_p_cards = 0
                                for card in your_cards:
                                    total_p_cards += card
                                total_c_cards = 0
                                for card in computer_cards:
                                    total_c_cards += card
                                print(total_c_cards)
                                print(total_p_cards)
                                input("> ")
                                if total_p_cards > total_c_cards:
                                    message = Fore.GREEN + "You win! +{}".format(pot) + Style.RESET_ALL
                                    gold += pot
                                    break
                                elif total_p_cards < total_c_cards:
                                    message = Fore.RED + "You lose :(" + Style.RESET_ALL
                                    break
                                else:
                                    message =  Fore.BLUE + "You tie +{}".format(pot) + Style.RESET_ALL
                                    gold += round(pot/2)
                                    break
                            else:
                                continue
                    else:
                        message = Fore.BLUE + "{} isn't the name or number of a game." + Style.RESET_ALL


        #
        # mysterious area
        #
            if (player == mysterious1):
                event = mysterious1_event
                if event == "gold":
                    sack_size = random.choice(["tiny", "small", "heavy", "large"])
                    if sack_size == "tiny":
                        gold_in_sack = random.randint(1,9)
                    if sack_size == "small":
                        gold_in_sack = random.randint(10,19)
                    if sack_size == "heavy":
                        gold_in_sack = random.randint(20,29)
                    if sack_size == "large":
                        gold_in_sack = random.randint(30,40)
                    print("You stumble apon a {} sack of gold coins.".format(sack_size))
                    take_coins = input("Take the coins? (y/n)\n> ").lower()
                    if take_coins == "y":
                        message = Fore.MAGENTA+"You got {} gold.".format(gold_in_sack)+Style.RESET_ALL
                        gold += gold_in_sack
                    else:
                        message = Fore.MAGENTA+"You decide to leave the coins for someone else."+Style.RESET_ALL

                elif event == "dead body":
                    dig_up_body = input("You are trotting along when you notice a leg sticking out of the ground. Would you like to try and dig the body up?\n(y/n)\n> ").lower()
                    if dig_up_body == "y":
                        name_tag = random.choice(["Grete", "Ben", "Kate", "Sophia"])
                        if name_tag == "Grete":
                            item_on_body = {
                            "name":"Brown fluffy jacket",
                            "durability":None,
                            "effect":None,
                            "value":125,
                            "type":"clothing"
                            }
                            fashion += 3
                        elif name_tag == "Ben":
                            item_on_body = {
                            "name":"Baseball cap",
                            "durability":3,
                            "effect":5,
                            "value":10,
                            "type":"armour"
                            }
                        elif name_tag == "Kate":
                            item_on_body = {
                            "name":"Volleyball",
                            "durability":None,
                            "effect":None,
                            "value":75,
                            "type":"toy"
                            }
                        elif name_tag == "Sophia":
                            item_on_body = {
                            "name":"Shinguard",
                            "durability":None,
                            "effect":None,
                            "value":100,
                            "type":"clothing"
                            }
                            max_health += 10
                        print("\nYou begin to dig up the leg. Slowly a body begins to emerge, face up.\nThere is a large flat stone on the corpses stomach, which has '{}' engraved in it.\nThis name seems to have belonged to the poor individual that lays here.".format(name_tag))
                        search_body = input("Would you like to search the body?\n(y/n)\n> ").lower()
                        if search_body == "y":
                            take_item_from_body = input("\nThere is a {} that you think you can take. Do you take it?\n(y/n)\n> ".format(item_on_body.get("name"))).lower()
                            if take_item_from_body == "y":
                                inventory.append(item_on_body)
                                message = Fore.MAGENTA+"You got a {}.".format(item_on_body.get("name"))+Style.RESET_ALL
                        else:
                            message = Fore.MAGENTA+"You leave the open grave and continue on your journey."+Style.RESET_ALL
                    else:
                        message = Fore.MAGENTA+"You leave the leg undisturbed and continue on your journey."+Style.RESET_ALL

                elif event == "ambush":
                    monster_health = 40
                    fighting = True
                    while fighting:
                        while True:
                            clear_screen()
                            print_monster(monster_health, SIZE)
                            print_UI(turn, health, hunger, armour, gold)
                            return_message(message, SIZE)
                            message = default_message
                            # players turn
                            print("Equiped weapon:", equiped_weapon.get("name"))
                            print("-"*2*SIZE+"---")
                            print("You can:  1)Attack  2)Wait  3)Run  4)Change weapon")
                            player_move = input("> ")
                            if (player_move.capitalize() == "Attack") or (player_move == "1"):
                                if len(inventory) <= 2:
                                    attack_chance = random.randint(0,5)
                                if len(inventory) <= 4 and len(inventory) > 2:
                                    attack_chance = random.randint(0,4)
                                if len(inventory) <= 6 and len(inventory) > 4:
                                    attack_chance = random.randint(0,3)
                                if len(inventory) >= 7:
                                    attack_chance = random.randint(0,2)
                                if attack_chance != 0:
                                    if equiped_weapon != Fists:
                                        durability = equiped_weapon.pop("durability")
                                        durability -= 1
                                        if durability == 0:
                                            inventory.remove(equiped_weapon)
                                            equiped_weapon = Fists
                                        else:
                                            equiped_weapon.update({"durability":durability})
                                    message = Fore.GREEN + "You attack the monster with your {} and do {} damage.".format(equiped_weapon.get("name"), equiped_weapon.get("effect")) + Style.RESET_ALL
                                    monster_health -= equiped_weapon.get("effect")
                                else:
                                    message = Fore.RED + "You swing with your {} but you miss.".format(equiped_weapon.get("name")) + Style.RESET_ALL
                            elif (player_move.capitalize() == "Wait") or (player_move.capitalize() == "2"):
                                add_health = random.randint(1,4)*2
                                health += add_health
                                if health > max_health:
                                    health = max_health
                                message = Fore.BLUE + "You rest and gain {} health.".format(add_health) + Style.RESET_ALL
                            elif (player_move.capitalize() == "Run") or (player_move.capitalize() == "3"):
                                if len(inventory) <= 2:
                                    run_away_chance = random.randint(0,1)
                                if len(inventory) <= 4 and len(inventory) > 2:
                                    run_away_chance = random.randint(0,2)
                                if len(inventory) <= 6 and len(inventory) > 4:
                                    run_away_chance = random.randint(0,3)
                                if len(inventory) >= 7:
                                    run_away_chance = random.randint(0,4)

                                if run_away_chance == 0:
                                    message = Fore.GREEN + "You manage to run from the monster!" + Style.RESET_ALL
                                    escape_move = escape(player, SIZE)
                                    player, message, health = move_player(default_message, health, max_health, player, escape_move)
                                    fighting = False
                                    break
                                else:
                                    health -= 10
                                    message = Fore.RED + "You don't manage to escape the monster, -10 health." + Style.RESET_ALL
                                continue
                            elif (player_move.capitalize() == "Change") or (player_move.capitalize() == "Change weapon") or (player_move.capitalize() == "4"):
                                missing_item = True
                                print("-", Fists.get("name"), "  Durability: N/A", "  Damage:", Fists.get("effect"))
                                for item in inventory:
                                    if item.get("type") == "weapon":
                                        print("-", item.get("name"), "  Durability:", item.get("durability"), "  Damage:", item.get("effect"))
                                print("Which item would you like to use?")
                                weapon_change = input("> ")
                                for item in inventory:
                                    if weapon_change.capitalize() == "Fists":
                                        equiped_weapon = Fists
                                        missing_item = False
                                    elif weapon_change.capitalize() == item.get("name"):
                                        equiped_weapon = item
                                        missing_item = False
                                if missing_item == True:
                                    message = Fore.RED + "You don't have '{}'.".format(weapon_change) + Style.RESET_ALL
                                continue
                            else:
                                fumble_damage = random.randint(1,3)*2
                                message = Fore.BLUE+"You fumble around while chosing what to do. " + Fore.RED + "-{} health.".format(fumble_damage)+Style.RESET_ALL
                                health -= fumble_damage
                            # exit player turn
                            break
                        while True:
                            if health <= 0:
                                fighting = False
                                break
                            if monster_health <= 0:
                                kills += 1
                                fighting = False
                                monster_loot = random.choice(random.choice([foods, tools, clothes]))
                                inventory.append(monster_loot)
                                gold += 30
                                message = Fore.GREEN + "You killed a monster and got a {} and 30 gold.".format(monster_loot.get("name")) + Style.RESET_ALL
                                break
                            clear_screen()
                            print_monster(monster_health, SIZE)
                            print_UI(turn, health, hunger, armour, gold)
                            return_message(message, SIZE)
                            message = default_message
                            time.sleep(1)
                            # monsters turn
                            original_armour = armour
                            monster_damage = random.randint(1,3)*3
                            if monster_damage > armour:
                                monster_damage -= armour
                                armour = 0
                            else:
                                armour -= monster_damage
                                monster_damage = 0
                            health -= monster_damage
                            if health <= 0:
                                fighting = False
                                break
                            message = Fore.RED + "The monster claws you. -{} health, -{} armour.".format(monster_damage, original_armour - armour) + Style.RESET_ALL
                            # exit monsters turn
                            break

                mysterious1 = None

            elif (player == mysterious2):
                event = mysterious2_event
                if event == "gold":
                    sack_size = random.choice(["tiny", "small", "heavy", "large"])
                    if sack_size == "tiny":
                        gold_in_sack = random.randint(1,9)
                    if sack_size == "small":
                        gold_in_sack = random.randint(10,19)
                    if sack_size == "heavy":
                        gold_in_sack = random.randint(20,29)
                    if sack_size == "large":
                        gold_in_sack = random.randint(30,40)
                    print("You stumble apon a {} sack of gold coins.".format(sack_size))
                    take_coins = input("Take the coins? (y/n)\n> ").lower()
                    if take_coins == "y":
                        message = Fore.MAGENTA+"You got {} gold.".format(gold_in_sack)+Style.RESET_ALL
                        gold += gold_in_sack
                    else:
                        message = Fore.MAGENTA+"You decide to leave the coins for someone else."+Style.RESET_ALL

                elif event == "dead body":
                    dig_up_body = input("You are trotting along when you notice a leg sticking out of the ground. Would you like to try and dig the body up?\n(y/n)\n> ").lower()
                    if dig_up_body == "y":
                        name_tag = random.choice(["Grete", "Ben", "Kate", "Sophia"])
                        if name_tag == "Grete":
                            item_on_body = {
                            "name":"Brown fluffy jacket",
                            "durability":None,
                            "effect":None,
                            "value":125,
                            "type":"clothing"
                            }
                            fashion += 3
                        elif name_tag == "Ben":
                            item_on_body = {
                            "name":"Baseball bat",
                            "durability":4,
                            "effect":13,
                            "value":60,
                            "type":"weapon"
                            }
                        elif name_tag == "Kate":
                            item_on_body = {
                            "name":"Volleyball",
                            "durability":None,
                            "effect":None,
                            "value":75,
                            "type":"toy"
                            }
                        elif name_tag == "Sophia":
                            item_on_body = {
                            "name":"Shinguard",
                            "durability":None,
                            "effect":None,
                            "value":100,
                            "type":"clothing"
                            }
                            max_health += 10
                        print("\nYou begin to dig up the leg. Slowly a body begins to emerge, face up.\nThere is a large flat stone on the corpses stomach, which has '{}' engraved in it.\nThis name seems to have belonged to the poor individual that lays here.".format(name_tag))
                        search_body = input("Would you like to search the body?\n(y/n)\n> ").lower()
                        if search_body == "y":
                            take_item_from_body = input("\nThere is a {} that you think you can take. Do you take it?\n(y/n)\n> ".format(item_on_body.get("name"))).lower()
                            if take_item_from_body == "y":
                                inventory.append(item_on_body)
                                message = Fore.MAGENTA+"You got a {}.".format(item_on_body.get("name"))+Style.RESET_ALL
                        else:
                            message = Fore.MAGENTA+"You leave the open grave and continue on your journey."+Style.RESET_ALL
                    else:
                        message = Fore.MAGENTA+"You leave the leg undisturbed and continue on your journey."+Style.RESET_ALL

                elif event == "ambush":
                    monster_health = 20
                    fighting = True
                    while fighting:
                        while True:
                            clear_screen()
                            print_monster(monster_health, SIZE)
                            print_UI(turn, health, hunger, armour, gold)
                            return_message(message, SIZE)
                            message = default_message
                            # players turn
                            print("Equiped weapon:", equiped_weapon.get("name"))
                            print("-"*2*SIZE+"---")
                            print("You can:  1)Attack  2)Wait  3)Run  4)Change weapon")
                            player_move = input("> ")
                            if (player_move.capitalize() == "Attack") or (player_move == "1"):
                                if len(inventory) <= 2:
                                    attack_chance = random.randint(0,5)
                                if len(inventory) <= 4 and len(inventory) > 2:
                                    attack_chance = random.randint(0,4)
                                if len(inventory) <= 6 and len(inventory) > 4:
                                    attack_chance = random.randint(0,3)
                                if len(inventory) >= 7:
                                    attack_chance = random.randint(0,2)
                                if attack_chance != 0:
                                    if equiped_weapon != Fists:
                                        durability = equiped_weapon.pop("durability")
                                        durability -= 1
                                        if durability == 0:
                                            inventory.remove(equiped_weapon)
                                            equiped_weapon = Fists
                                        else:
                                            equiped_weapon.update({"durability":durability})
                                    message = Fore.GREEN + "You attack the monster with your {} and do {} damage.".format(equiped_weapon.get("name"), equiped_weapon.get("effect")) + Style.RESET_ALL
                                    monster_health -= equiped_weapon.get("effect")
                                else:
                                    message = Fore.RED + "You swing with your {} but you miss.".format(equiped_weapon.get("name")) + Style.RESET_ALL
                            elif (player_move.capitalize() == "Wait") or (player_move.capitalize() == "2"):
                                add_health = random.randint(1,4)*2
                                health += add_health
                                if health > max_health:
                                    health = max_health
                                message = Fore.BLUE + "You rest and gain {} health.".format(add_health) + Style.RESET_ALL
                            elif (player_move.capitalize() == "Run") or (player_move.capitalize() == "3"):
                                if len(inventory) <= 2:
                                    run_away_chance = random.randint(0,1)
                                if len(inventory) <= 4 and len(inventory) > 2:
                                    run_away_chance = random.randint(0,2)
                                if len(inventory) <= 6 and len(inventory) > 4:
                                    run_away_chance = random.randint(0,3)
                                if len(inventory) >= 7:
                                    run_away_chance = random.randint(0,4)

                                if run_away_chance == 0:
                                    message = Fore.GREEN + "You manage to run from the monster!" + Style.RESET_ALL
                                    escape_move = escape(player, SIZE)
                                    player, message, health = move_player(default_message, health, max_health, player, escape_move)
                                    fighting = False
                                    break
                                else:
                                    health -= 10
                                    message = Fore.RED + "You don't manage to escape the monster, -10 health." + Style.RESET_ALL
                                continue
                            elif (player_move.capitalize() == "Change") or (player_move.capitalize() == "Change weapon") or (player_move.capitalize() == "4"):
                                missing_item = True
                                print("-", Fists.get("name"), "  Durability: N/A", "  Damage:", Fists.get("effect"))
                                for item in inventory:
                                    if item.get("type") == "weapon":
                                        print("-", item.get("name"), "  Durability:", item.get("durability"), "  Damage:", item.get("effect"))
                                print("Which item would you like to use?")
                                weapon_change = input("> ")
                                for item in inventory:
                                    if weapon_change.capitalize() == "Fists":
                                        equiped_weapon = Fists
                                        missing_item = False
                                    elif weapon_change.capitalize() == item.get("name"):
                                        equiped_weapon = item
                                        missing_item = False
                                if missing_item == True:
                                    message = Fore.RED + "You don't have '{}'.".format(weapon_change) + Style.RESET_ALL
                                continue
                            else:
                                fumble_damage = random.randint(1,3)*2
                                message = Fore.BLUE+"You fumble around while chosing what to do. " + Fore.RED + "-{} health.".format(fumble_damage)+Style.RESET_ALL
                                health -= fumble_damage
                            # exit player turn
                            break
                        while True:
                            if health <= 0:
                                fighting = False
                                break
                            if monster_health <= 0:
                                kills += 1
                                fighting = False
                                monster_loot = random.choice(random.choice([foods, tools, clothes]))
                                inventory.append(monster_loot)
                                gold += 30
                                message = Fore.GREEN + "You killed a monster and got a {} and 30 gold.".format(monster_loot.get("name")) + Style.RESET_ALL
                                break
                            clear_screen()
                            print_monster(monster_health, SIZE)
                            print_UI(turn, health, hunger, armour, gold)
                            return_message(message, SIZE)
                            message = default_message
                            time.sleep(1)
                            # monsters turn
                            original_armour = armour
                            monster_damage = random.randint(1,4)*4
                            if monster_damage > armour:
                                monster_damage -= armour
                                armour = 0
                            else:
                                armour -= monster_damage
                                monster_damage = 0
                            health -= monster_damage
                            if health <= 0:
                                fighting = False
                                break
                            message = Fore.RED + "The monster claws you. -{} health, -{} armour.".format(monster_damage, original_armour - armour) + Style.RESET_ALL
                            # exit monsters turn
                            break

                mysterious2 = None

                # elif event == "abandond house":

                # elif event == "mysterious box":

                # elif event == "bear trap":


        #
        # potato farm
        #
            if (player == potato_farm):
                message = Fore.GREEN+"You spot a small potato farm."+Style.RESET_ALL
                clear_screen()
                draw_map(
                    monster1, monster2, monster3,
                    potato_farm, mysterious1, mysterious2,
                    shop1,
                    casino1,
                    chest1, chest2, chest3,
                    berries1, berries2, berries3,
                    player,
                    SIZE)
                print_UI(turn, health, hunger, armour, gold)
                print_inventory(inventory)
                return_message(message, SIZE)
                print("A lady waves you over to her, she is standing behind\na small counter that says 'POTATO SALE'")
                go_to_lady = input("Do you walk up to her?\n(y/n)\n> ").lower()
                message = default_message
                if go_to_lady == "y":
                    while True:
                        clear_screen()
                        print_potato_farmer(SIZE)
                        print_UI(turn, health, hunger, armour, gold)
                        print_inventory(inventory)
                        return_message(message, SIZE)
                        print("Hello! I have some wares that I can sell you, take a look:")
                        for item in potato_shop1:
                            print(item.get("name"), "for {}G.".format(item.get("value")))
                        print("-"*2*SIZE+"---")
                        buy_item = input("What would you like to buy? ('exit' to exit)\n> ").capitalize()
                        if buy_item == "Exit":
                            break
                        for item in potato_shop1:
                            if buy_item == item.get("name"):
                                if gold < item.get("value"):
                                    message = Fore.RED + "You don't have enough money to afford {}.".format(item.get("name")) + Style.RESET_ALL
                                    break
                                else:
                                    print("Are you sure you want to buy 1 {} for {}G.".format(item.get("name"), item.get("value")))
                                    confirm_purchase = input("(y/n)\n> ").lower()
                                    if confirm_purchase == "y":
                                        gold -= item.get("value")
                                        inventory.append(item)
                                        potato_shop1.remove(item)
                                        message = Fore.MAGENTA + "You bought 1 {} for {}G.".format(item.get("name"), item.get("value")) + Style.RESET_ALL
                                        break
                                    else:
                                        message = Fore.RED + "Purchase cancelled." + Style.RESET_ALL
                                        break
                            message = Fore.RED + "Sorry, we don't have '{}' in stock.".format(buy_item) + Style.RESET_ALL
                else:
                    print("You pretend not to see the lady and continue on your way.")


        #
        # monster managemet area
        #
            if (player == monster1):
                monster_health = monster_max_health
                fighting = True
                while fighting:
                    while True:
                        clear_screen()
                        print_monster(monster_health, SIZE)
                        print_UI(turn, health, hunger, armour, gold)
                        return_message(message, SIZE)
                        message = default_message
                        # players turn
                        print("Equiped weapon:", equiped_weapon.get("name"))
                        print("-"*2*SIZE+"---")
                        print("You can:  1)Attack  2)Wait  3)Run  4)Change weapon")
                        player_move = input("> ")
                        if (player_move.capitalize() == "Attack") or (player_move == "1"):
                            if len(inventory) <= 2:
                                attack_chance = random.randint(0,5)
                            if len(inventory) <= 4 and len(inventory) > 2:
                                attack_chance = random.randint(0,4)
                            if len(inventory) <= 6 and len(inventory) > 4:
                                attack_chance = random.randint(0,3)
                            if len(inventory) >= 7:
                                attack_chance = random.randint(0,2)
                            if attack_chance != 0:
                                if equiped_weapon != Fists:
                                    durability = equiped_weapon.pop("durability")
                                    durability -= 1
                                    if durability == 0:
                                        inventory.remove(equiped_weapon)
                                        equiped_weapon = Fists
                                    else:
                                        equiped_weapon.update({"durability":durability})
                                message = Fore.GREEN + "You attack the monster with your {} and do {} damage.".format(equiped_weapon.get("name"), equiped_weapon.get("effect")) + Style.RESET_ALL
                                monster_health -= equiped_weapon.get("effect")
                            else:
                                message = Fore.RED + "You swing with your {} but you miss.".format(equiped_weapon.get("name")) + Style.RESET_ALL
                        elif (player_move.capitalize() == "Wait") or (player_move.capitalize() == "2"):
                            add_health = random.randint(1,4)*2
                            health += add_health
                            if health > max_health:
                                health = max_health
                            message = Fore.BLUE + "You rest and gain {} health.".format(add_health) + Style.RESET_ALL
                        elif (player_move.capitalize() == "Run") or (player_move.capitalize() == "3"):
                            if len(inventory) <= 2:
                                run_away_chance = random.randint(0,1)
                            if len(inventory) <= 4 and len(inventory) > 2:
                                run_away_chance = random.randint(0,2)
                            if len(inventory) <= 6 and len(inventory) > 4:
                                run_away_chance = random.randint(0,3)
                            if len(inventory) >= 7:
                                run_away_chance = random.randint(0,4)

                            if run_away_chance == 0:
                                message = Fore.GREEN + "You manage to run from the monster!" + Style.RESET_ALL
                                escape_move = escape(player, SIZE)
                                player, message, health = move_player(default_message, health, max_health, player, escape_move)
                                fighting = False
                                break
                            else:
                                health -= 10
                                message = Fore.RED + "You don't manage to escape the monster, -10 health." + Style.RESET_ALL
                            continue
                        elif (player_move.capitalize() == "Change") or (player_move.capitalize() == "Change weapon") or (player_move.capitalize() == "4"):
                            missing_item = True
                            print("-", Fists.get("name"), "  Durability: N/A", "  Damage:", Fists.get("effect"))
                            for item in inventory:
                                if item.get("type") == "weapon":
                                    print("-", item.get("name"), "  Durability:", item.get("durability"), "  Damage:", item.get("effect"))
                            print("Which item would you like to use?")
                            weapon_change = input("> ")
                            for item in inventory:
                                if weapon_change.capitalize() == "Fists":
                                    equiped_weapon = Fists
                                    missing_item = False
                                elif weapon_change.capitalize() == item.get("name"):
                                    equiped_weapon = item
                                    missing_item = False
                            if missing_item == True:
                                message = Fore.RED + "You don't have '{}'.".format(weapon_change) + Style.RESET_ALL
                            continue
                        else:
                            fumble_damage = random.randint(1,3)*2
                            message = Fore.BLUE+"You fumble around while chosing what to do. " + Fore.RED + "-{} health.".format(fumble_damage)+Style.RESET_ALL
                            health -= fumble_damage
                        # exit player turn
                        break
                    while True:
                        if health <= 0:
                            fighting = False
                            break
                        if monster_health <= 0:
                            fighting = False
                            monster1_respawn = turn + random.randint(2,5)
                            monster_loot = random.choice(foods)
                            inventory.append(monster_loot)
                            kills += 1
                            monster1 = None
                            message = Fore.GREEN + "You killed a monster and got a {}.".format(monster_loot.get("name")) + Style.RESET_ALL
                            break
                        clear_screen()
                        print_monster(monster_health, SIZE)
                        print_UI(turn, health, hunger, armour, gold)
                        return_message(message, SIZE)
                        message = default_message
                        time.sleep(1)
                        # monsters turn
                        original_armour = armour
                        monster_damage = random.randint(1,3)*3
                        if monster_damage > armour:
                            monster_damage -= armour
                            armour = 0
                        else:
                            armour -= monster_damage
                            monster_damage = 0
                        health -= monster_damage
                        if health <= 0:
                            fighting = False
                            break
                        message = Fore.RED + "The monster claws you. -{} health, -{} armour.".format(monster_damage, original_armour - armour) + Style.RESET_ALL
                        # exit monsters turn
                        break

            if (player == monster2):
                monster_health = monster_max_health
                fighting = True
                while fighting:
                    while True:
                        clear_screen()
                        print_monster(monster_health, SIZE)
                        print_UI(turn, health, hunger, armour, gold)
                        return_message(message, SIZE)
                        message = default_message
                        # players turn
                        print("Equiped weapon:", equiped_weapon.get("name"))
                        print("-"*2*SIZE+"---")
                        print("You can:  1)Attack  2)Wait  3)Run  4)Change weapon")
                        player_move = input("> ")
                        if (player_move.capitalize() == "Attack") or (player_move == "1"):
                            if len(inventory) <= 2:
                                attack_chance = random.randint(0,5)
                            if len(inventory) <= 4 and len(inventory) > 2:
                                attack_chance = random.randint(0,4)
                            if len(inventory) <= 6 and len(inventory) > 4:
                                attack_chance = random.randint(0,3)
                            if len(inventory) >= 7:
                                attack_chance = random.randint(0,2)
                            if attack_chance != 0:
                                if equiped_weapon != Fists:
                                    durability = equiped_weapon.pop("durability")
                                    durability -= 1
                                    if durability == 0:
                                        inventory.remove(equiped_weapon)
                                        equiped_weapon = Fists
                                    else:
                                        equiped_weapon.update({"durability":durability})
                                message = Fore.GREEN + "You attack the monster with your {} and do {} damage.".format(equiped_weapon.get("name"), equiped_weapon.get("effect")) + Style.RESET_ALL
                                monster_health -= equiped_weapon.get("effect")
                            else:
                                message = Fore.RED + "You swing with your {} but you miss.".format(equiped_weapon.get("name")) + Style.RESET_ALL
                        elif (player_move.capitalize() == "Wait") or (player_move.capitalize() == "2"):
                            add_health = random.randint(1,4)*2
                            health += add_health
                            if health > max_health:
                                health = max_health
                            message = Fore.BLUE + "You rest and gain {} health.".format(add_health) + Style.RESET_ALL
                        elif (player_move.capitalize() == "Run") or (player_move.capitalize() == "3"):
                            if len(inventory) <= 2:
                                run_away_chance = random.randint(0,1)
                            if len(inventory) <= 4 and len(inventory) > 2:
                                run_away_chance = random.randint(0,2)
                            if len(inventory) <= 6 and len(inventory) > 4:
                                run_away_chance = random.randint(0,3)
                            if len(inventory) >= 7:
                                run_away_chance = random.randint(0,4)

                            if run_away_chance == 0:
                                message = Fore.GREEN + "You manage to run from the monster!" + Style.RESET_ALL
                                escape_move = escape(player, SIZE)
                                player, message, health = move_player(default_message, health, max_health, player, escape_move)
                                fighting = False
                                break
                            else:
                                health -= 10
                                message = Fore.RED + "You don't manage to escape the monster, -10 health." + Style.RESET_ALL
                            continue
                        elif (player_move.capitalize() == "Change") or (player_move.capitalize() == "Change weapon") or (player_move.capitalize() == "4"):
                            missing_item = True
                            print("-", Fists.get("name"), "  Durability: N/A", "  Damage:", Fists.get("effect"))
                            for item in inventory:
                                if item.get("type") == "weapon":
                                    print("-", item.get("name"), "  Durability:", item.get("durability"), "  Damage:", item.get("effect"))
                            print("Which item would you like to use?")
                            weapon_change = input("> ")
                            for item in inventory:
                                if weapon_change.capitalize() == "Fists":
                                    equiped_weapon = Fists
                                    missing_item = False
                                elif weapon_change.capitalize() == item.get("name"):
                                    equiped_weapon = item
                                    missing_item = False
                            if missing_item == True:
                                message = Fore.RED + "You don't have '{}'.".format(weapon_change) + Style.RESET_ALL
                            continue
                        else:
                            fumble_damage = random.randint(1,3)*2
                            message = Fore.BLUE+"You fumble around while chosing what to do. " + Fore.RED + "-{} health.".format(fumble_damage)+Style.RESET_ALL
                            health -= fumble_damage
                        # exit player turn
                        break
                    while True:
                        if health <= 0:
                            fighting = False
                            break
                        if monster_health <= 0:
                            fighting = False
                            monster2_respawn = turn + random.randint(2,5)
                            monster_loot = random.choice(foods)
                            inventory.append(monster_loot)
                            kills += 1
                            monster2 = None
                            message = Fore.GREEN + "You killed a monster and got a {}.".format(monster_loot.get("name")) + Style.RESET_ALL
                            break
                        clear_screen()
                        print_monster(monster_health, SIZE)
                        print_UI(turn, health, hunger, armour, gold)
                        return_message(message, SIZE)
                        message = default_message
                        time.sleep(1)
                        # monsters turn
                        original_armour = armour
                        monster_damage = random.randint(1,3)*3
                        if monster_damage > armour:
                            monster_damage -= armour
                            armour = 0
                        else:
                            armour -= monster_damage
                            monster_damage = 0
                        health -= monster_damage
                        if health <= 0:
                            fighting = False
                            break
                        message = Fore.RED + "The monster claws you. -{} health, -{} armour.".format(monster_damage, original_armour - armour) + Style.RESET_ALL
                        # exit monsters turn
                        break

            if (player == monster3):
                monster_health = monster_max_health
                fighting = True
                while fighting:
                    while True:
                        clear_screen()
                        print_monster(monster_health, SIZE)
                        print_UI(turn, health, hunger, armour, gold)
                        return_message(message, SIZE)
                        message = default_message
                        # players turn
                        print("Equiped weapon:", equiped_weapon.get("name"))
                        print("-"*2*SIZE+"---")
                        print("You can:  1)Attack  2)Wait  3)Run  4)Change weapon")
                        player_move = input("> ")
                        if (player_move.capitalize() == "Attack") or (player_move == "1"):
                            if len(inventory) <= 2:
                                attack_chance = random.randint(0,5)
                            if len(inventory) <= 4 and len(inventory) > 2:
                                attack_chance = random.randint(0,4)
                            if len(inventory) <= 6 and len(inventory) > 4:
                                attack_chance = random.randint(0,3)
                            if len(inventory) >= 7:
                                attack_chance = random.randint(0,2)
                            if attack_chance != 0:
                                if equiped_weapon != Fists:
                                    durability = equiped_weapon.pop("durability")
                                    durability -= 1
                                    if durability == 0:
                                        inventory.remove(equiped_weapon)
                                        equiped_weapon = Fists
                                    else:
                                        equiped_weapon.update({"durability":durability})
                                message = Fore.GREEN + "You attack the monster with your {} and do {} damage.".format(equiped_weapon.get("name"), equiped_weapon.get("effect")) + Style.RESET_ALL
                                monster_health -= equiped_weapon.get("effect")
                            else:
                                message = Fore.RED + "You swing with your {} but you miss.".format(equiped_weapon.get("name")) + Style.RESET_ALL
                        elif (player_move.capitalize() == "Wait") or (player_move.capitalize() == "2"):
                            add_health = random.randint(1,4)*2
                            health += add_health
                            if health > max_health:
                                health = max_health
                            message = Fore.BLUE + "You rest and gain {} health.".format(add_health) + Style.RESET_ALL
                        elif (player_move.capitalize() == "Run") or (player_move.capitalize() == "3"):
                            if len(inventory) <= 2:
                                run_away_chance = random.randint(0,1)
                            if len(inventory) <= 4 and len(inventory) > 2:
                                run_away_chance = random.randint(0,2)
                            if len(inventory) <= 6 and len(inventory) > 4:
                                run_away_chance = random.randint(0,3)
                            if len(inventory) >= 7:
                                run_away_chance = random.randint(0,4)

                            if run_away_chance == 0:
                                message = Fore.GREEN + "You manage to run from the monster!" + Style.RESET_ALL
                                escape_move = escape(player, SIZE)
                                player, message, health = move_player(default_message, health, max_health, player, escape_move)
                                fighting = False
                                break
                            else:
                                health -= 10
                                message = Fore.RED + "You don't manage to escape the monster, -10 health." + Style.RESET_ALL
                            continue
                        elif (player_move.capitalize() == "Change") or (player_move.capitalize() == "Change weapon") or (player_move.capitalize() == "4"):
                            missing_item = True
                            print("-", Fists.get("name"), "  Durability: N/A", "  Damage:", Fists.get("effect"))
                            for item in inventory:
                                if item.get("type") == "weapon":
                                    print("-", item.get("name"), "  Durability:", item.get("durability"), "  Damage:", item.get("effect"))
                            print("Which item would you like to use?")
                            weapon_change = input("> ")
                            for item in inventory:
                                if weapon_change.capitalize() == "Fists":
                                    equiped_weapon = Fists
                                    missing_item = False
                                elif weapon_change.capitalize() == item.get("name"):
                                    equiped_weapon = item
                                    missing_item = False
                            if missing_item == True:
                                message = Fore.RED + "You don't have '{}'".format(weapon_change) + Style.RESET_ALL
                            continue
                        else:
                            fumble_damage = random.randint(1,3)*2
                            message = Fore.BLUE+"You fumble around while chosing what to do. " + Fore.RED + "-{} health".format(fumble_damage)+Style.RESET_ALL
                            health -= fumble_damage
                        # exit player turn
                        break
                    while True:
                        if health <= 0:
                            fighting = False
                            break
                        if monster_health <= 0:
                            fighting = False
                            monster3_respawn = turn + random.randint(2,5)
                            monster_loot = random.choice(foods)
                            inventory.append(monster_loot)
                            kills += 1
                            monster3 = None
                            message = Fore.GREEN + "You killed a monster and got a {}.".format(monster_loot.get("name")) + Style.RESET_ALL
                            break
                        clear_screen()
                        print_monster(monster_health, SIZE)
                        print_UI(turn, health, hunger, armour, gold)
                        return_message(message, SIZE)
                        message = default_message
                        time.sleep(1)
                        # monsters turn
                        original_armour = armour
                        monster_damage = random.randint(1,3)*3
                        if monster_damage > armour:
                            monster_damage -= armour
                            armour = 0
                        else:
                            armour -= monster_damage
                            monster_damage = 0
                        health -= monster_damage
                        if health <= 0:
                            fighting = False
                            break
                        message = Fore.RED + "The monster claws you. -{} health, -{} armour.".format(monster_damage, original_armour - armour) + Style.RESET_ALL
                        # exit monsters turn
                        break


        #
        # death management area
        #
            # if the player has 0 health, they die
            if health <= 0:
                playing = False
                clear_screen()
                print_death(turn, health, hunger, gold, kills, fashion)


        # error message if the player makes a move that is not valid
        else:
            message = (Fore.RED+"That is not a valid move."+Style.RESET_ALL)


    # if the game ends
    else:
        play_again = input("Play again? (y/n)\n> ").lower()
        if play_again != "n":
            game_loop()



#  !!! now we actually call the functions to make the game run: !!!  #

SIZE = 26
SIZE -= 1
set_grid(SIZE)
clear_screen()
tutorial()
print_title()
game_loop()

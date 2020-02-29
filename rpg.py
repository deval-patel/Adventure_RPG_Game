import random
import typing
from Monster import *
from Item import *
from Maps import *
"""
************************************************************************************************************************
Assignment Description:
Here is the RPG (Role-Playing Game) Assignment, the starter code is provided below.

The objective of this project is to create a text-based RPG with three fully functioning mini-games incorporated in
them. You will be required to write a story for the character who the user will be portraying, and guide them towards
their 3 tasks. Then you will code your 3 tasks/mini-games in the functions below,

Here are the following function descriptions:
     task1() is for Task #1
     task2() is for Task #2
     task3() is for Task #3
     task_lose() is for describing what the user wants to do after losing the task, either to try again or exit the
     game.
     end_game() is for the message displayed when the user wants to exit out the game after losing.
     final_ending() is for the final storyline after the user wins all 3 tasks.

As always, you are free to create additional helper functions needed to function your games. Be sure to uncomment the
pieces of code in the tasks, that you need to make the function work.

Have fun and enjoy!
************************************************************************************************************************
"""
# Put your name as CREATOR
CREATOR = 'Michael Marchello'
# Put the title of your RPG as RPG_NAME.
RPG_NAME = 'Old School'
"""
Global Variables:
password_collection: A collection of the user's obtained letters to the password
WIN: determines if the player won yet 
"""

password_collection = [['_', '_', '_', '_', '_', '_', '_', '_'],
                       ['_', '_', '_', '_', '_', '_', '_', '_'],
                       ['_', '_', '_', '_', '_', '_', '_', '_'],
                       ['_', '_', '_', '_', '_', '_', '_', '_'],
                       ['_', '_', '_', '_', '_', '_', '_', '_']]

password_store = [['e', 'l', 'e', 'v', 'a', 't', 'o', 'r'],
                  ['l', 'e', 'a', 'r', 'n', 'i', 'n', 'g'],
                  ['s', 'e', 'c', 'r', 'e', 't', 'i', 'n'],
                  ['p', 'r', 'i', 'n', 'c', 'i', 'p', 'a'],
                  ['l', 's', 'o', 'f', 'f', 'i', 'c', 'e']]

final_passwords = ["elevator", "", "", "", ""]

# All items
items = []
WIN = False
player = Player()
# current map that the player is on
ROW = 25
COL = 15
CURRENT_POSITION = [get_starting_position(1)[0], get_starting_position(1)[1]]
# Creates map of default 0's
SCREEN = [[0 for i in range(COL)] for j in range(ROW)]
current_map = [[0 for i in range(COL)] for j in range(ROW)]


def redraw():
    global SCREEN
    global current_map
    for row in range(ROW):
        for col in range(COL):
            SCREEN[row][col] = current_map[row][col]
    SCREEN[CURRENT_POSITION[0]][CURRENT_POSITION[1]] = 42


def check_password(floor):
    beep_message("In order to advance to the next floor you must enter a password")
    user_attempt = input("Enter password: ")
    # This checks if the password for your current floor is correct.
    if user_attempt == final_passwords[floor - 1]:
        load_floor(floor + 1)
    else:
        beep_message("Password is invalid. Please return to your classroom")


def load_floor(floor):
    global current_map
    beep_message("Password is valid. Please move on to the next floor")
    floor_map = get_floor(floor)
    global CURRENT_POSITION
    CURRENT_POSITION = [get_starting_position(floor)[0], get_starting_position(floor)[1]]
    for i in range(ROW):
        for j in range(COL):
            current_map[i][j] = floor_map[i][j]
    redraw()


def beep_message(message):
    print("*Beep*" + message + "*Beep*")

def r_p_s():
    valid_choice = True
    print ("Computer Login: Rock, Paper, Scissors")
    comp_wins = 0
    user_wins = 0
    # loop for the game
    while comp_wins != 2 or user_wins != 2:
        user_choice = input("Enter (r) Rock\n"
                            "      (p) Paper\n"
                            "      (s) Scissors\n"
                            "Your choice: ").lower().strip()

        if user_choice == 'r':
            user_choice = 'Rock'
        elif user_choice == 'p':
            user_choice = 'Paper'
        elif user_choice == 's':
            user_choice = 'Scissors'
        else:
            valid_choice = False

        random_num = random.randint(1, 3)
        if random_num == 1:
            comp_choice = "Rock"
        elif random_num == 2:
            comp_choice = "Paper"
        else:
            comp_choice = "Scissors"

        # check who won
        if user_choice == "Rock" and comp_choice == "Scissors":
            print("You picked " + user_choice + ". Computer picked " + comp_choice + ".\n"
                  "You win")
            user_wins += 1
        elif user_choice == "Paper" and comp_choice == "Rock":
            user_wins += 1
            print("You picked " + user_choice + ". Computer picked " + comp_choice + ".\n"
                                                                                     "You win")
        elif user_choice == "Scissors" and comp_choice == "Paper":
            user_wins += 1
            print("You picked " + user_choice + ". Computer picked " + comp_choice + ".\n"
                                                                                     "You win")
        elif user_choice == comp_choice:
            print("You picked " + user_choice + ". Computer picked " + comp_choice + ".\n"
                                                                                     "There was a tie")
        elif not valid_choice:
            print("Invalid input. Try again")
        else:
            comp_wins += 1
            print("You picked " + user_choice + ". Computer picked " + comp_choice + ".\n"
                                                                                     "You lose")
        print("\nUser wins:" + str(user_wins) + "\nComputer wins:" + str(comp_wins) +"\n")


    # check who won best 2/3
    if user_wins > comp_wins:
        print("You have logged in")
    else:
        print("Computer wins. Please try again")
        r_p_s()

#Pokemon game

def calculate_damage(move, opponent: Monster):
    #damage to opponent
    attack_damage = move[1] + player.get_attack()
    special_damage = move[2] + player.get_sp_attack()
    attack_damage *= ((100 - opponent.get_defence())/100)
    special_damage *= ((100 - opponent.get_sp_defence()) / 100)
    total = attack_damage + special_damage
    opponent.take_damage(total)

    #damage to player
    move = opponent.get_moves()[0]
    attack_damage = move[1] + opponent.get_attack()
    special_damage = move[2] + opponent.get_sp_attack()
    attack_damage *= ((100 - player.get_defence()) / 100)
    special_damage *= ((100 - player.get_sp_defence()) / 100)
    total = attack_damage + special_damage
    player.take_damage(total)

def get_choice():
    print("Your Moves:")
    for i, move in enumerate(player.moves):
        print(str(i + 1) + ": " + move[0] + "- Attack = " + str(move[1]) + ", Sp.Attack = " + str(move[2]))

    choice = input("Select your move (1,2,3,4):")
    if len(choice) != 1 or choice not in "1234":
        print("Choice not possible. Please try again.")
        return -1
    return int(choice)


def battle(opponent: Monster):
    while player.hp > 0 and opponent.get_hp() > 0:
        print("\n")
        choice = get_choice() - 1
        while choice == -1:
            choice = get_choice()
        move = player.get_moves()[choice]
        print("You used " + move[0] + ".")
        print(opponent.get_name() + " used " + opponent.get_moves()[0][0] + ".")
        print("\n")
        calculate_damage(move, opponent)
        print("Your HP: "+ str(player.get_hp()))
        print(opponent.get_name() + " HP: " + str(opponent.get_hp()))
        print("\n")

    print("Someone won")


def end_game():
    print("Thank you for playing this game! Hope you enjoyed!")
    exit()


def final_ending():
    # Wrap up your story to finish off the game.
    print("You won the game")
    exit()

def collect_item(item):
    if item:
        player.equip_item(item)
    else:
        x = random.randint(0, len(items)-1)
        item = items[x]
        player.equip_item(item)

    print ("You got a "+ item +".")

# MOVING FUNCTIONS
def move(x, y):
    # x is how much to move in the x direction, y is how much to move in the y direction
    global CURRENT_POSITION
    new_x = CURRENT_POSITION[0] + x
    new_y = CURRENT_POSITION[1] + y
    if not (0 <= new_x < ROW and 0 <= new_y < COL):
        print("You are out of range")
        return
    pos = current_map[new_x][new_y]
    if pos in {100, 101, 102}:
        CURRENT_POSITION[0] = new_x
        CURRENT_POSITION[1] = new_y
        random_chance = random.randint(1, 10)
        print(random_chance)
        if random_chance == 2:
            x = random.randint(1, 5)
            if (x == 1):
                battle(Bear())
            elif (x == 2):
                battle(Raccoon())
            elif (x == 3):
                battle(Fox())
            elif (x == 4):
                battle(Snake())
            else:
                battle(Wolf())

    # collect item and don't pass through the space.
    elif pos == 2:
        pass
    # collect item and don't pass through the space. Play rock paper scissors
    elif pos == 3:
        pass
    # collect item and don't pass through the space.
    elif pos == 4:
        pass
    # collect item and don't pass through the space.
    elif pos == 5:
        pass
    # collect item and don't pass through the space.
    elif pos == 6:
        pass
    # message pops up and don't go through
    elif pos == 7:
        pass
    # play rock paper scissors and don't go through
    elif pos == 8:
        r_p_s()

    # message pops up and don't go through
    elif pos == 9:
        pass
    # collect item and don't pass through the space.
    elif pos == 10:
        pass
    # interact with and don;t go through
    elif pos == 11:
        pass
    # message pops up and don't go through.
    elif pos == 12:
        pass
    # message pops up and don't go through.
    elif pos == 13:
        pass
    # message pops up and don't go through.
    elif pos == 14:
        pass
    # interact with and don't go through.
    elif pos == 15:
        pass
    # collect item and repalce with ground
    elif pos == 16:
        pass
    # collect item and don't go through
    elif pos == 17:
        pass
    # Room 1
    elif pos == 18:
        load_floor(ROOM1)
    # Room 2
    elif pos == 19:
        load_floor(ROOM2)
    # Room 3
    elif pos == 20:
        load_floor(ROOM3)
    # Load next floor when entered
    elif pos == 21:
        load_floor(FLOOR2)
    # Load next floor when entered
    elif pos == 22:
        load_floor(FLOOR3)
    # Load next floor when entered
    elif pos == 23:
        load_floor(FLOOR4)
    # Recieve an ending when interacted with
    elif pos == 24:
        pass
    # message pops up and don't go through
    elif pos == 25:
        pass
    # enter to get to the locked door in the basement
    elif pos == 26:
        pass
    # collect item and don't go through
    elif pos == 27:
        pass
    # collect item and replace with the ground
    elif pos == 28:
        pass
    # load comp room when entered
    elif pos == 29:
        load_floor(COMPUTER_ROOM)
    # load next floor when entered
    elif pos == 30:
        load_floor(FLOOR5)
    # message pops up and don't go through
    elif pos == 31:
        pass
    # load staff room when entered
    elif pos == 32:
        load_floor(STAFF_ROOM)
    # collect item and replace with ground
    elif pos == 33:
        pass
    # load p's office when entered
    elif pos == 34:
        load_floor(PRINCIPLES_OFFICE)
    # message pops up and don't go through
    elif pos == 35:
        pass
    # message pops up and don't go through
    elif pos == 36:
        pass
    # message pops up and don't go through
    elif pos == 37:
        pass
    # message pops up and don't go through
    elif pos == 38:
        pass
    # message pops up and don't go through
    elif pos == 39:
        pass
    # collect item and replace with ground
    elif pos == 40:
        pass
    # battle principal to get to the key
    elif pos == 41:
        pass
    # control the character
    elif pos == 42:
        pass
    # load secret passage when entered
    elif pos == 43:
        load_floor(PRINCIPLES_OFFICE_SECRET_PATH)
    # message pops up and don't go through
    elif pos == 44:
        pass
    # message pops up and don't go through
    elif pos == 45:
        pass
    # message pops up and don't go through
    elif pos == 46:
        pass
    # load floor 1 when entered
    elif pos == 47:
        load_floor(FLOOR1)
    # message pops up and don't go through
    elif pos == 48:
        pass
    # message pops up and don't go through
    elif pos == 49:
        pass
    # load p's office when entered
    elif pos == 50:
        load_floor(PRINCIPLES_OFFICE)

    elif pos == 51:
        load_floor(BASEMENTFLOOR)

    redraw()


# collect item and don't pass through the space.
def getScreen():
    return SCREEN

def isGameOver():
    if player.hp == 0 or WIN:
        return True
    return False
# if __name__ == '__main__':
    # print("Welcome to " + CREATOR + "'s RPG! called " + RPG_NAME + "!")
    #x = Raccoon()
    #battle(x)
    # print(og_map)
    # og_map[player.x][player.y] = 99
    # print(og_map)
    # player.set_xy(5,6)
    # og_map[player.x][player.y] = 99
    # print(og_map)
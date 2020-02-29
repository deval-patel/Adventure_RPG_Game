import Item
import typing

class Monster:
    """
    Monster class contains the attributes of different monsters and their stats
    """
    """
    ===Private Attributes===
    HP: Health of this monster
    AD: Attack Damage of this monster
    DF: Defence of this monster
    SPA: Special Attack of this monster
    SP: Speed of this monster
    MOVES: Moves of this monster
    """
    # Attributes
    hp: int
    attack: int
    defence: int
    sp_attack: int
    sp_defence: int
    speed: int
    moves: list
    name: str

    def __init__(self, name=""):
        self.name = name
        self.hp = 100
        self.attack = 50
        self.defence = 50
        self.sp_attack = 50
        self.sp_defence = 50
        self.speed = 50
        self.moves = []

    def get_name(self):
        return  self.name

    def get_hp(self):
        return self.hp

    def get_attack(self):
        return self.attack

    def get_defence(self):
        return self.defence

    def get_sp_defence(self):
        return self.sp_defence

    def get_sp_attack(self):
        return self.sp_attack

    def get_speed(self):
        return self.speed

    def get_moves(self):
        return self.moves

    def take_damage(self, damage):
        self.hp += (damage*-1)

#Todo set special defence stats for every monster

class Raccoon(Monster):
    def __init__(self, name = "Raccoon"):
        self.name = name
        self.hp = 50
        self.attack = 10
        self.defence = 20
        self.sp_attack = 15
        self.sp_defence = 10
        self.speed = 15
        self.moves = [("rawr", 0, 0)]


class Wolf(Monster):
    def __init__(self, name="Wolf"):
        self.name = name
        self.hp = 100
        self.attack = 40
        self.defence = 40
        self.sp_attack = 30
        self.speed = 35
        self.moves = [("", 0, 0)]


class Snake(Monster):
    def __init__(self, name = "Snake"):
        self.name = name
        self.hp = 200
        self.attack = 55
        self.defence = 35
        self.sp_attack = 45
        self.speed = 40
        self.moves = [("", 0, 0)]


class Fox(Monster):
    def __init__(self, name = "Fox"):
        self.name = name
        self.hp = 150
        self.attack = 45
        self.defence = 40
        self.sp_attack = 25
        self.speed = 40
        self.moves = [("", 0, 0)]


class Bear(Monster):
    def __init__(self, name = "Bear"):
        self.name = name
        self.hp = 400
        self.attack = 70
        self.defence = 80
        self.sp_attack = 50
        self.speed = 30
        self.moves = [("", 0, 0)]


class Principle(Monster):

    def __init__(self, name = "Principle"):
        self.name = name
        self.hp = 1000
        self.attack = 100
        self.defence = 75
        self.sp_attack = 60
        self.speed = 45
        self.moves = []


class Player(Monster):
    """
    The player
    """

    def __init__(self, name="Thomas"):
        self.x = 0
        self.y = 0
        self.name = name
        self.hp = 100
        self.attack = 0
        self.defence = 15
        self.sp_defence = 10
        self.sp_attack = 0
        self.speed = 25
        self.moves = [("Punch", 67, 0),
                      ("Kick", 0, 0),
                      ("Headbutt", 0, 0),
                      ("Stomp", 0, 0)
                      ]

    def equip_item(self, item: Item):
        self.hp += item.get_hp()
        self.attack += item.get_attack()
        self.sp_attack += item.get_sp_attack()
        self.sp_defence += item.get_sp_defence()
        self.defence += item.get_defence()
        self.speed += item.get_speed()

    def set_xy (self, x, y):
        self.x = x
        self.y = y
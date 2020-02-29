class Item:
    """
     ===Private Attributes===
    HP: Health of this item
    AD: Attack Damage of this item
    DF: Defence of this item
    SPA: Special Attack of this item
    SP: Speed of this item
    """
    # Attributes
    hp: int
    attack: int
    defence: int
    sp_attack: int
    speed: int
    name: str

    def __init__(self):
        self.hp = 0
        self.attack = 0
        self.defence = 0
        self.speed = 0
        self.sp_attack = 0
        self.sp_defence = 0
        self.name = "Item"

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

    def __str__(self):
        if self.name[0] in ['a', 'e', 'i', 'o', 'u']:
            return "an "+ self.name
        else:
            return "a " + self.name

class crowbar(Item):
    """
    A crowbar
    """
    def __init__(self):
        Item.__init__()
        self.attack = 50
        self.name = "crowbar"

class axe(Item):
    """
    An axe
    """
    def __init__(self):
        Item.__init__()
        self.attack = 70
        self.name = "axe"

class bandaid(Item):
    """
    A band-aid
    """
    def __init__(self):
        Item.__init__()
        self.hp = 30
        self.name = "band-aid"

class candyBar(Item):
    """
    A candy bar
    """
    def __init__(self):
        Item.__init__()
        self.speed = 25
        self.name = "candy bar"

class soda(Item):
    """
    A soda
    """
    def __init__(self):
        Item.__init__()
        self.speed = 50
        self.name = "soda"

class bristolBoard(Item):
    """
    A bristol board
    """
    def __init__(self):
        Item.__init__()
        self.defence = 20
        self.name = "bristol board"

class lockerDoor(Item):
    """
    A locker door
    """
    def __init__(self):
        Item.__init__()
        self.defence = 40
        self.name = "locker door"

class sharpRuler(Item):
    """
    A sharp ruler
    """
    def __init__(self):
        Item.__init__()
        self.sp_attack = 20
        self.name = "sharp ruler"

class clipBoard(Item):
    """
    A clip board
    """
    def __init__(self):
        Item.__init__()
        self.sp_defence = 30
        self.name = "clip board"


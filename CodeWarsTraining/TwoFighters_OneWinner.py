class Fighter:
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

    def __str__(self): return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)
    __repr__ = __str__


def declare_winner(fighter1, fighter2, first_attacker):
    while fighter1.health or fighter2.health <= 0:
        if first_attacker == fighter1.name:
            fighter2.health = fighter2.health - fighter1.damage_per_attack
            if fighter2.health <= 0:
                return fighter1.name
            elif fighter1.health <= 0:
                return fighter2.name
            fighter1.health = fighter1.health - fighter2.damage_per_attack
            if fighter2.health <= 0:
                return fighter1.name
            elif fighter1.health <= 0:
                return fighter2.name
        else:
            fighter1.health = fighter1.health - fighter2.damage_per_attack
            if fighter1.health <= 0:
                return fighter2.name
            elif fighter2.health <= 0:
                return fighter1.name
            fighter2.health = fighter2.health - fighter1.damage_per_attack
            if fighter1.health <= 0:
                return fighter2.name
            elif fighter2.health <= 0:
                return fighter1.name


### OR ###


def declare_winner1(fighter1, fighter2, first_attacker):
    cur, opp = (fighter1, fighter2) if first_attacker == fighter1.name else (fighter2, fighter1)
    while cur.health > 0:
        opp.health -= cur.damage_per_attack
        cur, opp = opp, cur
    return opp.name


print(declare_winner1(Fighter("Harald", 20, 5), Fighter("Harry", 5, 4), "Harry"))
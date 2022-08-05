import random
class Warrior:
    def __init__(self, warrior):
        self.warrior = warrior
        self.hp = 100
        self.strength = (4, 12)
        self.defense = (0, 5)
        self.critical_chance = 0.11
        self.critical_power = 3

    def _is_critical(self):
        return random.random() < self.critical_chance

    def _get_damage(self):
        damage = random.randint(*self.strength)

        if self._is_critical():
            return damage * self.critical_power

        return damage

    def _get_defence(self):
        defence = random.randint(*self.defense)
        return defence

    def attack(self, warrior):
        if self.is_alive():
            defence = warrior._get_defence()
            damage = self._get_damage()
            warrior.hp -= self._get_damage()

    def is_alive(self):
        return self.hp > 0


class Assassin:
    def __init__(self, warrior):
        self.warrior = warrior
        self.hp = 100
        self.strength = (4, 12)
        self.defense = (0, 5)
        self.critical_chance = 0.25
        self.critical_power = 4

    def _is_critical(self):
        return random.random() < self.critical_chance

    def _get_damage(self):
        damage = random.randint(*self.strength)

        if self._is_critical():
            return damage * self.critical_power

        return damage

    def _get_defence(self):
        defence = random.randint(*self.defense)
        return defence

    def attack(self, warrior):
        if self.is_alive():
            defence = warrior._get_defence()
            damage = self._get_damage()
            warrior.hp -= (damage - defence)

    def is_alive(self):
        return self.hp > 0
import random

class Warrior:
    def __init__(self):
        self.health = 100

    def is_alive(self):
        return self.health > 0

    def take_hit(self):
        self.health -= 20

warrior1 = Warrior()
warrior2 = Warrior()

while warrior1.is_alive() and warrior2.is_alive():
    attacker, defender = random.choice([(warrior1, warrior2), (warrior2, warrior1)])
    defender.take_hit()
    print(f'Атакующий юнит нанес удар. У защищающегося осталось {defender.health} очков здоровья.')
    if not defender.is_alive():
        print('Бой окончен. Победил атакующий юнит.')

class Player:
    def __init__(self, name: str, health: int, attack_power: int):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, monster):
        print(f'{self.name} attacks {monster.name}! {monster.name} new health is {monster.health - self.attack_power}')
        monster.take_damage(self.attack_power)

    def take_damage(self, damage):
        self.health -= damage

    def is_alive(self):
        return self.health > 0


class Monster:
    def __init__(self, name: str, health: int, attack_power: int):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, player):
        print(f'{self.name} attacks {player.name}! {player.name} new health is {player.health - self.attack_power}')
        player.take_damage(self.attack_power)

    def take_damage(self, damage):
        self.health -= damage

    def is_alive(self):
        return self.health > 0


def battle(player, monster):
    player.attack(monster)
    if not monster.is_alive():
        print(f"{player.name} wins! Congratulations!")
        return

    monster.attack(player)
    if not player.is_alive():
        print(f"{monster.name} wins! Congratulations!")
        return

    battle(player, monster)


m1 = Monster(name='BBM', health=5000, attack_power=100)
p1 = Player(name='Leni', health=10000, attack_power=300)

print(f'Welcome to the Dark Shadow {p1.name}!')
battle(p1, m1)

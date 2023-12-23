class Player:
    def __init__(self, name, level=1, health=100, mana=50):
        self.name = name
        self.level = level
        self.health = health
        self.max_health = health  # Store maximum health for reference
        self.mana = mana
        self.max_mana = mana  # Store maximum mana for reference
        self.experience = 0
        self.gold = 0

    def attack(self):
        # Logic for the player's attack
        return f"{self.name} attacks with a mighty swing!"

    def heal(self):
        # Logic to heal the player
        if self.health < self.max_health:
            amount_healed = 20  # Healing amount (can be adjusted)
            self.health = min(self.health + amount_healed, self.max_health)
            return f"{self.name} heals for {amount_healed} HP."
        else:
            return f"{self.name} is already at full health."

    def cast_spell(self):
        # Logic to cast a spell using mana
        if self.mana >= 10:  # Mana cost of the spell
            spell_power = 30  # Spell power (can be adjusted)
            self.mana -= 10  # Reduce mana after casting spell
            return f"{self.name} casts a spell, dealing {spell_power} damage!"
        else:
            return f"{self.name} does not have enough mana to cast a spell."

    def gain_experience(self, exp):
        # Method to handle gaining experience points
        self.experience += exp
        # Check for level up
        if self.experience >= 100 * self.level:  # Level up condition (can be adjusted)
            self.level += 1
            self.health = self.max_health  # Restore health on level up
            self.mana = self.max_mana  # Restore mana on level up
            return f"{self.name} leveled up to level {self.level}!"
        else:
            return f"{self.name} gained {exp} experience points."

    def collect_loot(self, gold):
        # Method to collect gold or other rewards
        self.gold += gold
        return f"{self.name} collected {gold} gold coins."

# Creating a player object
player1 = Player("Hero")

# Using some of the methods
print(player1.attack())
print(player1.heal())
print(player1.cast_spell())
print(player1.gain_experience(80))
print(player1.collect_loot(50))

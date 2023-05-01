from enum import Enum


class PokemonAction:
    class Tactic(Enum):
        ATTACK = 1
        DEFENSE = 2

    class Effectiveness(Enum):
        SUPER_EFFECTIVE = 2
        NEUTRAL = 1
        NOT_VERY_EFFECTIVE = 0.5

    class ActionType:
        def __init__(self, name, strengths, weaknesses):
            self.name = name
            self.strengths = strengths
            self.weaknesses = weaknesses

    ACTION_TYPES = {
        "FIRE": ActionType("FIRE", ["GRASS"], ["WATER"]),
        "WATER": ActionType("WATER", ["FIRE"], ["GRASS", "ELECTRIC"]),
        "GRASS": ActionType("GRASS", ["WATER"], ["FIRE"]),
        "ELECTRIC": ActionType("ELECTRIC", ["WATER"], [])
    }

    def __init__(self):
        self.tactic = PokemonAction.Tactic.ATTACK
        self.type = PokemonAction.ACTION_TYPES.get("FIRE")
        self.effectiveness = PokemonAction.Effectiveness.NEUTRAL
        self.power = 100

    def get_power_input(self, player, tactic):
        player.pokemon.action.tactic = tactic
        action_type = input(
            f"\n{player.first_name}, choose your {player.pokemon.action.tactic.name.lower()} "
            f"type (fire, water, grass, electric): ")
        while action_type.upper() not in PokemonAction.ACTION_TYPES:
            action_type = input("Invalid type, please choose again (fire, water, grass, electric): ")
        power = input(f"{player.first_name}, choose your {player.pokemon.action.tactic.name.lower()} power (1-100): ")
        while not power.isdigit() or int(power) < 1 or int(power) > 100:
            power = input("Invalid power, please choose again (1-100): ")
        player.pokemon.action.type = PokemonAction.ACTION_TYPES.get(action_type.upper())
        player.pokemon.action.power = int(power)

    def calculate_damage(self, player, opponent):
        self.calculate_effectiveness(player, opponent)
        return int(50 * (
                    player.pokemon.action.power / opponent.pokemon.action.power) * player.pokemon.action.effectiveness.value)

    def calculate_effectiveness(self, player, opponent):
        player.pokemon.action.effectiveness = PokemonAction.Effectiveness.NEUTRAL
        if player.pokemon.action.type.name == opponent.pokemon.action.type.name \
                or opponent.pokemon.action.type.name in player.pokemon.action.type.weaknesses:
            player.pokemon.action.effectiveness = PokemonAction.Effectiveness.NOT_VERY_EFFECTIVE
        elif opponent.pokemon.action.type.name in player.pokemon.action.type.strengths:
            player.pokemon.action.effectiveness = PokemonAction.Effectiveness.SUPER_EFFECTIVE

    def perform_action(self, player, opponent):
        print(f"\n{player.first_name}'s {player.pokemon.name} used {player.pokemon.action.type.name.lower()} "
              f"{player.pokemon.action.tactic.name.lower()}!")
        player.life_points -= player.pokemon.action.power
        print(f"{player.pokemon.action.tactic.name.lower()} power: {player.pokemon.action.power} was decreased "
              f"from {player.first_name}'s life points! "
              f" life points balance: {player.life_points}")
        opponent.life_points -= opponent.pokemon.action.power
        print(f"{opponent.pokemon.action.tactic.name.lower()} power: {opponent.pokemon.action.power} was decreased "
              f"from {opponent.first_name}'s life points!"
              f" life points balance: {opponent.life_points}")
        damage = player.pokemon.action.calculate_damage(player, opponent)
        opponent.life_points -= damage
        print(f"It's {player.pokemon.action.effectiveness.name.lower().replace('_', ' ')}!")
        print(f"damage is {damage}! life points balance of {opponent.first_name} is {max(0,opponent.life_points)}")

#TODO After each turn, the damage should be decreased from the life of the player who lost this turn.
#TODO unsupported types


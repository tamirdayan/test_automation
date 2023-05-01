from automation_final_project.questions.pokemon_damage_calculator import pokemon


class Player:
    def __init__(self, first_name, last_name, pokemon_name):
        self.first_name = first_name
        self.last_name = last_name
        self.pokemon = pokemon.Pokemon(pokemon_name)
        self.life_points = 1000

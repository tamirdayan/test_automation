from automation_final_project.questions.pokemon_damage_calculator import pokemon_action


class Pokemon:
    def __init__(self, pokemon_name):
        self.name = pokemon_name
        self.action = pokemon_action.PokemonAction()

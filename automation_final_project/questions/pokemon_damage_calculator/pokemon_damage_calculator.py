from automation_final_project.questions.pokemon_damage_calculator import player, pokemon_action


def get_player_details(player_order):
    player_first_name = input(f"\n{player_order}, Enter your first name: ")
    player_last_name = input("Enter your last name: ")
    player_pokemon_name = input("Enter your Pokemon name: ")
    return player.Player(player_first_name.upper(), player_last_name.upper(), player_pokemon_name.upper())


def main():
    print(f"\nIt's a Pokemon battle!")
    current_player = get_player_details("Player 1")
    opponent = get_player_details("Player 2")

    print(f"\n{opponent.first_name} {opponent.last_name} would like to battle!")
    print(f"{opponent.first_name} {opponent.last_name} sent out {opponent.pokemon.name}!")
    print(f"Go! {current_player.pokemon.name}!")
    print(f"What will {current_player.pokemon.name} Do?")

    while current_player.life_points > 0 and opponent.life_points > 0:
        print(f"\n{current_player.first_name} {current_player.last_name}'s Life: {current_player.life_points}")
        print(f"{opponent.first_name} {opponent.last_name}'s Life: {opponent.life_points}\n")
        current_player.pokemon.action.get_power_input(current_player, pokemon_action.PokemonAction.Tactic.ATTACK)
        opponent.pokemon.action.get_power_input(opponent, pokemon_action.PokemonAction.Tactic.DEFENSE)
        current_player.pokemon.action.perform_action(current_player, opponent)
        current_player, opponent = opponent, current_player

    if current_player.life_points <= 0 and opponent.life_points <= 0:
        print("\nIt's a draw!")
    elif current_player.life_points <= 0:
        print(f"\n{current_player.first_name}'s {current_player.pokemon.name.upper()} fainted!")
        print(f"\n{opponent.first_name} wins!")
    elif opponent.life_points <= 0:
        print(f"\n{opponent.first_name}'s {opponent.pokemon.name.upper()} fainted!")
        print(f"\n{current_player.first_name} wins!")


if __name__ == "__main__":
    main()

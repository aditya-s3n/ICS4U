import csv

pokemon_dict = {}
with open("Pokemon.csv") as file_pokemon:
    file_pokemon.readline()

    pokemon_list = csv.reader(file_pokemon)

    for pokemon in pokemon_list:
        pokemon.pop(0)
        secondary_type = pokemon

        if pokemon[1] not in pokemon_dict:
            pokemon_dict[pokemon[1]] = []

        type = pokemon[1]
        pokemon.pop(1)
        pokemon_dict[type].append(pokemon)

        if secondary_type[2] != "":
            if secondary_type[2] not in pokemon_dict:
                pokemon_dict[secondary_type[2]] = []

            type_2 = secondary_type[2]
            secondary_type.remove(secondary_type[2])
            pokemon_dict[type_2].append(secondary_type)

print(pokemon_dict)
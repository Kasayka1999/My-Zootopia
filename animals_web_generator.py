import json

def load_data(filepath):
    with open(filepath, "r") as handle:
        return json.load(handle)


def print_data(data):
    """
    check first if key which we are looking for exit or not
    then print the value
    """
    for animal in data:
        has_name = "name" in animal
        has_locations = "locations" in animal
        has_characteristics = "characteristics" in animal

        if has_characteristics:
            has_diet = "diet" in animal["characteristics"]
            has_type = "type" in animal["characteristics"]
        else:
            continue

        if has_name and has_locations and has_diet and has_type:
            animal_name = animal["name"]
            animal_locations = animal["locations"]
            animal_diet = animal["characteristics"]["diet"]
            animal_type = animal["characteristics"]["type"]
            print(f"Name: {animal_name} \n"
                  f"Diet: {animal_diet} \n"
                  f"Location: {animal_locations[0]} \n"
                  f"Type: {animal_type}\n\n")





animals_data = load_data('animals_data.json')
print_data(animals_data)


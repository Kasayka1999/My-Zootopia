import json
import re

def load_data(filepath):
    with open(filepath, "r") as handle:
        return json.load(handle)


def get_animal_data(data):
    """
    check first if key which we are looking for exit or not
    then print the value
    """
    output = ""
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

            output += f'<li class="cards__item">'
            output += f"Name: {animal_name}<br/>\n"
            output += f"Diet: {animal_diet}<br/>\n"
            output += f"Location: {animal_locations[0]}<br/>\n"
            output += f"Type: {animal_type}<br/>\n"
            output += f"</li>"

    return output


def read_and_replace_html(filepath, new_animal_data):
    with open(filepath, "r") as html_file:
        html = html_file.read() #read as string

    # Define the pattern to match everything between the markers (non-greedy)
    pattern = r"<!-- ANIMALS_INFO_START -->(.*?)<!-- ANIMALS_INFO_END -->"

    # Format the new replacement block
    replacement = f"<!-- ANIMALS_INFO_START -->\n{new_animal_data}\n<!-- ANIMALS_INFO_END -->"

    # Replace the old content with the new block
    updated_html = re.sub(pattern, replacement, html, flags=re.DOTALL)

    with open(filepath, "w") as new_html_code:
        new_html_code.write(updated_html)


#call & load data and save to animals_data
animals_data = load_data("animals_data.json")

#print animal data function
animal_data_output = get_animal_data(animals_data)


read_and_replace_html("animals_template.html", animal_data_output)

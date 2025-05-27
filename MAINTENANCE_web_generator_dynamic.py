import json
import re

def load_data(filepath):
    with open(filepath, "r") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """
    html output structure.
    """
    animal_name = animal_obj["name"]
    animal_locations = animal_obj["locations"]
    animal_diet = animal_obj["characteristics"]["diet"]
    animal_type = animal_obj["characteristics"]["type"]

    output = ''
    output += f'<li class="cards__item">\n'
    output += f'<div class="card__title">{animal_name}</div>\n'
    output += f'<p class="card__text">'
    output += f'<strong>Diet:</strong> {animal_diet}<br/>\n'
    output += f'<strong>Location:</strong> {animal_locations[0]}<br/>\n'
    output += f'<strong>Type:</strong> {animal_type}<br/>\n'
    output += f'</p>\n'
    output += f'</li>\n'
    return output

def get_animal_data(data):
    """
    check first if key which we are looking for exit or not
    then call the serialize_animal function to print data on html
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
            output += serialize_animal(animal) #call function

    return output


def read_and_replace_html(filepath, new_animal_data):
    """
    first read html as a string
    check for comment on html page
    replace comment with the new_animal_data
    rewrite html with the replaced one
    """
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


def main():
    #call & load data and save to animals_data
    animals_data = load_data("animals_data.json")

    #print animal data function
    animal_data_output = get_animal_data(animals_data)

    #calling function to replace html card with a animal data from the json
    read_and_replace_html("MAINTENANCE_animals_template_dynamic.html.html", animal_data_output)


if __name__ == "__main__":
    main()
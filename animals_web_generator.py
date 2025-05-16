import json

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

            output += f"Name: {animal_name} \n"
            output += f"Diet: {animal_diet} \n"
            output += f"Location: {animal_locations[0]} \n"
            output += f"Type: {animal_type}\n\n"

    return output

def read_html(filepath):
    with open(filepath, "r") as html_file:
        html_as_string = html_file.read()
        return html_as_string

def replace_and_rewrite_html(filepath, html_code, replace_string):
    existing_html = html_code
    new_html = existing_html.replace("__REPLACE_ANIMALS_INFO__", replace_string)

    with open(filepath, "w") as new_html_code:
        new_html_code.write(new_html)


#call & load data and save to animals_data
animals_data = load_data("animals_data.json")

#print animal data function
animal_data_output = get_animal_data(animals_data)

#save html code of animals_template.html to animals_template_html
animals_template_html = read_html("animals_template.html")


replace_and_rewrite_html("animals_template.html", animals_template_html, animal_data_output)

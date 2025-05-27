import data_fetcher

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
    new_file_name = 'animals.html'
    with open(filepath, "r") as html_file:
        html = html_file.read() #read as string

        replaced = html.replace("__REPLACE_ANIMALS_INFO__", f"{new_animal_data}")

    with open(new_file_name, "w") as html_file:
        html = html_file.write(replaced)
        print(f"Website was successfully generated to the file {new_file_name}")





def main():
    get_animal_name = input("Enter a name of an animal: ")

    #call & load API to update data and save to animals_data
    animals_data = data_fetcher.fetch_data(get_animal_name)
    if animals_data:
        # print animal data function
        animal_data_output = get_animal_data(animals_data)

        # calling function to replace html card with a animal data from the json
        read_and_replace_html("animals_template.html", animal_data_output)
    else:
        no_animal_found_message = ''
        no_animal_found_message += f'<li class="animal_not_exist">\n'
        no_animal_found_message += f'<div class="card__title not_found_text"><center>The animal "{get_animal_name}" '
        no_animal_found_message += f"doesn't exist.</center></div>\n"
        no_animal_found_message += f'</li>\n'
        read_and_replace_html("animals_template.html", no_animal_found_message)



if __name__ == "__main__":
    main()
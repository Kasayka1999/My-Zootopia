import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')

MAIN_API_URL = 'https://api.api-ninjas.com/v1/animals?name='

def fetch_data(animal_name):
    """
      Fetches the animals data for the animal 'animal_name'.
      Returns: a list of animals, each animal is a dictionary:
      {
        'name': ...,
        'taxonomy': {
          ...
        },
        'locations': [
          ...
        ],
        'characteristics': {
          ...
        }
      },
    """
    api_url = MAIN_API_URL + animal_name #update main api url call with user input

    res = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    if res.status_code == requests.codes.ok:
        res = res.json()  # because return json, converting to json
        return res
    else:
        print("Error:", res.status_code, res.text)
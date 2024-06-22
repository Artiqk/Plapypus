import json
from termcolor import colored

def load_json_data(filename):
    try:
        with open(filename, 'r') as file:
            existing_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = {}
    
    return existing_data


def save_json_data(filename, data):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file)
    except IOError as e:
        print(colored(f'Error writing data to {filename}: {e}', 'red'))
        return False
    
    return True


def credentials_already_exist(website_data, website, username):
    # website = new_website_data['website']
    # username = new_website_data['username']
    return any(username == data['username'] for data in website_data[website])


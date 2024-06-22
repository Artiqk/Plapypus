import json
from termcolor import colored

def load_json_data(filename):
    try:
        with open(filename, 'r') as file:
            existing_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = []
    
    return existing_data


def save_json_data(filename, data):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file)
    except IOError as e:
        print(colored(f'Error writing data to {filename}: {e}', 'red'))
        return False
    
    return True


def does_website_exist(data, new_website_data):
    if any(existing_website_data['website'] == new_website_data['website'] and existing_website_data['username'] == new_website_data['username'] for existing_website_data in data):
        return True
        
    return False


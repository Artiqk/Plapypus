import json


def load_json_data(filename: str) -> dict:
    try:
        with open(filename, 'r') as file:
            existing_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = {}
    
    return existing_data


def save_json_data(filename: str, data: dict) -> bool:
    try:
        with open(filename, 'w') as file:
            json.dump(data, file)
    except IOError as e:
        return False
    
    return True


def credentials_already_exist(website_data: dict, website: str, username: str) -> bool:
    return any(username == data['username'] for data in website_data[website])


def find_index_by_key_value(lst: list, key: str, value: str) -> int:
    return next((i for i, d in enumerate(lst) if d.get(key) == value), -1)
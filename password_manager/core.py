from termcolor import colored
from password_manager.utils import load_json_data, save_json_data, does_website_exist


def add_website(filename, new_website_data):
    data = load_json_data(filename)
    
    if does_website_exist(data, new_website_data):
        print(colored(f'`{new_website_data["username"]}` for {new_website_data["website"]} already exists.', 'red'))
        return
        
    data.append(new_website_data)
    
    print(colored(f'Adding `{new_website_data["username"]}` for {new_website_data["website"]}...', 'blue'))
    
    if save_json_data(filename, data):
        print(colored(f'`{new_website_data["username"]}` for {new_website_data["website"]} has successfully been written.', 'green'))


def add_websites(filename, new_website_data_list):
    for new_website_data in new_website_data_list:
        add_website(filename, new_website_data)
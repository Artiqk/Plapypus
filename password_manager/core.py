from termcolor import colored
from password_manager.utils import load_json_data, save_json_data, credentials_already_exist


def add_website(filename, website, username, password):
    data = load_json_data(filename)
    
    if website in data and credentials_already_exist(data, website, username):
        print(colored(f'`{username}` for {website} already exists.', 'red'))
        return
    
    if website not in data:
        data[website] = []
    
    data[website].append({'username': username, 'password': password})
    
    if save_json_data(filename, data):
        print(colored(f'`{username}` for {website} has successfully been written.', 'green'))


def add_websites(filename, new_website_data_list):
    for new_website_data in new_website_data_list:
        add_website(filename, **new_website_data)
        

def list_websites(filename):
    data = load_json_data(filename)
    
    for website, credentials in data.items():
        print(colored(website, 'blue'))
        for credential in credentials:
            print('\t=>', end=' ')
            print(colored(f'{credential["username"]}', 'green'), end=':')
            print(colored(f'{credential["password"]}', 'red'))
        print('============================')
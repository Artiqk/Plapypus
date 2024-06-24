from termcolor import colored
from password_manager.utils import *
from password_manager.exceptions import *


class CredentialManager:
    
    def __init__(self, filename):
        self.filename = filename

    def add(self, website, username, password):
        data = load_json_data(self.filename)
        
        if website in data and credentials_already_exist(data, website, username):
            raise CredentialAlreadyExistsError(username, website)
        
        if website not in data:
            data[website] = []
        
        data[website].append({'username': username, 'password': password})
        
        return save_json_data(self.filename, data)


    def add_multiple(self, new_website_data_list):
        for new_website_data in new_website_data_list:
            self.add_credentials_for_website(**new_website_data)
        

    def list(self):
        data = load_json_data(self.filename)
        
        for website, credentials in data.items():
            print(colored(website, 'blue'))
            for credential in credentials:
                print('\t=>', end=' ')
                print(colored(f'{credential["username"]}', 'green'), end=':')
                print(colored(f'{credential["password"]}', 'red'))
            print()
        

    def remove(self, website, username):
        data = load_json_data(self.filename)
        
        if website in data:
            index_to_remove = find_index_by_key_value(data[website], 'username', username)
            
            if index_to_remove != -1:
                data[website].pop(index_to_remove)
            else:
                raise CredentialNotFoundError(username, website)
        else:
            raise WebsiteNotFoundError(website)
        
        return save_json_data(self.filename, data)
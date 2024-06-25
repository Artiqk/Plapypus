from termcolor import colored
from password_manager.utils import *
from password_manager.exceptions import *


class CredentialManager:
    
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def add(self, website: str, username: str, password: str) -> bool:
        data = load_json_data(self.filename)
        
        if website in data and credentials_already_exist(data, website, username):
            raise CredentialAlreadyExistsError(username, website)
        
        if website not in data:
            data[website] = []
        
        data[website].append({'username': username, 'password': password})
        
        return save_json_data(self.filename, data)


    def add_multiple(self, new_website_data_list: list) -> None:
        for new_website_data in new_website_data_list:
            self.add_credentials_for_website(**new_website_data)
        

    def list(self) -> None:
        data = load_json_data(self.filename)
        
        for website in sorted(data.keys()):
            credentials = data[website]
            print(colored(website, 'blue'))
            for credential in credentials:
                print('\t=>', end=' ')
                print(colored(f'{credential["username"]}', 'green'), end=':')
                print(colored(f'{credential["password"]}', 'red'))
            print()

    
    def update(self, website: str, username: str, new_password: str) -> bool:
        data = load_json_data(self.filename)
        
        if website not in data:
            raise WebsiteNotFoundError(website)
        
        index_to_update = find_index_by_key_value(data[website], 'username', username)
        
        if index_to_update == -1:
            raise CredentialNotFoundError(username, website)
        
        data[website][index_to_update]['password'] = new_password
        
        return save_json_data(self.filename, data)


    def remove(self, website: str, username: str) -> bool:
        data = load_json_data(self.filename)
        
        if website not in data:
            raise WebsiteNotFoundError(website)
        
        index_to_remove = find_index_by_key_value(data[website], 'username', username)
        
        if index_to_remove == -1:
            raise CredentialNotFoundError(username, website)
            
        data[website].pop(index_to_remove)
        
        if not data[website]:
            del data[website]
        
        return save_json_data(self.filename, data)
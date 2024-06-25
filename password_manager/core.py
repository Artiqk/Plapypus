from termcolor import colored
from password_manager.utils import *
from password_manager.exceptions import *


class CredentialManager:
    
    def __init__(self, filename: str) -> None:
        self.filename = filename
        
        
    def load_data(self, master_password: str) -> dict:
        return load_encrypted_json_data(self.filename, master_password)
    
    
    def save_data(self, data: dict, master_password: str) -> None:
        save_encrypted_json_data(self.filename, data, master_password)
        del master_password


    def add(self, website: str, username: str, password: str, master_password: str) -> bool:
        data = self.load_data(master_password)
        
        if website in data and credentials_already_exist(data, website, username):
            raise CredentialAlreadyExistsError(username, website)
        
        if website not in data:
            data[website] = []
        
        data[website].append({'username': username, 'password': password})
        
        self.save_data(data, master_password)


    def add_multiple(self, new_website_data_list: list, master_password: str) -> None:
        for new_website_data in new_website_data_list:
            self.add(**new_website_data, master_password=master_password)
        

    def list(self, master_password: str) -> None:
        data = self.load_data(master_password)
        
        del master_password
        
        for website in sorted(data.keys()):
            credentials = data[website]
            print(colored(website, 'blue'))
            
            sorted_credentials = sorted(credentials, key=lambda x: x['username'])
            
            for credential in sorted_credentials:
                print('\t=>', end=' ')
                print(colored(f'{credential["username"]}', 'green'), end=':')
                print(colored(f'{credential["password"]}', 'red'))
            print()

    
    def update(self, website: str, username: str, new_password: str, master_password: str) -> None:
        data = self.load_data(master_password)
        
        if website not in data:
            raise WebsiteNotFoundError(website)
        
        index_to_update = find_index_by_key_value(data[website], 'username', username)
        
        if index_to_update == -1:
            raise CredentialNotFoundError(username, website)
        
        data[website][index_to_update]['password'] = new_password
        
        self.save_data(data, master_password)


    def remove(self, website: str, username: str, master_password: str) -> None:
        data = self.load_data(master_password)
        
        if website not in data:
            raise WebsiteNotFoundError(website)
        
        index_to_remove = find_index_by_key_value(data[website], 'username', username)
        
        if index_to_remove == -1:
            raise CredentialNotFoundError(username, website)
            
        data[website].pop(index_to_remove)
        
        if not data[website]:
            del data[website]
        
        self.save_data(data, master_password)
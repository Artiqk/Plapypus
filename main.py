from password_manager.core import *

FILENAME = 'credentials.json'

data = [{
    'website': 'google.com',
    'username': 'user',
    'password': 'pass'
}, {
    'website': 'minecraft.com',
    'username': 'steve',
    'password': 'herobrine'
}, {
    'website': 'hackthebox.com',
    'username': 'pwner',
    'password': 'he11ow0rld!'
}, {
    'website': 'minecraft.com',
    'username': 'herobrine', 
    'password': 'pass' 
}]

def main():
    # add_websites(FILENAME, data)
    list_websites(FILENAME)


if __name__ == '__main__':
    main()
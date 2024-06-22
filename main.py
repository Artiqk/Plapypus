from password_manager.core import *

FILENAME = 'credentials.json'

data = [{
    'website': 'google.com',
    'username': 'user',
    'password': 'pass'
}, {
    'website': 'hackthebox.com',
    'username': 'pwner',
    'password': 'he11ow0rld!'
}, {
    'website': 'minecraft.com',
    'username': 'steve',
    'password': 'herobrine'
}]

def main():
    add_websites(FILENAME, data)


if __name__ == '__main__':
    main()
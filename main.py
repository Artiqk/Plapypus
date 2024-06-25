#!/usr/bin/python3

import argparse
from password_manager.core import CredentialManager
from password_manager.utils import generate_password
from termcolor import colored
import getpass


def main():
    parser = argparse.ArgumentParser(description="Manage your passwords securely.")
    parser.add_argument('--file', '-f', type=str, required=True, help='Path to the password file.')

    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # Add command
    add_parser = subparsers.add_parser('add', help='Add a new credential')
    add_parser.add_argument('website', type=str, help='Website to add a credential for')
    add_parser.add_argument('username', type=str, help='Username for the website')
    add_parser.add_argument('--password', nargs='?', const=True, default=False, help='Prompt for password if not provided')

    # List command
    list_parser = subparsers.add_parser('list', help='List all credentials')

    # Update command
    update_parser = subparsers.add_parser('update', help='Update an existing credential')
    update_parser.add_argument('website', type=str, help='Website of the credential')
    update_parser.add_argument('username', type=str, help='Current username')

    # Remove command
    remove_parser = subparsers.add_parser('remove', help='Remove a credential')
    remove_parser.add_argument('website', type=str, help='Website of the credential')
    remove_parser.add_argument('username', type=str, help='Username to remove')

    args = parser.parse_args()

    # Create an instance of the CredentialManager
    manager = CredentialManager(args.file)

    master_password = getpass.getpass('Enter the master password: ')

    # Handle commands
    if args.command == 'add':
        password = getpass.getpass(f'Enter the password for `{args.username}`: ') if args.password is True else generate_password(32, True)
        manager.add(args.website, args.username, password, master_password)
        print(colored(f'Credentials successfully added for {args.website} => {args.username}:{password}', 'green'))
    elif args.command == 'list':
        manager.list(master_password)
    elif args.command == 'update':
        new_password = getpass.getpass(f'Enter the new password for `{args.username}`: ')
        manager.update(args.website, args.username, new_password, master_password)
        print(colored(f'Credentials successfully updated for {args.website} => {args.username}:{new_password}', 'green'))
    elif args.command == 'remove':
        manager.remove(args.website, args.username, master_password)
        print(colored('Credential removed successfully.', 'green'))


if __name__ == "__main__":
    main()
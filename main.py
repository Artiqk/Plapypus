#!/usr/bin/python3

import argparse
from password_manager.core import CredentialManager
from password_manager.utils import generate_password
import getpass


def main():
    parser = argparse.ArgumentParser(description="Manage your passwords securely.")
    parser.add_argument('--file', '-f', type=str, required=True, help='Path to the password file.')

    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # Add command
    add_parser = subparsers.add_parser('add', help='Add a new credential')
    add_parser.add_argument('website', type=str, help='Website to add a credential for')
    add_parser.add_argument('username', type=str, help='Username for the website')

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
        manager.add(args.website, args.username, master_password)
        print("Credential added successfully.")
    elif args.command == 'list':
        manager.list(master_password)
    elif args.command == 'update':
        new_password = getpass.getpass(f'Enter the new password for `{args.username}`: ')
        manager.update(args.website, args.username, new_password, master_password)
        print("Credential updated successfully.")
    elif args.command == 'remove':
        manager.remove(args.website, args.username, master_password)
        print("Credential removed successfully.")


if __name__ == "__main__":
    main()
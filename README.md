# Password Manager

This Password Manager is a secure tool designed to store, retrieve, update, and manage your passwords effectively. It uses strong encryption to ensure that all credentials are securely stored and provides a command-line interface for easy interaction.

## Features

- **Secure Storage**: Encrypts password data using Fernet symmetric encryption to ensure security.
- **Command Line Interface**: Easily manage your passwords through a command-line interface.
- **Secure Password Input**: Uses `getpass` to securely input passwords without revealing them on-screen or storing them in command history.
- **Add, List, Update, and Remove Credentials**: Supports multiple operations to manage credentials.

## Installation

To set up the Password Manager on your system, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/password-manager.git
   ```
2. Navigate to the project directory:
   ```bash
   cd password-manager
   ```
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Here's how to use the Password Manager:

- **Add a credential (custom password)**:
  ```bash
  python password_manager.py add --website example.com --username user --password
  ```
  (The password will be securely prompted)

- **Add a credential (generated password)**:
  ```bash
  python password_manager.py add --website example.com --username user
  ```
  (The password will be automatically generated)

- **List all credentials**:
  ```bash
  python password_manager.py list
  ```

- **Update a credential**:
  ```bash
  python password_manager.py update --website example.com --username user
  ```
  (The new password will be securely prompted)

- **Remove a credential**:
  ```bash
  python password_manager.py remove --website example.com --username user
  ```

## Contributing

If you'd like to contribute to the development of the Password Manager, please follow the guidelines below:

- Fork the repository.
- Create a new branch (`git checkout -b feature-branch`).
- Make your changes and commit them (`git commit -am 'Add some feature'`).
- Push to the branch (`git push origin feature-branch`).
- Create a new Pull Request.
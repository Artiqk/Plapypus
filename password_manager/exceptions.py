
class CredentialError(Exception):
    """ Base-class for all credential-related errors. """
    pass


class CredentialAlreadyExistsError(CredentialError):
    
    def __init__(self, username, website):
        self.username = username
        self.website = website
        super().__init__(f'`{username}` for {website} already exists.')

        
class CredentialNotFoundError(CredentialError):

    def __init__(self, username, website):
        self.username = username
        self.website = website
        super().__init__(f'No records found for `{username}` in {website}.')


class WebsiteNotFoundError(CredentialError):

    def __init__(self, website):
        self.website = website
        super().__init__(f'`{website}` does not exist in the database.')
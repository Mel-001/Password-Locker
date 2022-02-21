import random
from credentials import Credential
class User(Credential):
    """
    Class that generates a new instance User
    """

    def __init__(self, first_name, last_name,  user_email, user_password):
        
        self.first_name = first_name
        self.last_name = last_name
        self.user_email = user_email
        self.user_password = user_password
        self.isLoggedIn = True





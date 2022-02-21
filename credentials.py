from secrets import choice
from string import ascii_letters, digits,punctuation
class Credential:
    '''
    a class that creates a new instance of credential
    '''

    account_list = []









def generate_password(self,pass_len=8):
        random_str = ascii_letters+punctuation+digits
        password = "".join(choice(random_str) for x in range(pass_len))
        # import pdb; pdb.set_trace()
        return password


def save_credential(self,name,username,password):

        '''
        save_credential mothod saves the user credentials into the credential_list
        '''
        new_account = dict(name=name,username=username,password=password)
        self.account_list.append(new_account)
        return True


def delete_credential(self,name):

        '''
        delete_credential method allows the user to delete the credentials from the credential_list
        '''
        self.account_list = [x for x in self.account_list if x["name"] !=name]
        return True




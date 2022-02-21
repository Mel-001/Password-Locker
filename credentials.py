









def generate_password(self,pass_len=8):
        random_str = ascii_letters+punctuation+digits
        password = "".join(choice(random_str) for x in range(pass_len))
        # import pdb; pdb.set_trace()
        return password










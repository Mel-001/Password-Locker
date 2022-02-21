#!/usr/bin/env python3.8

import os
from credentials import Credential
from user import User
import random


def main():
    print("Hi,Hello!! Welcome password_locker. Enter User First Name.")
    first_name = input()

    print(f"Hey {first_name} you're a step into password_locker. Please enter your last name.")
    last_name = input()

    print(f"Hey {first_name} {last_name} input your credential user email ")
    user_email = input()

user_in = int(input("Reply with 1 to enter password or 2 to generate a new password for you"))
if user_in ==1:
        password = input("Enter password: ")
        conf_pass = input("Confirm password: ")
        while password !=conf_pass:
            print("password does not match")
            conf_pass = input("Confirm password: ")

else:
        pass_len = int(input("Specifiy password length: "))
        password = User.generate_password(pass_len)
        print(f"The generated password is {password}")













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
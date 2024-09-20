#!/usr/bin/python3

### Imports
from gen import *
from config import *

password = generate12()

print("Here is your password => ", password)
print("But how strong is it?")
print("\n" + checkPassword(password))
#!/usr/bin/env python3

import random
from time import sleep
from config import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

# The code that generatees the password

def generate12():
    includeAllCharacters = [] ### Making sure that it has 1 of every character
    password = []

    keepGoing = True

    while keepGoing:
        for _ in range(random.randint(1, 15)):
            whichCharacter = random.randint(1, 3)
            if whichCharacter not in includeAllCharacters:
                includeAllCharacters.append(whichCharacter)
            
            if whichCharacter == 1:
                password.append(random.choice(CAPITAL_LETTERS))
            
            elif whichCharacter == 2:
                password.append(random.choice(LOWERCASE_LETTERS))
            
            else:
                password.append(random.choice(SYMBOLS))
            
        if len(includeAllCharacters) == 3:
            keepGoing = False
    
    return "".join(password)

def checkPassword(password):
    output = []
    driver = webdriver.Chrome()  # or specify the path to your ChromeDriver executable
    driver.get("https://random-ize.com/how-long-to-hack-pass/")
    driver.maximize_window()
    inputInput = driver.find_element("id", "password")
    inputInput.send_keys(password)
    elements = driver.find_elements(By.ID, "time")
    [output.append(e.text) for e in elements]
    return elements[0].text
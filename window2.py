#!/usr/bin/python3

### Imports
from gen import *
from config import *

driver = webdriver.Chrome()  # or specify the path to your ChromeDriver executable
# driver.get("https://static0.gamerantimages.com/wordpress/wp-content/uploads/2024/04/honkai-star-rail-version-2-2-five-star-character-robin-explained.jpg")

driver.get("https://media.tenor.com/UnFx-k_lSckAAAAM/amalie-steiness.gif")
driver.maximize_window()

sleep(8)
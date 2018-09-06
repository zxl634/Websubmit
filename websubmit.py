#!/usr/bin/env python3

# This script attempts to submit an answer to DataCamp through the browser

# It first logs the user in and then navigates to the desired site
# where it copy-pastes the script

from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import websubmitFuncs
import os.path
import time

# Using Chrome to access web
driver = webdriver.Chrome("./chromedriver")

# Check whether user cookie is present to avoid signing in
if os.path.isfile(websubmitFuncs.getPath()):
    driver.get("https://datacamp.com")
    websubmitFuncs.load_cookie(driver)

else:
    # Sign in
    websubmitFuncs.signin(driver)

# Navigate to page to paste code in
url = "https://campus.datacamp.com/courses/data-types-for-data-science/fundamental-data-types?ex=2" # noqa
driver.get(url)

# Locate code editor and paste answer
try:
    el_id = "ace-code-editor-6"
    el = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, el_id))
            )
finally:
    script = websubmitFuncs.create_script()
    # script = 'ace.edit("ace-code-editor-6").setValue("the new text here")' # noqa
    time.sleep(3)
    print(script)

    driver.execute_script(script)

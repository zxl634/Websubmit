#!/usr/bin/env python3

# This script attempts to submit an answer to DataCamp through the browser

# It first logs the user in and then navigates to the desired site
# where it copy-pastes the script

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import websubmitFuncs
import argparse


def main():
    # Read filename
    parser = argparse.ArgumentParser()
    parser.add_argument(
            'exercise_file',
            help='exercise file including url to exercise')
    args = parser.parse_args()
    filename = args.exercise_file

    # Navigate to page to paste code in
    driver = websubmitFuncs.start_driver()

    # Read url from exercise
    url = websubmitFuncs.read_url(filename)
    # url = "https://campus.datacamp.com/courses/data-types-for-data-science/fundamental-data-types?ex=2" # noqa
    driver.get(url)

    # Locate code editor and paste answer
    try:
        el_id = "ace-code-editor-6"
        WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, el_id))
                )
    finally:
        script = websubmitFuncs.create_script(filename)
        driver.execute_script(script)

    # Submit answer
    actions = ActionChains(driver)
    actions.send_keys(Keys.LEFT_CONTROL + Keys.LEFT_SHIFT + Keys.ENTER)
    actions.perform()

    # Await user input
    input_text = input("Have you seen enough?")
    print(input_text)


if __name__ == '__main__':
    main()

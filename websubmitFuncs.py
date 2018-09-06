#!/usr/bin/env python3
import pickle
import os


def getPath():
    return os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            "DcCookie"
            )


def save_cookie(driver):
    path = getPath()
    with open(path, 'wb') as filehandler:
        pickle.dump(driver.get_cookies(), filehandler)


def load_cookie(driver):
    path = getPath()
    with open(path, 'rb') as cookiesfile:
        cookies = pickle.load(cookiesfile)
        for cookie in cookies:
            driver.add_cookie(cookie)


def create_script():
    with open('ex2.py', 'r') as myfile:
        # script = 'ace.edit("ace-code-editor-6").setValue("the new text here")' # noqa
        file_content = myfile.read()
        # print(file_content)
        script = str(
                '''ace.edit("ace-code-editor-6").setValue("''' +
                # r'''# Create a list containing the names: baby_names\n''' +
                # '''baby_names = ['Ximena', 'Aliza', 'Ayden', 'Calvin']''' +
                file_content +
                '''")'''
                )
        return script


print(create_script())


def signin(driver):
    url = "https://www.datacamp.com/users/sign_in"
    driver.get(url)

    # Submit e-mail
    el_id = "user_email"
    el = driver.find_element_by_id(el_id)
    el.send_keys("avr@moos-bjerre.dk")

    # Submit password
    el_id = "user_password"
    el = driver.find_element_by_id(el_id)
    el.send_keys("3gCNXg46T3yE")

    # Sign In
    el_name = "commit"
    el = driver.find_element_by_name(el_name)
    el.click()

    # Save cookie
    save_cookie(driver)

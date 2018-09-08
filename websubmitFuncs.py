#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pickle
import os
import re
import validators
from selenium import webdriver
import os.path
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import config


def get_filename_from_url(url):
    # Extract ex no
    ex_pos = url.find("ex")
    exno = url[ex_pos:ex_pos+len(url)]
    exno = exno.replace("=", "").capitalize()

    # Extract title
    title_pos = url.rfind("/")
    full_title = url[title_pos+1:ex_pos-1]
    title_split = full_title.split("-")
    title = ""
    for w in title_split:
        title += w[0:3].capitalize()

    title = title + exno + ".py"
    return title


def get_code_template(driver):
    # Locate code editor and get code template
    try:
        # el_id = "ace-code-editor-6"
        el_id = get_ace_id()
        WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, el_id))
                )
    finally:
        script = 'return ace.edit("' + get_ace_id() + '").getValue()'  # noqa: E501
        return driver.execute_script(script)


def start_driver():
    # Using Chrome to access web
    driver = webdriver.Chrome("./chromedriver")

    # Check whether user cookie is present to avoid signing in
    if os.path.isfile(getPath()):
        driver.get("https://datacamp.com")
        load_cookie(driver)

    else:
        # Sign in
        signin(driver)

    return driver


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


def validate_url(url):
    if not validators.url(url):
        exit("not valid url: " + url)
    else:
        return url


def read_url(filename):
    with open(filename, 'r') as myfile:
        for i, line in enumerate(myfile):
            if i == 2:
                url = re.sub("# ", "", line)
                validate_url(url)
                return url


def get_ace_id():
    return "ace-code-editor-6"


def create_script(filename):
    with open(filename, 'r') as myfile:
        file_content = myfile.read().replace("\n", r"\n")
        script = (
                '''ace.edit("ace-code-editor-6").setValue("''' +
                file_content +
                '''")'''
                )

        return script


def signin(driver):
    url = "https://www.datacamp.com/users/sign_in"
    driver.get(url)

    # Submit e-mail
    el_id = "user_email"
    el = driver.find_element_by_id(el_id)
    # el.send_keys("avr@moos-bjerre.dk")
    el.send_keys(config.user)

    # Submit password
    el_id = "user_password"
    el = driver.find_element_by_id(el_id)
    # el.send_keys("3gCNXg46T3yE")
    el.send_keys(config.pw)

    # Sign In
    el_name = "commit"
    el = driver.find_element_by_name(el_name)
    el.click()

    # Save cookie
    save_cookie(driver)

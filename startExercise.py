#!/usr/bin/env python3
# Get code template from IPython shell

# from selenium import webdriver
import argparse
import websubmitFuncs


def main():
    # Read url from argument
    parser = argparse.ArgumentParser()
    parser.add_argument(
            'exercise_url',
            help='Url to exercise')
    url = parser.parse_args().exercise_url
    websubmitFuncs.validate_url(url)

    # Start Chrome
    driver = websubmitFuncs.start_driver()
    driver.get(url)

    # Locate code editor and get code template
    code_template = websubmitFuncs.get_code_template(driver)

    # Write code_template to file

    # Find appropriate filename
    filename = websubmitFuncs.get_filename_from_url(url)

    with open(filename, "w") as f:
        f.write("#!/usr/bin/env python3\n\n")
        f.write("# " + url + "\n\n")
        code_template_list = code_template.split("\n")
        for line in code_template_list:
            f.write(line + "\n")

    # Await user input
    input_text = input("Have you seen enough?")
    print(input_text)

    # Close browser
    driver.quit()


if __name__ == "__main__":
    main()

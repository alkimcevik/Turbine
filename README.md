# Overview

## Purpose

Automation suite for Design System's Turbine app.

Written with Python and SeleniumBase. Page object model has been used for the tests.

Test file are in examples/nypl_tests


# Setup

Create a new project in PyCharm and clone this repo.

Go to terminal in PyCharm, and run command “pip3 install seleniumbase”
Type “sbase” or “seleniumbase” to check if it is installed. You should see its version and other related stuff.
Install chromedriver with “sbase install chromedriver latest”
Install requirements/dependencies with “pip freeze > requirements.txt” for Github/Jenkins integration
Base interpereter is Python 3.10 for this test suite.

# Running Tests
 ## By Command Line
 
 cd into the examples file and type 'pytest file_name'
 for instance: - cd ~/examples/nypl_tests 
               - pytest test_sign_up.py
               
 ## In PyCharm
 
 Click on the Green arrow next to the 'test_' files or right click anywhere and choose 'Run'.








# Overview

## Purpose

Automation suite for Design System's Turbine app.

Written with Python and SeleniumBase. Page object model has been used for the tests.

Test files are in examples/nypl_tests


# Setup

Download Pycharm CE and create a new project and clone this repo.

Go to terminal in PyCharm, and run command “pip3 install seleniumbase”. Sbase must be at least 4.11.3. To upgrade, use “pip3 install seleniumbase --upgrade” 

Type “sbase” or “seleniumbase” to check if it is installed. You should see its version and other related stuff.

Install chromedriver with “sbase install chromedriver latest”.

Install requirements/dependencies with “pip freeze > requirements.txt” for Github/Jenkins integration.

Base interpereter is Python 3.10 for this test suite.

# Running Tests
 ## By Command Line
 
 cd into the nypl_tests files under examples (examples/nypl_tests) file and type 'pytest file_name'
 
 for instance: - cd ~/examples/nypl_tests 
               - pytest test_sign_up.py
               
 try adding --demo for a slower run:
 pytest test_sign_up.py --demo

               
 ## In PyCharm CE
 
 Click on the Green arrow next to the 'test_' files or right click anywhere and choose 'Run'.
 
 # Note
 
 To test the mobile tests in 'test_mobile.py', the test should be run with --mobile command on terminal, for instance:
 pytest test_mobile.py --headless --mobile








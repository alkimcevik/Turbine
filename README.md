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
 
 ## Github Actions CI/CD
 
 Click on the "Actions" tab at the top of the repository.
 
 Select the workflow you want to run from the list of workflows on the left.
 
 Click the "Run workflow" button on the right.
 
 # Note
 
 To test the mobile tests in 'test_mobile.py', the test should be run with --mobile command on terminal, for instance:
 pytest test_mobile.py --headless --mobile
 
 # URL Management
 
 Use `URLManager` in `examples/nypl_utility` for easy URL handling. Set `SMOKE_TEST_ACTIVE` in `URLManager` to toggle between regular and smoke test URLs, 
 and change the BASE_SMOKE_TEST_URL to the new test build. 







from seleniumbase import BaseCase
from examples.nypl_utility.url_manager import URLManager


class SignUpPage(BaseCase):
    email = '//*[@id="email"]'
    altEmail = '//*[@id="altEmail"]'

    first_name = '//*[@id="firstName"]'
    last_name = '//*[@id="lastName"]'
    school = '//*[@id="school"]'
    select_school = '//*[@id="school"]/option[5]'
    school_website = '//*[@id="website"]'
    date_of_hire = '//*[@id="hiredDate-start"]'
    pin = '//*[@id="pin"]'
    comments = '//*[@id="comments"]'
    sign_up = '//*[@id="submit-button"]'
    submission_text = '//*[contains(text(), "Your submission information")]'

    invalid_email = '//*[@id="email-helperText"]'
    invalid_pin = '//*[@id="pin-helperText"]'
    invalid_school = '//*[@id="school-helperText"]'


    def open_sign_up_page(self):
        page_path = 'sign-up'
        url = URLManager.get_url(page_path)
        self.open(url)



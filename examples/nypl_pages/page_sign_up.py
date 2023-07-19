from seleniumbase import BaseCase


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
    submission_text = '//*[@id="submit-list-info-heading"]'

    invalid_email = '//*[@id="email-helperText"]'
    invalid_pin = '//*[@id="pin-helperText"]'
    invalid_school = '//*[@id="school-helperText"]'

    def open_sign_up_page(self):
        url = 'https://nypl-ds-test-app.vercel.app/fullPages/sign-up#above-header-notification'  # regular URL
        smoke_test_url = "https://nypl-ds-test-app-git-dsd-1530-ds-170-update-nypl.vercel.app/fullPages/sign-up#above-header-notificationz"  # smoke tes url
        self.open(smoke_test_url)
        #self.open("https://nypl-ds-test-li3jif416-nypl.vercel.app/fullPages/sign-up#above-header-notification")  # dark mode URL



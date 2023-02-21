from examples.nypl_pages.page_sign_up import SignUpPage


class SignUpTests(SignUpPage):
    # https://jira.nypl.org/browse/DSD-1130

    # https://nypl-ds-test-app.vercel.app/fullPages/sign-up#above-header-notification

    def setUp(self):
        super().setUp()
        print("\nRUNNING BEFORE EACH TEST")

        # open blog page
        self.open_sign_up_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        super().tearDown()

    def test_nyc_teacher(self):
        # As a valid NYC teacher, I want to successfully sign-up and clearly understand any error that may arise while completing the form.

        # positive test scenario
        # filling out everything properly so the user can submit the form
        self.send_keys(self.email, "teacher@schools.nyc.gov")
        self.send_keys(self.altEmail, "alt_teacher@schools.nyc.gov")
        self.send_keys(self.first_name, "Joe")
        self.send_keys(self.last_name, "Dalton")
        self.click(self.school)
        self.click(self.select_school)
        self.send_keys(self.school_website, "https://bhsec.bard.edu/manhattan/")
        self.send_keys(self.date_of_hire, "2022-01-01")
        self.click(self.pin)
        self.send_keys(self.pin, "1234")
        self.send_keys(self.comments, "Joe needs a new laptop")
        self.click(self.sign_up)
        # asserting submission text is visible
        self.assert_element(self.submission_text)
        # self.wait(3)

    def test_non_nyc_teacher(self):
        # As a teacher from a district outside NYC, I want to try to submit the form without properly filling in the required fields.

        # negative test scenario, the user would not be able to submit the form
        # entering a non_nyc school
        self.send_keys(self.email, "non_nyc_teacher@schools.non_nyc.gov")
        self.send_keys(self.altEmail, "non_nyc_teacher@schools.non_nyc.gov")

        self.send_keys(self.first_name, "Megan")
        self.send_keys(self.last_name, "Dulany")
        self.send_keys(self.date_of_hire, "2022-01-01")

        # entering an invalid PIN
        self.click(self.pin)
        self.send_keys(self.pin, "123")
        self.send_keys(self.comments, "Megan needs a new laptop")
        self.click(self.sign_up)

        # asserting email is invalid
        invalid_email = self.get_text(self.invalid_email)
        print(invalid_email)
        self.assert_true(self.get_text(self.invalid_email) == "Please enter a valid @schools.nyc.gov email address")

        # asserting PIN is invalid
        invalid_pin = self.get_text(self.invalid_pin)
        print(invalid_pin)
        self.assert_true(self.get_text(self.invalid_pin) == "Please enter a valid PIN")

        # asserting school is invalid
        invalid_school = self.get_text(self.invalid_school)
        print(invalid_school)
        self.assert_true(self.get_text(self.invalid_school) == "Please select your school")

        # asserting submission text is not visible
        self.assert_element_not_visible(self.submission_text)

        # self.wait(3)

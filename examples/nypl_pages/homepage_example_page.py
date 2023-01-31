from seleniumbase import BaseCase


class HomePage(BaseCase):

    staff_picks = '/html/body/div/div[1]/div[2]/main/div/div[2]/div[2]/div'
    nypl_blogs = '/html/body/div/div[1]/div[2]/main/div/div[3]/div[2]/div'
    doug_reside_blog_link = '//*[@id="row-card-heading-1-2-link"]'
    ender_game = '//*[@id="homepage-tabs-2--tab-2"]'
    ender_awards = '/html/body/div/div[1]/div[2]/main/div/div[4]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div[3]'

    related_books_h4 = '//*[@id="related-books-2"]'
    related_books_locator = '/html/body/div/div[1]/div[2]/main/div/div[4]/div[2]/div[2]/div[3]/div/div[2]/div'

    feedback_form = '//*[@id="open"]'
    bug_radio = '//*[@id="bug-wrapper"]/label/span[2]/span'
    comment = '//*[@id="feedbackbox-comment"]'
    e_mail = '//*[@id="feedbackbox-email"]'
    submit_button = '//*[@id="submit"]'
    submission_text = 'Thank you for submitting your feedback.'

    def open_homepage(self):
        self.open("https://nypl-ds-test-app.vercel.app/fullPages/homepage")

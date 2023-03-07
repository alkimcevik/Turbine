from seleniumbase import BaseCase


class HomePage(BaseCase):

    staff_picks = "//div[contains(@id,'grid-0')]/div[contains(@id,'card-0')]"
    nypl_blogs = '//div[contains(@id,\'grid-1\')]/div[contains(@id,\'card-1\')]'
    doug_reside_blog_link = '//*[@id="row-card-heading-1-2-link"]'
    ender_game = '//*[@id="homepage-tabs-2--tab-2"]'
    ender_awards = '//*[@id="Ender\'sGame-card"]/div[2]/div[3]/ul'

    related_books_h4 = '//*[@id="related-books-2"]'
    # relative xpath used for telated books locator below
    related_books_locator = '//div[contains(@class,\'chakra-stack\')]/div[contains(@class,\'css-gvpfax\')]'

    feedback_form = '//*[@id="open"]'
    bug_radio = '//*[@id="bug-wrapper"]/label/span[2]/span'
    comment = '//*[@id="feedbackbox-comment"]'
    e_mail = '//*[@id="feedbackbox-email"]'
    submit_button = '//*[@id="submit"]'
    submission_text = 'Thank you for submitting your feedback.'

    dune_related_1 = '//*[@id="related-book-heading-0-0-link"]'
    dune_related_2 = '//*[@id="related-book-heading-0-1-link"]'
    dune_related_3 = '//*[@id="related-book-heading-0-2-link"]'

    the_eye_of_the_world_tab = '//*[@id="homepage-tabs-2--tab-1"]'
    teofw_related_1 = '//*[@id="related-book-heading-1-0-link"]'
    teofw_related_2 = '//*[@id="related-book-heading-1-1-link"]'

    enders_game_tab = '//*[@id="homepage-tabs-2--tab-2"]'
    ender_related_1 = '//*[@id="related-book-heading-2-0-link"]'
    ender_related_2 = '//*[@id="related-book-heading-2-1-link"]'
    ender_related_3 = '//*[@id="related-book-heading-2-2-link"]'

    def open_homepage(self):
        self.open("https://nypl-ds-test-app.vercel.app/fullPages/homepage")

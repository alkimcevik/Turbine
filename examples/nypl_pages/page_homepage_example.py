from seleniumbase import BaseCase
from examples.nypl_utility.url_manager import URLManager


class HomePage(BaseCase):

    staff_picks = "//*[contains(text(), 'Staff Picks')]//..//..//h4"

    nypl_blogs = "//*[contains(text(), 'NYPL Blog')]//..//..//h4"

    nypl_blog_content = "//*[contains(text(), 'NYPL Blog')]//..//.."

    doug_reside_blog_link = '//*[contains(text(), "Company in the Archive")]'

    ender_game_tab = '(//*[contains(text(), "Ender\'s Game")])[1]'

    ender_awards = '(//*[contains(text(), "Ender\'s Game")])[2]//..'  # relative XPath

    related_books_h4 = '//*[@id="related-books-2"]'
    related_books_locator = "// *[contains(@id, 'related-books-2-')]"  # relative XPath with contains

    feedback_form = '//*[@id="open"]'
    bug_button = '//*[contains(text(), "Bug")]'
    comment = '//*[@id="feedbackbox-comment"]'
    e_mail = '//*[@id="feedbackbox-email"]'
    submit_button = '//*[@id="submit"]'
    submission_text = 'Thank you for submitting your feedback.'

    dune_related_1 = '((//*[contains(text(), "Related Books")])//..//a)[1]'
    dune_related_2 = '((//*[contains(text(), "Related Books")])//..//a)[2]'
    dune_related_3 = '((//*[contains(text(), "Related Books")])//..//a)[3]'

    the_eye_of_the_world_tab = '(//*[contains(text(), "The Eye of the World")])'

    teofw_related_1 = '((//*[contains(text(), "Related Books")])//..//a)[1]'
    teofw_related_2 = '((//*[contains(text(), "Related Books")])//..//a)[2]'

    ender_related_1 = '((//*[contains(text(), "Related Books")])//..//a)[1]'
    ender_related_2 = '((//*[contains(text(), "Related Books")])//..//a)[2]'
    ender_related_3 = '((//*[contains(text(), "Related Books")])//..//a)[3]'


    def open_homepage(self):
        page_path = 'homepage'
        url = URLManager.get_url(page_path)
        self.open(url)

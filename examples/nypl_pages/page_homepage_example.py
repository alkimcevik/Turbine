from seleniumbase import BaseCase
from examples.nypl_utility.url_manager import URLManager


class HomePage(BaseCase):

    staff_picks = "//div[contains(@id,'grid-0')]/div[contains(@id,'card-0')]"
    staff_picks_DS1605 = '//*[@id="grid-1"]/div' # TODO, change after deployment

    nypl_blogs = '//div[contains(@id,\'grid-1\')]/div[contains(@id,\'card-1\')]'
    nypl_blogs_DS1605 = '//*[@id="grid-2"]/div'  # todo: change after deployment

    nypl_blog_content = '//*[@id="grid-1"]'
    nypl_blog_content_DS1605 = '//*[@id="grid-2"]'  # todo: change after deployment

    doug_reside_blog_link = '//*[@id="row-card-heading-1-2-link"]'
    doug_reside_blog_link_DS1605 = '//*[@id="row-card-heading-1-2-link"]'  # todo: change after deployment

    ender_game = '//*[@id="homepage-tabs-2--tab-2"]'
    ender_game_DS1605 = '//*[@id="homepage-tabs-3--tab-2"]'  # todo: change after deployment

    ender_awards = '//div[@id="Ender\'sGame-card"]//p'  # relative XPath

    related_books_h4 = '//*[@id="related-books-2"]'
    related_books_locator = "// *[contains(@id, 'related-books-2-')]"  # relative XPath with contains

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
    the_eye_of_the_world_tab_DS1605 = '//*[@id="homepage-tabs-3--tab-1"]'  # todo: change after deployment

    teofw_related_1 = '//*[@id="related-book-heading-1-0-link"]'
    teofw_related_2 = '//*[@id="related-book-heading-1-1-link"]'

    enders_game_tab = '//*[@id="homepage-tabs-2--tab-2"]'
    enders_game_tab_DS1605 = '//*[@id="homepage-tabs-3--tab-2"]'  # todo: change after deployment

    ender_related_1 = '//*[@id="related-book-heading-2-0-link"]'
    ender_related_2 = '//*[@id="related-book-heading-2-1-link"]'
    ender_related_3 = '//*[@id="related-book-heading-2-2-link"]'


    def open_homepage(self):
        page_path = 'homepage'
        url = URLManager.get_url(page_path)
        self.open(url)

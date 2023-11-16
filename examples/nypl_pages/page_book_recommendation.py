from seleniumbase import BaseCase
from examples.nypl_utility.url_manager import URLManager


class BookRecommendationPage(BaseCase):

    breadcrumb = '//*[@id="book-recommendations-breadcrumbs"]'
    br_home = '(//*[contains(text(), "Home")])[1]'
    br_books_and_more = '(//*[contains(text(), "Books & More")])[1]'
    br_recommendations = '(//*[contains(text(), "Recommendations")])[1]'
    br_staff_picks = '(//*[contains(text(), "Staff Picks")])[1]'

    kids = '//*[@id="kids-link"]'
    teens = '//*[@id="teens-link"]'

    fiction = '//*[@id="filter-item-Fiction"]'
    horror = '//*[@id="filter-item-Horror"]'

    season_selector = '//*[@id="season-selector"]'
    fall_season = '//*[@id="season-selector"]/option[2]'
    submit = '//*[@id="season-selector-button"]'
    stacked_view = '//*[@id="button-row-icon"]'

    picture_books = '//*[@id="filter-item-Picture Books"]'
    picture_books_result = '//*[@id="mainContent"]/div[3]/div[2]/p/span/b'
    book_images = '/html/body/div/div[1]/div[2]/main/div[3]/div[3]/div'
    m_letter = '//*[@id="filter-m"]'
    k_letter = '//*[@id="filter-k"]'
    m_result = '//*[@id="mainContent"]/div[3]/div[2]/p/span/b'
    k_result = '//*[@id="mainContent"]/div[3]/div[2]/p/span/b'
    j_letter = '//*[@id="filter-j"]'
    s_letter = '//*[@id="filter-s"]'
    show_all = '//*[@id="filter-showAll"]'
    kazuo_book = '//*[@id="book-TheDriftingClassroom"]'
    h3_heading = '//*[@id="main-grid"]//h3//..//p'  # author name on the grid
    winter_teen_h2 = '//*[@id="data-heading"]'
    book_result = '//*[@id="mainContent"]/div[3]/div[2]/p/span'
    author_result = '//*[@id="main-grid"]//h3//..//p'


    def open_book_recommendation_page(self):
        page_path = 'recommendations/adults'
        url = URLManager.get_url(page_path)
        self.open(url)

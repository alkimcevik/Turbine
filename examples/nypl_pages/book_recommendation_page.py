from seleniumbase import BaseCase


class BookRecommendationPage(BaseCase):

    breadcrumb = '//*[@id="book-recommendations-breadcrumbs"]'
    br_home = '/html/body/div/div[1]/div[2]/div[1]/div/div/nav/ol/li[1]/a/span'
    br_books_and_more = '/html/body/div/div[1]/div[2]/div[1]/div/div/nav/ol/li[2]/a/span'
    br_recommendations = '/html/body/div/div[1]/div[2]/div[1]/div/div/nav/ol/li[3]/a/span'
    br_staff_picks = '//*[@id="book-recommendations-breadcrumbs"]/ol/li[4]/span/span'

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

    def open_book_recommendation_page(self):
        self.open("https://nypl-ds-test-app.vercel.app/fullPages/recommendations/adults")

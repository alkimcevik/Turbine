from seleniumbase import BaseCase
from examples.nypl_utility.url_manager import URLManager


class SearchPage(BaseCase):
    result_amount = '//*[@id="mainContent"]//h4'  # h4 amount

    slider_left = '//*[@id="slider-thumb-grades-slider-0"]'
    slider_right = '//*[@id="slider-thumb-grades-slider-1"]'

    search_bar = '//*[@id="searchbar-textinput-search-bar"]'
    search_button = '//*[@id="searchbar-button-search-bar"]'

    subjects = '//*[@title="Subjects"]'
    subject_animals = '//*[@id="Animals-wrapper"]//*[contains(text(), "Animals")]'

    sort_by = '(//*[contains(text(), "Sort by")]//..//..)[2]'
    sort_by_z_a = '(//*[contains(text(), "Set Titles, Z - A")])'
    sort_by_high_low = '(//*[contains(text(), "Grades, Low to High")])'
    h4_links = '(//div//h4)'

    language = '//*[@title="Language"]'
    lan_view_all = '//*[@id="view-all-text-btn-language"]'
    lan_french = '//*[@id="French-wrapper"]//*[contains(text(), "French")]'


    def open_search_filter_page(self):
        page_path = 'search-and-filter'
        url = URLManager.get_url(page_path)
        self.open(url)

from seleniumbase import BaseCase
from examples.nypl_utility.url_manager import URLManager


class SearchPage(BaseCase):
    result_text = '//b'

    slider_left = '//*[@id="slider-thumb-grades-slider-0"]'
    slider_right = '//*[@id="slider-thumb-grades-slider-1"]'

    search_bar = '//*[@id="searchbar-textinput-search-bar"]'
    search_button = '//*[@id="searchbar-button-search-bar"]'

    subject_animals = '//*[@id="subjects-1-wrapper"]/label/span[1]'

    sort_by = '//*[contains(text(), "Sort By")]//..//..'
    sort_by_z_a = '(//*[contains(text(), "Set Titles, Z - A")])'
    sort_by_high_low = '(//*[contains(text(), "Grades, Low to High")])'
    h4_links = '(//div//h4)'

    lan_french = '//*[@id="language-10-wrapper"]/label/span[2]'


    def open_search_filter_page(self):
        page_path = 'search-and-filter'
        url = URLManager.get_url(page_path)
        self.open(url)

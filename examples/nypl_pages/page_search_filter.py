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

    sort_by = '//*[@id="menu-button-:RaslqlacnkmH1:"]'  # new locator for 'Sort By' dropdown
    sort_by_z_a = '(//*[@id="menu-list-:RaslqlacnkmH1:"]//button)[4]'
    sort_by_high_low = '(//*[@id="menu-list-:RaslqlacnkmH1:"]//button)[6]'
    h4_links = '(//div//h4)'

    language = '//*[@title="Language"]'
    lan_view_all = '//*[@id="view-all-text-btn-language"]'
    lan_french = '//*[@id="French-wrapper"]//*[contains(text(), "French")]'


    def open_search_filter_page(self):
        # https://nypl-ds-test-app.vercel.app/fullPages/search-and-filter
        page_path = 'search-and-filter'
        url = URLManager.get_url(page_path)
        self.open(url)

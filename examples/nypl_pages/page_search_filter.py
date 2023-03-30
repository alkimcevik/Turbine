from seleniumbase import BaseCase


class SearchPage(BaseCase):
    result_text = '//b'

    slider_left = '//*[@id="slider-thumb-grades-slider-0"]'
    slider_right = '//*[@id="slider-thumb-grades-slider-1"]'

    search_bar = '//*[@id="searchbar-textinput-search-bar"]'
    search_button = '//*[@id="searchbar-button-search-bar"]'

    subject_animals = '//*[@id="subjects-1-wrapper"]/label/span[1]'

    sort_by = '//*[@id="sort-by-select"]'
    sort_by_z_a = '//*[@id="sort-by-select"]/option[3]'
    sort_by_high_low = '//*[@id="sort-by-select"]/option[5]'
    h4_links = '//*[@id="mainContent"]/div[3]/div/div[2]/div[1]/div'

    lan_french = '//*[@id="language-10-wrapper"]/label/span[2]'

    def open_search_filter_page(self):
        self.open("https://nypl-ds-test-app.vercel.app/fullPages/search-and-filter#above-header-notification")
        #self.goto('https://nypl-ds-test-li3jif416-nypl.vercel.app/fullPages/search-and-filter')  # dark mode URL


from seleniumbase import BaseCase


class SearchPage(BaseCase):
    result_text = '//*[@id="mainContent"]/div[3]/div/p'

    slider_left = '//*[@id="slider-thumb-grades-slider-0"]'
    slider_right = '//*[@id="slider-thumb-grades-slider-1"]'


    search_bar = '//*[@id="searchbar-textinput-search-bar"]'
    search_button = '//*[@id="searchbar-button-search-bar"]'

    subject_animals = '//*[@id="subjects-1-wrapper"]/label/span[1]'

    sort_by = '//*[@id="sort-by-select"]'
    sort_by_z_a = '//*[@id="sort-by-select"]/option[3]'
    sort_by_high_low = '//*[@id="sort-by-select"]/option[5]'
    h4_links = '/html/body/div/div/div[2]/main/div[3]/div/div/div[1]/div'

    lan_french = '//*[@id="language-10-wrapper"]/label/span[2]'


    def open_search_filter_page(self):
        self.open("https://nypl-ds-test-app.vercel.app/fullPages/search-and-filter#above-header-notification")



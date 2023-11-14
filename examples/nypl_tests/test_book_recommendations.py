import pytest

from examples.nypl_pages.page_book_recommendation import BookRecommendationPage


class BookRecommendationTests(BookRecommendationPage):

    # https://jira.nypl.org/browse/DSD-1195

    # https://nypl-ds-test-app.vercel.app/fullPages/recommendations/adults

    def setUp(self):
        super().setUp()
        print("\nRUNNING BEFORE EACH TEST")

        # open home page
        self.open_book_recommendation_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        super().tearDown()

    def test_breadcrumbs(self):
        print("test_breadcrumbs()\n")
        # As a desktop user, I expect to see a complete page hierarchy in the breadcrumbs, and I want to be able to
        # navigate to any of the pages in the hierarchy other than the current page.

        # asserting breadcrumbs element
        self.assert_element(self.breadcrumb)

        # checking page hierarchy
        first_breadcrumb = self.get_text(self.br_home)
        second_breadcrumb = self.get_text(self.br_books_and_more)
        third_breadcrumb = self.get_text(self.br_recommendations)
        fourth_breadcrumb = self.get_text(self.br_staff_picks)

        # optional prints to see the texts of the breadcrumbs
        print(first_breadcrumb)
        print(second_breadcrumb)
        print(third_breadcrumb)
        print(fourth_breadcrumb)

        self.assert_true(first_breadcrumb == "Home")
        self.assert_true(second_breadcrumb == "Books & More")
        self.assert_true(third_breadcrumb == "Recommendations")
        self.assert_true(fourth_breadcrumb == "Staff Picks")

        # asserting navigation to the other pages other than the current page
        current_url = self.get_current_url()
        self.click(self.br_home)  # Home link
        print(self.get_current_url())
        self.assert_true("vercel.app" in current_url, "expected URL = " + "vercel.app" + "actual URL = " + current_url)
        self.go_back()
        self.click(self.br_books_and_more)  # Books & More Link
        print(self.get_current_url())
        self.assert_true("vercel.app" in current_url, "expected URL = " + "vercel.app" + "actual URL = " + current_url)
        self.go_back()
        self.click(self.br_recommendations)  # Recommendations Link
        print(self.get_current_url())
        self.assert_true("vercel.app" in current_url, "expected URL = " + "vercel.app" + "actual URL = " + current_url)

    def test_picture_books(self):
        print("test_picture_books()\n")
        # As a parent, I want to be able to see a list of picture books for kids.

        # clicking kids and picture books tabs respectively
        self.click(self.kids)
        self.click(self.picture_books)
        # asserting result is larger than 0
        result_amount = int(self.get_text(self.picture_books_result).split()[0])
        print("Picture books for kids result: " + str(result_amount))

        self.assert_true(result_amount > 0, "Result amount is not greater than 0")

        # assertion by image element amounts
        image_amount = len(self.find_elements('img'))-1  # (len-1) because one of the images on the Footer is NYPL SASB
        print("Image amount on the page: " + str(image_amount))  # optional print of image/book amount
        self.assert_true(image_amount > 1, "Image amount is not greater than 0")

    def test_filter_author(self):
        print("test_filter_author()\n")
        # As a fan of Mashama Bailey, I want to be able to filter the list and find a book by my favorite author.

        # clicking 'M' letter to filter
        self.click(self.m_letter)
        result_amount = int(self.get_text(self.m_result).split()[0])
        print(result_amount)
        # asserting result is larger than 0
        self.assert_true(result_amount > 0)

        # asserting the results have "Mashama Bailey" as the author in the results.
        h4_text = self.get_text(BookRecommendationPage.h3_heading)  # getting the text of the h4
        print(h4_text)  # optional print of the h4
        self.assert_text("Mashama", BookRecommendationPage.h3_heading)  # asserting "Mashama" text in h4

        self.wait(2)

    def test_teens(self):
        print("test_teens()\n")
        # As a teenager, I want to pull up the staff picks for teens for Winter 2022 and see if a book by Kazuo Umezz
        # is on the list and then view the book in the catalog.

        # clicking teens tab
        self.click(self.teens)
        # asserting the text "Winter 2022 Picks for Teens" to verify we are viewing "Winter 2022" results.
        print(self.get_text(self.winter_teen_h2))  # optional print of the Winter 2022 Teen h2
        self.assert_text("Winter 2022 Picks for Teens", self.winter_teen_h2)

        # self.click(self.fall_season)  # comment out to select default 'Winter 2022'
        # self.click(self.submit)  # comment out to leave default

        self.click(self.k_letter)  # filtering by 'K' letter
        k_result = int(self.get_text(self.k_result).split()[0])  # getting the first digit of the result for 'for loop'
        print("'K' letter result = " + str(k_result))  # optional printing

        # finding 'Kazuo' in the results and then clicking the book link to the catalog
        for x in range(1, k_result + 1):
            author_name = \
                self.get_text(BookRecommendationPage.author_result).split()[1]
            if author_name == "Kazuo":
                self.click(self.kazuo_book)
                title = self.get_title()
                print("Title is = " + self.get_title())
                self.assert_true('The drifting classroom.' in title)

    def test_stacked_list(self):
        print("test_stacked_list()\n")
        # As a patron who has trouble with visual organization, I want to filter the recommendations for Winter 2022
        # by Fiction and Horror and then view the results as a stacked list of items.

        self.click(self.fiction)  # choosing Fiction
        self.click(self.horror)  # choosing Horror
        self.click(self.stacked_view)  # stacked view
        # asserting the 'stacked view' with the 'class' attribute. when the view is changed from stacked to grid,
        # the 'class' attribute changes from 'css-1ubn3an' to 'css-q5xggl' and the assertion in on the latter one.
        self.assert_attribute('//*[@id="main-grid"]', "class", 'css-q5xggl')

    def test_author(self):
        print("test_author()\n")
        # As a finicky library patron, I want to quickly see which books were written by authors whose name begins
        # with "J" and then with "S" and then I want to reset the list and see all the books in the list.

        # asserting there are 12 results initially
        initial_result = int(self.get_text(self.book_result).split()[0])
        print("Initial book result = " + str(initial_result))
        self.assert_true(initial_result == 12)

        self.click(self.j_letter)  # Author name starting with J
        # after clicking on the letter "J", there are 2 results, and they should only have authors with names that start
        # with "J".
        j_result = int(self.get_text(self.book_result).split()[0])
        print("\nAuthors starting with 'J' = " + str(j_result))
        self.assert_true(j_result == 2)

        # asserting names starting with 'J' letter
        self.assert_true(
            self.get_text(BookRecommendationPage.h3_heading).split()[1].startswith('J'))

        for x in range(1, 3):
            print(self.get_text(BookRecommendationPage.h3_heading).split()[1])
            self.assert_true(
                self.get_text(BookRecommendationPage.h3_heading).split()[1].startswith('J'))

        print("------------------------------------------------")

        self.click(self.s_letter)  # Author name starting with S
        # after clicking on the letter "S", there are 2 results, and they should only have authors with names that start
        # with "S".
        s_result = int(self.get_text(self.book_result).split()[0])
        print("Authors starting with 'S' = " + str(s_result))
        self.assert_true(s_result == 2)

        # asserting names starting with 'S' letter
        self.assert_true(
            self.get_text(BookRecommendationPage.h3_heading).split()[1].startswith('S'))

        for x in range(1, 3):
            print(self.get_text(BookRecommendationPage.h3_heading).split()[1])
            self.assert_true(
                self.get_text(BookRecommendationPage.h3_heading).split()[1].startswith('S'))

        # after clicking on "Show All", the list will reset with a total of 12 results.
        self.click(self.show_all)  # Resetting the list
        initial_result = int(self.get_text(self.book_result).split()[0])
        print("\nAfter clicking 'Show All', book result = " + str(initial_result))
        self.assert_true(initial_result == 12)


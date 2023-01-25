import pytest

from examples.nypl_pages.book_recommendation_page import BookRecommendationPage


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
        self.click(self.br_home)  # Home link
        self.go_back()
        self.click(self.br_books_and_more)  # Books & More Link
        self.go_back()
        self.click(self.br_recommendations)  # Recommendations Link

    def test_picture_books(self):
        print("test_picture_books()\n")
        # As a parent, I want to be able to see a list of picture books for kids.

        # clicking kids and picture books tabs respectively
        self.click(self.kids)
        self.click(self.picture_books)
        # asserting result is larger than 0
        result_amount = int(self.get_text(self.picture_books_result).split()[0])
        print(result_amount)

        self.assert_true(result_amount > 0)

        # assertion by image element amounts
        image_amount = len(self.find_elements('/html/body/div/div[1]/div[2]/main/div[3]/div[3]/div'))
        print(image_amount)  # optional print of image/book amount
        self.assert_true(image_amount == 4)

    def test_filter_author(self):
        print("test_filter_author()\n")
        # As a fan of Mashama Bailey, I want to be able to filter the list and find a book by my favorite author.

        # clicking 'M' letter to filter
        self.click(self.m_letter)
        result_amount = int(self.get_text(self.m_result).split()[0])
        print(result_amount)
        # asserting result is larger than 0
        self.assert_true(result_amount > 0)

    def test_teens(self):
        print("test_teens()\n")
        # As a teenager, I want to pull up the staff picks for teens for Winter 2022 and see if a book by Kazuo Umezz
        # is on the list and then view the book in the catalog.

        # clicking teens tab
        self.click(self.teens)
        # self.click(self.fall_season)  # comment out to select default 'Winter 2022'
        # self.click(self.submit)  # comment out to leave default
        self.click(self.k_letter)  # filtering by 'K' letter
        k_result = int(self.get_text(self.k_result).split()[0])  # getting the first digit of the result for 'for loop'
        print("'K' letter result = " + str(k_result))  # optional printing

        # finding 'Kazuo' in the results and then clicking the book link to the catalog
        for x in range(1, k_result + 1):
            author_name = \
                self.get_text(
                    '/html/body/div/div[1]/div[2]/main/div[3]/div[3]/div[' + str(x) + ']/div/div[2]/h4').split()[
                    1]
            if author_name == "Kazuo":
                self.click(self.kazuo_book)
                print("Title is = " + self.get_title())
                self.assert_title("NYPL Catalog")
                return True

    def test_stacked_list(self):
        print("test_stacked_list()\n")
        # As a patron who has trouble with visual organization, I want to filter the recommendations for Winter 2022
        # by Fiction and Horror and then view the results as a stacked list of items.

        self.click(self.fiction)  # choosing Fiction
        self.click(self.horror)  # choosing Horror
        self.click(self.stacked_view)  # stacked view

    def test_author(self):
        print("test_author()\n")
        # As a finicky library patron, I want to quickly see which books were written by authors whose name begins
        # with "J" and then with "S" and then I want to reset the list and see all the books in the list.

        self.click(self.j_letter)  # Author name starting with J
        self.click(self.s_letter)  # Author name starting with S
        self.click(self.show_all)  # Resetting the list

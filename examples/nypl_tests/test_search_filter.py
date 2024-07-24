import pytest

from examples.nypl_pages.page_search_filter import SearchPage

@pytest.mark.desktop
class SearchFilterTests(SearchPage):
    # https://jira.nypl.org/browse/DSD-1129

    # https://nypl-ds-test-app.vercel.app/fullPages/search-and-filter#above-header-notification

    def setUp(self):
        super().setUp()
        print("\nRUNNING BEFORE EACH TEST")

        # open blog page
        self.open_search_filter_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        super().tearDown()

    def test_slider(self):
        print("test_slider()")
        # As an elementary, middle school or high school teacher, I want to find teacher sets that are currently
        # available and appropriate for my level of teaching.

        # get the first title to compare against the last title
        title_1 = self.get_title()
        print(self.get_title())

        # test for Grades 1 to 5
        # move slider thumb left and right to adjust the grades 1-5
        self.press_right_arrow(self.slider_left, times=1)
        self.press_left_arrow(self.slider_right, times=7)
        self.wait(1)
        # result amount for 1-5 grades
        result_amount = int(self.get_text(self.result_text).split()[0])
        print(str(result_amount) + " results amount for grades 1 to 5")
        # assert result amount is equal to expected amount
        expected_amount_1 = 11
        self.assert_true(result_amount == expected_amount_1, "Result amount is NOT greater than expected amount")

        # test for Grades 5 to 8
        # refresh the page so that slider can go back to original values
        self.refresh()
        # move slider thumb left and right to adjust the grades 5-8
        self.press_right_arrow(self.slider_left, times=5)
        self.press_left_arrow(self.slider_right, times=4)
        self.wait(1)
        # result amount for 5-8 grades
        result_amount = int(self.get_text(self.result_text).split()[0])
        print(str(result_amount) + " results amount for grades 5 to 8")
        # assert result amount is equal to expected amount
        expected_amount_2 = 17
        self.assert_true(result_amount == expected_amount_2, "Result amount is NOT greater than expected amount")

        # test for Grades 9 to 12
        # refresh the page so that slider can go back to original values
        self.refresh()
        # move slider thumb left and right to adjust the grades 9-12
        self.press_right_arrow(self.slider_left, times=9)
        self.press_left_arrow(self.slider_right, times=0)
        self.wait(1)
        # result amount for 9-12 grades
        result_amount = int(self.get_text(self.result_text).split()[0])
        print(str(result_amount) + " results amount for grades 9 to 12")
        # assert result amount is equal to expected amount
        expected_amount_3 = 9
        self.assert_true(result_amount == expected_amount_3, "Result amount is NOT greater than expected amount")

        # get the last title
        title_2 = self.get_title()
        print(self.get_title())

        # compare first and last titles
        self.assert_true(title_1 == title_2)

    def test_search_bar(self):
        print("test_search_bar()")
        # As a teacher of children with vision disabilities, I want to find teacher sets that include books with
        # large print.

        # get the first title to compare against the last title
        title_1 = self.get_title()
        print(self.get_title())

        # sending 'Large Print' to the search bar
        self.send_keys(self.search_bar, "Large Print")
        self.click(self.search_button)
        self.wait(1)

        # optional print of the result
        print(self.get_text(self.result_text))
        # first element of the result text, which is the result amount to be compared for assertion
        result_amount = int(self.get_text(self.result_text).split()[0])
        # print the result amount
        print(str(result_amount) + " results found")

        # assert the result is == expected amount
        expected_amount = 15
        self.assert_true(result_amount == expected_amount, "Result is NOT greater than expected amount")
        self.wait(2)

        # get the last title
        title_2 = self.get_title()
        print(self.get_title())

        # compare first and last titles
        self.assert_true(title_1 == title_2)

    def test_subjects(self):
        print("test_subjects()")
        # As a biology teacher, I want to find all teacher sets about animals.

        # get the first title to compare against the last title
        title_1 = self.get_title()
        print(self.get_title())

        self.click(self.subjects)  # click "Subjects" accordion
        self.click(self.subject_animals)  # click "Animals" selection
        self.wait(0.5)
        self.scroll_to_element(self.result_text)

        # optional print of the result
        print(self.get_text(self.result_text))
        # first element of the result text, which is the result amount to be compared for assertion
        result_amount = int(self.get_text(self.result_text).split()[0])
        # print the result amount
        print(str(result_amount) + " results found")

        # assert the result == expected
        expected_result = 2
        self.assert_true(result_amount == expected_result, "Result is NOT equal to the expected amount")
        self.wait(2)

        # get the last title
        title_2 = self.get_title()
        print(self.get_title())

        # compare first and last titles
        self.assert_true(title_1 == title_2)

    def test_first_letter(self):
        print("test_first_letter()")
        # As an elementary school teacher, I want to find teacher sets with books that start with the letter W.

        # get the first title to compare against the last title
        title_1 = self.get_title()
        print(self.get_title())

        # change the 'Sort By' to 'Set Titles, Z-A'
        self.click(self.sort_by)
        self.click(self.sort_by_z_a)
        self.wait(1)

        actual_amount = 0
        for x in range(1, 6):

            first_letter = self.get_text(SearchPage.h4_links + '[' + str(x) + ']').split()[0][0]
            print(first_letter + " is the first letter")

            if first_letter == 'W' or first_letter == 'w':
                actual_amount += 1

        print("\n" + str(actual_amount) + " total word starting with W.")
        # asserting the result is equal to expected amount
        expected_amount = 1
        self.assert_true(actual_amount >= expected_amount, "Actual = " + str(actual_amount) + ", Expected = " + str(expected_amount) +  " No teacher sets with books that start with the letter W.")

        # get the last title
        title_2 = self.get_title()
        print(self.get_title())

        # compare first and last titles
        self.assert_true(title_1 == title_2)

    def test_high_low(self):
        print("test_high_low()")
        # As a school administrator, I want to review the teacher sets in grade order from highest to lowest.

        # get the first title to compare against the last title
        title_1 = self.get_title()
        print(self.get_title())

        # change the 'Sort By' to 'Grades, High to Low'
        self.click(self.sort_by)
        self.click(self.sort_by_high_low)
        self.wait(1)

        print(self.get_current_url())

        result_amount = int(self.get_text(self.result_text).split()[0])

        # print the result amount
        print(str(result_amount) + " results found")
        # asserting the result is equal to expected amount
        expected_amount = 20
        self.assert_true(result_amount == expected_amount, "Expected amount = " + str(expected_amount) + ", Actual = " + str(result_amount) + "There is not enough teacher sets in this order")

        # get the last title
        title_2 = self.get_title()
        print(self.get_title())

        # compare first and last titles
        self.assert_true(title_1 == title_2)

    def test_language(self):
        print("test_language()")
        # As a French teacher, I want to find teacher sets that are written in French.

        # get the first title to compare against the last title
        title_1 = self.get_title()
        print(self.get_title())

        # click on French
        self.click(self.language)  # click 'Language' accordion
        self.click(self.lan_french)  # click "French" selection
        self.wait(1)

        result_amount = int(self.get_text(self.result_text).split()[0])

        # print the result amount
        print(str(result_amount) + " results found")
        # asserting the result is equal to expected amount
        expected_amount = 1
        self.assert_true(result_amount == expected_amount, "There is not enough teacher sets in this order")

        # get the last title
        title_2 = self.get_title()
        print(self.get_title())

        # compare first and last titles
        self.assert_true(title_1 == title_2)


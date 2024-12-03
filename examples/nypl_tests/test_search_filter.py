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
        result_amount = len(self.find_elements(self.result_amount))
        print(str(result_amount) + " results amount for grades 1 to 5")
        # assert result amount is equal to expected amount
        self.assert_true(1 <= result_amount <= 20, "Result is NOT between the expected range")

        # test for Grades 5 to 8
        # refresh the page so that slider can go back to original values
        self.refresh()
        # move slider thumb left and right to adjust the grades 5-8
        self.press_right_arrow(self.slider_left, times=5)
        self.press_left_arrow(self.slider_right, times=4)
        self.wait(1)
        # result amount for 5-8 grades
        result_amount = len(self.find_elements(self.result_amount))
        print(str(result_amount) + " results amount for grades 5 to 8")
        # assert result amount is equal to expected amount
        self.assert_true(1 <= result_amount <= 20, "Result is NOT between the expected range")

        # test for Grades 9 to 12
        # refresh the page so that slider can go back to original values
        self.refresh()
        # move slider thumb left and right to adjust the grades 9-12
        self.press_right_arrow(self.slider_left, times=9)
        self.press_left_arrow(self.slider_right, times=0)
        self.wait(1)
        # result amount for 9-12 grades
        result_amount = len(self.find_elements(self.result_amount))
        print(str(result_amount) + " results amount for grades 9 to 12")
        # assert result amount is equal to expected amount
        self.assert_true(1 <= result_amount <= 20, "Result is NOT between the expected range")

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
        result_amount = len(self.find_elements(self.result_amount))
        print(result_amount)
        # first element of the result text, which is the result amount to be compared for assertion
        result_amount = len(self.find_elements(self.result_amount))
        # print the result amount
        print(str(result_amount) + " results found")

        # assert the result is between 1  < 20
        self.assert_true(1 <= result_amount <= 20, "Result is NOT greater than expected amount")
        self.wait(2)

        # get the last title
        title_2 = self.get_title()
        print(self.get_title())

        # compare first and last titles
        self.assert_true(title_1 == title_2)

    def test_subjects(self):
        print("Running test_subjects()")
        # As a biology teacher, I want to find all teacher sets about animals.

        # Get the first title to compare against the last title later
        title_1 = self.get_title()
        print("First title:", title_1)

        # Open "Subjects" accordion and select "Animals"
        self.click(self.subjects)
        self.click(self.subject_animals)
        self.wait(0.5)  # Brief wait to ensure filter is applied

        # Optionally print the number of results found
        result_text = self.get_text(self.result_amount)
        print("Result text:", result_text)

        # Get the result count based on the elements found and display it
        result_amount = len(self.find_elements(self.result_amount))
        print(f"{result_amount} results found")

        # Assert that the result is within the expected range (1 to 20)
        self.assert_true(
            1 <= result_amount <= 20,
            f"Result amount {result_amount} is NOT between the expected range of 1 and 20"
        )

        # Optional wait for any final loading
        self.wait(2)

        # Get the last title for comparison
        title_2 = self.get_title()
        print("Last title:", title_2)

        # Compare first and last titles to ensure they are the same
        self.assert_true(
            title_1 == title_2,
            f"Titles do not match: First title = '{title_1}', Last title = '{title_2}'"
        )

    def test_first_letter(self):
        print("Running test_first_letter()")
        # As an elementary school teacher, I want to find teacher sets with books that start with the letter W.

        # Get the first title to compare against the last title later
        title_1 = self.get_title()
        print("First title:", title_1)

        # Change the 'Sort By' to 'Set Titles, Z-A'
        self.click(self.sort_by)
        self.click(self.sort_by_z_a)
        self.wait(1)  # Allow page to refresh after sorting

        # Initialize counter for titles starting with 'W'
        actual_amount = 0

        # Loop through the first 5 h4 links to check for 'W' as the first letter
        for x in range(1, 6):
            first_letter = self.get_text(f"{SearchPage.h4_links}[{x}]").split()[0][0].upper()
            print(f"{first_letter} is the first letter")

            # Count if the first letter is 'W'
            if first_letter == 'W':
                actual_amount += 1

        print(f"\nTotal words starting with 'W': {actual_amount}")

        # Assert that the actual count is at least the expected amount
        expected_amount = 1
        self.assert_true(
            actual_amount >= expected_amount,
            f"Actual = {actual_amount}, Expected = {expected_amount}. No teacher sets with books that start with the letter W."
        )

        # Get the last title and compare it to the first title
        title_2 = self.get_title()
        print("Last title:", title_2)

        # Verify that the first and last titles are the same after sorting
        self.assert_true(
            title_1 == title_2,
            f"Titles do not match: First title = '{title_1}', Last title = '{title_2}'"
        )

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

        result_amount = len(self.find_elements(self.result_amount))

        # print the result amount
        print(str(result_amount) + " results found")
        # asserting the result is equal to expected amount (12-20)
        self.assert_true(12 <= result_amount <= 20, "Expected amount = 12- 20 "", Actual = " + str(result_amount) + "There is not enough teacher sets in this order")

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
        self.click(self.lan_view_all)  # click view all underneath Language
        self.click(self.lan_french)  # click "French" selection
        self.wait(1)

        result_amount = len(self.find_elements(self.result_amount))

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


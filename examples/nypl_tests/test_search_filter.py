from examples.nypl_pages.search_filter_page import SearchPage


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
        # As an elementary, middle school or high school teacher, I want to find teacher sets that are currently
        # available and appropriate for my level of teaching.

        # test for Grades 1 to 5
        # move slider thumb left and right to adjust the grades 1-5
        self.press_right_arrow(self.slider_left, times=1)
        self.press_left_arrow(self.slider_right, times=7)
        self.wait(1)
        # result amount for 1-5 grades
        result_amount = int(self.get_text(self.result_text).split()[0])
        print(str(result_amount) + " results amount for grades 1 to 5")
        # assert result amount is greater than 1
        self.assert_true(result_amount >= 1, "Result amount is NOT greater than expected amount")

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
        # assert result amount is greater than 1
        self.assert_true(result_amount >= 1, "Result amount is NOT greater than expected amount")

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
        # assert result amount is greater than 1
        self.assert_true(result_amount >= 1, "Result amount is NOT greater than expected amount")

    def test_search_bar(self):
        # As a teacher of children with vision disabilities, I want to find teacher sets that include books with
        # large print.

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

        # assert the result is >= 1
        self.assert_true(result_amount >= 1, "Result is NOT greater than expected amount")
        self.wait(2)

    def test_subjects(self):
        # As a biology teacher, I want to find all teacher sets about animals.

        self.click(self.subject_animals)

        # optional print of the result
        print(self.get_text(self.result_text))
        # first element of the result text, which is the result amount to be compared for assertion
        result_amount = int(self.get_text(self.result_text).split()[0])
        # print the result amount
        print(str(result_amount) + " results found")

        # assert the result is >= 1
        self.assert_true(result_amount >= 1, "Result is NOT greater than expected amount")
        self.wait(2)

    def test_first_letter(self):
        # As an elementary school teacher, I want to find teacher sets with books that start with the letter W.

        # change the 'Sort By' to 'Set Titles, Z-A'

        self.click(self.sort_by)
        self.click(self.sort_by_z_a)
        self.wait(1)

        # find h4 amount on the page to use for the length in the for loop
        h4_amount = len(self.find_elements(self.h4_links))

        count = 0
        for x in range(1, h4_amount + 1):

            first_letter = self.get_text('/html/body/div/div/div[2]/main/div[3]/div/div/div[1]/div[' + str(x) + ']/div/div/div/h4/a').split()[0][0]
            print(first_letter + " is the first letter")

            if first_letter is 'W' or first_letter is 'w':
                count += 1

        print(str(count) + " total word starting with W.")
        # asserting the result is >= 1
        self.assert_true(count >= 1, "No teacher sets with books that start with the letter W.")

    def test_high_low(self):
        # As a school administrator, I want to review the teacher sets in grade order from highest to lowest.

        # change the 'Sort By' to 'Grades, High to Low'

        self.click(self.sort_by)
        self.click(self.sort_by_high_low)
        self.wait(1)

        result_amount = int(self.get_text(self.result_text).split()[0])

        # print the result amount
        print(str(result_amount) + " results found")
        # asserting the result is >= 1
        self.assert_true(result_amount >= 1, "There is not enough teacher sets in this order")

    def test_language(self):
        # As a French teacher, I want to find teacher sets that are written in French.
        self.click(self.lan_french)
        self.wait(1)

        result_amount = int(self.get_text(self.result_text).split()[0])

        # print the result amount
        print(str(result_amount) + " results found")
        # asserting the result is >= 1
        self.assert_true(result_amount >= 1, "There is not enough teacher sets in this order")


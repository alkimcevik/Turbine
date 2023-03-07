from examples.nypl_pages.page_homepage_example import HomePage


class HomepageTests(HomePage):

    # https://jira.nypl.org/browse/DSD-1194

    # https://nypl-ds-test-app.vercel.app/fullPages/homepage

    def setUp(self):
        super().setUp()
        print("\nRUNNING BEFORE EACH TEST")

        # open home page
        self.open_homepage()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        super().tearDown()

    def test_headings_4_items(self):
        print("test_headings_4_items()\n")
        # As a library patron, I expect to see four items under the Staff Picks heading and four items under the NYPL
        # Blog heading.

        staff_picks_items_amount = len(self.find_elements(self.staff_picks))
        print("Staff Picks has " + str(staff_picks_items_amount) + " items.")
        self.assert_true(staff_picks_items_amount == 4, "Expected = 4, Actual = " + str(staff_picks_items_amount))

        nypl_blog_items_amount = len(self.find_elements(self.nypl_blogs))
        print("NYPL Blogs has " + str(nypl_blog_items_amount) + " items.")
        self.assert_true(nypl_blog_items_amount == 4, "Expected = 4, Actual = " + str(nypl_blog_items_amount))

    def test_doug_reside(self):
        print("test_doug_reside()\n")
        # As a library patron, I want to find and read a blog post by Doug Reside.

        # assertion 1: to find the blog post

        blog_writer = 'Doug Reside'  # blog author
        # blog_2 = 'Carrie McBride'  # optional author

        count = 0  # count to use in assertion

        # for loop to find the amount of the author's blog posts
        for x in range(1, 5):
            if blog_writer in self.get_text(
                    '//*[@id="mainContent"]/div/div[' + str(x) + ']'):
                print('Author has a blog post on number ' + str(x) + ' blog')  # optional print of the order of teh blog
                count += 1
        print(count)

        # asserting the count is >= 1
        self.assert_true(count >= 1, "The count is not greater than 1")

        # assertion 2: to read the blog post

        # click the author's post and see if the link will go through
        self.is_element_clickable(self.doug_reside_blog_link)
        self.click(self.doug_reside_blog_link)

    def test_featured_books(self):
        print("test_featured_books()\n")
        # As a library patron viewing the Featured Books, I expect the related books to be different for each
        # featured book.

        # asserting if the 'Featured Books' are related
        book_dict = {}  # creating a dictionary to add the book names from the 'featured books' link
        for x in range(0, 3):
            book_dict["book{0}".format(x)] = self.get_text('//*[@id="homepage-tabs-2--tab-' + str(x) + '"]')

        print(book_dict)  # optional print to see the book names
        print("_-_-_-_-_-_-_-_-_-")

        # creating a reusable function 'check_unique_values' to check if the values are different
        def check_unique_values(dictionary):
            book_set = set()  # creating a set() to add the book names later
            # for loop to go over the elements of the 'dictionary' parameter to check if they are unique
            # if they are unique, they will be added to the 'book_set' set
            for book in dictionary.values():
                print(book)
                if book in book_set:
                    return False
                book_set.add(book)
            return True

        # calling and asserting the check_unique_values function to check the book_dict dictionary items we created
        result = check_unique_values(book_dict)  # boolean result
        print("_-_-_-_-_-_-_-_-_-")
        self.assert_true(result, "related books are not unique")  # checking if the result is TRUE
        print(result)  # printing the boolean result

        # assertion for DUNE's 'related books'
        dune_book_1 = self.get_text(self.dune_related_1)
        dune_book_2 = self.get_text(self.dune_related_2)
        dune_book_3 = self.get_text(self.dune_related_3)
        print("\n" + dune_book_1)  # optional print
        print(dune_book_2)  # optional print
        print(dune_book_3)  # optional print

        assert dune_book_1 != dune_book_2 != dune_book_3

        # assertion for "The Eye of the World's" 'related books'
        self.click(self.the_eye_of_the_world_tab)
        teofw_book_1 = self.get_text(self.teofw_related_1)
        teofw_book_2 = self.get_text(self.teofw_related_2)
        print("\n" + teofw_book_1)  # optional print
        print(teofw_book_2)  # optional print

        assert teofw_book_1 != teofw_book_2

        # assertion for "Ender's Game" 'related books'
        self.click(self.enders_game_tab)
        ender_book_1 = self.get_text(self.ender_related_1)
        ender_book_2 = self.get_text(self.ender_related_2)
        ender_book_3 = self.get_text(self.ender_related_3)
        print("\n" + ender_book_1)  # optional print
        print(ender_book_2)  # optional print
        print(ender_book_3)  # optional print

        assert ender_book_1 != ender_book_2 != ender_book_3

    def test_featured_awards(self):
        print("test_featured_awards()\n")
        # As a library patron viewing the Featured Books, I want to see the awards won by and the books related to
        # Ender's Game.

        print("\nAwards Won by Ender's Game")
        # the awards won by Ender's Game

        # click on "Ender's Game" tab
        self.click(self.ender_game)

        # getting the 'Awards' element text and asserting the text
        awards_text = self.get_text(self.ender_awards)
        print(awards_text)  # optional print of the text
        self.assert_true('Award' in awards_text, "Expected word > Award " + ' is not in Actual > ' + awards_text)
        # asserting the 'Awards' element
        self.assert_element(self.ender_awards)

        print("\nRelated Books")
        # related books to "Ender's Game"

        # asserting 'related books' h4 heading
        self.assert_element(self.related_books_h4)

        # asserting the amount of the related books == 3
        related_books_amount = len(self.find_elements(self.related_books_locator))
        print("There are " + str(related_books_amount) + " related books to Ender's Game.")  # optional print
        self.assert_true(related_books_amount == 3, "Related books amount is not 3, it is = " + str(related_books_amount))

    def test_feedback_form(self):
        print("test_feedback_form()\n")
        # As a know-it-all website user who found a typo in a description for a blog post, I want to be able to use
        # the feedback form to inform NYPL about the error.

        # positive testing to see the submission text after all the necessary fields filled
        # todo: Is negative testing necessary for this test?
        self.click(self.feedback_form)  # clicking the feedback form on the right bottom corner
        self.click(self.bug_radio)  # clicking bug button
        self.send_keys(self.comment, "What is the 2003 movie directed by Tim Burton?")  # commenting
        self.send_keys(self.e_mail, "drizzt_dourden@menzoberranzan.org")  # entering email
        self.click(self.submit_button)  # submitting the feedback

        self.assert_true("Thank you for submitting" in self.submission_text)

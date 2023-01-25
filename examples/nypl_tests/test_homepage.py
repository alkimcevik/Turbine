from examples.nypl_pages.homepage_example_page import HomePage


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
        self.assert_true(staff_picks_items_amount == 4)

        nypl_blog_items_amount = len(self.find_elements(self.nypl_blogs))
        print("NYPL Blogs has " + str(nypl_blog_items_amount) + " items.")
        self.assert_true(nypl_blog_items_amount == 4)

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
                    '/html/body/div/div[1]/div[2]/main/div/div[3]/div[2]/div[' + str(x) + ']/div[2]/div[1]'):
                print('Author has a blog post on number ' + str(x) + ' blog')  # optional print of the order of teh blog
                count += 1
        print(count)

        # asserting the count is >= 1
        self.assert_true(count >= 1)

        # assertion 2: to read the blog post

        # click the author's post and see if the link will go through
        self.is_element_clickable(self.doug_reside_blog_link)
        self.click(self.doug_reside_blog_link)

    def test_featured_books(self):
        print("test_featured_books()\n")
        # As a library patron viewing the Featured Books, I expect the featured books to be different for each
        # featured book.

        book_dict = {}  # creating a dictionary to add the book names from the 'featured books' link
        for x in range(1, 4):
            book_dict["book{0}".format(x)] = self.get_text('/html/body/div/div[1]/div[2]/main/div/div[4]/div[2]/div['
                                                           '1]/div/div/div/button[' + str(x) + ']')

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
        self.assert_true(result)  # checking if the result is TRUE
        print(result)  # printing the boolean result

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
        self.assert_true('Awards' in awards_text)
        # asserting the 'Awards' element
        self.assert_element(self.ender_awards)

        print("\nRelated Books")
        # related books to "Ender's Game"

        # asserting 'related books' h4 heading
        self.assert_element(self.related_books_h4)

        # asserting the amount of the related books >= 1
        related_books_amount = len(self.find_elements(self.related_books_locator))
        print("There is/are " + str(related_books_amount) + " related books to Ender's Game.")  # optional print
        self.assert_true(related_books_amount >= 1)

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

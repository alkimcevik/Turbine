from seleniumbase import BaseCase
from examples.nypl_pages.page_book_recommendation import BookRecommendationPage


class MobileTests(BookRecommendationPage):

    # https://jira.nypl.org/browse/DSD-1195

    # https://nypl-ds-test-app.vercel.app/fullPages/recommendations/adults
    def test_mobile(self):
        print("test_mobile()\n")
        # this test should be run with --mobile command on terminal, for instance:
        # pytest test_mobile.py --headless --mobile
        # running on an IDE will result with a failure and 'Element was still visible after 7 seconds!' Exception

        # As a mobile user, I expect to see only the current page in the breadcrumbs, and I want to be able to
        # navigate to the parent page.

        # go to URL
        url = 'https://nypl-ds-test-app.vercel.app/fullPages/recommendations/adults'  # regular URL
        smoke_test_url = "https://nypl-ds-test-app-git-dsd-1605-ds-210-update-nypl.vercel.app/fullPages/recommendations/adults"  # smoke test url
        self.goto(smoke_test_url)
        # self.goto('https://nypl-ds-test-li3jif416-nypl.vercel.app/fullPages/recommendations/adults')  # dark mode URL

        # assert no other elements visible other than 'staff picks'
        self.assert_element_not_visible(self.br_home)
        self.assert_element_not_visible(self.br_books_and_more)
        self.assert_element_not_visible(self.br_recommendations)
        # assert the 'Staff Picks' web element
        self.assert_element_visible(self.br_staff_picks)



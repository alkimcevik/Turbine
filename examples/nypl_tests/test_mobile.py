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

        # todo: CI/CD > add a new command line for mobile on python-package.yml on Github Actions
        # for instance:
        """
        - name: Run pytest examples/nypl_tests/test_mobile.py --browser=chrome --xvfb
          run: |
            pytest examples/nypl_tests/test_mobile.py --browser=chrome --headless -v -s --mobile
        """
        # As a mobile user, I expect to see only the current page in the breadcrumbs, and I want to be able to
        # navigate to the parent page.
        # https://nypl-ds-test-app.vercel.app/fullPages/recommendations/adults

        # go to URL
        self.goto('https://nypl-ds-test-app.vercel.app/fullPages/recommendations/adults')
        self.assert_element_not_visible(self.br_home)
        self.assert_element_not_visible(self.br_books_and_more)
        self.assert_element_not_visible(self.br_recommendations)
        self.assert_element_visible(self.br_staff_picks)

        # assert the 'Staff Picks' web element

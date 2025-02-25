import pytest

from examples.nypl_pages.page_book_recommendation import BookRecommendationPage
from examples.nypl_utility.url_manager import URLManager  # Import the URLManager

@pytest.mark.mobile
class MobileTests(BookRecommendationPage):

    # https://jira.nypl.org/browse/DSD-1195

    # https://nypl-ds-test-app.vercel.app/fullPages/recommendations/adults

    @pytest.fixture(autouse=True)
    def setup_and_teardown(self, request):
        super().setUp()

        # Use URLManager to get the correct URL
        page_path = 'recommendations/adults'
        url = URLManager.get_url(page_path)  # This will automatically pick regular or smoke test URL
        self.goto(url)

        self.wait_for_ready_state_complete()
        self.session_id = self.driver.session_id  # Retrieve the session_id from the WebDriver instance
        # Store the session_id in the request node
        request.node.session_id = self.session_id
        yield
        # Perform teardown
        super().tearDown()

    def test_mobile(self):
        print("test_mobile()\n")

        """
        # this test should be run with --mobile command on terminal, for instance:
        # pytest test_mobile.py --headless --mobile,
        # or with a marker, e.g.: pytest -m mobile
        # running on an IDE will result with a failure and 'Element was still visible after 7 seconds!' Exception
        """

        # As a mobile user, I expect to see only the current page in the breadcrumbs, and I want to be able to
        # navigate to the parent page.


        # # Use URLManager to get the correct URL
        # page_path = 'recommendations/adults'
        # url = URLManager.get_url(page_path)  # This will automatically pick regular or smoke test URL
        #
        # self.goto(url)

        # assert no other elements visible other than 'staff picks'
        self.assert_element_not_visible(self.br_home)
        self.assert_element_not_visible(self.br_books_and_more)
        self.assert_element_not_visible(self.br_recommendations)
        # assert the 'Staff Picks' web element
        self.assert_element_visible(self.br_staff_picks)



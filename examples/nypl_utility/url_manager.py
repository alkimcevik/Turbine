class URLManager:
    """
        URLManager centralizes the management of URLs used across various tests.
        It facilitates the easy switch between regular test URLs and smoke test URLs for different pages.

        Attributes:
            BASE_REGULAR_URL (str): The base URL for regular test runs. This URL is steady and typically doesn't change.
            BASE_SMOKE_TEST_URL (str): The base URL for smoke tests. This URL can change with each new release.

        Usage:
            To use URLManager, simply call the get_url method with the specific page path you need.
            The method will return the correct full URL based on whether smoke tests are active.

        Example:
            # To get a URL for a specific page:
            page_path = 'fullPages/recommendations/adults'
            url = URLManager.get_url(page_path)

            # This will return either the regular or smoke test URL for the 'recommendations/adults' page,
            # depending on the state of the SMOKE_TEST_ACTIVE flag.

        Note:
            When preparing for a new release and running smoke tests, set SMOKE_TEST_ACTIVE to True.
            After the release, revert it back to False to switch back to the regular URLs for standard test runs.
        """

    BASE_REGULAR_URL = 'https://nypl-ds-test-app.vercel.app/fullPages/'
    BASE_SMOKE_TEST_URL = 'https://nypl-ds-test-app-git-dsd-1757-ds-310-update-nypl.vercel.app/fullPages/'

    # Set this to True when running smoke tests, False otherwise
    SMOKE_TEST_ACTIVE = False


    @staticmethod
    def get_url(page_path):
        if URLManager.SMOKE_TEST_ACTIVE:
            print("Running Smoke Test...")
            base_url = URLManager.BASE_SMOKE_TEST_URL
        else:
            print("Running Regular Test...")
            base_url = URLManager.BASE_REGULAR_URL

        return f"{base_url}{page_path}"

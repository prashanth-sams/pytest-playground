"""Simple Playwright test for Google search."""

import pytest
from playwright.sync_api import Page, expect
# from pytest_html_reporter import attach


# @pytest.fixture(autouse=True)
# def capture_screenshot_on_failure(page: Page, request):
#     """Capture screenshot on test failure."""
#     yield
#     if request.node.rep_call.failed:
#         attach(data=page.screenshot())


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Make test result available to fixtures."""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


def test_google_search(page: Page):
    """Test Google search functionality."""
    # Navigate to Google
    page.goto("https://www.google.com")
    # attach(data=page.screenshot())

    # Accept cookies if the dialog appears (common in EU)
    # try:
    #     page.click("text=Accept all", timeout=3000)
    # except:
    #     pass  # Cookie dialog might not appear
    
    # Find the search box and enter a query
    search_box = page.locator("textarea[name='qasdasd']")

    # click search box
    search_box.click()

    # Wait for results to load
    page.wait_for_load_state("networkidle")
    
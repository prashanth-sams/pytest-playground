"""Simple Selenium test for Google search."""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pytest_html_reporter import attach


@pytest.fixture
def driver():
    """Create and quit Chrome WebDriver."""
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_google_search(driver):
    """Test Google search functionality with Selenium."""
    # Navigate to Google
    driver.get("https://www.google.com")
    
    # Accept cookies if present
    try:
        accept_button = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Accept all')]"))
        )
        accept_button.click()
    except:
        pass  # Cookie dialog might not appear
    
    attach(data=driver.get_screenshot_as_png())

    # Find the search box and enter a query
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium WebDriver")
    search_box.send_keys(Keys.RETURN)
    
    
    # Wait for search results
    # WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.ID, "search"))
    # )
    
    # # Verify we're on the search results page
    # assert "Selenium WebDriver" in driver.title
    
    # # Verify search results are present
    # results = driver.find_element(By.ID, "search")
    # assert results.is_displayed()

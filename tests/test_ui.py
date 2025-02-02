import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from business.text_box_page import TextBoxPage

@pytest.fixture
def setup():
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://demoqa.com/text-box")
    driver.maximize_window()
    yield driver
    driver.quit()


def test_submit_form(setup):
    text_box_page = TextBoxPage(setup)

    # Input Data
    full_name = "Donald Duck"
    email = "donald.duck@example.com"
    current_address = "56 Main St"
    permanent_address = "379 Apple Rd"

    # Actions
    text_box_page.enter_full_name(full_name)
    text_box_page.enter_email(email)
    text_box_page.enter_current_address(current_address)
    text_box_page.enter_permanent_address(permanent_address)
    text_box_page.click_submit()

    # Expected results
    expected_name = f"Name:{full_name}"
    expected_email = f"Email:{email}"
    expected_current_address = f"Current Address :{current_address}"
    expected_permanent_address = f"Permananet Address :{permanent_address}"

    # Outputs
    actual_name, actual_email, actual_current_address, actual_permanent_address = text_box_page.get_output()

    # Assertions
    assert actual_name == expected_name
    assert actual_email == expected_email
    assert actual_current_address == expected_current_address
    assert actual_permanent_address == expected_permanent_address
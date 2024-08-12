
import time
from pages.login import Login
import pytest
from utils.csv_file import read_csv_as_tuples

@pytest.mark.parametrize("user_id",read_csv_as_tuples("data/user_login.csv"))
def test_login(driver,user_id):
    login_page=Login(driver)
    login_page.wait(id="userSelect",wait_timeout=10)
    login_page.select_element_by_id(element_id="userSelect",select_index=user_id)
    login_page.click_element(class_name="btn-default")
    time.sleep(2)
    driver.get_screenshot_as_file(f"screenshot_{user_id}.png")
    time.sleep(3)
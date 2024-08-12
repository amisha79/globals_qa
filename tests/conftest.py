import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer') 
    yield driver
    driver.quit()
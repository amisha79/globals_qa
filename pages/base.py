import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Page:
    
    def __init__(self,driver):
        self.driver=driver
    def select_element_by_id(self,element_id,select_index):
        dropdown = self.driver.find_element(By.ID, element_id)
        select = Select(dropdown)
        #dropdown.click()
        time.sleep(3)
        print (select.options)
        select.select_by_index(select_index)

    def wait(self,id=None,class_name=None,wait_timeout=3):
        wait = WebDriverWait(self.driver, wait_timeout)  
        if id:
            wait.until(EC.visibility_of_element_located((By.ID, id)))
        if class_name:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, class_name)))
        
    def click_element(self,id=None,class_name=None):
        if id:
            self.driver.find_element(By.ID, id).click()
        if class_name:
            self.driver.find_element(By.CLASS_NAME, class_name).click()
        
            
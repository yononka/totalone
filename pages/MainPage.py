from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def go_to_page(self, url):
        return self.driver.get(url)

    def find_element(self, locator, time=15):
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")


    def check_element_clickable(self, locator, time=10):
        return WebDriverWait(self.driver,time).until(EC.element_to_be_clickable(locator),
                                                      message=f"Element is not clickable {locator}")

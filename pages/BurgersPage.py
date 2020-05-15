from pages.MainPage import BasePage
from selenium.webdriver.common.by import By

class BugergsLocators:
    pass


class Burgers(BasePage):
    def select_burger(self, burger_type):
        BURGER = (By.XPATH, f"//span[text()='{burger_type}']")
        burger = self.find_element(BURGER)
        burger.click()
        return burger
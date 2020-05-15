from pages.MainPage import BasePage
from selenium.webdriver.common.by import By

class SlamburgerLocators:
    ADD_TO_BAG_BUTTON = (By.XPATH, "//span[text()='Add to Bag']/parent::button")


class Slamburger(BasePage):
    def choose_ingredient(self, ingredient):
        INGREDIENT = (By.XPATH, f"//span[text()='{ingredient}']/../../../../div")
        ingredient = self.find_element(INGREDIENT)
        ingredient.click()
        return ingredient

    def add_to_bag(self):
        into_bag = self.find_element(SlamburgerLocators.ADD_TO_BAG_BUTTON)
        into_bag.click()
        return into_bag

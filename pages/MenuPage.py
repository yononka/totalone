from pages.MainPage import BasePage
from selenium.webdriver.common.by import By


class MenuLocators:
    BURGERS_MENU = (By.XPATH, "//span[text()='Burgers']")


class Menu(BasePage):

    def open_burger_menu(self):
        burger_menu = self.find_element(MenuLocators.BURGERS_MENU)
        burger_menu.click()
        return burger_menu
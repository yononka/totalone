from pages.MainPage import BasePage
from selenium.webdriver.common.by import By


class LocationsLocators:
    BROOKLYN_ZIP = '11207'
    LOCATION_SEARCH_FIELD = (By.ID, "locationSearchInput")
    GO_BUTTON = (By.XPATH, "//button[@class = 'simplesearch__btn']")
    ORDER_AT_BROOKLYN_LOCATION = (By.XPATH, "//span[contains (text(), '11207')]/parent::button")


class Locations(BasePage):

    def set_brooklyn_location(self):
        search_brooklyn_location = self.find_element(LocationsLocators.LOCATION_SEARCH_FIELD)
        search_brooklyn_location.send_keys(LocationsLocators.BROOKLYN_ZIP)
        self.find_element(LocationsLocators.GO_BUTTON).click()
        brooklyn_location = self.find_element(LocationsLocators.ORDER_AT_BROOKLYN_LOCATION)
        brooklyn_location.click()
        return brooklyn_location
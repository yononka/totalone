from pages.MainPage import BasePage
from selenium.webdriver.common.by import By

class AsGuestLocators:
    FIRST_NAME = (By.ID, "guest-user-firstname")
    LAST_NAME = (By.ID, "guest-user-lastname")
    EMAIL = (By.ID, "guest-user-email")
    PHONE_1 = (By.ID, "userPhone0")
    PHONE_2 = (By.ID, "userPhone1")
    PHONE_3 = (By.ID, "userPhone2")
    CONTINUE_BUTTON = (By.XPATH, "//button[contains(text(), 'Continue')]")


class AsGuest(BasePage):
    def fill_firstname(self, firsname_txt):
        firstname = self.find_element(AsGuestLocators.FIRST_NAME)
        firstname.click()
        firstname.send_keys(firsname_txt)
        return firstname

    def fill_lastname(self, lastname_txt):
        lastname = self.find_element(AsGuestLocators.LAST_NAME)
        lastname.click()
        lastname.send_keys(lastname_txt)
        return lastname

    def fill_email(self, email_txt):
        email = self.find_element(AsGuestLocators.EMAIL)
        email.click()
        email.send_keys(email_txt)
        return email

    def fill_phone(self, phone_txt):
        phone1 = self.find_element(AsGuestLocators.PHONE_1)
        phone2 = self.find_element(AsGuestLocators.PHONE_2)
        phone3 = self.find_element(AsGuestLocators.PHONE_3)
        phone1.send_keys(phone_txt[:3])
        phone2.send_keys(phone_txt[3:6])
        phone3.send_keys(phone_txt[6:])

    def click_continue(self):
        return self.find_element(AsGuestLocators.CONTINUE_BUTTON).click()

from pages.MainPage import BasePage
from selenium.webdriver.common.by import By


class CheckoutLocators:
    PICKUP_OPTION = (By.XPATH, "//button[text()='Pickup']")
    CHECKOUT_URL = 'https://order.dennys.com/checkout/method'
    CONTINUE_AS_GUEST_BUTTON = (By.XPATH, "//button[text()='Continue as guest']")
    IN_STORE_PICKUP_BUTTON = (By.XPATH, "//button[text()='In-store pickup']")
    PICKUP_LATER_OPTION = (By.XPATH, "//input[@id='pickuptime2']/parent::label")
    ORDER_DATE = (By.XPATH, "//select[@id='dropdown1']")
    ORDER_DATE_CHOOSE = (By.XPATH, "//select[@id='dropdown1']/option[2]")
    ORDER_TIME = (By.XPATH, "//select[@id='dropdown2']")
    ORDER_TIME_CHOOSE = (By.XPATH, "//select[@id='dropdown2']/option[text()='12:30 AM']")
    # ORDER_TIME_CHOOSE = (By.XPATH, "//select[@id='dropdown2']/option[text()='12:30 PM']")
    CONTINUE_TO_PAYMENT_BUTTON = (By.XPATH, "//button[contains(text(), 'Continue To Payment')]")
    MODAL_IS_OPEN = (By.XPATH, "//div[@class='modal is-open']")
    CLOSE_MODAL_BUTTON = (By.XPATH, "//div[@class='modal is-open']//button[contains(@class, 'modal-close')]")


class Checkout(BasePage):

    def open_checkout_page(self):
        return self.go_to_page(CheckoutLocators.CHECKOUT_URL)

    def contunue_as_guest(self):
        return self.find_element(CheckoutLocators.CONTINUE_AS_GUEST_BUTTON).click()

    def choose_pickup(self):
        pickup = self.find_element(CheckoutLocators.PICKUP_OPTION)
        pickup.click()
        return pickup

    def choose_in_store_pickup(self):
        self.find_element(CheckoutLocators.IN_STORE_PICKUP_BUTTON).click()

    def pickup_later(self):
        self.find_element(CheckoutLocators.PICKUP_LATER_OPTION).click()

    def choose_date(self):
        self.find_element(CheckoutLocators.ORDER_DATE).click()
        self.find_element(CheckoutLocators.ORDER_DATE_CHOOSE).click()

    def choose_time(self):
        self.find_element(CheckoutLocators.ORDER_TIME).click()
        self.find_element(CheckoutLocators.ORDER_TIME_CHOOSE).click()

    def continue_to_payment(self):
        payment = self.find_element(CheckoutLocators.CONTINUE_TO_PAYMENT_BUTTON)
        payment.click()
        return payment

    def close_modal_if_exist(self):
        try:
            self.check_element_clickable(CheckoutLocators.CLOSE_MODAL_BUTTON).click()
        except:
            print("modal popup hasn't appeared")

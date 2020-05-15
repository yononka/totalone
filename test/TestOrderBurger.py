from pages.LocationsPage import Locations
from pages.MenuPage import Menu
from pages.BurgersPage import Burgers
from pages.SlamburgerPage import Slamburger
from pages.CheckoutPage import Checkout
from pages.ContinueAsGuestPage import AsGuest


def test_order_slamburger(browser):
    location_page = Locations(browser)
    location_page.set_brooklyn_location()
    menu_page = Menu(browser)
    menu_page.open_burger_menu()
    burgers_page = Burgers(browser)
    burgers_page.select_burger('Slamburger')
    slamburger_page = Slamburger(browser)
    slamburger_page.choose_ingredient('Over Medium')
    slamburger_page.choose_ingredient('Fresh Avocado')
    slamburger_page.choose_ingredient('Red-Skinned Potatoes')
    slamburger_page.add_to_bag()
    checkout_page = Checkout(browser)
    checkout_page.open_checkout_page()
    checkout_page.contunue_as_guest()
    asguest_page = AsGuest(browser)
    asguest_page.fill_firstname("Paul")
    asguest_page.fill_lastname("Grey")
    asguest_page.fill_email("testmail@fake.fake")
    asguest_page.fill_phone("1234567890")
    asguest_page.click_continue()
    checkout_page.choose_pickup()
    checkout_page.choose_in_store_pickup()
    checkout_page.pickup_later()
    checkout_page.choose_date()
    checkout_page.choose_time()
    checkout_page.continue_to_payment()
    checkout_page.close_modal_if_exist()










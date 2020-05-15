import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.yield_fixture(scope='session')
def browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    driver.get('https://order.dennys.com/')
    yield driver
    driver.quit()

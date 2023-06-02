from selenium.webdriver import Chrome
from DZ20Loichenko.pages.dashboard import Dashboard
import pytest



@pytest.fixture(scope="session")
def driver():
    driver = Chrome('/DZ20Loichenko/drivers/chromedriver.exe')
    driver.get("https://allo.ua/ua/harkiv/")
    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.fixture
def dashboard(driver):
    yield Dashboard(driver)





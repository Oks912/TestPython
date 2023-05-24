from selenium.webdriver import Chrome
from DZ19Loichenko.pages.dashboard import Dashboard
import pytest


@pytest.fixture(scope="session")
def driver():
    driver = Chrome('D:\Python\L1Loichenko\DZ19Loichenko\drivers\chromedriver.exe')
    driver.get("https://allo.ua/")
    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.fixture
def dashboard(driver):
    yield Dashboard(driver)
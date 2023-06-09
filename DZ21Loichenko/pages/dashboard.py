from DZ21Loichenko.pages.base_page import BasePage
from selenium.webdriver.chrome.webdriver import WebDriver
from DZ21Loichenko.core.locator import Locator
from DZ21Loichenko.pages.category_page import CategoryPage
from DZ21Loichenko.pages.login_page import LoginPage
import time


class Dashboard(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        # self.__nav_bar_locator =('xpath', '//div[@class="ct-button"]' )
        self.__kat_locator = ('xpath', '//div[@class="ct-button"]')
        self.__profile_locator = ('xpath', '//button[@aria-label="Профіль"]')
        self.__Login_pas_locator = ('xpath', '//button[@type="submit" and @class="a-button a-button--block a-button--outline a-button--lg a-button--base"]')

    def click_on_kat(self):
        element = self._wait_until_element_appears(self.__kat_locator)
        time.sleep(5)
        element.click()
        return CategoryPage(self._driver)

    def login_form(self):
        profile = self._wait_until_element_appears(self.__profile_locator)
        profile.click()
        Login_pas = self._wait_until_element_appears(self.__Login_pas_locator)
        Login_pas.click()
        time.sleep(5)
        return LoginPage(self._driver)
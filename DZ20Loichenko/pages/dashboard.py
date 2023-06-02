from DZ20Loichenko.pages.base_page import BasePage
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver import Keys
from DZ20Loichenko.pages.Category_page import CategoryPage
import time


class Dashboard(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        # self.__nav_bar_locator =('xpath', '//div[@class="ct-button"]' )
        self.__kat_locator = ('xpath', '//div[@class="ct-button"]')
        # self.__search_locator = ('xpath', '//input[@id="search-form__input"]')
        # self.__add_to_ord_locator = ('xpath', '//button[@type="button" and @title="Купити"]')
        # self.__by_locator = ('xpath', '//button[@data-proceed-to-checkout and contains(text(), "Оформити замовлення")]')

    # def click_on_navbar(self):
    #     element = self._wait_until_element_appears(self.__nav_bar_locator)
    #     time.sleep(5)
    #     element.click()

    def click_on_kat(self):
        element = self._wait_until_element_appears(self.__kat_locator)
        time.sleep(5)
        element.click()
        return CategoryPage(self._driver)


    # def choose_subcategory(self, name):
    #     locator = ('xpath', f'//div[@class="sub-title" and contains(text(), "{name}")]')
    #     element = self._wait_until_element_appears(locator)
    #     time.sleep(5)
    #     element.click()

    # def search_text(self):
    #     search_input = self._wait_until_element_appears(self.__search_locator)
    #     time.sleep(5)
    #     search_input.send_keys('Apple iPhone 14 Pro Max 256GB Deep Purple (MQ9X3)')
    #     search_input.send_keys(Keys.ENTER)
    #
    # def add_to_order(self):
    #     add_to_ord = self._wait_until_element_appears(self.__add_to_ord_locator)
    #     add_to_ord.click()
    #
    # def by(self):
    #     by_somth = self._wait_until_element_appears(self.__by_locator)
    #     by_somth.click()



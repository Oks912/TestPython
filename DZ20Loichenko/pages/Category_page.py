from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from DZ20Loichenko.pages.base_page import BasePage
from DZ20Loichenko.pages.kitchen import KitchenPage


class CategoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__category_locator = ('xpath', '//a[@href="https://allo.ua/ua/harkiv/bytovaya-tehnika/"]')

    def byt_button(self):
        element = self._wait_until_element_appears(self.__category_locator)
        element.click()
        return KitchenPage(self._driver)
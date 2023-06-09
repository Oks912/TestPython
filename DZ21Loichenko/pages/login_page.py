import time
from selenium.webdriver.common.by import By
from DZ21Loichenko.pages.base_page import BasePage
from DZ21Loichenko.core.locator import Locator


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def fill_row(self, login_fill: str, password_fill: str):
        login_locator = (By.XPATH, '//input[@placeholder="Введіть телефон або e-mail"]')
        login = self._wait_until_element_appears(login_locator)
        login.send_keys(login_fill)
        time.sleep(3)
        password_locator = (By.XPATH, '//input[@placeholder="Введіть пароль"]')
        password = self._wait_until_element_appears(password_locator)
        password.send_keys(password_fill)
        time.sleep(3)
        self._click('xpath', '//button[@type="submit"]')

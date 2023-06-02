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






# Ініціалізуємо веб-драйвер
driver = webdriver.Chrome()

# Створюємо сторінку пошуку і передаємо їй драйвер
search_page = SearchPage(driver)

# Використовуємо локатори і методи сторінки
search_page.search("HP laptop")

# Отримуємо результати пошуку
results = search_page.results
for result in results:
    print(result.text)
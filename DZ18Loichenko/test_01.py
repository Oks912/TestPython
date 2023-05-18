from selenium.webdriver import Chrome, Keys
import time
#from selenium.webdriver.common.action_chains import ActionChains


def test_01():
    driver = Chrome('D:\Python\L1Loichenko\DZ18Loichenko\drivers\chromedriver.exe')
    driver.get('https://www.sportchek.ca/')
    driver.maximize_window()
    search_input_field = '//input[@class="header-search__input"]'
    search_input_field = driver.find_element(by='xpath', value=search_input_field)
    search_input_field.send_keys('Nike')
    time.sleep(2)
    search_input_field.send_keys(Keys.ENTER)
    first_non_ad_link_locator = '//*[@id="main-content"]/div/div[3]/div[2]/div/div/div/a/span'
    time.sleep(2)
    first_non_ad_link = driver.find_element(by='xpath', value=first_non_ad_link_locator)
    first_non_ad_link.click()
    time.sleep(3)
    search_checkbox = '//span[contains(@class, "facets-side__checkbox-text") and contains(text(), "Women")]'
    search_checkbox_element = driver.find_element(by='xpath', value=search_checkbox)
    search_checkbox_element.click()
    time.sleep(5)
    # search_element_lowprice_locator = '//div[contains(@style, "margin-left: 0px;") and text()="$9"]'
    # search_element_lowprice_element = driver.find_element(by='xpath', value=search_element_lowprice_locator)
    # actions = ActionChains(driver)
    # actions.move_to_element(search_element_lowprice_element).click().send_keys(Keys.HOME + '100').perform()
    search_page = '//a[@class="pagination__page-link" and contains(text(), "10")]'
    search_page_element = driver.find_element(by='xpath', value=search_page)
    search_page_element.click()

    time.sleep(10)
    driver.quit()


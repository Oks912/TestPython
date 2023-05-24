import time


def test_check_choose_category(dashboard):
    dashboard.click_on_navbar()
    time.sleep(3)
    dashboard.click_on_kat()
    time.sleep(5)
    dashboard.choose_subcategory('Apple iPhone 14 Pro Max')
    time.sleep(5)
    dashboard.search_text()
    time.sleep(5)
    dashboard.add_to_order()
    time.sleep(5)
    dashboard.by()
    time.sleep(5)
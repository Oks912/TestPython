import time


def test_check_choose_category(dashboard):

    pick_subcategory = dashboard.click_on_kat()
    time.sleep(3)
    buildin_subcategory = pick_subcategory.byt_button()
    time.sleep(3)




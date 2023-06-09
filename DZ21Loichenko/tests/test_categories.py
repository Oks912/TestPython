import time


def test_check_choose_category(dashboard):

    pick_subcategory = dashboard.click_on_kat()
    time.sleep(3)
    buildin_subcategory = pick_subcategory.byt_button()
    time.sleep(4)


def test_check_login(dashboard):
    click_profile = dashboard.login_form()
    time.sleep(3)
    login_form = click_profile.fill_row('test@gmail.com', '123445hjgj')
    time.sleep(4)
    login = dashboard.login_form()
    time.sleep(3)

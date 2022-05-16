import time
link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_add_to_basket_btn_available(browser):
    browser.get(link)
    browser.find_element_by_class_name('btn-add-to-basket')
    time.sleep(30)


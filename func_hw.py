# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__

def func_name(func, *args):
    print(f'Название функции: {func.__name__}')
    print('Аргумент(ы) функции:')
    for arg in args:
        print(arg)
    print('')


def open_browser(browser_name):
    func_name(open_browser, browser_name)
    pass


def go_to_companyname_homepage(page_url):
    func_name(go_to_companyname_homepage, page_url)
    pass


def find_registration_button_on_login_page(page_url, button_text):
    func_name(find_registration_button_on_login_page, page_url, button_text)
    pass


open_browser('Chrome')
go_to_companyname_homepage('google.com')
find_registration_button_on_login_page('google.com/signup', 'Sign up')
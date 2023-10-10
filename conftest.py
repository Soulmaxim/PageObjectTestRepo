import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.safari.options import Options as SafariOptions


def pytest_addoption(parser):
    parser.addoption('--bro_name', action='store', default='chrome', help='Choose browser: chrome or safari')
    parser.addoption('--language', action='store', default='en', help='Choose language: ru or en')

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("user_language")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        chrome_options = ChromeOptions()
        chrome_options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=chrome_options)
    elif browser_name == "safari":
        print("\nstart safari browser for test..")
        safari_options = SafariOptions()
        # кажется никто не знает как это в Safari сделать
        browser = webdriver.Safari(options=safari_options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or safari")
    browser.implicitly_wait(5)

    yield browser
    print("\nquit browser..")
    browser.quit()

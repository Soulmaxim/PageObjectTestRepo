import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome', help='Choose browser: chrome, firefox or safari')
    parser.addoption('--language', action='store', default='en', help='Choose language: ru or en')

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser")
    user_language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        chrome_options = ChromeOptions()
        chrome_options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=chrome_options)
    elif browser_name == "safari":
        print("\nstart safari browser for test..")
        safari_options = SafariOptions()
        # кажется никто не знает как в Safari установить accept_languages
        browser = webdriver.Safari(options=safari_options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        firefox_options = FirefoxOptions()
        firefox_options.set_preference('intl.accept_languages', user_language)
        browser = webdriver.Firefox(options=firefox_options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or safari")

    yield browser
    print("\nquit browser..")
    browser.quit()

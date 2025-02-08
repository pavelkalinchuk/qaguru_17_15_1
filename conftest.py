import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selene import browser

base_url = 'https://github.com'

# Фикстура для десктопной версии
@pytest.fixture(scope='function')
def desktop_browser():
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'normal'
    driver_options.add_argument('--window-size=1920,1080')
    browser.config.base_url = base_url
    yield
    browser.quit()


# Фикстура для мобильной версии
@pytest.fixture(scope='function')
def mobile_browser():
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'normal'
    driver_options.add_argument('--window-size=375,677')
    browser.config.base_url = base_url
    yield
    browser.quit()


# Фикстура для инициализации браузера с параметризацией размера окна
@pytest.fixture(scope='function')
def setup_browser(request):
    width = request.param['width']
    height = request.param['height']
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    browser.config.driver = driver
    browser.config.driver.set_window_size(width, height)
    browser.config.base_url = base_url
    yield
    browser.quit()


# Фикстура для инициализации браузера с определением типа устройства по размеру окна
@pytest.fixture(scope='function', params=[(1920, 1080), (1366, 768), (1440, 900), (390, 844), (414, 896), (375, 667)])
def setup_browser_with_check_device_type(request):
    width, height = request.param
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    browser.config.driver = driver
    browser.config.driver.set_window_size(width, height)
    browser.config.base_url = base_url
    device_type = "desktop" if width > 1000 else "mobile"
    yield device_type
    browser.quit()


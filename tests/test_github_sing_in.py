import pytest
from selene import browser, be, have, by


def test_github_sign_in_desktop(desktop_browser):
    browser.open('/')
    sing_in_button = browser.element("a.HeaderMenu-link--sign-in")
    sing_in_button.should(be.visible)
    sing_in_button.click()
    browser.should(have.url_containing("login"))


def test_github_sing_in_mobile(mobile_browser):
    browser.open('/')
    sign_in_button = browser.element(by.text("Sign up"))
    sign_in_button.should(be.visible)
    sign_in_button.click()


@pytest.mark.parametrize("setup_browser, width, height", [
    ({"width": 390, "height": 844}, 390, 844),
    ({"width": 414, "height": 896}, 414, 896),
    ({"width": 375, "height": 667}, 375, 667)
], indirect=["setup_browser"])
def test_mobile_parametrize(setup_browser, width, height):
    browser.open('/')
    browser.element("[class='Button-content']").click()
    sign_in_button = browser.element(by.text("Sign up"))
    sign_in_button.click()


@pytest.mark.parametrize("setup_browser, width, height", [
    ({"width": 1920, "height": 1080}, 1920, 1080),
    ({"width": 1366, "height": 768}, 1366, 768),
    ({"width": 1440, "height": 900}, 1440, 900)
], indirect=["setup_browser"])
def test_desktop_parametrize(setup_browser, width, height):
    browser.open('/')
    sign_in_button = browser.element(by.text("Sign up"))
    sign_in_button.click()


def test_skip_if_mobile(setup_browser_with_check_device_type):
    device_type = setup_browser_with_check_device_type

    if device_type == "mobile":
        pytest.skip("Устройство определено как мобильное и будет пропущено")
    else:
        browser.open('/')
        sign_in_button = browser.element(by.text("Sign up"))
        sign_in_button.click()


def test_skip_if_desktop(setup_browser_with_check_device_type):
    device_type = setup_browser_with_check_device_type

    if device_type == "desktop":
        pytest.skip("Устройство определено как ПК и будет пропущено")
    else:
        browser.open('/')
        browser.element("[class='Button-content']").click()
        sign_in_button = browser.element(by.text("Sign up"))
        sign_in_button.click()

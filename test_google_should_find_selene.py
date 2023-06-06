from selene.support.shared import browser
from selene import be, have
import pytest

@pytest.fixture
def set_browser():
    browser.config.window_height = 1080
    browser.config.window_width = 1920

def test_positive_google_search(set_browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_negative_google_search(set_browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('1GKsPRYgZTT3BKNVdj7RuNiWCtQPXhq8UpVPkjJ26rUI').press_enter()
    browser.element('[id="res"]').should(have.text('По запросу 1GKsPRYgZTT3BKNVdj7RuNiWCtQPXhq8UpVPkjJ26rUI ничего не найдено.'))

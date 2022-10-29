from selene import be, by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_github():
    browser.open('https://github.com/')

    s('.header-search-input').click()
    s('.header-search-input').type('eroshenkoam/allure-example')
    s('.header-search-input').submit()

    s(by.partial_link_text('allure-example')).click()

    s('#issues-tab').click()

    s('#issue_81').should(be.visible)



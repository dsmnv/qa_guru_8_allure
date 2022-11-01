import allure
from selene import be, by
from selene.support.shared import browser, config
from selene.support.shared.jquery_style import s


def test_github():
    with allure.step('Открываем главную страницу Github'):
        browser.open('https://github.com/')

    with allure.step('Ищем репозиторий'):
        s('.header-search-input').click()
        s('.header-search-input').type('eroshenkoam/allure-example')
        s('.header-search-input').submit()

    with allure.step('Переходим в нужный репозиторий'):
        s(by.partial_link_text('allure-example')).click()

    with allure.step('Переходим на табу issue'):
        s('#issues-tab').click()

    with allure.step('Проверяем наличие issue_81'):
        s('#issue_81').should(be.visible)

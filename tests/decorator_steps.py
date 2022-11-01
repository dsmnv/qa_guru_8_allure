from selene import by, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
import allure


def test_decorator_steps():
    open_main_page()
    search_for_repository('eroshenkoam/allure-example')
    go_to_repository('allure-example')
    open_issue_tab()
    issue_is_visible('81')


@allure.step('Открываем главную страницу Github')
def open_main_page():
    browser.open('https://github.com/')


@allure.step('Ищем репозиторий {repo}')
def search_for_repository(repo):
    s('.header-search-input').click()
    s('.header-search-input').type(repo)
    s('.header-search-input').submit()


@allure.step('Переходим в нужный репозиторий {repo}')
def go_to_repository(repo):
    s(by.partial_link_text(repo)).click()


@allure.step('Открываем табу issue')
def open_issue_tab():
    s('#issues-tab').click()


@allure.step('Проверяем наличие issue_81')
def issue_is_visible(number):
    s('#issue_'+number).should(be.visible)

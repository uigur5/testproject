from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium import webdriver


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    MESSAGE_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "div.alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_PRICE_OF_BASKET = (By.CSS_SELECTOR,".alert-info .alertinner strong")
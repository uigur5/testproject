from .base_page import BasePage
from .locators import BasketPageLocators, BasePageLocators


class BasketPage(BasePage):
    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Form with items is presented, but shouldn't be"

    def should_be_text_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.NO_ITEMS_TEXT), \
            "There is no text about empty basket"

    def go_to_basket_page(self):
        view_basket_button = self.browser.find_element(*BasePageLocators.BASKET_BUTTON)
        view_basket_button.click()
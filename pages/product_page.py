from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def guest_can_add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()
        # self.solve_quiz_and_get_code()
        assert True

    def should_be_message_about_adding(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_IN_BASKET).text
        assert product_name == message, "No product name in the message"

    def should_be_message_about_basket(self):
        message_basket_total = self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE_OF_BASKET).text
        product_price = self.browser.find_element(*ProductPageLocators.PRICE).text
        assert product_price == message_basket_total, "No product price in the message"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_PRODUCT_IN_BASKET), \
            "Success message is presented, but should not be"

    def should_disapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_PRODUCT_IN_BASKET), \
            "Success message should be disappeared"
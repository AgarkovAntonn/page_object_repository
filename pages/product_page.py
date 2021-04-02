from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
#import time

class ProductPage(BasePage):
    """
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
    """
    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BUTTON), "There is no Add_To_Cart button on page"
        
    def add_product_to_cart(self):
        promo = False
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        add_to_cart_button.click()
        if self.promo:
            self.solve_quiz_and_get_code()
        #time.sleep(3)
        product_name_in_cart = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_CART).text
        product_price_in_cart = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_CART).text
        # ~ print('Product name - ', product_name)
        # ~ print('Product price - ', product_price)
        # ~ print('Product name in cart - ', product_name_in_cart)
        # ~ print('Product price in cart - ', product_price_in_cart)
        
        assert (product_name == product_name_in_cart), "Wrong product's name in cart"
        assert (product_price == product_price_in_cart), "Wrong product's price in cart"
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
        
    def should_disappear_success_mesage(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappeared, but should be"
        
        

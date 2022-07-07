from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class AddToCart(BasePage):

    """Locators for AddToCart page"""
    button_add_to_cart_id = {"by": By.ID, "value": "add-to-cart-sauce-labs-bike-light"}
    link_cart_icon_xpath = {"by": By.XPATH, "value": "//*[@id='shopping_cart_container']/a"}
    text_item_to_add_xpath = {"by": By.XPATH, "value": "//*[@id='item_0_title_link']/div"}
    text_cart_item_xpath = {"by": By.XPATH, "value": "//*[@id='item_0_title_link']/div"}
    text_item_price_xpath = {"by": By.XPATH, "value": "//div[@class='inventory_item_price']"}

    def __init__(self, driver):
        """Constructor of AddToCart Class"""
        super().__init__(driver)

    def add_to_cart(self):
        """A function that adds an item to the cart"""
        self._click(self.button_add_to_cart_id)

    def go_to_cart(self):
        """A function that opens cart page"""
        self._click(self.link_cart_icon_xpath)

    def get_item_to_add_name(self):
        """A function that returns the name of the item to be added in the cart """
        self._get_element_text(self.text_cart_item_xpath)

    def is_item_price_displayed(self):
        """A function that returns the price of the item to be added in the cart """
        ele = self._is_displayed(self.text_item_price_xpath)
        return bool(ele)

    def get_cart_item_name(self):
        """A function that returns the name of the item present in the cart"""
        self._get_element_text(self.text_cart_item_xpath)


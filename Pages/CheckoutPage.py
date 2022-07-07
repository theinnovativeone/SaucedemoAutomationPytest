from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class Checkout(BasePage):

    """Locators for PlaceOrderPage"""
    button_checkout_id = {"by": By.ID, "value": "checkout"}
    textbox_first_name_id = {"by": By.ID, "value": "first-name"}
    textbox_last_name_id = {"by": By.ID, "value": "last-name"}
    textbox_postal_code_id = {"by": By.ID, "value": "postal-code"}
    button_continue_id = {"by": By.ID, "value": "continue"}
    text_final_item_name_id = {"by": By.ID, "value": "//*[@id='item_0_title_link']/div"}
    text_final_item_qty_id = {"by": By.ID, "value": "//*[@id='item_0_title_link']/div"}
    button_finish_id = {"by": By.ID, "value": "finish"}
    text_order_message_xpath = {"by": By.XPATH, "value": "//*[@id='checkout_complete_container']/h2"}
    text_item_quantity_xpath = {"by": By.XPATH, "value": "//div[@class ='cart_quantity']"}
    text_total_payment_xpath = {"by": By.XPATH, "value": "//div[@class ='summary_total_label']"}

    def __init__(self, driver):
        """Constructor of PlaceOrder Class"""
        super().__init__(driver)

    def do_checkout(self):
        """A function that clicks on Checkout button"""
        self._click(self.button_checkout_id)

    def enter_details(self, firstname, lastname, postalcode):
        """A function that enters firstname, lastname and zip/postal code and clicks on continue button"""
        self._type(self.textbox_first_name_id, firstname)
        self._type(self.textbox_last_name_id, lastname)
        self._type(self.textbox_postal_code_id, postalcode)
        self._click(self.button_continue_id)

    def get_item_name_after_checkout(self):
        """A function that returns the name of the item in the cart after checkout"""
        ele = self._get_element_text(self.text_final_item_name_id)
        return ele

    def get_item_quantity_after_checkout(self):
        """A function that returns the quantity of the item in the cart after checkout"""
        ele = self._get_element_text(self.text_final_item_qty_id)
        return ele

    def is_item_quantity_displayed(self):
        """A function that returns true if item quantity is displayed for each item in the cart"""
        ele = self._is_displayed(self.text_item_quantity_xpath)
        return bool(ele)

    def is_total_payment_displayed(self):
        """A function that returns true if total payment is shown in checkout page"""
        ele = self._is_displayed(self.text_total_payment_xpath)
        return bool(ele)

    def thankyou_message_exists(self):
        """A function that returns true if a message is displayed after placing order"""
        ele = self._get_element_text(self.text_order_message_xpath)
        return bool(ele)

    def get_thankyou_message(self):
        """A function that returns message is displayed after placing order"""
        ele = self._get_element_text(self.text_order_message_xpath)
        return ele

    def place_order(self, firstname, lastname, postalcode):
        """A function that inputs firstname, lastname and places order"""
        self.do_checkout()
        self.enter_details(firstname, lastname, postalcode)
        self._click(self.button_finish_id)



        """self._type(self.textbox_first_name_id, firstname)
        self._type(self.textbox_last_name_id, lastname)
        self._type(self.textbox_postal_code_id, postalcode)
        self._click(self.button_continue_id)"""

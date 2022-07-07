import pytest
from Pages.LoginPage import Login
from Pages.AddToCartPage import AddToCart
from Pages.CheckoutPage import Checkout
from Config.config import TestData


class Test_Place_Order:
    """Tests for CheckoutPage"""

    def test_item_quantity_present(self, init_driver):
        """Test that checks if item quantity is present on the checkout page"""
        self.driver = init_driver
        self.driver.get(TestData.baseURL)
        self.driver.maximize_window()
        """Login in sauce demo account"""
        self.lp = Login(self.driver)
        self.lp.login(TestData.username, TestData.password)
        """Add 1 item in the cart"""
        self.ac = AddToCart(self.driver)
        self.ac.add_to_cart()
        """Go to cart for placing order"""
        self.ac.go_to_cart()
        self.checkout = Checkout(self.driver)
        self.checkout.do_checkout()
        self.checkout.enter_details(TestData.firstname, TestData.lastname, TestData.postalcode)
        item_quantity_exists = self.checkout.is_item_quantity_displayed()
        """Checks whether item quantity is present on the checkout page"""
        if item_quantity_exists:
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_item_quantity_present.png")
            self.driver.close()
            assert False

    def test_total_payment_present(self, init_driver):
        """Test that checks if total payment is present on the checkout page"""
        self.driver = init_driver
        self.driver.get(TestData.baseURL)
        self.driver.maximize_window()
        """Login in sauce demo account"""
        self.lp = Login(self.driver)
        self.lp.login(TestData.username, TestData.password)
        """Add 1 item in the cart"""
        self.ac = AddToCart(self.driver)
        self.ac.add_to_cart()
        """Go to cart for placing order"""
        self.ac.go_to_cart()
        self.checkout = Checkout(self.driver)
        self.checkout.do_checkout()
        self.checkout.enter_details(TestData.firstname, TestData.lastname, TestData.postalcode)
        total_payment_exists = self.checkout.is_total_payment_displayed()
        """Check whether total payment is present on the checkout page"""
        if total_payment_exists:
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_total_payment_present.png")
            self.driver.close()
            assert False

    def test_thankyou_message_shown(self, init_driver):
        """Test that checks if a message is shown after placing order"""
        self.driver = init_driver
        self.driver.get(TestData.baseURL)
        self.driver.maximize_window()
        """Login in sauce demo account"""
        self.lp = Login(self.driver)
        self.lp.login(TestData.username, TestData.password)
        """Add 1 item in the cart"""
        self.ac = AddToCart(self.driver)
        self.ac.add_to_cart()
        """Go to cart for placing order"""
        self.ac.go_to_cart()
        self.checkout = Checkout(self.driver)
        self.checkout.place_order(TestData.firstname, TestData.lastname, TestData.postalcode)
        order_message_exists = self.checkout.thankyou_message_exists()
        order_message = self.checkout.get_thankyou_message()
        self.driver.implicitly_wait(30)
        """Check whether (THANK YOU FOR YOUR ORDER) is shown at the end"""
        if order_message_exists != 0 and order_message == "THANK YOU FOR YOUR ORDER":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_thankyou_message_shown.png")
            self.driver.close()
            assert False

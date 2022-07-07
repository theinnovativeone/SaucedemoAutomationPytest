import pytest
from Pages.LoginPage import Login
from Pages.AddToCartPage import AddToCart
from Config.config import TestData


class Test_Add_To_Cart:
    """Tests for AddToCartPage"""

    def test_item_added_to_cart(self, init_driver):
        """Test to check if the same item is added to the cart"""
        self.driver = init_driver
        self.driver.get(TestData.baseURL)
        self.driver.maximize_window()
        """Login in sauce demo account"""
        self.lp = Login(self.driver)
        self.lp.login(TestData.username, TestData.password)
        self.driver.implicitly_wait(10)
        """Add 1 item in the cart"""
        self.ac = AddToCart(self.driver)
        item_to_add = self.ac.get_item_to_add_name()
        self.ac.add_to_cart()
        self.driver.implicitly_wait(10)
        """Go to cart"""
        self.ac.go_to_cart()
        item_added = self.ac.get_cart_item_name()
        """Check whether the same item is added in the cart"""
        if item_to_add == item_added:
            print("The same item is successfully added in the cart")
            self.driver.close()
            assert True
        else:
            print("A different item is added in the cart")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_item_added_to_cart.png")
            self.driver.close()
            assert False

    def test_item_price_displayed(self, init_driver):
        """Test to check if the same item is added to the cart"""
        self.driver = init_driver
        self.driver.get(TestData.baseURL)
        self.driver.maximize_window()
        """Login in sauce demo account"""
        self.lp = Login(self.driver)
        self.lp.login(TestData.username, TestData.password)
        self.driver.implicitly_wait(10)
        """Add 1 item in the cart"""
        self.ac = AddToCart(self.driver)
        self.ac.add_to_cart()
        self.driver.implicitly_wait(10)
        """Go to cart"""
        self.ac.go_to_cart()
        item_price_exists = self.ac.is_item_price_displayed()
        """Check whether item price is present on the cart page"""
        if item_price_exists:
            print("The item price is present on the cart page")
            self.driver.close()
            assert True
        else:
            print("The item price is present on the cart page")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_item_price_displayed.png")
            self.driver.close()
            assert False


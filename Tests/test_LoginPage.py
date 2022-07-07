import pytest
from Pages.LoginPage import Login
from Config.config import TestData


class Test_Login:
    """Tests for testing Login Page"""
    def test_login_valid_credentials(self, init_driver):
        """Test login with valid credentials"""
        self.driver = init_driver
        self.driver.get(TestData.baseURL)
        self.driver.set_page_load_timeout(2)
        self.driver.maximize_window()
        self.lp = Login(self.driver)
        self.lp.login(TestData.username, TestData.password)
        logout = self.lp.is_logout_present()
        """Checks if logout option is available on the page to validate successful login"""
        if logout:
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login_valid_credentials.png")
            self.driver.close()
            assert False

    def test_login_invalid_credentials(self, init_driver):
        """Test login with invalid credentials"""
        self.driver = init_driver
        self.driver.get(TestData.baseURL)
        self.driver.maximize_window()
        self.lp = Login(self.driver)
        self.lp.login(TestData.invalid_username, TestData.invalid_password)
        error_message_text = self.lp.get_error_message()
        """Checks if an error message is displayed on attempting login with invalid credentials"""
        if error_message_text == "Epic sadface: Username and password do not match any user in this service":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login_invalid_credentials.png")
            self.driver.close()
            assert False

    def test_login_invalid_username(self, init_driver):
        """Test login with invalid username and valid password"""
        self.driver = init_driver
        self.driver.get(TestData.baseURL)
        self.driver.maximize_window()
        self.lp = Login(self.driver)
        self.lp.login(TestData.invalid_username, TestData.password)
        error_message_text = self.lp.get_error_message()
        """Checks if an error message is displayed on attempting login with invalid username"""
        if error_message_text == "Epic sadface: Username and password do not match any user in this service":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login_invalid_username.png")
            self.driver.close()
            assert False

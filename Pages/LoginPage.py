from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.BasePage import BasePage


class Login(BasePage):

    """"Locators for Login Page"""
    textbox_username_id = {"by": By.ID, "value": "user-name"}
    textbox_password_id = {"by": By.ID, "value": "password"}
    button_login_id = {"by": By.ID, "value": "login-button"}
    button_error_msg_xpath = {"by": By.XPATH, "value": "//*[@id='login_button_container']/div/form/div[3]/h3"}
    button_menu_id = {"by": By.ID, "value": "react-burger-menu-btn"}
    text_logout_id = {"by": By.ID, "value": "logout_sidebar_link"}

    def __init__(self, driver):
        """Constructor for Login class"""
        super().__init__(driver)

    """Methods for login class"""
    def login(self, username, password):
        """A function that performs login"""
        self._type(self.textbox_username_id, username)
        self._type(self.textbox_password_id, password)
        self._click(self.button_login_id)

    def get_error_message(self):
        """A function that returns the error message on incorrect username and password """
        ele = self._get_element_text(self.button_error_msg_xpath)
        return ele

    def is_logout_present(self):
        """A function that true if logout option is present on the main page after successful login"""
        self._click(self.button_menu_id)
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link")))
        except TimeoutException:
            return False
        return True



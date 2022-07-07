class BasePage:
    """A class that includes all the base methods"""

    def __init__(self, driver):
        """Constructor of BasePage Class"""
        self.driver = driver

    def _find(self, locator):
        """A function that locates on the specified web element in the parameter"""
        return self.driver.find_element(locator["by"], locator["value"])

    def _click(self, locator):
        """A function that clicks on the specified web element in the parameter"""
        self._find(locator).click()

    def _type(self, locator, input_text):
        """A function that sends text input to the specified web element in the parameter"""
        self._find(locator).send_keys(input_text)

    def _get_element_text(self, locator):
        """A function that gets text of the specified web element in the parameter"""
        element = self._find(locator)
        return element.text

    def _is_displayed(self, locator):
        """A function that returns true when the specified web element is present on the page, otherwise false"""
        return self._find(locator).is_displayed()


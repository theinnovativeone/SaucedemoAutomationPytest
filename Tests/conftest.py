from selenium import webdriver
import pytest

@pytest.fixture()
def init_driver():
    driver = webdriver.Chrome("C:/Users/snehagupta01/Downloads/chromedriver_win32 (2)/chromedriver.exe")
    return driver

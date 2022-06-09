from base.page_base import BaseClass
from selenium.webdriver.common.by import By
from base import data


class PanelLoginPage(BaseClass):
    """
    Login with Insider account in this class

    """
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)

    def login(self):
        """
        User logs in with an existing account

        """
        self.send_keys(self.EMAIL_INPUT, data.email)
        self.send_keys(self.PASSWORD_INPUT, data.password)
        self.presence_for_element(self.LOGIN_BUTTON).click()

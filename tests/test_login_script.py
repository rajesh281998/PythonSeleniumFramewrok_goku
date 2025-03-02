import os.path

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from base.webdriverfactory import WebDriverFactory
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utilities.excel_utils import ExcelUtils


@pytest.mark.usefixtures("setup")
class TestLoginScenario():

    file_path = os.path.join(os.path.dirname(__file__),"..","testdata","testdata.xlsx")

    @pytest.mark.parametrize("email,password",ExcelUtils.get_excel_data(file_path,"Sheet1"))
    def test_login(self,email,password):

        login=LoginPage(self.driver)

        login.login_to_application(email,password)

        home = HomePage(self.driver)

        try:
            welcome_message = home.get_welcome_text()
            assert "Welcome" in welcome_message, "Login failed for valid credentials"
            home.logout_from_application()

        except Exception:
            # If login fails, check the error message
            try:
                error_message = login.login_error_message_for_invalid_mail_and_password_text()

                # Handle different failure scenarios
                if not email and password:
                    assert "Email is required" in error_message, "Missing email error not displayed"
                elif email and not password:
                    assert "Password is required" in error_message, "Missing password error not displayed"
                elif email and password:
                    assert "Email and Password Doesn't match" in error_message, "Invalid login error not displayed"
                else:
                    assert "Email and Password are required" in error_message, "Generic missing credentials error not displayed"
            except Exception:
                assert False, "Neither welcome message nor error message found - Possible UI issue"






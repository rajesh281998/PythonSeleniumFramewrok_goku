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

        welcome_message = home.get_welcome_text()

        assert "Welcome" in welcome_message
        home.logout_from_application()


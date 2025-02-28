from selenium.webdriver.common.by import By

from base.selenium_driver import SeleniumDriver


class HomePage(SeleniumDriver):

    welcome_message_xpath = "//h4[@class='welcomeMessage']"
    side_menu_xpath = "//img[@alt='menu']"
    signout_button_xpath = "//button[normalize-space()='Sign out']"

    def __init__(self,driver):
        self.driver = driver

    def get_welcome_text(self):
        return self.get_element(self.welcome_message_xpath,"xpath").text

    def logout_from_application(self):
        self.click_element(self.side_menu_xpath,"xpath")
        self.click_element(self.signout_button_xpath,"xpath")




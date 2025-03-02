from selenium.webdriver.common.by import By

from base.selenium_driver import SeleniumDriver


class LoginPage(SeleniumDriver):

    email_field_XPATH = "//input[@id='email1']"
    password_field_XPATH = "//input[@id='password1']"
    login_button_XPATH = "//button[normalize-space()='Sign in']"
    login_error_message_xpath = "//h2[@class='errorMessage']"

    def __init__(self,driver):
        super().__init__(driver)


    def login_to_application(self,email,password):
        self.type_element(email,self.email_field_XPATH,"xpath")
        self.type_element(password,self.password_field_XPATH,"xpath")
        self.click_element(self.login_button_XPATH,"xpath")

    def login_error_message_for_invalid_mail_and_password_text(self):
        return self.get_element(self.login_error_message_xpath,"xpath").text






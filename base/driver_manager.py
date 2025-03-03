from selenium import webdriver
class DriverManager:
    _driver = None
    @classmethod
    def get_driver (cls):
        if cls.driver is None:
            cls._driver = webdriver.Chrome()
        return cls._driver

    @classmethod
    def quit_driver(cls):
        if cls._driver:
            cls. _driver.quit()
            cls. driver = None
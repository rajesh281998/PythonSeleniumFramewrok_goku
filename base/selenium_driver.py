import logging
import os.path
from datetime import datetime
from traceback import print_stack

from selenium.common import NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException, \
    ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import utilities.custom_logger as cl


class SeleniumDriver():

    log = cl.customlogger(logging.DEBUG)

    def __init__(self,driver):
        self.driver = driver


        #screenshot,clickelement,typeElement,mouseHover,scrolls,dragDrop,WaitsCondition

    def take_screenshot(self):
        try:
            screenshot_dir=os.path.join(os.getcwd(), "screenshots")

            timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

            file_name = f"Automation_{timestamp}.png"

            filepath = os.path.join(screenshot_dir,file_name)

            self.driver.save_screenshot(filepath)

            return filepath
        except Exception as e:
            self.log.warning(f"could not cature the screenshot {e}")

            return None

    def get_by_type(self,locatorType):
        locatorType=locatorType.lower()

        if locatorType =="id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "link":
            return By.LINK_TEXT
        elif locatorType == "partial_link":
            return By.PARTIAL_LINK_TEXT
        elif locatorType == "tag":
            return By.TAG_NAME

        else:

            self.log.warning("Locator type " +locatorType+ " not supported")

    def get_element(self,locator,locatorType="id"):
        element=None
        try:
            locatorType = locatorType.lower()
            bytype = self.get_by_type(locatorType)
            element = self.driver.find_element(bytype,locator)
            self.log.info("Element Found Using "+locatorType+" with value "+locator)
        except:
            self.log.warning("Element Not found Using "+locatorType+" with value "+locator)
        return element

    def click_element(self,locator,locatorType="id"):
        try:
            element = self.get_element(locator,locatorType)
            element.click()
            self.log.info("Clicked on element using this locator "+locator)
        except:
            self.log.warning("Couldn't Clicked on element using this locator "+locator)
            print_stack()

    def type_element(self,data,locator,locatorType):
        try:
            element = self.get_element(locator,locatorType)
            element.send_keys(data)
            self.log.info("Typed " +data+  "on element using this locator "+locator)
        except:
            self.log.warning("Couldn't Typed " +data+ " on element using this locator "+locator)
            print_stack()


    def waitforelement(self,locator,locatorType="id",timeout=30,pollfrequency=1):
        element=None

        try:
            locatorType=locatorType.lower()
            bytype=self.get_by_type(locatorType)
            wait=WebDriverWait(self.driver,timeout,poll_frequency=1,ignored_exceptions=[NoSuchElementException,StaleElementReferenceException,ElementNotInteractableException,ElementNotVisibleException])
            element = wait.until(EC.element_to_be_clickable((bytype,locator)))
            self.log.info("Element Found With Explicit Conditions")
        except:
            self.log.warning("Element Not Found within time interval")

        return element





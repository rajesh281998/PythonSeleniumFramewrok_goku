import logging

import allure
import pytest

from base.selenium_driver import SeleniumDriver
from base.driver_manager import DriverManager
from base.webdriverfactory import WebDriverFactory

import utilities.custom_logger as cl

log = cl.customlogger(logging.DEBUG)
@pytest.fixture(scope="session",autouse=True)
def setup():
    driver = DriverManager.get_driver()
    yield driver

    DriverManager.quit_driver()
# def setup(request):
#     wdf = WebDriverFactory("chrome")
#     driver = wdf.getWebDriverInstance()
#
#     if request.cls is not None:
#         request.cls.driver = driver
#
#     log.info("Application is up and running")
#
#     yield driver
#
#     driver.quit()
#     log.info("Closing the browser")


@pytest.hookimpl(tryfirst=True,hookwrapper=True)
def pytest_runtest_makereport(item,call):
    log.info("Executing PyTest Hooks")


    outcome = yield
    report = outcome.get_result()
    log.info("Captured Results")

    if report.when =="call" and (report.failed or report.outcome == "broken"):
        log.info("Test Failed Attaching Screenshot to report")

        if hasattr(item.instance,"driver"):
            driver = item.instance.driver
            selenium_driver = SeleniumDriver(driver)
            screenshot_path = selenium_driver.take_screenshot()
            log.info(screenshot_path)
            if screenshot_path:
                with allure.step("Attach Screenshot On Failure/Broken"):
                    allure.attach.file(screenshot_path,name = "Failure Screenshot",attachment_type=allure.attachment_type.PNG)

                with allure.step("Exception Details"):
                    allure.attach(str(call.excinfo),name =  "Exception Details",attachment_type= allure.attachment_type.TEXT)

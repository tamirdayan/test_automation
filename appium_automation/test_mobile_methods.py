import time

import pytest
import unittest
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

EXPECTED_LIST_SIZE = 11


class Test_Mobile_Methods():
    reportDirectory = 'reports'
    reportFormat = 'xml'
    dc = {}
    testName = 'Untitled'
    driver = None

    def setup_class(self):
        self.dc['reportDirectory'] = self.reportDirectory
        self.dc['reportFormat'] = self.reportFormat
        self.dc['testName'] = self.testName
        self.dc['udid'] = 'R58RC0H2RWK'
        self.dc['appPackage'] = 'com.example.android.apis'
        self.dc['appActivity'] = '.ApiDemos'
        self.dc['platformName'] = 'android'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',self.dc)

    def tearDown(self):
        self.driver.quit()

    def test_mobile_methods(self):
        menu_list = self.driver.find_elements_by_xpath("xpath=//*[@id='list']/*[@id='text1']")
        assert len(menu_list) == EXPECTED_LIST_SIZE

    def test_02_mobile_methods(self):
        content = self.driver.find_element_by_xpath("xpath=//*[@text='Content']")
        print("\nwidth: " + str(content.rect["width"]))
        print("height: " + str(content.rect["height"]))
        print("x: " + str(content.rect["x"]))
        print("y: " + str(content.rect["y"]))

    def test_03_mobile_methods(self):
        print("Application Name: ", self.driver.current_activity)
        print("Device Time: ", self.driver.device_time)

    def test_04_mobile_methods(self):
        assert self.driver.is_app_installed("com.experitest.ExperiBank")

    def test_05_mobile_methods(self):
        if self.driver.orientation == "portrait":
            print("Device Orientation is Portrait")
        else:
            print("Device Orientation is Landscape")

    def test_06_mobile_methods(self):
        self.driver.open_notifications()
        time.sleep(1)
        self.driver.save_screenshot("notification.png")
        self.driver.press_keycode(3) #homepage
        self.driver.save_screenshot("home.png")

    def test_07_mobile_methods(self):
        if not self.driver.is_locked():
            self.driver.lock()
        time.sleep(2)
        if self.driver.is_locked():
            self.driver.unlock()
        time.sleep(2)
        assert not self.driver.is_locked()

    def test_08_mobile_methods(self):
        source = self.driver.page_source
        assert source.count("ListView") == 4

    def teardown_class(self):
        self.driver.quit()







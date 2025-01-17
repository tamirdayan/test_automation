import pytest
import unittest
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class Test_Execute_Appium():
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
        self.dc['appPackage'] = 'com.experitest.ExperiBank'
        self.dc['appActivity'] = '.LoginActivity'
        self.dc['platformName'] = 'android'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.dc)

    def test_execute_appium(self):
        self.driver.find_element_by_xpath("xpath=//*[@id='usernameTextField']").send_keys('company')
        self.driver.find_element_by_xpath("xpath=//*[@id='passwordTextField']").send_keys('company')
        self.driver.find_element_by_xpath("xpath=//*[@text='Login']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='Logout']").click()



# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class PpEdcAddNewCustomer(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.blazedemo.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_pp_edc_add_new_customer(self):
        driver = self.driver
        # Label: Test
        # ERROR: Caught exception [ERROR: Unsupported command [resizeWindow | 1920,912 | ]]
        driver.get("http://gepp-edc/Account/Login")
        driver.find_element_by_id("Email").click()
        driver.find_element_by_id("Password").clear()
        driver.find_element_by_id("Password").send_keys("Ets!Test8")
        driver.find_element_by_id("Email").clear()
        driver.find_element_by_id("Email").send_keys("epdtrader.test@gazprom-energy.com")
        driver.find_element_by_css_selector("button.btn.btn-lg.btn-block.btn-gazprom").click()
        driver.find_element_by_css_selector("a.nav-link.collapsed > span").click()
        driver.find_element_by_xpath("//div[@id='tradeManagement']/span[2]/span[2]").click()
        driver.find_element_by_css_selector("div.multiselect.multiselect--active > div.multiselect__select").click()
        driver.find_element_by_css_selector("div.multiselect.multiselect--active > div.multiselect__content-wrapper > ul.multiselect__content > li.multiselect__element > span.multiselect__option.multiselect__option--highlight").click()
        driver.find_element_by_css_selector("div.multiselect.multiselect--active > div.multiselect__select").click()
        driver.find_element_by_css_selector("div.multiselect.multiselect--active > div.multiselect__content-wrapper > ul.multiselect__content > li.multiselect__element > span.multiselect__option.multiselect__option--highlight").click()
        driver.find_element_by_css_selector("div.multiselect.multiselect--active > div.multiselect__select").click()
        driver.find_element_by_css_selector("div.multiselect.multiselect--active > div.multiselect__content-wrapper > ul.multiselect__content > li.multiselect__element > span.multiselect__option.multiselect__option--highlight").click()
        driver.find_element_by_css_selector("div.col-sm-12 > select.form-control").click()
        Select(driver.find_element_by_css_selector("div.col-sm-12 > select.form-control")).select_by_visible_text("Standard")
        driver.find_element_by_xpath("//div[@id='addNewTradePopup']/div/div/div[2]/div/div[7]/div/select").click()
        Select(driver.find_element_by_xpath("//div[@id='addNewTradePopup']/div/div/div[2]/div/div[7]/div/select")).select_by_visible_text("Index")
        driver.find_element_by_css_selector("div.col-sm-12.col-md-6.col-lg-4.col-xl-4 > select.form-control").click()
        Select(driver.find_element_by_css_selector("div.col-sm-12.col-md-6.col-lg-4.col-xl-4 > select.form-control")).select_by_visible_text("Day")
        driver.find_element_by_xpath("//div[@id='addNewTradePopup']/div/div/div[2]/div/div[10]/div/div/input").click()
        driver.find_element_by_xpath("//div[@id='addNewTradePopup']/div/div/div[2]/div/div[10]/div/div/input").clear()
        driver.find_element_by_xpath("//div[@id='addNewTradePopup']/div/div/div[2]/div/div[10]/div/div/input").send_keys("100")
        driver.find_element_by_xpath("//div[@id='addNewTradePopup']/div/div/div[2]/div/div[11]/div/div/input").click()
        driver.find_element_by_xpath("//div[@id='addNewTradePopup']/div/div/div[2]/div/div[11]/div/div/input").clear()
        driver.find_element_by_xpath("//div[@id='addNewTradePopup']/div/div/div[2]/div/div[11]/div/div/input").send_keys("500")
        driver.find_element_by_xpath("//div[@id='addNewTradePopup']/div/div/div[2]/div/div[11]/div[2]/div/input").click()
        driver.find_element_by_xpath("//div[@id='addNewTradePopup']/div/div/div[2]/div/div[11]/div[2]/div/input").clear()
        driver.find_element_by_xpath("//div[@id='addNewTradePopup']/div/div/div[2]/div/div[11]/div[2]/div/input").send_keys("1000")
        driver.find_element_by_xpath("//div[@id='addNewTradePopup']/div/div/div[2]/div/div[12]/div/div/input").click()
        driver.find_element_by_xpath("//div[@id='addNewTradePopup']/div/div/div[2]/div/div[12]/div/div/input").clear()
        driver.find_element_by_xpath("//div[@id='addNewTradePopup']/div/div/div[2]/div/div[12]/div/div/input").send_keys("500.0000")
        driver.find_element_by_css_selector("div.col-sm-4.col-md-6.col-lg-2.col-xl-2 > div").click()
        driver.find_element_by_css_selector("div.col-sm-4.col-md-6.col-lg-2.col-xl-2.mt-4.float-right > span.btn.btn-gazprom.btn-icon-split.btn.mt-2.cursor-pointer > span.text").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


#def test_pp_edc_add_new_customer(self):
    #driver = self.driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://gepp-edc/Account/Login")

print(driver.title)
print(driver.current_url)
driver.maximize_window()

driver.find_element(By.ID, "Email").click()
driver.find_element(By.ID, "Password").clear()
driver.find_element(By.ID, "Password").send_keys("Ets!Test8")
driver.find_element(By.ID, "Email").clear()
driver.find_element(By.ID, "Email").send_keys("epdtrader.test@gazprom-energy.com")
driver.find_element(By.CSS_SELECTOR, "button.btn.btn-lg.btn-block.btn-gazprom").click()
driver.find_element(By.CSS_SELECTOR, "a.nav-link.collapsed > span").click()
driver.find_element(By.XPATH, "//div[@id='tradeManagement']/span[2]/span[2]").click()
driver.find_element(By.CSS_SELECTOR, "div.multiselect.multiselect--active > div.multiselect__select").click()
driver.find_element(By.CSS_SELECTOR, "div.multiselect.multiselect--active > div.multiselect__content-wrapper > ul.multiselect__content > li.multiselect__element > span.multiselect__option.multiselect__option--highlight").click()
driver.find_element(By.CSS_SELECTOR, "div.multiselect.multiselect--active > div.multiselect__select").click()
driver.find_element(By.CSS_SELECTOR, "div.multiselect.multiselect--active > div.multiselect__content-wrapper > ul.multiselect__content > li.multiselect__element > span.multiselect__option.multiselect__option--highlight").click()
driver.find_element(By.CSS_SELECTOR, "div.multiselect.multiselect--active > div.multiselect__select").click()
driver.find_element(By.CSS_SELECTOR, "div.multiselect.multiselect--active > div.multiselect__content-wrapper > ul.multiselect__content > li.multiselect__element > span.multiselect__option.multiselect__option--highlight").click()
driver.find_element(By.CSS_SELECTOR,"div.col-sm-12 > select.form-control").click()
Select(driver.find_element(By.CSS_SELECTOR, "div.col-sm-12 > select.form-control")).select_by_visible_text("Standard")
driver.find_element(By.XPATH, "//div[@id='addNewTradePopup']/div/div/div[2]/div/div[7]/div/select").click()
Select(driver.find_element(By.XPATH, "//div[@id='addNewTradePopup']/div/div/div[2]/div/div[7]/div/select")).select_by_visible_text("Index")
driver.find_element(By.CSS_SELECTOR, "div.col-sm-12.col-md-6.col-lg-4.col-xl-4 > select.form-control").click()
Select(driver.find_element(By.CSS_SELECTOR, "div.col-sm-12.col-md-6.col-lg-4.col-xl-4 > select.form-control")).select_by_visible_text("Day")
driver.find_element(By.XPATH, "//div[@id='addNewTradePopup']/div/div/div[2]/div/div[10]/div/div/input").click()
driver.find_element(By.XPATH, "//div[@id='addNewTradePopup']/div/div/div[2]/div/div[10]/div/div/input").clear()
driver.find_element(By.XPATH, "//div[@id='addNewTradePopup']/div/div/div[2]/div/div[10]/div/div/input").send_keys("100")
driver.find_element(By.XPATH, "//div[@id='addNewTradePopup']/div/div/div[2]/div/div[11]/div/div/input").click()
driver.find_element(By.XPATH, "//div[@id='addNewTradePopup']/div/div/div[2]/div/div[11]/div/div/input").clear()
driver.find_element(By.XPATH, "//div[@id='addNewTradePopup']/div/div/div[2]/div/div[11]/div/div/input").send_keys("500")
driver.find_element(By.XPATH, "//div[@id='addNewTradePopup']/div/div/div[2]/div/div[11]/div[2]/div/input").click()
driver.find_element(By.XPATH, "//div[@id='addNewTradePopup']/div/div/div[2]/div/div[11]/div[2]/div/input").clear()
driver.find_element(By.XPATH, "//div[@id='addNewTradePopup']/div/div/div[2]/div/div[11]/div[2]/div/input").send_keys("1000")
driver.find_element(By.XPATH, "//div[@id='addNewTradePopup']/div/div/div[2]/div/div[12]/div/div/input").click()
driver.find_element(By.XPATH, "//div[@id='addNewTradePopup']/div/div/div[2]/div/div[12]/div/div/input").clear()
driver.find_element(By.XPATH, "//div[@id='addNewTradePopup']/div/div/div[2]/div/div[12]/div/div/input").send_keys("500.0000")
driver.find_element(By.CSS_SELECTOR, "div.col-sm-4.col-md-6.col-lg-2.col-xl-2 > div").click()
driver.find_element(By.CSS_SELECTOR, "div.col-sm-4.col-md-6.col-lg-2.col-xl-2.mt-4.float-right > span.btn.btn-gazprom.btn-icon-split.btn.mt-2.cursor-pointer > span.text").click()

#driver.find_element(By.XPATH,
def is_element_present(self, how, what):
    try:
        self.driver.find_element(by=how, value=what)
    except NoSuchElementException as e:
        return False
    return True


def is_alert_present(self):
    try:
        self.driver.switch_to_alert()
    except NoAlertPresentException as e:
        return False
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
    finally:
        self.accept_next_alert = True


def tearDown(self):
    self.driver.quit()
    self.assertEqual([], self.verificationErrors)
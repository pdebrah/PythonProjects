
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

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
#Trade Management
driver.find_element(By.CSS_SELECTOR, "a.nav-link.collapsed > span").click()
driver.find_element(By.CSS_SELECTOR, "span.text").click()

driver.find_element(By.CSS_SELECTOR, "div.col-sm-12 > div > select.form-control").click()
Select(driver.find_element(By.CSS_SELECTOR, "div.col-sm-12 > div > select.form-control")).select_by_visible_text("UKG DA")
driver.find_element(By.CSS_SELECTOR, "div.col-sm-12 > select.form-control").click()
Select(driver.find_element(By.CSS_SELECTOR, "div.col-sm-12 > select.form-control")).select_by_visible_text("Standard")
driver.find_element(By.XPATH, "//div[@id='addNewTradePopup']/div/div/div[2]/div/div[7]/div/select").click()
Select(driver.find_element(By.XPATH, "//div[@id='addNewTradePopup']/div/div/div[2]/div/div[7]/div/select")).select_by_visible_text("Index - Mid")
driver.find_element(By.CSS_SELECTOR, "div.col-sm-12.col-md-6.col-lg-4.col-xl-4 > select.form-control").click()
Select(driver.find_element(By.CSS_SELECTOR, "div.col-sm-12.col-md-6.col-lg-4.col-xl-4 > select.form-control")).select_by_visible_text("Day")
driver.find_element(By.XPATH, "//div[@id='addNewTradePopup']/div/div/div[2]/div/div[11]/div/div/input").click()
driver.find_element(By.XPATH, "//div[@id='addNewTradePopup']/div/div/div[2]/div/div[11]/div/div/input").clear()
driver.find_element(By.XPATH, "//div[@id='addNewTradePopup']/div/div/div[2]/div/div[11]/div/div/input").send_keys("50")
driver.find_element(By.XPATH, "//div[@id='addNewTradePopup']/div/div/div[2]/div/div[11]/div[2]/div/input").click()
driver.find_element(By.XPATH, "//div[@id='addNewTradePopup']/div/div/div[2]/div/div[11]/div[2]/div/input").clear()

driver.find_element(By.XPATH, "//div[@id='addNewTradePopup']/div/div/div[2]/div/div[11]/div[2]/div/input").send_keys("1000")
#driver.find_element(By.XPATH, "//div.col-sm-4.col-md-6.col-lg-2.col-xl-2.mt-4.float-right > div > div > span.btn.btn-gazprom.btn-icon-split.btn.mt-2.cursor-pointer > span.text").click()
#driver.find_element(By.XPATH, "//div[@id='addNewTradePopup']/div[@role='document']/div[@class='modal-content']//div[@class='container']/div[11]/div[4]//span[@role='button']/span[@class='text']").click()
#driver.find_element(By.CSS_SELECTOR, "[aria-modal] [class='row mt-2']:nth-of-type(11) .text").click()
driver.get_screenshot_as_file("screen.png")
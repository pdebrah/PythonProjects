from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://gepp-edc/Account/Login")

print(driver.title)
print(driver.current_url)
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@type='email']").send_keys("epdtrader.test@gazprom-energy.com")
driver.find_element(By.XPATH, "//input[@type='password']").send_keys("Ets!Test8")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

#Trade Management
driver.find_element(By.XPATH, "//ul[@id='accordionSidebar']//a[@href='/TradeManagement']/span[.='Trade Management']").click()

driver.find_element(By.XPATH, "//div[@id='tradeManagement']/span[1]/span[@class='text']").click()
#driver.find_element(By.XPATH, " ").send_keys('UKG Annual WAP')



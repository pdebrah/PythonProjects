from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://geqa-edc/Account/Login")

print(driver.title)
print(driver.current_url)
driver.maximize_window()
#driver.find_element(By.CSS_SELECTOR, 'input#Email').send_keys('epdtrader.test@gazprom-energy.com')
#driver.find_element(By.CSS_SELECTOR, "input[id='email']").send_keys("epdtrader.test@gazprom-energy.com")
driver.find_element(By.XPATH, "//input[@type='email']").send_keys("epdtrader.test@gazprom-energy.com")
driver.find_element(By.XPATH, "//input[@type='password']").send_keys("Ets!Test8")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
#driver.find_element(By.CSS_SELECTOR, '.mt-2 > .field-validation-valid.text-danger').send_keys('Ets!Test8')
#driver.find_element(By.CSS_SELECTOR, 'button').click()
#Trade Management
#driver.find_element(By.CSS_SELECTOR, "body:nth-child(2) div:nth-child(1) ul.navbar-nav.sidebar.sidebar-dark.accordion.toggled.sidebar-colour-QA li.nav-item:nth-child(6) > a.nav-link.collapsed").click()

#Trade Management
#driver.find_element(By.XPATH, "//body/div[@id='wrapper']/ul[@id='accordionSidebar']/li[2]/a[1]").click()
driver.find_element(By.XPATH, "//ul[@id='accordionSidebar']//a[@href='/TradeManagement']/span[.='Trade Management']").click()

driver.find_element(By.XPATH, "//div[@id='tradeManagement']/span[1]/span[@class='text']").click()
driver.find_element(By.XPATH, "//div[@id='addNewTradePopup']/div[@role='document']/div[@class='modal-content']/div[@class='modal-body']/div/div[1]/div[1]/div/select[@class='form-control']").send_keys('UKG Annual WAP')



#BasketMangement
#driver.find_element(By.XPATH, "//ul[@id='accordionSidebar']//a[@href='/BasketManagement']/span[.='Basket Management']").click()
#AuthorisedTrader
#driver.find_element(By.XPATH, "//body/div[@id='wrapper']/ul[@id='accordionSidebar']/li[1]/a[1]/span[1]").click()
#ContractManagemnet
#driver.find_element(By.XPATH, "")
#driver.find_element(By.XPATH, "//ul[@id='accordionSidebar']//a[@href='/ContractManagement']/span[.='Contract Management']").click()
#Report
#driver.find_element(By.XPATH, "//ul[@id='accordionSidebar']//a[@href='/Reports']").click()

#driver.find_element(By.XPATH, "").click()
#def find_element_by_id(param):
#driver.implicitly_wait(0.5)
    #pass


#element = find_element_by_id("email").send_keys("epdtrader.test@gazprom-energy.com")
#driver.implicitly_wait(5000)

#driver.close()
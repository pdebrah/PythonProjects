from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://dev.id.netwealth.com/account/register?returnUrl=https://dev.netwealth.com/login")

print(driver.title)
print(driver.current_url)
driver.maximize_window()


driver.find_element(By.ID, "FirstName").click()
driver.find_element(By.ID, "FirstName").clear()
driver.find_element(By.ID, "FirstName").send_keys("Philip")
driver.find_element(By.ID, "LastName").click()
driver.find_element(By.ID, "LastName").clear()
driver.find_element(By.ID, "LastName").send_keys("Debrah")
driver.find_element(By.ID, "Email").click()
driver.find_element(By.ID, "Email").clear()
driver.find_element(By.ID, "Email").send_keys("Pdebrah32@yahoo.com")
driver.find_element(By.ID, "Email").click()
driver.find_element(By.ID, "Email").clear()
driver.find_element(By.ID, "Email").send_keys("phildebrah32@gmail.com")
driver.find_element(By.ID, "Password").click()
driver.find_element(By.ID, "Password").clear()
driver.find_element(By.ID, "Password").send_keys("Akwasi1!")
driver.find_element(By.ID, "ReferralSource").click()
Select(driver.find_element(By.ID, "ReferralSource")).select_by_visible_text("Newspaper Advert")
driver.find_element(By.ID, "HasOptedOutOfMarketingMaterial").click()
driver.find_element(By.NAME, "RegistrationForm").click()
driver.get_screenshot_as_file("screen.png")

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

driver = webdriver.Firefox()
driver.get("https://ati.su/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element_by_xpath("//*[contains(@href,'https://trucks.ati.su/')]").click()
driver.find_element_by_xpath('//input[@id="input-geo-from"]').click()
driver.find_element_by_xpath('//span[contains(text(),"Беларусь")]').click()
driver.find_element_by_xpath('//input[@id="input-geo-to"]').click()
driver.find_element_by_xpath("//span[contains(text(),'Россия')]").click()
driver.find_element_by_xpath('//*[@class="_2c8wr-2-0-680  _38IFK-2-0-680 _1dpk_-2-0-680"]').click()

driver.find_element_by_xpath("//div[contains(@data-qa, 'truck-card')][last()]")

last = driver.find_element_by_xpath("//body/div[@id='page']/div[@id='root']/main[1]/div[3]/div[1]/div[4]/div[13]/div["
                                    "1]/div[1]/div[1]/div[1]/div[1]/button[1]/div[1]")
driver.execute_script("arguments[0].click();", last)

try:
    # wait for the alert to show up
    WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')
    # if it does
    alert = driver.switch_to.alert()
    alert.accept()
    print("alert accepted")
except TimeoutException:
    print("no alert")

driver.quit()

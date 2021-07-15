import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://ati.su/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element_by_xpath("//*[contains(@href,'https://trucks.ati.su/')]").click()
driver.find_element_by_xpath('//input[@id="input-geo-from"]').click()
driver.find_element_by_xpath('//span[contains(text(),"Беларусь")]').click()
driver.find_element_by_xpath('//input[@id="input-geo-to"]').click()
driver.find_element_by_xpath("//span[contains(text(),'Россия')]").click()
driver.execute_script("window.scrollTo(0, 400)")
driver.find_element_by_xpath('//*[@class="_2c8wr-2-0-680  _38IFK-2-0-680 _1dpk_-2-0-680"]').click()
driver.execute_script("window.scrollTo(0, 2500)")

last = driver.find_element_by_xpath("//body/div[@id='page']/div[@id='root']/main[1]/div[3]/div[1]/div[4]/div[13]/div["
                                    "1]/div[1]/div[1]/div[1]/div[1]/button[1]/div[1]")

driver.execute_script("arguments[0].click();", last)
time.sleep(3)
driver.switch_to.frame(driver.find_element_by_css_selector("iframe[title=\"Login popup\"]"))

driver.find_element_by_css_selector(".ati-id-rui h1").get_attribute("Зарегистрируйтесь")

driver.quit()

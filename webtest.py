from selenium import webdriver
import time
driver = webdriver.chrome('driver/chromedriver')
driver.get('http:127.0.0.1:5000/base')
time.sleep(3)
driver.close()
driver.quit()

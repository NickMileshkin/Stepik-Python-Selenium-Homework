from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
book = browser.find_element_by_id("book")

t = WebDriverWait(browser, 20).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
if (t ==True):
    book.click()
x = browser.find_element_by_id("input_value").text
z = calc(x)

answer = browser.find_element_by_id("answer")
answer.send_keys(z)
browser.find_element_by_id("solve")

button = browser.find_element_by_id("solve")
button.click()

time.sleep(10)
browser.quit()

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    browser = webdriver.Chrome(options=chrome_options)
    # browser.implicitly_wait(5)
    browser.get(link)

    tx = WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    browser.find_element(By.ID, 'book').click()


    # browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]').click()
    #
    # rb = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    # browser.execute_script("return arguments[0].scrollIntoView(true);", rb)
    # rb.click()

    # in1 = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    # in1.send_keys('aa')
    # browser.find_element(By.CSS_SELECTOR, '[name="lastname"]').send_keys('bb')
    # browser.find_element(By.CSS_SELECTOR, '[name="email"]').send_keys('cc')
    #
    # current_dir = os.path.abspath(os.path.dirname('auto.py'))  # получаем путь к директории текущего исполняемого файла
    # file_path = os.path.join(current_dir, 'aaa.txt')  # добавляем к этому пути имя файла
    # browser.find_element(By.CSS_SELECTOR, '#file').send_keys(file_path)

    # b1 = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    # b1.click()
    #
    # # alert = browser.switch_to.alert
    # # alert.accept()
    # w = browser.window_handles[1]
    # browser.switch_to.window(w)
    #
    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(x)
    i = browser.find_element(By.CSS_SELECTOR, '#answer')
    i.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
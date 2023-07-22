from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1")
    num1 = int(num1.text)

    num2 = browser.find_element(By.ID, "num2")
    num2 = int(num2.text)

    y = num1 + num2

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select = select.select_by_visible_text(str(y))

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
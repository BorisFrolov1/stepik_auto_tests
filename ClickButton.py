
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://yopmail.com/ru/email-generator")


button = driver.find_element_by_css_selector("#cprnd")
button.click()


# После выполнения всех действий мы не должны забыть закрыть окно браузера
driver.quit()

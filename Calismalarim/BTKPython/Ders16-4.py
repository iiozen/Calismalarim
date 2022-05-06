from selenium import webdriver
from selenium.webdriver.common.keys import Keys as buton
import time
driver = webdriver.Chrome()

url = "https://github.com/"
driver.get(url)

aramayap = driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div[2]/div/div/div/form/label/input[1]")
time.sleep(1)
aramayap.send_keys("python")
time.sleep(1)
aramayap.send_keys(buton.ENTER)
time.sleep(1)
# result = driver.page_source
# print(result)
result = driver.find_elements_by_css_selector(".repo-list-item .mt-n1 .f4 a")

for i in result:
    print(i.text)


driver.close()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

website = "https://www.pudelek.pl/"
path = "/home/witut/Downloads/chromedriver_linux64/chromedriver"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)

#//div[@class="sc-1gawtz3-0 jjSoSR"]

data = driver.find_element(by="xpath", value='//div[@class="sc-1gawtz3-0 jjSoSR"]')

print(data)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36'
options.add_argument('user-agent={0}'.format(user_agent))
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 20)
action = ActionChains(driver)
driver.get("https://www.elibrary.ru/rubric_titles.asp?rcode=200000")

lks = driver.find_elements(By.XPATH ,'//a[@href]')
nums = driver.find_elements(By.XPATH ,'//*[@id="a102391"]/td[4]/font')
res = []
print(driver.title)
for lk in lks:
    res.append(lk.get_attribute('href'))

res = list(filter(lambda x: 'contents.asp?titleid=' in x, res))

with open('info_j.txt', 'w') as f:
    f.write('\n'.join(res))
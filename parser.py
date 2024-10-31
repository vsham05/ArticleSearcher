from selenium import webdriver
from fake_useragent import UserAgent
from time import sleep

#create a UserAgent instance
user_agent = UserAgent()
#create a ChromeOptions instance
options = webdriver.ChromeOptions()
#add a random user agent to our options
options.add_argument(f'user-agent={user_agent.random}')
options.add_argument("disable-infobars")
#start chrome with our custom options
driver = webdriver.Chrome(options=options)
#navigate to a webpage
driver.get("https://www.elibrary.ru/rubric_titles.asp?rcode=440000")
#sleep 5 seconds so we can see the site
sleep(5)
#take a screenshot
#close the browser
driver.quit()
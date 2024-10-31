from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def get_journal_name(code =200000):
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
    return res


def find_states(link):
    options = Options()
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36'
    options.add_argument('user-agent={0}'.format(user_agent))
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 20)
    action = ActionChains(driver)
    driver.get(link)

    if 'title_about' in driver.current_url:
        print('Zero states')
        return False

    lks = driver.find_elements(By.XPATH ,'//a[@href]')
    nums = driver.find_elements(By.XPATH ,'//*[@id="a102391"]/td[4]/font')
    res = []
    print(driver.title)

    if driver.title == 'Тест Тьюринга':
        raise Exception
    
    for lk in lks:
        res.append(lk.get_attribute('href'))

    res = list(filter(lambda x: 'item.asp?id=' in x, res))

    return res
    
def get_title_and_common_words(link):
    options = Options()
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36'
    options.add_argument('user-agent={0}'.format(user_agent))
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 20)
    action = ActionChains(driver)
    driver.get(link)
    title = driver.page_source.split('<meta property="og:title" content=')[1].split('>')[0]
    description = driver.page_source.split('<meta name="description" content=')[1].split('>')[0]
    return title, description




if __name__ == '__main__':
    with open('info_j.txt', 'r') as file:
        g = list(map(lambda x: x.replace('\n', ''),file.readlines()))

    with open('pointer.txt', 'r') as file:
        k = int(file.read())

    with open('energy_states.txt', 'r') as file:
        states = list(map(lambda x: x.replace('\n', ''),file.readlines()))

    while k < len(g):
        try:
            s = g[k]
            s = find_states(s)
            if type(s) is bool:
                continue
            states += s
        except Exception as e:

            print(e, s)
            with open('energy_states.txt', 'w') as writer:
                writer.write('\n'.join(states))

            k += 1
            with open('pointer.txt', 'w') as writer:
                writer.write(str(k))
            break
        
        k += 1


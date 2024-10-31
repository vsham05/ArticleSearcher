import requests
from bs4 import BeautifulSoup
from time import sleep

with open('regression.txt', 'r') as f:
    links = f.read().split('\n')


with open('pointer_cyb.txt', 'r') as f:
    p = int(f.read())

data = []
for i, link in enumerate(links):
    if i < p:
        continue
    try:
        m = requests.get(link)

        title = m.text.split('<meta property="og:title" content="')[1].split('" />')[0]
        desc = m.text.split('<meta property="og:description" content="')[1].split('" />')[0]
        title = title.replace(',', '')
        desc = desc.replace(',', '')
        if len(title) == 0 :
            print('FATAL ERROR: COMPUTER WILL EXPLODE IN 10 SECONDS')

            with open('pointer_cyb.txt', 'w') as f:
                f.write(str(i))

            break
        print(title, link ,desc)
        res = f'{title},{link},{desc}'
        data.append(res)
    except:
        continue

with open('data_cyberlen11_info.csv', 'w', encoding='utf-8') as f:
    f.write('\n'.join(data))

with open('pointer_cyb.txt', 'w') as f:
                f.write(str(i))

import requests
from bs4 import BeautifulSoup
from IPython.display import SVG, display
url = "https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}

r = requests.get(url=url, headers=headers)


soup = BeautifulSoup(r.content, 'html.parser')

caption = soup.find('caption')
table = caption.parent

rows = table.find_all('tr')




for row in rows[2:]:
    src = row.th.span.img['src']
    part = src.split('.svg')[0]
    cleaned = part.replace('thumb/', '')
    stripped = cleaned.strip('//')
    img = "https://{}.svg".format(stripped) 
    filename = img.split('/')[-1]
    flag = requests.get(img, headers=headers)
#shift enter
    if flag.status_code != 200:
        print('Error getting {}'.format(filename))
    else:
            display(SVG(img)) 
#right click the code
#run in interactive
            

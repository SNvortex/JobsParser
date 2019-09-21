import re
from bs4 import BeautifulSoup as bs
import html.parser
import requests
import json
from pprint import pprint

headers = {'accept': '*/*',
           'user_agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'}

base_url = 'https://www.work.ua/ru/jobs-kyiv-python/?days=122'
href_url = 'https://www.work.ua'


def work_parse(base_url, headers):
    jobs = []
    session = requests.Session()
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        divs = soup.find_all('div', attrs={'class': 'card card-hover card-visited wordwrap job-link'})
        for div in divs:
            title = div.find('h2', attrs={'class': 'add-bottom-sm'}).text
            href = href_url + div.find('a').get('href')
            company = div.find('b').text
            with open('jobs.json', 'w') as jobfile:
                jobs.append({
                    'title': title,
                    'href': href,
                    'company': company
                })
                json.dump(jobs, jobfile, indent=4, ensure_ascii=False)
        print(jobs)
    else:
        print('ERROR')


work_parse(base_url, headers)
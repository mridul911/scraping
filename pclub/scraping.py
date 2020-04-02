import requests
from bs4 import BeautifulSoup
import pandas as pd

r=requests.get("https://summerofcode.withgoogle.com/archive/2019/projects/")
soup = BeautifulSoup(r.text, 'html.parser')
results = soup.find('ul',{'class':'project-list-container no-style-list'})
result=results.find_all('li')
records = []
for result1 in result:
    name = result1.find('div').find('a').text
    proname = result1.find('div').find('div').text
    orgname = result1.find('div').contents[5].text
    records.append((name,proname,orgname))
df= pd.DataFrame(records,columns=['name','proname','orgname'])
df.to_csv('GSOC 2019.csv',index=False,encoding='utf-8')

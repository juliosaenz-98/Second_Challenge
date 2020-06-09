
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
from datetime import datetime, timedelta, date

data=dict()
scraped_df = pd.DataFrame() 
pages = 11
page_num = 1
for page_num in range(pages):
  # Mention the URL of website here from which you want to scrape
  url = 'https://www.poynter.org/ifcn-covid-19-misinformation/page/'+ str(page_num) +'/'
  response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
  soup = BeautifulSoup(response.content, 'html.parser')
  page_elements = soup.find_all('h2', attrs={'class': 'entry-title'}) 

  
  for link in page_elements:
    print(link.a.get('href'))

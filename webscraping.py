import pandas as pd 
import numpy as np 
import seaborn as sns
import requests
page = requests.get("https://dataquestio.github.io/web-scraping-pages/simple.html")
from bs4 import BeautifulSoup

from tapware import tapware_and_accesories_dict

for subcat in tapware_and_accesories_dict.keys():
    for subsubcat in subcat.keys():
        main_website = subcat[subsubcat]

query  = '/?sortBy=POPULARITY&sortDirection=DESCENDING&pageNumber=1&pageSize=15'

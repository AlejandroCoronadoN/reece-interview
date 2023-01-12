import pandas as pd 
import numpy as np 
import seaborn as sns
import requests
from tqdm import tqdm
page = requests.get("https://dataquestio.github.io/web-scraping-pages/simple.html")
from bs4 import BeautifulSoup
import time
import copy
import random

def stringfy_name(text:str) -> str:
    return text.replace("\\n", '').strip()


from tapware import tapware_and_accesories_dict
new_dict = copy.deepcopy( tapware_and_accesories_dict)


requests_time = {}
df_products = pd.DataFrame()

for subcat in tapware_and_accesories_dict.keys():
    subcat_dict= tapware_and_accesories_dict[subcat]
    for subsubcat in tqdm(subcat_dict.keys(), 'SUB SUB CATEGORY:  ' ):
        requests_time[subsubcat] = []
        main_website = subcat_dict[subsubcat]
        
        initial_query  = '/?sortBy=POPULARITY&sortDirection=DESCENDING&pageNumber=1&pageSize=15'
        website_query = main_website + initial_query
        page = requests.get(website_query)

        pagination_class = 'product-listing__pagination-control--page'
        soup = BeautifulSoup(page.content, 'html.parser')
        soup_pages = soup.find_all("select", {"class": pagination_class})[0]
        max_page = soup_pages.get_text().split('\\n')[0].split(" ")[-1]
        max_page = int(stringfy_name(max_page))
        print(f"There are a total of {max_page} pages")
        #PAGES
        i =1
        new_dict[subcat][subsubcat] = dict()
        new_dict[subcat][subsubcat]["name"] = [] 
        new_dict[subcat][subsubcat]["href"] = [] 
        new_dict[subcat][subsubcat]["price"] = [] 

        while i <= max_page:
            print(f"\nWEBSITE PAGE: {i}")
            main_website = subcat_dict[subsubcat]
            query  = f'/?sortBy=POPULARITY&sortDirection=DESCENDING&pageNumber={i}&pageSize=15'
            website_query = main_website + query
            
            #LOG requests times
            starttime = time.time()
            page = requests.get(website_query)
            endtime = time.time()
            tm = endtime -starttime
            requests_time[subsubcat].append(tm)
            
            soup = BeautifulSoup(page.content, 'html.parser')
            wrapper_class = 'product-grid-wrapper'
            price_class =  'product-tile__section-prices'
            name_class = 'product-tile__detail-name'
            soup_wrapper = soup.find_all("div", {"class": wrapper_class})[0]
            soup_name = soup_wrapper.find_all("a", {"class": name_class})
            soup_price = soup_wrapper.find_all("div", {"class": price_class})
            #ELEMENTS
            for sn, sp in  zip(soup_name, soup_price):
                name = stringfy_name(sn.get_text())
                href = sn['href']

                new_dict[subcat][subsubcat]["name"].append(name)
                new_dict[subcat][subsubcat]["href"].append(href)
                new_dict[subcat][subsubcat]["price"].append(random.randint(0,100))
                print(f' ELEMENTS: {name}')


            i+=1
        #Create df at subsubcategory using all the products from i=1 to i==max_page
        
        new_df = pd.DataFrame.from_dict(new_dict[subcat][subsubcat])
        new_df["Subcategory"] = subcat
        new_df["SubSubCategory"] = subsubcat
        new_df["request_avg_time"] = np.mean(requests_time[subsubcat])
        
        if len(df_products) == 0:
            df_products   = new_df 
        else:
            df_products =df_products.append(new_df)
                
with open('sample.html', "w+") as f:
    soup = BeautifulSoup(page.content, 'html.parser')
    f.write(soup.prettify())





    
import pandas as pd 
import numpy as np 
import datetime
import np as np 
import random 

numdays = 1000  
base = datetime.datetime.today()
date_list = [base - datetime.timedelta(days=x) for x in range(numdays)]


df = pd.read_csv('checkpoint.csv')
df_p = {}
df_all = pd.DataFrame()
for product in df.name.unique():
    mu = random.randint( 100, 1000)
    sigma =mu * random.randint( .1, 2)
    s = np.random.normal(mu, sigma, 1000)
    df_p = {}
    df_p["date"] = date_list
    df_p["orders"] = s
    df_p = pd.DataFrame.from_dict(df_p)
    
    if len(df_all) == 0: 
        df_all = df_p
    else: 
        df_all = df_all.append(df_p)


df_all['year_month'] = df_all.date.dt.strftime('%Y-%m')    
#Group by weeks
df_ss = df_all.groupby(['name', 'year_month']).sum().reset_index()
for product in df_ss.name.unique():
    df_ss_p = df_ss[df_ss.name == product]
    df_ss_p["orders"].quantile(.95)
    # s.rolling(2).quantile(.4, interpolation='lower')
